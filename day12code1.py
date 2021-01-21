facing = "E"
navigation_instructions = []
while True:
    try:
        temp = input()
        temp1 = temp[0]
        temp = temp[1:]
        navigation_instructions.append([temp1,int(temp)])
    except:
        break

position = {}
position["E"] = 0
position["N"] = 0

turning = {}
turning["E"]=["E","N","W","S"]
turning["N"]=["N","W","S","E"]
turning["W"]=["W","S","E","N"]
turning["S"]=["S","E","N","W"] 

for i in range(len(navigation_instructions)):
    if navigation_instructions[i][0] == "F":
        if facing == "E" or facing == "N":
            position[facing] += navigation_instructions[i][1]
        if facing == "W":
            position["E"] -= navigation_instructions[i][1]
        if facing == "S":
            position["N"] -= navigation_instructions[i][1]
            
        continue
    
    if navigation_instructions[i][0] == "N" or navigation_instructions[i][0] == "E":
        position[navigation_instructions[i][0]] += navigation_instructions[i][1]
        continue
        
    if navigation_instructions[i][0] == "S":
        position["N"]-= navigation_instructions[i][1]
        continue
        
    if navigation_instructions[i][0] == "W":
        position["E"]-= navigation_instructions[i][1]
        continue
        
    if navigation_instructions[i][0] == "L":
        turns = navigation_instructions[i][1]//90
        facing = turning[facing][turns]
        continue
    
    if navigation_instructions[i][0] == "R":
        turns = navigation_instructions[i][1]//90
        facing = turning[facing][0-turns]
        continue

print(abs(position["E"])+abs(position["N"]))





