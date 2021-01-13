def Binary_to_decimal(binary):
    decimal = 0
    for i in range(0,len(binary)):
        decimal = decimal + int(binary[len(binary)-1-i])*(2**i)
    return decimal
    
seatid = set()
smallestseatid = 866
largestseatid = 866
while True:
    try:
        seat = input()
        row = seat[:7]
        column = seat[7:]
        row = row.replace("B","1")
        row = row.replace("F","0")
        row=Binary_to_decimal(row)
        column = column.replace("R","1")
        column = column.replace("L","0")
        column=Binary_to_decimal(column)
        seatid.add(row*8+column)
        if smallestseatid > row*8+column:
            smallestseatid = row*8+column
    except EOFError:
        break
for i in range (smallestseatid,largestseatid+1):
    if i not in seatid:
        print(i)
    
