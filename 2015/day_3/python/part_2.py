name = './2015/inputs/third.txt'

with open(name, 'r') as f:
    f = f.read()

    s_coords = [0, 0]
    r_coords = [0, 0]
    visited = ['0,0']

    for index, direct in enumerate(f):
        if direct == '^':
            if index % 2 == 0:
                s_coords[1] += 1
            else:
                r_coords[1] += 1
        elif direct == 'v':
            if index % 2 == 0:
                s_coords[1] -= 1
            else:
                r_coords[1] -= 1
        elif direct == '>':
            if index % 2 == 0:
                s_coords[0] += 1
            else:
                r_coords[0] += 1
        elif direct == '<':
            if index % 2 == 0:
                s_coords[0] -= 1
            else:
                r_coords[0] -= 1

        visited.append(f"{s_coords[0]},{s_coords[1]}")
        visited.append(f"{r_coords[0]},{r_coords[1]}")

print(len(set(visited)))

    

        
