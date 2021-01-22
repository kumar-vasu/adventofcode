import re

temp = input()
busid= []
buses = {}
temp = re.split(",",temp)
for i in range(len(temp)):
    if temp[i] == "x":
        continue
    busid.append(temp[i])
    buses[temp[i]]=int(len(temp)-i-1)

bi =[]
N=1

for key in busid:
    bi.append(buses[key])
    N=N*int(key)

ni = []
for key in busid:
    ni.append(N//int(key))
    
xi = []
for i in range(len(busid)):
    rem = ni[i]%int(busid[i])
    j=1
    while True:
        if (rem*j)%int(busid[i]) == 1:
            xi.append(j)
            break
        j+=1
    
final = 0
for i in range(len(busid)):
    final+= xi[i]*ni[i]*bi[i]

    
print((final%N)-len(temp)+1)
