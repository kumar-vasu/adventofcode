import re
earliest_departure_timestamp = int(input())
temp = input()
temp = temp.replace("x,","")
buses = re.split(",",temp)
for i in range(len(buses)):
    buses[i]=int(buses[i])
earliest = [0,1000000000000]
for i in range(len(buses)):
    earliest_bus_departure = 0
    while earliest_bus_departure < earliest_departure_timestamp:
        earliest_bus_departure+=buses[i]
    if earliest_bus_departure < earliest[1]:
        earliest[1] = earliest_bus_departure
        earliest[0] = buses[i]
print(earliest[0]*(earliest[1]-earliest_departure_timestamp))
