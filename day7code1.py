import re
#define recursive function to return number of gold bags
def no_of_gold_bags(ruledic,key):
    print("key :",key)
    if ruledic[key] == None:
    #    print("returning None")
        return 0 
    shiny = 0
    for i in ruledic[key]:
        if i == "shiny gold bag":
    #        print("retirning 1")
            shiny = 1
            continue
    #    print("calling for ",i)
        shiny = shiny + no_of_gold_bags(ruledic,i)
    #    print("shiny fot ",i, shiny)
    #print("shiny for ",key, shiny)
    return shiny
#initiate variables
ruledic = {}
no_of_outer_bags = 0
#inputdata
while True:
    try:
        rule = input()
        temp = re.split(" contain ",rule)
        if temp[1] == "no other bags.":
            ruledic[temp[0].rstrip("s")] = None
        else:
            temp[1]=temp[1].rstrip(".")
            ruledic[temp[0].rstrip("s")]=[]
            for i in re.split(", ",temp[1]):
                ruledic[temp[0].rstrip("s")].append(i.lstrip("123456789 ").rstrip("s"))
    except EOFError:
        break
#print(ruledic)
#when the input dictionary is complete
#call a recursion on the dictionary keys to find no of gold bags
for key in ruledic.keys():
    if no_of_gold_bags(ruledic,key)>= 1:
        no_of_outer_bags = no_of_outer_bags + 1 
    #print("............................bags",no_of_outer_bags)
print(no_of_outer_bags)
