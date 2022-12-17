"""
north (^), south (v), east (>), west (<)
 How many houses receive at least one present?

    > delivers presents to 2 houses: start starting location, and one to the east.
    ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
    ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

I should 
Know how many houses have at least one present?
I have four directions 
Santa delivers present wherever he is and 
  the direction that elf gave 

should loop throught input 
and give + direction


"""

name = './2015/inputs/third.txt'

with open(name, 'r') as f:
    f = f.readlines()
    directions = f[0]
    direction_set = set(directions)
    
    south = direction_set.count("v")
    north = direction_set.count('^')
    east = direction_set.count('>')
    west = direction_set.count('<')

    y = abs(south-north)
    x = abs(east-west)

    print(south, north, east, west)
    print(x + y)

    

        
