# 1. Missing Number - from a list of integers from 1 to n, find the missing number
# Hint: 1+2+3+....+n = n(n+1)/2
myList = [1, 2, 3, 5, 6, 7, 8, 9, 10]
def findMissing(list, n):
    sum1 = (n*(n+1))//2
    sum2 = sum(list)
    print(sum1 - sum2)
findMissing(myList, 10) # or remove n arg and pass max(mylist) to sum1 var

