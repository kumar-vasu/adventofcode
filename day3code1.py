#import the map
map = [[char for char in input()] for i in range(323)]
#initialize the coordinates and tree count
x,y =0,0
tree=0
#repeat till y is not equal to length of map
while y <= len(map)-1:
    print(x,y)
    #check if coordinate has a tree or free space
    if map[y][x]=='#':
        print("tree")
        #increment if tree
        tree+=1
    #if y is not equal to length of map but x is equal to breath of map put x =-1
    if y == len(map)-1:
        print("breakpoint")
        break
    x+= 3
    y+= 1
    if x > len(map[0])-1 and y < len(map)-1:
        print("incrementing x")
        x-= len(map[0])
print(tree)
