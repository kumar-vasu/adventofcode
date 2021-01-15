import re
#define recursive function to return number of gold bags
def no_of_gold_bags(ruledic,key,cache):
    print("key :",key)
    if ruledic[key] == None:
        print("returning None")
        cache[key] = 0
        return cache,cache[key] 
    shiny = 0
    for i in ruledic[key].keys():
        if i not in cache.keys():
            cache,cache[i] = no_of_gold_bags(ruledic,i,cache)
        shiny = shiny + int(ruledic[key][i])*cache[i] + int(ruledic[key][i])
        print("cache[i]",i,cache[i])
    #print("shiny for ",key, shiny)
    print("shiny fot ",key , shiny)
    return cache,shiny
#initiate variables
ruledic = {}
cache ={}
bags=0
#inputdata
while True:
    try:
        rule = input()
        temp = re.split(" contain ",rule)
        if temp[1] == "no other bags.":
            ruledic[temp[0].rstrip("s")] = None
        else:
            temp[1]=temp[1].rstrip(".")
            ruledic[temp[0].rstrip("s")]={}
            for i in re.split(", ",temp[1]):
                ruledic[temp[0].rstrip("s")][i.lstrip("123456789 ").rstrip("s")]=i[0]
    except EOFError:
        break
#print(ruledic)
#when the input dictionary is complete
#call a recursion on the dictionary keys to find no of gold bags
cache,bags = no_of_gold_bags(ruledic,"shiny gold bag",cache)
#print("............................bags",no_of_outer_bags)
print(bags)
