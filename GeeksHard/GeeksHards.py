from re import L


def MaximumSubsetXOR(arr):
    for i in range(len(arr)):
        ans = i ^ arr[i]
        print(ans)
    pass

# arr =[2,4,5]
arr = [9,8,5]
print("maximum subset of xor is", MaximumSubsetXOR(arr))

def countSubArrayProductLessThanK(arr,n, k):
    s = 0
    e = 0
    p = 1
    res = 0

    while e < len(arr):
        p = p * arr[e]
        if p >= k:
            while s < e and p>=k:
                p = p/arr[s]
                s += 1
        if p < k:
            l = e - s + 1
            res += l
            e += 1

        
    return res                

# k = 10
# a = [1, 2, 3, 4]
k = 100
a = [1, 9, 2, 8, 6, 4, 3]
print("Count the subarrays having product less than k", countSubArrayProductLessThanK(a, len(a), k))

def MedianOfTwoArray(arr1, arr2):
        A = arr1
        B = arr2
        m = len(A)
        n = len(B)

        if m > n:
            A, B, m, n = B, A, n, m
        
        left_A = 0
        right_A = m

        while left_A <= right_A:
            partition_A = (left_A + right_A) // 2
            partition_B = (m + n + 1) // 2 - partition_A

            max_left_A = A[partition_A - 1] if partition_A != 0 else -float('inf')
            min_right_A = A[partition_A] if partition_A != m else float('inf')

            max_left_B = B[partition_B - 1] if partition_B != 0 else -float('inf')
            min_right_B = B[partition_B] if partition_B != n else float('inf')

            if max_left_A > min_right_B:
                right_A = partition_A - 1
            elif max_left_B > min_right_A:
                left_A = partition_A + 1
            else:
                if (m + n) & 1:
                    return int(max(max_left_A, max_left_B))
                else:
                    
                    res= (max(max_left_A, max_left_B) + min(min_right_A, min_right_B)) / 2.0
                    if res.is_integer():
                        return int(res)
                    return res

# array1 = [1,5,9]
# array2 = [2,3,6,7]
# array1 = [4,6]
# array2 = [1,2,3,5]
array1 = [2]
array2 = [4]
print("Median of two sorted array is", MedianOfTwoArray(array1, array2))


def CountSmallerElement(arr):
    count = 0
    ans = []
    i = 0
    j = 1
    while i < len(arr):
        if j == len(arr):
            ans.append(count)
            count = 0
            i += 1
            j = i + 1
        elif arr[j] < arr[i]:
            count += 1
            j += 1
        else:
            j += 1
    return ans            

arr = [12, 1, 2, 3, 0, 11, 4]
# arr = [1, 2, 3, 4, 5]
print("Count smaller element at right side ", CountSmallerElement(arr))

def smallestpositive(arr):
    arr.sort()
    ans = 1
    for i in arr:
        if ans < i:
            return ans
        else:
            ans += i
    return ans            
arr = [1, 10, 3, 11, 6, 15]
print("smallest positive number and missing or not sum of two or more elements", smallestpositive(arr))

def maxSubarrayXOR(arr):
    x = 0
    while True:
        y = max(arr)
        if y == 0:
           return x
        x = max(x, x ^ y)
        arr = [min(z, z ^ y) for z in arr]
    return x

# arr = [2,4,5]
arr = [9,5,8]
print("Maximum subset XOR", maxSubarrayXOR(arr))

def findMaxLen(string):
    stack = []
    ans = 0
    for i in string:
        if i == "(":
            stack.append(i)
        else:
            if len(stack) > 0:
                top = stack[-1]
                if top == "(":
                    stack.pop()
                ans += 2
    return ans                
    pass

# S = "(()("
S = "()(())("
print("IPL 2021 - Final", findMaxLen(S))
