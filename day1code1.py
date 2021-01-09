my_dict = {}
for i in range(200):
    my_dict[int(input())]=True
for key in my_dict.keys():
    if 2020-key in my_dict.keys():
        print(key*(2020-key))
        break
