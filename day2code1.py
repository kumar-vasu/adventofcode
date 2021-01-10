# importing regular expression for ints findall, split function, search can also be used
 
import re
#initilaizing number of valid passwords equal to zero
valid=0
#looping over all the inputs
for i in range(1000):
    data = str(input())
    #spliting the ith input and seperating the limits and the password itself  
    #using re.split() because split function of re is faster and also readable. 
    data=re.split("-|:\s|\s",data)
    #finding all occurances of character in password
    occurances = re.findall(data[2],data[3])
    #checking if the occurances lie between the prescibed limit
    if int(data[0])<=len(occurances)<=int(data[1]):
        #incrementing valid every time it is within the limit
        valid+=1
print(valid)
