import re
#initilaizing number of valid passwords equal to zero
valid=0
#looping over all the inputs
for i in range(1000):
    data = str(input())
    #spliting the ith input and seperating the limits and the password itself  
    #using re.split() because split function of re is faster and also readable. 
    data=re.split("-|:\s|\s",data)
    password = []
    for letter in data[3]:
        password.append(letter)
    #taking the bool if the letters are present at defined positions and taking there xor 
    #this way the answer is true only if one of them is true 
    if bool(password[int(data[0])-1] == data[2]) ^ bool(password[int(data[1])-1] == data[2]):
        valid +=1
print(valid)
