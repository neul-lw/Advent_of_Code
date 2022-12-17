name = './inputs/first.txt'

with open(name, 'r') as f:
    
    info = f.readlines()[0]

    current_base = 0

    for i, base in enumerate(info):
        if current_base == -1:
            print(i)
            break
        elif base == '(':
            current_base += 1
        elif base == ')':
            current_base -= 1

