def check26th(element,cache):
    for key in cache.keys():
        if element - key in cache.keys():
            return True
    return False

portoutput = []
#form input array
while True:
    try:
        portoutput.append(int(input()))
    except EOFError:
        break
#initialize a cache
cache = {}
#initialize weaklink
weaklink = 0
# edges to zero
leftedge = 0
cache[int(portoutput[0])]=True
rightedge = 0
#while right edge is lest than length of input array
while rightedge < len(portoutput)-1 :
    #if left-right +1 is less than 25 expand ie move the right edge .continue
    if (rightedge - leftedge)+1 < 25:
        rightedge +=1
        cache[int(portoutput[rightedge])]=True
        continue
    #if its 25 check the 26 element
    else:
        if not check26th(int(portoutput[rightedge+1]),cache):
            weaklink = int(portoutput[rightedge+1])
            break
        else:
            del cache[int(portoutput[leftedge])]
            leftedge+=1
    #postcheck move the left edge one bit and continue
#reset left edge and right edge
leftedge = 0
rightedge = 1
#keep tab of max and min
maxi=portoutput[leftedge]
mini = portoutput[rightedge]
#and sum
sum = portoutput[rightedge]+portoutput[leftedge]
print(weaklink,len(portoutput))
#while right edge is less than len
while rightedge < len(portoutput)-1:
    print(leftedge,rightedge)
#if sum of elements between left and right < weaklink. increase right
    if sum < weaklink or rightedge == leftedge:
        rightedge += 1
        if portoutput[rightedge]>maxi:
            maxi = portoutput[rightedge]
        if portoutput[rightedge]<mini:
            mini = portoutput[rightedge]
        sum += portoutput[rightedge]
        print("sum1",sum)
        continue
    if sum > weaklink:
        if portoutput[leftedge] == mini:
            mini = min(portoutput[leftedge+1:rightedge+1])
        if portoutput[leftedge] == maxi:
            maxi = max(portoutput[leftedge+1:rightedge+1])
        sum -= portoutput[leftedge]
        print("sum2",sum)
        leftedge+=1
        continue
#if sum of element = link print max multiply min
    if sum == weaklink:
        print(mini + maxi)
        break
#
