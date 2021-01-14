count = 0
answerset = set()
beginning = True
while True:
    try:
        answers = input()
        #print(answers)
        if answers == "":
            #dostuff
            count = count +len(answerset)
            #print(count)
            answerset = set()
            beginning = True
        else:
            tempset = set()
            for answer in answers:
                tempset.add(answer)
            #print(tempset)
            if len(answerset) == 0 and beginning == True:
                answerset = answerset.union(tempset)
            #    print("empty")
            else:
                answerset = answerset.intersection(tempset)
                if len(answerset) == 0 :
                    beginning = False
            #print(answerset)
    except EOFError :
        count = count +len(answerset)
        break
print(count)
