def check26th(element,cache):
    for key in cache.keys():
        if element - key in cache.keys():
            return True
    return False

portoutput = []
#form input array
while True:
    try:
        portoutput.append(input())
    except EOFError:
        break
#initialize a cache
cache = {}
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
            print(portoutput[rightedge+1])
            break
        else:
            del cache[int(portoutput[leftedge])]
            leftedge+=1
    #postcheck move the left edge one bit and continue
