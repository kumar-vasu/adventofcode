#take the input
def Decimal_to_binary(n):
    n=int(n)
    return bin(n).replace("0b", "")
    
def perform_masking(memory,mask,command):
    #set memory[command] to new value and also do masking
    temp=[i for i in mask]
    for i in range(len(command[1])):
        if mask[-i-1] == "X":
            temp[-1-i] = command[1][-1-i]
    for i in range(len(temp)):
        if temp[i] =="X":
           temp[i] = "0" 
    temp = ''.join(str(e) for e in temp)
    memory[command[0]]=int(temp,2)
    return memory
    
program =[]
while True:
    try:
        temp = input()
        program.append(temp.split(" = "))
        if program[-1][0]=="mask":
            continue
        program[-1][0]=program[-1][0].strip("mem[]")
        program[-1][1]=Decimal_to_binary(program[-1][1])
    except EOFError:
        break

memory ={}
result =0
#put input in a 2d array 
mask = program[0][1]
#set mask for the first mask
for i in program:
    if i[0]=="mask":
        #updatemask
        mask = i[1]
    else:
        memory = perform_masking(memory,mask,i)
#perform action till next mask
#when next mask arrives replace mask
for key in memory.keys():
    result+=memory[key]
print(result)
