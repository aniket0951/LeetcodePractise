def LongestPalindromInt(arr):
    return Helper(arr,0,len(arr)-1,0)

def Helper(arr, i, j,count):
    if i > j:
        return arr
    
    if arr[i] == arr[j]:
        count +=1 
        i += 1
        j -= 1
    else:
        del arr[j]
        j -= 1

  
    return Helper(arr, i, j, count)   
    # Helper(arr, i+1, j, count)

# arr = [2, 3, 7, 3, 2, 12, 24]
       # 24,12,2,3,7,3,2
arr = [12, 4, 4, 3, 14]
print("Longest palindrom element in arr", LongestPalindromInt(arr))

def subsetsum(arr, curr_sum):
    return subsetHelper(arr, curr_sum, 0,0)

def subsetHelper(arr, cur_sum, temp, idx):
    if cur_sum == temp:
        return True
    
    if idx >= len(arr):
        return False

    call1 = subsetHelper(arr, cur_sum, temp+arr[idx], idx+1)
    call2 = subsetHelper(arr, cur_sum, temp, idx+1)
    return call1 or call2    


# arr = [3, 34, 4, 12, 5, 2]
# s = 9
arr = [3, 34, 4, 12, 5, 2]
s = 30
print("subset sum of array is", subsetsum(arr,s))