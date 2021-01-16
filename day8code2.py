import re

def check(bootcode,counter,past_instruction,acc):
    tempset = set()
    tempset = tempset.union(past_instruction)
    #print(id(tempset))
    while True:
        #print(id(tempset))
        if counter == len(bootcode)-1:
            print(acc,"works")
            break
        if counter in tempset:
            break
        if bootcode[counter][0] == "acc":
            tempset.add(counter)
            acc += int(bootcode[counter][1])
            counter += 1
            continue
        if bootcode[counter][0] == "jmp":
            tempset.add(counter)
            counter+=int(bootcode[counter][1])
            continue
        if bootcode[counter][0] == "nop":
            tempset.add(counter)
            counter += 1 
    return 

bootcode = []
while True:
    try:
        bootcode.append(re.split("\s",input()))
    except EOFError:
        break

bootcode = tuple(bootcode)
past_instructions = set()
counter = 0
acc=0
while True:
    #print(past_instructions,"counter =",counter)
    if counter in past_instructions or counter == len(bootcode)-1:
        print("does not work",acc)
        break
    if bootcode[counter][0] == "acc":
        past_instructions.add(counter)
        acc += int(bootcode[counter][1])
        counter += 1
        continue
    if bootcode[counter][0] == "jmp":
        past_instructions.add(counter)
        check(bootcode,counter+1,past_instructions,acc)
        counter+=int(bootcode[counter][1])
        continue
    if bootcode[counter][0] == "nop":
        past_instructions.add(counter)
        #print(id(past_instructions))
        check(bootcode,counter+int(bootcode[counter][1]),past_instructions,acc)
        counter += 1 
