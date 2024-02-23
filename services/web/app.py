from flask import Flask, request, render_template, jsonify
from create_datasets import DATABASE
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

    responses = list(client[DATABASE]['responses'].aggregate([{'$sample': {'size': 4}}]))

    response_set = {
        'response_numbers': ' '.join(response['response_number'] for response in responses),
        'initial_answers': [response['initial_answers'][question_number - 1] for response in responses],
        'meta_errors': [response['meta_errors'][question_number - 1] for response in responses],
    }

    server_response = jsonify(response_set)
    server_response.headers.add('Access-Control-Allow-Origin', '*')

    return server_response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
