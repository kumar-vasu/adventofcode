count = 0
answerset = set()
while True:
    try:
        answers = input()
        if answers == "":
            #dostuff
            print(count)
            count = count +len(answerset)
            answerset = set()
        else:
            for answer in answers:
                answerset.add(answer) 
                
    except EOFError :
        print(count)
        count = count +len(answerset)
        break
print(count)
