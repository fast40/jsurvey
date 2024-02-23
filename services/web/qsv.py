import csv
import tempfile


with tempfile.SpooledTemporaryFile(max_size=1024, mode='w') as temp:
    temp.write('x1,x2,x3\n1,2,3\n')
    temp.seek(0)

    reader = csv.reader(temp.readlines())

    for line in reader:
        print(line)





datasets.get_random_row()