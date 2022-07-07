# Problem statement: 
# User inputs daily temperatures, 
# we need to calculate average temperature and number of days that have crossed the average temperature.

# Solution without using array/lists
from numpy import average


numDays = int(input("How many day's temperature? "))
total = 0
for i in range(1, numDays+1):
    dayTemp = int(input("Day "+str(i)+"'s high temperature: ")) 
    total += dayTemp
average = round(total/numDays, 2)
print("Average: ", average)

# With above approach we can get avg but can't count #days with > avg cuz that needs a second pass through data.
# which we did not maintain. Taking input once more for this would be a bad approach. 
# So, here comes array/list into the picture.

numDays = int(input("How many day's temperature? "))
total = 0
temp = []
for i in range(numDays):
    dayTemp = int(input("Day "+str(i+1)+"'s high temperature: "))
    temp.append(dayTemp)
    total += temp[i]
average = round(total/numDays, 2)
print("Average: ", average)
above = 0
for i in temp:
    if i > average:
        above += 1
print(str(above) + " day(s) above average")


