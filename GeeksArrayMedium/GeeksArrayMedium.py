
def MergeKSortedArray(arr):
    temp = []
    for i in range(len(arr)):
        for j in arr[i]:
            temp.append(j)

    temp.sort()           
    return temp

arr=[[1,2,3,4],[2,2,3,4],[5,5,6,6],[7,8,9,9]]
print("Merge k sorted array", MergeKSortedArray(arr))

def MinimumSwapKTogether(arr, k):
    count = 0
    n = len(arr)
    for i in range(0, n) :
        if (arr[i] <= k) :
            count = count + 1
    bad = 0
    for i in range(0, count) :
        if (arr[i] > k) :
            bad = bad + 1
    ans = bad
    j = count
    for i in range(0, n) :
         
        if(j == n) :
            break
        if (arr[i] > k) :
            bad = bad - 1

        if (arr[j] > k) :
            bad = bad + 1
         
        ans = min(ans, bad)
 
        j = j + 1
 
    return ans

# arr = [2, 1, 5, 6, 3] 
# K = 3
arr = [2, 7, 9, 5, 8, 7, 4] 
K = 6
# arr = [10, 12, 20, 20, 5, 19, 19, 12, 1, 20,1] 
# K = 1
# arr = [4, 16, 3, 8, 13, 2, 19, 4, 12, 2, 7, 17, 4, 19, 1]
# K = 9
print("Minimum swap k together", MinimumSwapKTogether(arr, K))

