#import the map
map = [[char for char in input()] for i in range(323)]
slopes =[[1,1],[3,1],[5,1],[7,1],[1,2]]
#initialize the coordinates and tree count
tree=[0,0,0,0,0]
t=0
#repeat till y is not equal to length of map
for k in slopes :
    x,y =0,0
    while y <= len(map)-1:
        print(x,y)
        #check if coordinate has a tree or free space
        if map[y][x]=='#':
            print("tree")
            #increment if tree
            tree[t]+=1
        #if y is not equal to length of map but x is equal to breath of map put x =-1
        if y == len(map)-1:
            print("breakpoint")
            t+=1
            break
        x+= k[0]
        y+= k[1]
        if x > len(map[0])-1 and y < len(map)-1:
            print("incrementing x")
            x-= len(map[0])
print(tree[0]*tree[1]*tree[2]*tree[3]*tree[4])
