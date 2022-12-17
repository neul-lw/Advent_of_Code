

name = './inputs/first.txt'

with open(name, 'r') as f:
    info = f.readlines()
    plus_count = info[0].count('(')
    minus_count = info[0].count(')')

    print(plus_count-minus_count)