print((6//2) - 1)

def KthLargestElement(arr, k):
    temp = []
    count = 0
    if k <= 1:
        temp.append(max(arr))
        return temp
    
    arr.sort()
    while count < k:
        res = arr[-1]
        temp.append(res)
        arr.pop(-1)
        count += 1

    return temp        


arr = [12, 5, 787, 1, 23]
k = 2
# arr = [1, 23, 12, 9, 30, 2, 50]
# k = 3
print("K Largest element in the array is", KthLargestElement(arr, k))

def MinimumSum(arr):
    even = ""
    odd = ""
    
    arr.sort()

    for i in range(len(arr)):
        if i % 2 == 0:
            even += str(arr[i])
        else:
            odd += str(arr[i])
    ans = int(even) + int(odd)
    return ans            
    pass

# arr = [6, 8, 4, 5, 2, 3]
arr = [5, 3, 0, 7, 4]
print("Minimum sum of array is", MinimumSum(arr))


def MaximumIndex(arr):

    n = len(arr)
    leftMin = [0]*n
    leftMin[0] = arr[0]
    for i in range(1,n):
        leftMin[i] = min(leftMin[i-1], arr[i])
    maxDist = - 2**32
    i = n-1
    j = n-1
    
    while(i>=0  and  j>=0):
        if(arr[j] >= leftMin[i]):
            maxDist = max(maxDist, j-i)
            i-=1
        else:
            j-=1
            
    return maxDist   

arr = [1, 10]
# arr = [34, 8, 10, 3, 2, 80, 30, 33, 1]
# arr = [65, 6, 74, 94, 56, 89, 9, 63, 75, 25, 34, 68, 93, 48, 16]
print("Maximum index of array is", MaximumIndex(arr))

def CountInversion(arr):
        n = len(arr)
        i = 0
        j = 1
        temp = arr.copy()
        temp.sort()
        
        if arr == temp:
            return 0
        
        ans = 0
        
        while i < n:
            if j == n:
                i += 1
                j = i+1
                continue
            elif arr[i] > arr[j]:
                ans += 1
                j += 1
            else:
                j += 1
        return ans         


arr = [2, 4, 1, 3, 5]
print("Count inversion",CountInversion(arr))

def CelebrityProblem(matrix):  
    n =  len(matrix)
    c = 0
    for i in range(n):
        if M[c][i] == 1:
            c = i
        
    for i in range(n):
        if i!=c and (M[c][i] == 1 or M[i][c] == 0):
            return -1
        
    return c  

M = [[0, 1, 0],
         [0, 0 ,0], 
         [0, 1, 0]]

print("the celebrity problem is", CelebrityProblem(M))

def NextPermutation(arr):
    n = len(arr)
    k = n - 2
    while k >= 0:
        if arr[k] < arr[k + 1]:
            break
        k -= 1
    if k < 0:
        arr = arr[::-1]
    else:
        for l in range(n - 1, k, -1):
            if arr[l] > arr[k]:
                break     
        arr[l], arr[k] = arr[k], arr[l]
        arr[k + 1:] = reversed(arr[k + 1:])

    return arr

# arr = [1, 2, 3, 6, 5, 4]
arr = [3, 2, 1]
print("Next permutation is", NextPermutation(arr))

def FindkthSmallestElement(ranges, queries):
    i = 0
    temp = []
    while i < len(ranges):
        if ranges[i][0] not in temp:
            temp.append(ranges[i][0])
        start = ranges[i][0]
        end = ranges[i][-1]
        
        for j in range(start, end):
            res = temp[-1] + 1
            if res not in temp:
                temp.append(res) 
 
        i += 1
    
    ans = []
    for j in queries:
        res = j - 1
        if res > len(temp) - 1:
            ans.append(-1)
        else:
            ans.append(temp[res])   
    return ans    
    

ranges = [[1, 4], [6, 8]]
queries = [2, 6, 10]
# ranges = [[2, 6], [5, 7]]
# queries = [5, 8]
print("Find k-th smallest element in given n ranges", FindkthSmallestElement(ranges, queries))

def CountTripllet(arr, sums):
    count = 0

    for i in range(len(arr)):
        j = i + 1
        k = len(arr) - 1
        if j == k:
            break
        while j < k:
            if arr[i] + arr[j] + arr[k] < sums:
                count += 1

            k -= 1    
    if count == 0:
        return 1
    return count

# sums = 2
# arr = [-2, 0, 1, 3]
# sums = 12
# arr = [5, 1, 3, 4, 7]
sums = 12
arr = [5, 1]
print("Count triplets with sum smaller than X", CountTripllet(arr, sums))

import sys
def BuyAndSellShareTwice(arr):
    first_buy = -sys.maxsize;
    first_sell = 0;
    second_buy = -sys.maxsize;
    second_sell = 0
 
    for i in range(len(arr)):
        first_buy = max(first_buy, -arr[i])
        first_sell = max(first_sell, first_buy + arr[i])
        second_buy = max(second_buy, first_sell - arr[i]);
        second_sell = max(second_sell, second_buy + arr[i]);
 
     
    return second_sell;    

arr = [10, 22, 5, 75, 65, 80]
print("Buy and Sell a Share at most twice", BuyAndSellShareTwice(arr))

def MaximumProductSubset(arr):
    a = arr
    n = len(a)
    ncount = 0
    prod = 1
    mneg = -11
    zero = 0
    for i in range(n):
        if a[i] == 0:
            zero += 1
        else:
            prod *= a[i]
            if a[i] < 0:
                mneg = max(mneg, a[i])
                ncount += 1
                    
    if prod == -1 or n - zero == 1:
        return max(a)
            
    if ncount%2 == 1:
        return (prod//mneg)%(10**9 + 7)
    else:
        return prod%(10**9 + 7)


# arr = [-1, -1, -2, 4, 3]
# arr = [-1,0]
# arr = [-5, 1, -3, -1, 0, -2, 4, 0, 1]
arr = [2, -2, 0, -5, -4, -3, -2, -5, -4]
print("maximum subset of array is", MaximumProductSubset(arr))


# lower_value = int(input ("Please, Enter the Lowest Range Value: "))  
# upper_value = int(input ("Please, Enter the Upper Range Value: "))  
  
# print ("The Prime Numbers in the range are: ")  
# for number in range (lower_value, upper_value + 1):  
#     if number > 1:  
#         for i in range (2, number):  
#             if (number % i) == 0:  
#                 break  
#         else:  
#             print (number)  

def buyMaximumProducts(price, k):
    n = len(price)
    arr = []
    
    for i in range(n):
        arr.append([i + 1, price[i]])

    # Sort based on the price of stock
    arr.sort(key = lambda x: x[1])
    print(arr)    
    total_purchase = 0
    for i in range(n):
        P = min(arr[i][0], k//arr[i][1])
        print(P)
        total_purchase += P
        k -= (P * arr[i][1])

    return total_purchase                       

price = [10, 7, 19]
k = 45
# price = [7, 10, 4]
# k = 100
print("Buy Maximum Stocks if i stocks can be bought on i-th day", buyMaximumProducts(price, k))

def maxMeetings(s, f):
    l=[]
    ans=[]
    for i in range(len(s)):
        l.append([s[i],f[i],i+1])

    l.sort(key=lambda val:val[1])
    k=l[0][1]
    ans.append(l[0][2])
    for i in range(1,len(l)):
        if k<l[i][0]:
            ans.append(l[i][2])
            k=l[i][1]
    ans.sort()
    return ans

# S = [1,3,0,5,8,5]
# F = [2,4,6,7,9,9]
# S = [3]
# F = [7]
S = [12, 6, 16, 12, 6, 9, 16, 6, 17, 5]
F = [17, 13, 16, 18, 17, 10, 18, 12, 18, 11]
print("Maximum Meetings in One Room", maxMeetings(S,F)) 

def calculatespan(price):
        n = len(price)
        a = price
        stack=[]
        span=[1]*n
        stack.append(0)

        for i in range(1,n):
            while len(stack)!=0 and a[stack[-1]]<=a[i]:
                stack.pop()
            if len(stack)==0:
                span[i]=(i+1)
            else:
                span[i]=(i-stack[-1])
            stack.append(i)
        return span
#1 1 1 2 1 4 6
price = [100, 80, 60, 70, 60, 75, 85]
#1 1 2 4 5 1
# price = [10, 4, 5, 90, 120, 80]
# price = [68, 735, 101, 770, 525, 279, 559, 563, 465, 106, 146, 82, 28, 362, 492, 596, 743, 28, 637, 392,205 ,703 ,154 ,293 ,383 ,622 ,317 ,519 ,696 ,648 ,127 ,372 ,339 ,270 ,713 ,68 ,700 ,236, 295, 704, 612, 123]
print("Stock span problem", calculatespan(price))

def countPairs(x, y):
    tempx = []
    tempy = []
    j = 0
    while j < len(Y):
        for i in range(len(x)):
            res = pow(x[i], y[j])
            tempx.append(res)
        j += 1    
    
    j = 0
    while j < len(y):
        for i in range(len(x)):
            res = pow(x[i], y[j])
            tempy.append(res)
        j += 1    

    i = 0
    j = 0
    count = 0
    while i < len(tempx) and j < len(tempy):
        if tempx[i] > tempy[j]:
            count += 1

        i += 1
        j += 1
    return count        


X = [2, 3, 4, 5]
Y = [1, 2, 3]
print("count pairs", countPairs(X, Y))

def canPair(arr, k):
    stack = []
    stack.append(arr[0])
    i = 1
    flag = False
    while i < len(arr):
        last = stack[-1]
        if (last + arr[i]) % k == 0:
            flag = True
            stack.pop()
        else:
            stack.append(arr[i])

        i += 1    
    return flag             

# arr = [9, 5, 7, 3]
# k = 6
arr = [2, 4, 1, 3]
k = 4
print("Array Pair Sum Divisibility Problem", canPair(arr, k))

def find3Numbers(arr, x):
    arr.sort()
    a = arr[0]

    for i in range(1,len(arr)):
        for j in range(i, len(arr)):
            res = arr[i] + arr[j] + a
            if res == x:
                print(arr[i], arr[j], a)
                return True
        # a = arr[i]

    return False            


# X = 13
# arr = [1, 4, 45, 6, 10, 8]
# X = 6
# arr = [3, 2, 2, 3]
X = 3
arr = [1, 2, 2, 1]
print("Triplet Sum in Array", find3Numbers(arr, X))


def lenOfLongSubarr(arr, k):
    ans = 0
    i = 0
    j = 0
    res = 0

    while j < len(arr) and i < len(arr):
        res = res + arr[j]
        if res == k:
            temp = (j-i+1)
            ans = max(ans, temp)
            j += 1
        elif res < k:
            j += 1
        elif res > k:
            res -= arr[i]
            i += 1
    return ans                

A = [10, 5, 2, 7, 1, 9]
K = 15
# A = [-1, 2, 3]
# K = 6
print("Longest Sub-Array with Sum K", lenOfLongSubarr(A, K))

def smallestSumSubarray(arr):
    min_el = min(arr)
    res = 100000000
    stack = []
    i = 0
    while i < len(arr):
        if len(stack) <= 0:
            stack.append(arr[i])
            i += 1
        else:
            temp = sum(stack)
            if (temp + arr[i]) < res:
                res = temp + arr[i]
                stack.append(arr[i])
                i +=1 
            else:
                stack.pop(0)
    ans = min(min_el, res)
    return ans

# arr = [3,-4, 2,-3,-1, 7,-5]
arr = [2, 6, 8, 1, 4]
print("Smallest sum contiguous subarray", smallestSumSubarray(arr))

def kthSmallestNum(arr, query):
    temp = []
    for i in range(len(arr)):
        start = arr[i][0]
        end = arr[i][1]
        if start not in temp:
            temp.append(start)
        curr = start
        for j in range(start, end-1):
            curr = (curr+1)
            if curr not in temp:
                temp.append(curr)
            arr[i].insert(j, curr)    
        if end not in temp:
            temp.append(end)    
    
    
    temp.sort()
    n = len(temp)
    arr.clear()
    arr =  temp.copy()
    temp.clear()
    for i in range(len(query)):
        res = query[i] - 1
        if n > res:
            temp.append(arr[res])
        else:
            temp.append(-1)    
    return temp


range_ = [[1, 4], [6, 8]]
queries = [2, 6, 10]
# range_ = [[2, 6], [5, 7]] 
# queries = [5, 8]
# range_ = [[29 ,40]]
# queries = [3, 4, 8, 10, 11, 13, 14, 18, 19, 20]
print("Kth smallest elements", kthSmallestNum(range_, queries))