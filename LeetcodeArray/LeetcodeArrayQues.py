def MoveZeroes(nums):
    i = 0
    k = 0
    while k < len(nums):
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)
        else:
            i += 1
        k += 1  
    return nums         

# nums = [0,1,0,3,12]
nums = [0,0,1]
print("Moves all zero into last of array", MoveZeroes(nums))

def ThirdMaxNumber(arr):
    if len(arr) <= 2:
        return max(arr)
      
    a = list(set(arr))
    a.sort()
    n = len(a)
    ans = a[n-3]
    return ans      

# nums = [2,2,3,1]
# nums = [3,2,1]
# nums = [1,2]
# nums = [1,2,2,5,3,5]
# nums = [1,2,-2147483648]
nums = [-1,2,3]
print("Third max number of array is", ThirdMaxNumber(nums))

def MissingNumber(nums):
        nums.sort()
        res=None
        if(len(nums)==1):
            if(nums[0]==0):
                return 1
            else:
                return 0
        for x in range(0,len(nums)):
            
            if(nums[x]!=x):
                return x
            
        if(res==None):
            return len(nums)     
# nums = [3,0,1]
# nums = [0,1]
# nums = [9,6,4,2,3,5,7,0,1]
nums = [1,2,3,5]
print("Missing number of array", MissingNumber(nums))

def NumberDissappered(arr):
    n = len(arr)
    temp = [i for i in range(1,n+1)]
    arr.sort()
    arr = set(arr)
    ans = []
    for i in temp:
        if i not in arr:
            ans.append(i)

    if len(ans) > 0:
        return ans
    else:
        return n
    

# nums = [4,3,2,7,8,2,3,1]
nums = [1,1]
print("Find All Numbers Disappeared in an Array", NumberDissappered(nums))

def MaxConsecutiveOnes(arr):
    ans = 0
    count = 0
    for i in arr:
        if i == 1:
            count += 1
        else:
            ans = max(ans, count)
            count = 0
    ans = max(count, ans)
    return ans            
    pass

# nums = [1,1,0,1,1,1]
nums = [1,0,1,1,0,1]
print("Max Consecutive Ones", MaxConsecutiveOnes(nums))

def AssignCookies(g,s):
    # g.sort()
    # s.sort()
    i = 0

    for j in range(len(s)):
        if i < len(g) and g[i] <= s[j]:
            i += 1
    return i        

g = [1,2,3]
s = [1,1]
# g = [1,2]
# s = [1,2,3]
print("Assign cookies", AssignCookies(g,s))
ans = []
def subsets(nums):
    ans =[[]]
            
    for i in nums:
        for j in range(len(ans)):
            ans.append(ans[j] + [i])
            
    return ans

def HelperSubset(arr, temp, i):
    if i == len(arr):
        ans.append(temp)
        return ans

    rec1 = HelperSubset(arr, temp+arr[i], i+1)
    rec2 = HelperSubset(arr, temp, i+1)    
    return rec1 + rec2
nums = [1,2,3]
print("subse or array", subsets(nums))

n = 15
ans = [None for i in range(n+1)]
print(ans)
def fib(n):
    if ans[n] == None:
        if n <= 1:
            ans[n] = n
        else:
            ans[n] = fib(n-1) + fib(n-2) 

    return ans[n]                   

print(fib(n))
print(ans)