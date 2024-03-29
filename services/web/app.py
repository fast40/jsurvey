from flask import Flask, request, render_template, jsonify
from create_datasets import DATABASE, create_datasets
import pymongo

app = Flask(__name__)
client = pymongo.MongoClient('mongodb://mongo:27017/qualtricks')


@app.route('/')
def index():
    with open('static/javascript/fill_template.js') as file:
        javascript_code = file.read()
    
    with open('templates/template.html') as file:
        html_code = file.read()

    return render_template('index.html', html_code=html_code, javascript_code=javascript_code)


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/get_responses')
def get_responses():
    try:
        question_number = int(request.args.get('question_number'))
    except Exception:
        return jsonify({})

    responses = list(client[DATABASE]['responses'].aggregate([{'$sample': {'size': 2}}]))

    response_set = {
        'response_numbers': ' '.join(response['response_number'] for response in responses),
        'initial_answers': [response['initial_answers'][question_number - 1] for response in responses],
        'meta_errors': [response['meta_errors'][question_number - 1] for response in responses],
        'meta_error_ranks': [response['meta_error_ranks'][question_number - 1] for response in responses],
    }

    response_set['ranks'] = sorted(range(len(response_set['meta_error_ranks'])), key=lambda i: abs(response_set['meta_errors'][i]))

    server_response = jsonify(response_set)
    server_response.headers.add('Access-Control-Allow-Origin', '*')

    return server_response


@app.route('/populate')
def populate():
    create_datasets()

    return 'populated. do not go here again.'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
