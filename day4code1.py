import re
# cook your dish here
def check(datadic,fields):
#    print(datadic)
    for field in fields:
        if field not in datadic.keys():
            return 0
    return 1
    
requiredfields=["byr","iyr","eyr","hgt","hcl","ecl","pid"]
datadic = {}
pair =[]
valid = 0
while True :
    try:
        temp = input()
        if temp == "":
            valid+=check(datadic,requiredfields)
            datadic ={}
            continue
        else:
            temp=re.split("\s",temp)
            for i in temp:
                pair = re.split(":",i)
                datadic[pair[0]]=pair[1]
    except EOFError: 
        valid+=check(datadic,requiredfields)
        break
        
print(valid)
