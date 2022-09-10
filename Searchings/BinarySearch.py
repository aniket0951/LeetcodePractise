def BinarySearch(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        else:
            if arr[mid] < target:
                left = mid
            else:
                right = mid

    return -1                    

nums, target = [-1,0,3,5,9,12],  9
print("Binary Search target is present", BinarySearch(nums, target))

def SearchAndInsert(arr, target):
    l = 0
    u = len(arr) -1

    while l <= u:
        mid = (l+u) // 2

        if arr[mid] < target:
            ans = int(target - arr[mid])
            if len(arr) >= ans:
                return ans
        else:
            u = mid        
    
    pass

# nums, target = [1,3,5,6],  5
# nums, target = [1,3,5,6],  2
# nums, target = [1,3,5,6],  7
nums, target = [1,3,5,6],  0
print("Search and insert is", SearchAndInsert(nums, target))