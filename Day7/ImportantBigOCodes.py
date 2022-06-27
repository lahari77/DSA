#Question1
def foo(array):
    sum = 0
    product = 1
    for i in array:
        sum += i
    for i in array:
        product *= i
    print("Sum = "+str(sum)+", Product = "+str(product))

ar1 = [1,2,3,4]
foo(ar1)

# Ans: Time complexity: O(n+n) = O(2n) = O(n) - after removing constant ( as one loop is exec after other len of array times i.e n times, remaining all O(1))

#Question2

def printPairs(array):
    for i in array:
        for j in array:
            print(str(i)+","+str(j))

# Ans: Time complexity: O(n*n) = O(n^2)( as one loop is exec inside other len of array times i.e n*n times, remaining all O(1))

#Question3
def printUnorderedPairs(array):
    for i in range(0,len(array)):
        for j in range(i+1,len(array)):
            print(array[i] + "," + array[j])

# Ans: Time complexity: O(n * n-1 ) = O(n^2 + n) = O(n^2) ( iteration count used, outside loop: ntimes, inside: n-1 as starting from i+1, remaining all O(1))

#Question4
def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            if arrayA[i] < arrayB[j]:
                print(str(arrayA[i]) + "," + str(arrayB[j]))

# common mistake --> assuming it's n^2 but it's not cuz observe that loops aren't iterating on same lenth arrays sooo,
# a = len(arrA)
# b = len(arrB)
# Ans: O(a*b)

arrayA = [1,2,3,4,5]
arrayB = [2,6,7,8]

#Question5
def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            for k in range(0,100000):
                print(str(arrayA[i]) + "," + str(arrayB[j]))

# printUnorderedPairss(arrayA,arrayB)

# common mistake --> assuming it's n^2 but it's not cuz observe that loops aren't iterating on same lenth arrays sooo,
# a = len(arrA)
# b = len(arrB)
# k = 100,000 so whatever the number is it's fixed already so constant
# Ans: O(a*b)


#Question6
def reverse(array):
    for i in range(0,int(len(array)/2)):
        other = len(array)-i-1
        temp = array[i]
        array[i] = array[other]
        array[other] = temp
    print(array)

reverse(arrayA)

# common mistake --> assuming it's directly n, but it's not cuz observe that loop isn't iterating on full length( 1/2 ) sooo,
# Ans: O(n/2) = O(n)

#Question8

def factorial(n):
    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(3))

# say complexity of func = M(n)
# all other statements - O(1)
# In return statement -> M(n-1)
# so, M(n) = O(1) + M(n-1)
# M(0) = O(1)
# M(n-1) = O(1) + M((n-1) -1)
# M(n-2) = O(1) + M((n-2) -1)
# with above 2 statements,
# M(n) = 1 + M(n-1)
#       = 1 + (1 + M((n-1) -1))
#       = 2 + M(n-2)
#       = 2 + 1 + M((n-2) -1)
#       = 3 + M(n-3)
#       = a + M(n-a)
# for n,= n + M(n-n) ( we took n cuz we need to find M(n) for that M should be romoved from RHS so to make it ) take a as n)
#       = n = O(n) 

#Question9
def allFib(n):
    for i in range(n):
        print(str(i)+":, " + str(fib(i)))

def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)

# Ans: for n>1 for every n, 2^n calls are made
# so, 2^1 + 2^2 + ..... + 2^n = 2^(n+1) - 1 - 1 ( cuz no 2^0 included in adding as per formula)
#                               = 2^(n+1) = O(2^n)

allFib(4)

#Question10
def powersOf2(n):
    # print("n:"+str(n))
    if n < 1:
        return 0
    elif n == 1:
        print(1)
        return 1
    else:
        prev = powersOf2(int(n/2))
        # print("prev:"+str(prev))
        print(prev)
        curr = prev*2
        print(curr)
        return curr

powersOf2(50)

# powersOf2(50) = 32*2 = 8 <----
#       ||
# powersOf2(25) = 16*2 = 32 <----
#       ||
# powersOf2(12) = 8*2 = 16 <----
#       ||                     |
# powersOf2(6) = 4*2 = 8   <----
#       ||                     |
# powersOf2(3) = 2*1 = 2   <----
#       ||                     |
# powersOf2(1) = 1    ----------