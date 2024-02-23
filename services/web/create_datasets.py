import pymongo
import csv

DATABASE = 'c1'

if __name__ == '__main__':
    client = pymongo.MongoClient(f'mongodb://127.0.0.1:27017/{DATABASE}')
    db = client['c1']

    initial_answers = []

    with open('initial_answer.csv', 'r') as file:
        reader = csv.reader(file)

        _ = next(reader)

        for line in reader:
            initial_answers.append(line)


    meta_errors = []

    with open('meta_meta_error.csv', 'r') as file:
        reader = csv.reader(file)
        
        _ = next(reader)

        for line in reader:
            meta_errors.append(line)


    db['responses'].delete_many({})
    db['responses'].insert_many(
        {
            "response_number": str(i + 1),
            "initial_answers": [float(initial_answer) for initial_answer in initial_answers[i]],
            "meta_errors": [float(meta_error) for meta_error in meta_errors[i]],
        } for i in range(len(initial_answers))
    )