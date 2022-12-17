# 2*l*w + 2*w*h + 2*h*l + l * w
# length, width, height
name = './inputs/second.txt'

with open(name, 'r') as f:
    total = 0
    total_2 = 0
    for line in f.readlines()[0:-1]:
        line = line.strip()
        l, w, h = line.split('x')
        l, w, h = int(l), int(w), int(h)
        area = 2*((l*w)+(w*h)+(h*l))
        slack = min(l*w, w*h, h*l)
        total += area + slack
        ribbon = 2 * min(l+w, w+h, h+l)
        bow = l*w*h
        total_2 += ribbon + bow
    print(total, total_2)
        

    