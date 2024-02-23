import requests
import uuid

with open('log.txt', 'w') as log:
    for i in range(100):
        response_id = uuid.uuid1()

        log.write('-------------------------------------------------\n')

        for loop_number in range(20):
            url = f'https://c1.seardev.com/get_file?response_id={response_id}&loop_number={loop_number + 1}&redirect=false'

            response = requests.get(url)

            log.write(response.text + '\n')

            print(loop_number, '', end='')
        
        print('')