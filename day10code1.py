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

# keep track of +1 and +3
no_of_1_difference = 0
no_of_3_difference = 0


#joltage value of plug is 0
joltage_value=0


#loop while joltage_value <= highest adapter
while joltage_value <= max_adapter_joltage:
    
    #if i== highest +3 
    if joltage_value == max_adapter_joltage :
        no_of_3_difference += 1
        joltage_value += 3
        break

    #check for i plus 1
    if joltage_value+1 in cache:
        joltage_value +=1
        no_of_1_difference+=1
        continue
    
    #check for i +2
    if joltage_value+2 in cache:
        joltage_value +=2
        continue
    
    #check for i+3
    if joltage_value+3 in cache:
        joltage_value +=3
        no_of_3_difference+=1
        continue
    
print(no_of_3_difference * no_of_1_difference)    
    
    
