import re
# cook your dish here
def check(datadic,fields):
#    print(datadic)
    for field in fields:
        if field in datadic.keys():
            if field == "byr" :
            #    print (field,datadic[field])
                if 1920 <= int(datadic[field]) <= 2002:
            #        print("byr continue")
                    continue
                else:
                    return 0
            
            if field == "iyr" :
                if 2010 <= int(datadic[field]) <= 2020:
           #         print("iyr continue")
                    continue
                else:
                    return 0
                
            if field == "eyr" :
                if 2020 <= int(datadic[field]) <= 2030:
          #          print("eyr continue")
                    continue
                else:
                    return 0
                
            if field == "hgt":
                if datadic[field].endswith("cm"):
                    datadic[field] = datadic[field].replace("cm","")
                    if 150 <=int(datadic[field])<= 193:
         #               print("hgt continue")
                        continue
                    else:
                        return 0
                        
                elif datadic[field].endswith("in"):
                    datadic[field] = datadic[field].replace("in","")
                    if 59 <=int(datadic[field])<= 76:
        #                print("hgt continue")
                        continue
                    else:
                        return 0
                else:
                    return 0
                
            if field == "hcl":
                temp2={"0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"}
                temp1=[]
                if datadic[field].startswith("#"):
                    datadic[field] = datadic[field].replace("#","")
                    for i in datadic[field]:
                        if i not in temp2:
                            return 0
       #             print("hcl continue")        
                    continue
                else:
                    return 0
                
            if field == "ecl" :
                temp3={"amb","blu","brn","gry","grn","hzl","oth"}
                if datadic[field] not in temp3 :
                    return 0 
                else :
      #              print("ecl continue")
                    continue
                
            if field == "pid":
                temp4 = []
                if len(datadic[field]) == 9:
                    for i in datadic[field]:
                        if int(i) not in range(0,10):
                            return 0 
     #               print("pid continue")
                    continue            
                else:
                    return 0
        else:
            return 0
    #print("wait")
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
