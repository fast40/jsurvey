from collections import Counter


c = Counter()

with open('log.txt', 'r') as file:
    for line in file:
        if line[0] == '-':
            continue

        c[line[:8]] += 1


for batch, count in c.items():
    print(f'{batch}: {count}')