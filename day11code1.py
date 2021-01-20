
def count_seat(a,b,seating_pattern,row,column):
    try:
        if row+a == -1 or column+b == -1:
            return 0
        elif seating_pattern[row+a][column+b] == "#":
            return 1
        else:
            return 0
    except IndexError:    
        return 0

def check_seats(seating_pattern,row,column):
    
    count = count_seat(-1,0,seating_pattern,row,column)+\
    count_seat(-1,1,seating_pattern,row,column)+\
    count_seat(0,1,seating_pattern,row,column)+\
    count_seat(1,1,seating_pattern,row,column)+\
    count_seat(1,0,seating_pattern,row,column)+\
    count_seat(1,-1,seating_pattern,row,column)+\
    count_seat(0,-1,seating_pattern,row,column)+\
    count_seat(-1,-1,seating_pattern,row,column)
    
    return count

def rearrange_seats(seating_pattern):
    #breath first search
    seating_pattern2 = [["." for i in seating_pattern[0]]for j in seating_pattern]
    
    for row in range(len(seating_pattern)):
       
        for column in range(len(seating_pattern[0])):
            
            #check if element if taken
            if seating_pattern[row][column]== "#":
                
                #change state or not based on condition
                #condition being that there are 4 or more adjacent seats adjacet to it
                
                no_of_occupied = check_seats(seating_pattern,row,column)
                
                if no_of_occupied >= 4 :
                    seating_pattern2[row][column] = "L"
                else:
                    seating_pattern2[row][column] = "#"
                #continue
                continue
            #check if element is empty
            if seating_pattern[row][column]== "L":
                
                #change state or not based on condition
                no_of_occupied = check_seats(seating_pattern,row,column)
                
                if no_of_occupied == 0:
                    
                    seating_pattern2[row][column] = "#"
                else:
                    seating_pattern2[row][column] = "L"
                    
                #continue
                continue
    return seating_pattern2


#initiate seating pattern
seating_pattern=[]

#input seating pattern
while True:
    try:
        seating_pattern.append([i for i in input()])
    except EOFError:
        break

previous_pattern = seating_pattern
no_change = False
while no_change == False :
    
    seating_pattern = rearrange_seats(seating_pattern)
    
    if previous_pattern == seating_pattern:
        no_change =True
    else:
        previous_pattern = seating_pattern

count = 0
for i in seating_pattern:
    for j in i:
        if j == "#":
            count+=1
            
print(count)
