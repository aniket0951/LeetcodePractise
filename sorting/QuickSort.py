def QuickSort(arr):
    if len(arr) <=1:
        return arr
    
    pivot = arr.pop()
    
    greater = []
    loweat = []

    for i in range(len(arr)):
        if arr[i] > pivot:
            greater.append(arr[i])
        else:
            loweat.append(arr[i])          

    left = QuickSort(loweat)
    print(left)
    return arr

    pass

arr = [4, 1, 3, 9, 7]
print("Quick sort is", QuickSort(arr))

def SearchInSort(arr, K):

    l = 0
    r = len(arr) - 1
    while l < r:
        mid = l + (r-l) // 2
        if arr[l] == K or arr[r] == K:
            return 1
        if arr[mid] == K:
            return 1
        elif arr[mid] < K:
            l = mid + 1
        else:
            r = mid - 1
    return -1

K = 6
arr = [1,2,3,4,6]   
# arr = [1,3,4,5,6]
# K = 2         
print("search in sorted array is", SearchInSort(arr, K))    