def CountOfTriplest(arr):
    count = 0

    s = set(arr)

    for i in range(len(arr) - 1):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] in s:
                count += 1
    return count                                        

arr = [1, 5, 3, 2]
# arr = [2, 3, 4]
print("Count of triplest is", CountOfTriplest(arr))

def MergeListWithoutUsingExtraSpace(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    i = 0
    j = 0
    k = n - 1
    while (i <= k and j < m):
        if (arr1[i] < arr2[j]):
            i+=1
        else:
            temp = arr2[j]
            arr2[j] = arr1[k]
            arr1[k] = temp
            j += 1
            k -= 1
        
    arr1.sort()
    arr2.sort()
    return arr1, arr2


arr1 = [1, 3, 5, 7] 
arr2 = [0 ,2, 6, 8, 9]
print("Merge two list without using extra space", MergeListWithoutUsingExtraSpace(arr1, arr2))

def RearrangeArrayAlternately(arr):
    n = len(arr)
    temp = n*[None]
 
    small, large = 0, n-1
    flag = True
 
    for i in range(n):
        if flag is True:
            temp[i] = arr[large]
            large -= 1
        else:
            temp[i] = arr[small]
            small += 1
 
        flag = bool(1-flag)

    for i in range(n):
        arr[i] = temp[i]
    return arr  

# arr = [1,2,3,4,5,6]
arr = [10,20,30,40,50,60,70,80,90,100,110]
# arr = [1969 ,2677 ,3142 ,4631 ,4764 ,5748 ,6476 ,6487]
print("rearrange the array alternately", RearrangeArrayAlternately(arr))

def TwoNonRepeating(arr):
    sums = 0
    for i in arr:
        sums = sums ^ i
    
    
    sums = (sums & -sums)
    
    sum1 = 0
    sum2 = 0
    for i in range(len(arr)):
        if (arr[i] & sums) > 0:
            sum1 = sum1 ^ arr[i]
        else:
            sum2 = sum2 ^ arr[i]    
    return sum1, sum2

    pass

arr = [2, 3, 7, 9, 11, 2, 3, 11]
print("Two non-repeating element in array is", TwoNonRepeating(arr))