name = './2015/inputs/third.txt'

with open(name, 'r') as f:
    f = f.read()

    coords = [0, 0]
    visited = ['0,0']

    for direct in f:
        if direct == '^':
          coords[1] += 1
        elif direct == 'v':
          coords[1] -= 1
        elif direct == '>':
          coords[0] += 1
        elif direct == '<':
          coords[0] -= 1
        visited.append(f"{coords[0]},{coords[1]}")

print(len(set(visited)))

    

        
