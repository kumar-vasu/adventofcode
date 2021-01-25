import re
starting_numbers=[]
starting_numbers=re.split(",",input())
spoken_at={}
prelast = None
lastnumber=None
for i in range(2020):
    if i < len(starting_numbers):
        lastnumber=starting_numbers[i]
        if i > 0:
            prelast = starting_numbers[i-1]
            spoken_at[int(prelast)] = i
    else:
        if lastnumber in spoken_at.keys():
            #print(i,"here1",lastnumber,spoken_at)
            prelast = lastnumber
            lastnumber=i-spoken_at[lastnumber]
            spoken_at[int(prelast)] = i
        else:
            #print(i,"here2",lastnumber,spoken_at)
            prelast = lastnumber
            lastnumber = 0
            spoken_at[int(prelast)] = i
print(i,lastnumber)

