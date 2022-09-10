def alternatePosNegNumber(arr):
    pos = []
    neg = []

    for i in range(len(arr)):
        if arr[i] < 0:
            neg.append(arr[i])
        else:
            pos.append(arr[i])

    i = 0
    j = 0
    k = 0
    while i < len(neg) and j < len(pos):
        arr[k] = pos[j]
        j += 1
        k += 1
        arr[k] = neg[i]
        i += 1
        k += 1

    while j < len(pos):
        arr[k] = pos[j]
        j += 1
        k += 1

    while i < len(neg):
        arr[k] = neg[i]
        i += 1
        k += 1
    return arr


A = [9, 4, -2, -1, 5, 0, -5, -3, 2]
# A = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
print(alternatePosNegNumber(A))

def SpecificDifferance(arr, k):
    arr.sort()
    temp = arr[::-1]
    i = 0
    j = 1
    ans = 0          

    while i < len(temp):
        if i == len(temp)-1:
            break
        else:
            res = abs(temp[i] - temp[i+1])
            if res < k:
                ans += temp[i]
                ans += temp[i+1]
                i += 2
            else:
                i += 1
    return ans                  

# arr = [3, 5, 10, 15, 17, 12, 9]
# k = 4
arr = [5, 15, 10, 300]
k = 12
print("Specfic diffrance is array", SpecificDifferance(arr, k))

def SmallestSubsetWithGreaterSum(arr):
    arr.sort()
    # [0,1,2,3,4]
    
    s = sum(arr)
    if s < 1:
        return len(arr)
    ans = 0
    s1 = 0
    j = len(arr) - 1
    while True:
        s = s - arr[j]
        s1 += arr[j]
        j -= 1
        ans += 1
        if s1 > s:
            break

    return ans    

# arr = [4,3,1,0,2]
# arr = [3,6,0,2]
arr = [0, 0]
# arr = [1, 0]
print("Smallest Subset with Greater Sum", SmallestSubsetWithGreaterSum(arr))

def MiniumSumDifferance(A,B):
    A.sort()
    B.sort()
    i = 0
    j = 0
    ans = 0
    while i < len(A) and j < len(B):
        res = abs(A[i] - B[j])
        ans += res
        i += 1
        j += 1
    return ans    


# A = [4,1,8,7]
# B = [2,3,6,5]
A = [4,1,2]
B = [2,4,1]
print("Minimum differance with sum", MiniumSumDifferance(A,B))

def MaxSumPathInTwoArray(arr1, arr2):
    i, j = 0,0
    result, sum1, sum2 = 0,0,0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sum1 += arr1[i]
            i += 1
        elif arr1[i] > arr2[j]:
            sum2 += arr2[j]
            j += 1
        else:
            result += max(sum1, sum2)
            sum1 = 0
            sum2 = 0
            while i < len(A) and j < len(B) and arr1[i] == arr2[j]:
                result += arr1[i]
                i += 1
                j += 1

    while i < len(arr1):
        sum1 += arr1[i]
        i += 1

    while j < len(arr2):
        sum2 += arr[j]
        j += 1

    result += max(sum1, sum2)
    return result        

A = [2,3,7,10,12]
B = [1,5,7,8]
print("Max sum path in two arrays", MaxSumPathInTwoArray(A, B))

def MaxmizeToys(arr, k):
    arr.sort()
    ans = 0
    for i in arr:
        if i<= k:
            ans += 1
            k = k - i
    return ans   

# k = 50
# arr = [1, 12, 5, 111, 200, 1000, 10]
k = 100
arr = [20, 30, 50]
print("Maximize toys purchase", MaxmizeToys(arr, k))
from collections import defaultdict
def SortAsscendingOrder(arr1, arr2):
    val_count, ans = defaultdict(int), []
    for item in A1: val_count[item] += 1
    for item in A2:
        if item in val_count:
            ans.extend([item] * val_count[item])
            del val_count[item]
    temp = []
    for key in val_count:
        temp.extend([key] * val_count[key])
    temp.sort()
    ans.extend(temp)
    return ans
A1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
A2 = [2, 1, 8, 3]
# A1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
# A2 = [99, 22, 444, 56]
print("Sort an array according to the other", SortAsscendingOrder(A1,A2))

def SumPairClosetX(arr, x):
    res_l, res_r = 0,0
    max_val = 100000000
    l,r,diff = 0,len(arr)-1, max_val

    while r > l:
        if abs(arr[l]+arr[r]-x) < diff:
            res_l = l
            res_r = r
            diff = abs(arr[l]+arr[r]-x)

        if arr[l] + arr[r] > x:
            r -= 1
        else:
            l += 1

    return f"{arr[res_l]}  {arr[res_r]}"                

    pass

arr = [10, 22, 28, 29, 30, 40]
x = 54
print("Sum pair closet x is", SumPairClosetX(arr, x))