def no_of_ways(joltage_value,max_adapter_joltage,ways,cheatsheet) :
    #print(joltage_value,ways)
    #print(cheatsheet)
    if joltage_value in cheatsheet.keys():
        #print("cheatsheet",joltage_value,cheatsheet[joltage_value])
        return ways+cheatsheet[joltage_value]
        
    #check for i plus 1
    if joltage_value+1 in cache:
        if joltage_value+1 == max_adapter_joltage :
            #print("plus1max",joltage_value,ways+1)
            #if joltage_value in cheatsheet.keys():
            cheatsheet[joltage_value]=ways+1
            return ways+1
            
        else:
            ways = no_of_ways(joltage_value+1,max_adapter_joltage,ways,cheatsheet)
            #print("plus1call",joltage_value,ways)
    
    #print(joltage_value,ways)
    #check for i +2
    if joltage_value+2 in cache:
        if joltage_value+2 == max_adapter_joltage :
            #print("plus2max",joltage_value,ways+1)
            cheatsheet[joltage_value]=ways+1
            return ways+1
            
        else:
            ways = no_of_ways(joltage_value+2,max_adapter_joltage,ways,cheatsheet)
            #print("plus2call",joltage_value,ways)    
    
    #print(joltage_value,ways)        
    #check for i+3
    if joltage_value+3 in cache:
        if joltage_value+3 == max_adapter_joltage :
            #print("plus3max",joltage_value,ways+1)
            cheatsheet[joltage_value]=ways+1
            return ways+1
            
        else:
            ways = no_of_ways(joltage_value+3,max_adapter_joltage,ways,cheatsheet)
            #print("plus3call",joltage_value,ways)
    #print(joltage_value,ways)        
    
    cheatsheet[joltage_value] = ways
    #print(cheatsheet)
    return ways

#put input into set
cache = set()

# keep track of highest value
max_adapter_joltage=0


while True:
    try:
        curr = int(input())
        cache.add(curr)
        if curr > max_adapter_joltage:
            max_adapter_joltage = curr
    except EOFError:
        break

#joltage value of plug is 0
joltage_value=0

cheatsheet = {}
#recurse to find no of ways
possible_ways = no_of_ways(joltage_value,max_adapter_joltage,0,cheatsheet)

    
print(possible_ways)    
    
    
