waypoint = {}
waypoint["E"] = 10
waypoint["N"] = 1



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


for i in range(len(navigation_instructions)):
    print(navigation_instructions[i])
    if navigation_instructions[i][0] == "F":
        position["E"]+=navigation_instructions[i][1]*waypoint["E"]
        position["N"]+=navigation_instructions[i][1]*waypoint["N"]
        print("pos",position)
        continue
    
    if navigation_instructions[i][0] == "N" or navigation_instructions[i][0] == "E":
        waypoint[navigation_instructions[i][0]] += navigation_instructions[i][1]
        print("way",waypoint)
        continue
        
    if navigation_instructions[i][0] == "S":
        waypoint["N"]-= navigation_instructions[i][1]
        print("way",waypoint)    
        continue
        
    if navigation_instructions[i][0] == "W":
        waypoint["E"]-= navigation_instructions[i][1]
        print("way",waypoint)
        continue
        
    if navigation_instructions[i][0] == "L" :
        turns = navigation_instructions[i][1]//90
        if turns == 1:
            waypoint["E"],waypoint["N"]=-waypoint["N"],waypoint["E"]
        if turns == 2:
            waypoint["E"]=-waypoint["E"]
            waypoint["N"]=-waypoint["N"]
        if turns == 3:
            waypoint["E"],waypoint["N"]=waypoint["N"],-waypoint["E"]
        print("way",waypoint)
        continue
    
    if navigation_instructions[i][0] == "R":
        turns = navigation_instructions[i][1]//90
        if turns == 3:
            waypoint["E"],waypoint["N"]=-waypoint["N"],waypoint["E"]
        if turns == 2:
            waypoint["E"]=-waypoint["E"]
            waypoint["N"]=-waypoint["N"]
        if turns == 1:
            waypoint["E"],waypoint["N"]=waypoint["N"],-waypoint["E"]
        print("way",waypoint)
        continue

print(abs(position["E"])+abs(position["N"]))





