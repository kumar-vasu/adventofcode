def checkforpairs(requirement,my_dict):
    for key in my_dict.keys():
        if requirement-key in my_dict.keys():
            print(key*(requirement-key)*(2020-requirement))
            return True
    return False
    
my_dict = {}
for i in range(200):
    my_dict[int(input())]=True
for key in my_dict.keys():
    requirement = 2020 - key
    if checkforpairs(requirement,my_dict) == True :
        break
