def PalindromInteger(integer):
    old_num = integer
    Reverse = 0
    while(integer > 0):
        Reminder = integer % 10
        Reverse = (Reverse * 10) + Reminder
        integer = integer // 10

    if Reverse == old_num:
        return True
    else:
        return False


# integer = 121
# integer = -121
integer = 10
print("palindrom indeger is", PalindromInteger(integer))


def RemoveDuplicateEle(nums):

    left = 0

    for right in range(1, len(nums)):
        if nums[left] != nums[right]:
            nums[left + 1] = nums[right]
            left += 1

    return left + 1


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print("remove duplicate and replace them with _", RemoveDuplicateEle(nums))


def IntegerToRoman(num):
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    ans = ""
    for key, val in reversed(roman.items()):
        while num > 0:
            if val <= num:
                ans += (key)
                num -= val
            else:
                break
    return ans


num = 13
print("Integer to roman is", IntegerToRoman(num))


def RomanToInteger(roman_in):
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    prev = "I"
    result = 0

    for curr in roman_in[::-1]:
        if roman[curr] < roman[prev]:
            result = result - roman[curr]
        else:
            result = result + roman[curr]
        prev = curr
    return result            

# roman_in = "III"
roman_in = "LVIII"
print("Roman to integer is", RomanToInteger(roman_in))

def MissingFirstPositiveNum(arr):
    target = 1
    for i in arr:
         if i == target:
            target += 1
    return target

# arr = [7,8,9,11,12]
arr = [3,4,-1,1]
print("Missing first element is", MissingFirstPositiveNum(arr))

def ThreeSum(arr):
    if len(arr) <=1:
        return arr

    arr.sort()

    res = set()

    for ind, n in enumerate(arr):
        left = ind + 1
        right = len(arr) -1

        while left < right:
            cun_sum = arr[left] + arr[ind] + arr[right]
            if cun_sum == 0:
                res.add((arr[left], arr[ind], arr[right]))
                left +=1 
                right -=1 
            elif cun_sum < 0:
                left += 1
            else:
                right -= 1
    return res                   

nums = [-1,0,1,2,-1,-4]
print("Three sum ans is", ThreeSum(nums))

def MergeSortedArray(arr1, arr2, m,n):
    a1 = m - 1
    a2 = n - 1
    i = m+n -1

    while a2 >= 0 and a1 >= 0:
        if arr1[a1] >= 0 and arr2[a2] > arr1[a1]:
            arr1[i] = arr2[a2]
            a2 -= 1
            i -= 1
        elif arr1[a1] > arr2[a2]:
            arr1[i] = arr1[a1]
            a1 -= 1
            i -= 1
        elif arr1[a1] == arr2[a2]:
            arr1[i] = arr2[a2]
            i -= 1
            a2 -= 1
    
    if a2 == 0 and a1 < 0:
        arr1[i] = arr2[a2]
        a2 -= 1
        i -= 1


    return arr1        
                                            

# nums1 = [1,2,3,0,0,0] 
# m, n = 3, 3
# nums2 = [2,5,6]
# nums1 = [2,0]
# m = 1
# nums2 = [1]
# n = 1
nums1 = [4,5,6,0,0,0]
m = 3
nums2 = [1,2,3]
n = 3
print("Merge two sorted array is", MergeSortedArray(nums1, nums2, m, n))
print(len(nums2))

def BestTimetoBuyandSellStock(arr):
    ans = 0
    cur_stock = arr[0]
    for i in range(1, len(arr)):
        res = arr[i] - cur_stock
        if res > 0:
            ans = max(ans, res)
        else:
            cur_stock = arr[i]
    return ans            

prices = [7,1,5,3,6,4]
# prices = [7,6,4,3,1]
print("Best time to buy and sell stock", BestTimetoBuyandSellStock(prices))

def NonDecreasingArray(arr):
        cnt_violations=0        
        for i in range(1, len(nums)):                       
            if nums[i]<nums[i-1]:
                if cnt_violations==1:
                    return False
                cnt_violations+=1
                if i>=2 and nums[i-2]>nums[i]:
                    nums[i]=nums[i-1]                       
        return True              

# nums = [4,2,3]
# nums = [4,2,1]
nums = [3,4,2,3]
print("Non Decreasing array", NonDecreasingArray(nums))

def FirstAndLastPositionOfArray(arr, target):
      if(target not in nums):
        return [-1,-1]
			
      res=[]
		
      count=nums.count(target)-1
      res.append(nums.index(target))
      res.append(nums.index(target)+count)
		
      return res

nums = [5,7,7,8,8,10]
target = 8
# nums = [5,7,7,8,8,10]
# target = 6
print("Find First and Last Position of Element in Sorted Array with giving target", FirstAndLastPositionOfArray(nums, target))

def SingleNumbers(arr):

    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] == arr[j]:
                arr[i] = "_"
                arr[j] = "_"
    return arr            

nums = [2,2,1]
print("Single number without using any space ", SingleNumbers(nums))

def ContainsII(arr, k):
    data = dict()

    for i in range(len(arr)):
        if arr[i] in data:
            data[arr[i]] -= 1
        else:
            data[arr[i]] = 1

    m = None
    n = None            

    for k, v in data.items():
        if v > 0 :
            if m == None:
                m = v
            else:
                if n == None:
                    n = v
                    ans = abs(m -n)
                    if ans <= k:
                        return True
                    else:
                        n = None
    return False                          

# nums = [1,2,3,1]
# k = 3
nums = [1,2,3,1,2,3]
k = 2
print("Contains II ", ContainsII(nums, k))

def LengthOfLastword(s):
    s = s.split(' ')
    i = -1

    while i >= -len(s):
        if s[i]:
            return len(s[i])
        i -= 1           

# s = "Hello World"
s = "   fly me   to   the moon  "
print("Length of last word is", LengthOfLastword(s))

def SummaryRanges(arr):
    nums = arr
    res=[]
    s=""
        
    for i in range(len(nums)):
        if len(s)==0:
            s+=str(nums[i])
        if i==len(nums)-1 or nums[i+1]!=nums[i]+1:
            if str(nums[i])==s:
                res.append(s)
            else:
                s+="->"+str(nums[i])
                res.append(s)
            s=""
    return res    

nums = [0,1,2,4,5,7]
print("Summary ranges", SummaryRanges(nums))
import imp
from itertools import count, permutations
import sys
from typing import OrderedDict
def ThreeSumCloset(arr, target):
    arr.sort() 
    n = len(arr)
    closestSum = sys.maxsize 
    for i in range(n-2):
      j,k = i+1,n-1 
      while j<k:
        sum = arr[i]+arr[j]+arr[k] 
        
        if (abs(target-closestSum) > abs(target-sum)):
          closestSum = sum 
          
        if sum > target:
          k-=1 
        else:
          j+=1 
  
    return closestSum        
           


nums = [-1,2,1,-4]
target = 1
# nums = [0,0,0]
# target = 1
# nums = [1,1,1,0]
# target = 100 
# nums = [1,1,1,1]
# target = 4 
# nums = [1,1,1,0]
# target = -100

print("The sum that is closest to the target is ", ThreeSumCloset(nums, target))

def fourSum(arr, target):
    ans = set()
    i = 0
    j = len(arr) -1
    arr.sort()
    while i < j:
        l = i + 1
        r = j - 1
        if l == r:
            break
        while l < r:
            sum_ = arr[i] + arr[l] + arr[r] + arr[j]
            if sum_ == target:
                ans.add((arr[i], arr[l], arr[r], arr[j]))
                r -= 1
            elif sum_ > target:
                r -= 1
            elif sum_ < target:
                l += 1
        i += 1
        j -= 1
    ans = sorted(list(ans))
    return ans                    

# arr = [10,2,3,4,5,7,8]
# k =  23
arr = [0,0,2,1,1]
k = 3
print("4 sum of array is", fourSum(arr, k))

def removeDuplicates(arr):
    for i in range(len(arr)):
        count = 0
        for j in range(i,len(arr)):
            if arr[i] != "_":
                if arr[i] == arr[j]:
                    count += 1
                    if count >= 3:
                        arr[j] = "_"
                else:
                    break
    i = 0
    n = len(arr)
    while i < n:
        if arr[i] == "_":
            arr.remove(arr[i])
            n = len(arr)
        else:
            i +=1     
    return arr

nums = [0,0,1,1,1,1,2,3,3]
# nums = [1,1,1,2,2,3]
# nums = [1,1,1,2,2,3]
print("remove a duplicates from arr without changing a size of array", removeDuplicates(nums))


def groupAnagrams(arr):
    data = OrderedDict()
    for i in range(len(arr)):
        sort_word = "".join(sorted(arr[i]))
        if sort_word in data:
            data[sort_word].append(arr[i])
        else:
            data[sort_word] = []
            data[sort_word].append(arr[i])
    ans = []
    for i in data.values():
        ans.append(i)
    return ans        

strs = ["eat","tea","tan","ate","nat","bat"]
print("group anagram is", groupAnagrams(strs))

def mergeIntervals(intervals):
    intervals.sort()
    stack = []

    for i in range(len(intervals)):
        if len(stack) <= 0:
            stack.append(intervals[i])
        else:
            elem = stack[-1]
            if elem[1] >= intervals[i][0]:
                stack.pop()
                min_ = min(intervals[i][0], elem[0])
                max_ = max(intervals[i][1], elem[1])
                stack.append([min_, max_])
            else:
                stack.append(intervals[i])
    return stack                            

intervals = [[1,3],[2,6],[8,10],[15,18]]
# intervals = [[1,4],[4,5]]
# intervals = [[1,4],[5,6]]
# intervals = [[1,4],[0,0]]
print("Merge Intervals", mergeIntervals(intervals))

def minPathSum(grid):
        def f(i,j):
            if i==0 and j==0:
                return grid[0][0]
            if i<0 or j<0:
                return float('inf')
            if dp[i][j]!=-1:
                return dp[i][j]
            up=grid[i][j]+f(i-1, j)
            left=grid[i][j]+f(i, j-1)
            dp[i][j]=min(up,left)
            return min(up, left)
        dp=[[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        return f(len(grid)-1, len(grid[0])-1)   


# grid = [[1,3,1],[1,5,1],[4,2,1]]
# grid = [[1,2,3],[4,5,6]]
grid = [[1,2],[1,1]]

print("Minimum Path Sum", minPathSum(grid))

def maxProduct(nums):
        curmin, curmax = 1, 1
        res = max(nums)
        
        for i in nums:
            if i == 0:
                curmin, curmax = 1, 1
                continue
            temp = curmax * i
            curmax = max(temp, curmin*i, i)
            curmin = min(temp, curmin*i, i)
            # print(curmax, curmin)
            res = max(res, curmax)
        return res

nums = [2,3,-2,4]
# nums = [-2,0,-1]
# nums = [0,2]
print("Maximum Product Subarray", maxProduct(nums))


def zeroFilledSubarray(nums):
    dp = [-1]*len(nums)
    ans = 0
    for i in range(len(nums)):
        if i == 0 and nums[i] == 0:
            dp[i] = 1
            ans += dp[i]
        else:
            if nums[i] == 0 and dp[i-1] !=-1:
                dp[i] = dp[i-1]+1
                ans += dp[i]
            elif nums[i] == 0 and dp[i-1] == -1:
                dp[i] = 1
                ans += dp[i]
    # ans = 0
    # for i in range(len(dp)):
    #     if dp[i] != -1:ans+=dp[i]
    return ans                


# nums = [0,0,0,2,0,0]
# nums = [1,3,0,0,2,0,0,4]
# nums = [1,2,3,4,5,6,0,0,0]
# nums = [2,10,2019]
nums = [0, 0, 5, 5, 0, 0]
print("Number of Zero-Filled Subarrays", zeroFilledSubarray(nums))

def minSumSquareDiff(nums1, nums2, k1,k2):
    if k1 ==0 and k2 ==0:
        ans = 0
        for i in range(len(nums1)):
            res = (nums1[i] - nums2[i])**2
            ans += res
        return ans    
    else:
        pass

# nums1 = [1,2,3,4]
# nums2 = [2,10,20,19]
# k1 = 0
# k2 = 0
nums1 = [1,4,10,12]
nums2 = [5,8,6,9]
k1 = 1
k2 = 1
print("Minimum Sum of Squared Difference", minSumSquareDiff(nums1, nums2, k1, k2))

def equalPartition(arr):
    arr.sort()
    i = 0
    j = len(arr)-1
    mid = i + (j-i)//2 
    left = arr[:mid]
    right = arr[mid:]
    print(left, right, mid)
    # while True:
    #     if len(right) <=0:break
    #     a_sum = sum(left)
    #     b_sum = sum(right)
    #     if a_sum == b_sum:return "YES"
    #     if a_sum < b_sum:
    #         left.append(right[0])
    #         del right[0]
    # return "NO"        


# arr = [1, 5, 11, 5]
# arr = [1, 3, 5]
arr = [2, 4, 11, 10, 5]
print("Partition Equal Subset Sum", equalPartition(arr))

def maxSumIs(arr):
    dp = [0]*len(arr)
    dp[0] = arr[0]
    max_ = dp[0]

    for i in range(1,len(arr)):
        temp = 0
        for j in range(i):
            if arr[j] < arr[i]:
                temp = max(temp, dp[j])

        dp[i] = temp + arr[i]
        max_ = max(max_, dp[i])
    return max_                


# arr = [1, 101, 2, 3, 100]
# arr = [1,2,3]
arr = [2,3,5,7,1]
print("Maximum sum increasing subsequence", maxSumIs(arr))

def rearrangeArray(arr):
    neg = [i for i in arr if i < 0]
    pos = [i for i in arr if i > 0]
    k = 0
    j = 0
    for i in range(len(arr)):
        if i == 0:
            arr[i] = pos[k]
            k += 1
        else:
            prev = i-1
            if arr[prev] < 0:
                arr[i] = pos[k]
                k += 1
            elif arr[prev] > 0:
                arr[i] = neg[j]
                j += 1   
    return arr

nums = [3,1,-2,-5,2,-4]
# nums = [-1,1]
print("Rearrange Array Elements by Sign", rearrangeArray(nums))

def maxCoins(arr):
    dp = [-1]*len(arr)
    ans = 0
    n = len(arr)
    for i in range(n-1,-1,-1):
        res = max(arr[i-1], arr[i-2])
        ans += res
    return ans
    pass

arr = [8, 15, 3, 7]
print("Pots of Gold Game", maxCoins(arr))    

def diagonalSum(mat):
    n = len(mat)
    if n <=1:return mat[0][0]
    


# mat = [[5]]
mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
print("Matrix Diagonal Sum", diagonalSum(mat))    

def totalSteps(nums):
    count = 0
    i = 1

    while i < len(nums):
        if nums[i] > nums[i-1]:
            i += 1
        elif nums[i] < nums[i-1]:
            j = i+1
            while j < len(nums):
                if nums[i-1] > nums[j]:
                    j += 1
                else:
                    i = j
                    break
            count += 1
        i += 1
    return count        


# nums = [5,3,4,4,7,3,6,11,8,5,11]
# nums = [4,5,7,7,13]
nums = [10,1,2,3,4,5,6,1,2,3]
print("Steps to Make Array Non-decreasing", totalSteps(nums))

def triangularSum(nums):
    n = len(nums)
    while n > 1:
        i = 0
        while i < n:
            if i >= n-1 or i == n-1:
                break
            else:
                res = (nums[i] + nums[i+1])%10
                nums[i] = res
                i += 1
        nums = nums[:i]
        n = len(nums)        
    return nums    

# nums = [1,2,3,4,5]
nums = [5]
print("Find Triangular Sum of an Array", triangularSum(nums))

def removeKdigits(num, k):
    res = []
    n = len(num)
    
    if n == k: return "0"
    
    for i in range(n):
        while k and res and res[-1] > num[i]:
            res.pop()
            k -= 1
        res.append(num[i])
    
    while k:
        res.pop()
        k -= 1
        
    return "".join(res).lstrip('0') or "0"


# nums = "10200"
# k = 1
nums = "1432219"
k = 3
print("Remove K Digits", removeKdigits(nums, k))

def removeDigit(num, digit):
    ans = "-1000"
    nums = list(num)
    for i in range(len(nums)):
        if nums[i] == digit:
            del nums[i]
            ans = max(int(ans), int("".join(nums)))
            nums.insert(i, digit)
    return ans

number = "123"
digit = "3"
# number = "1231"
# digit = "1"
# number = "551"
# digit = "5"
# number = "133235"
# digit = "3"
print("Remove Digit From Number to Maximize Result", removeDigit(number, digit))

def countBadPairs(nums):
    tot = len(nums) * (len(nums) - 1) // 2
    good = 0
    dp = {}
        
    for i,num in enumerate(nums):
        v = i - num
        good += dp.get(v, 0)
        dp[v] = dp.get(v, 0) + 1   
    return tot - good

nums = [4,1,3,3]
# nums = [1,2,3,4,5]
# nums = [43,69,66,40,33]
print("Count Number of Bad Pairs", countBadPairs(nums))

def shiftingLetters(s, shifts):
        l = len(shifts)
        s = list(s)[:l]
        print(s)
        a = ord('a')
        for i in range(1, len(shifts), 1):
            shifts[l - 1 - i] += shifts[l - i]
        print(shifts)
        for i in range(len(shifts)):
            s[i] = chr((ord(s[i]) - a + shifts[i]) % 26 + a)
        return ''.join(s)

s = "abc"
shifts = [3,5,9]
print("Shifting Letters", shiftingLetters(s, shifts))

def numberOfPairs(nums):
    nums.sort()
    count = 0
    for i in range(len(nums)-1):
        if nums[i] == 1000000:continue
        elif nums[i] == nums[i+1]:
            nums[i] = 1000000
            nums[i+1] = 1000000
            count += 1
    ans = []
    rem_count = 0
    for i in nums:
        if i != 1000000:
            rem_count += 1
    ans.append(count)
    ans.append(rem_count)
    return ans      

# nums = [1,3,2,1,3,2,2]
# nums = [1,1]
nums = [0]
print(" Maximum Number of Pairs in Array", numberOfPairs(nums))
from collections import defaultdict
def frequencySort(s):
    data = defaultdict(int)
    for i in s:
        data[i] += 1
    
    data = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))

    s = ""
    for k, v in data.items():
        temp = k * v
        s += str(temp)

    return s    

s = "tree"
# s = "cccaaa"
# s = "Aabb"
print("Sort Characters By Frequency", frequencySort(s))
import collections
def findAnagrams(s,p):

        myDictP=collections.Counter(p)
        myDictS=collections.Counter(s[:len(p)])
        output=[]
        i=0
        j=len(p)
        while j<=len(s):
            if myDictS==myDictP:
                output.append(i)

            myDictS[s[i]]-=1
            if myDictS[s[i]]<=0:
                myDictS.pop(s[i])
                
            if j<len(s):    
                 myDictS[s[j]]+=1
            j+=1
            i+=1
            
        return output         
s = "cbaebabacd"
p = "abc"
# s = "abab"
# p = "ab"
print("Find All Anagrams in a String", findAnagrams(s,p))


def findDuplicate(numRay):
    arr_size = len(numRay)
    for i in range(arr_size):
        x = numRay[i] % arr_size
        numRay[x] = numRay[x] + arr_size
    
    for i in range(arr_size):
        if (numRay[i] >= arr_size*2):
            return i
    

nums = [1,3,4,2,2]  
print("Find the Duplicate Number", findDuplicate(nums))    

def kthSmallest(mat,k):
    if k == 1:return mat[0][0]
    arr = []
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            arr.append((mat[i][j]))
    
    arr.sort()
    ans = arr[k-1]    
    return ans

# matrix = [[1,5,9],[10,11,13],[12,13,15]]
# k = 8  
matrix = [[-5]]
k = 1
# matrix = [[1,2],[1,3]]
# k = 2
print("Kth Smallest Element in a Sorted Matrix", kthSmallest(matrix, k))  

def combinationSum2(nums, target):
    ret = []
    dfs(sorted(candidates), target, 0, [], ret)
    return ret

def dfs( nums, target, idx, path, ret):
    if target <= 0:
        if target == 0:
            ret.append(path)
        return 
    for i in range(idx, len(nums)):
        if i > idx and nums[i] == nums[i-1]:
            continue
        dfs(nums, target-nums[i], i+1, path+[nums[i]], ret)
    
# candidates = [10,1,2,7,6,1,5]
# target = 8 
# candidates = [2,5,2,1,2]
# target = 5  
candidates = [1,2]
target = 4
print("Combination Sum II", combinationSum2(candidates, target)) 


def combinationalSum(arr, target):
    res = []
    arr = sorted(set( [x for x in arr if x<=target] ))
    HelperCombinationalSum(sorted(arr), target, res, [],0)
    return res
def HelperCombinationalSum(arr, target, res, path, idx):
    if target == 0:
        res.append(path.copy()) 
        return
    for i in range(idx,len(arr)):
        v = arr[i]
        if v <= target:
            path.append(v)
            HelperCombinationalSum(arr, target-v, res, path,i)
            path.pop()
        else:break    

# arr = [7,2,6,5]
# target = 16 
# arr = [6,5,7,1,8,2,9,9,7,7,9]
# target = 6  
arr = [8, 1, 8, 6, 8]
target =12
print("Combination Sum", combinationalSum(arr, target))


def matrixSpiral(matrix):
    rowbegin = 0
    rowend = len(matrix)
    columnbegin = 0
    columnend = len(matrix[0])
    res = []

    while rowend > rowbegin and columnend > columnbegin:

        for i in range(columnbegin, columnend):
            res.append(matrix[rowbegin][i])

        for j in range(rowbegin+1, rowend-1):
            res.append(matrix[j][columnend-1])

        if rowend != rowbegin+1:
            for i in range(columnend-1, columnbegin-1, -1):
                res.append(matrix[rowend-1][i])

        if columnbegin != columnend+1:
            for i in range(rowend-2, rowbegin,-1):
                res.append(matrix[i][columnbegin])

        rowbegin += 1
        rowend -= 1
        columnbegin += 1
        columnend -= 1
    return res   

def spiMat(n):

    res = [[0 for i in range(n)] for i in range(n)]
    top = 0
    bottom = len(res)
    left = 0
    right = len(res[0])    
    count = 1

    while bottom > top and right > left:
        for i in range(left, right):
            res[top][i] = count
            count += 1

        for j in range(top+1, bottom-1):
            # res.append(mat[j][right-1])
            res[j][right-1] = count
            count += 1

        if bottom != top+1:
            for i in range(right-1, left-1,-1):
                # res.append(mat[bottom-1][i])
                res[bottom-1][i] = count
                count += 1

        if left != right+1:
            for i in range(bottom-2, top, -1):
                # res.append(mat[i][top])
                res[i][top] = count
                count += 1
            
        top += 1
        left += 1
        right -= 1
        bottom -= 1
    
    return res        
            
mat = [[1,2,3],[8,9,4],[7,6,5]]
print("spiral matrix",matrixSpiral(mat)) 
print("spiral matrix2", spiMat(1))   

def rob(nums):
    n = len(nums)

    dp = [i for i in nums]
    dp[0] = nums[0]
    dp[1] = max(nums[1], nums[0])
    for i in range(2, n):
        if dp[0] != nums[i]:
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
    
    print(dp)
    ans = max(dp)
    return ans

# nums = [1,2,3,1]
# nums = [2,3,2]
# nums = [1,2,3,1]
# nums = [1,2,3]
nums = [1,2,1,1]

print(" House Robber", rob(nums))    
 
def addDigits(num):
    while True:
        num = list(str(num))
        if len(num) <= 1:
            return num[0]
        sum_ = 0
        for i in range(len(num)):
            sum_ += int(num[i])
        num = (sum_)
    return num

# num = 38
num = 0
print("Add Digits", addDigits(num))    

def combine(n, k):
    temp = [i+1 for i in range(n)]
    ans = []
    HelperCombine(temp, 0, [], k, ans)
    return ans
    pass

def HelperCombine(arr, idx, temp, k, ans):
    if idx>=len(arr):
        if len(temp) == k:
            ans.append(temp.copy())
        return     
    temp.append(arr[idx])
    HelperCombine(arr, idx+1, temp, k,ans)
    temp.pop()
    HelperCombine(arr, idx+1, temp, k, ans)    


n = 4
k = 2
# n = 1
# k = 1
print("Combinations", combine(n,k))

def maxUniqueSplit(s):
    arr = list(s)
    n = len(arr)
    dp = []

    HelperMaxUniuq(arr, 0, [], dp)
    return dp
    pass

def HelperMaxUniuq(arr, idx, temp, dp):
    if idx>= len(arr):
        if temp not in dp:
            dp.append(temp.copy())
        return
    temp.append(arr[idx])
    HelperMaxUniuq(arr, idx+1, temp, dp)
    temp.pop()
    HelperMaxUniuq(arr, idx+1, temp, dp)    

s = "ababccc"
# print("Split a String Into the Max Number of Unique Substrings", maxUniqueSplit(s))   
from collections import defaultdict
def findRepeatedDnaSequences(s):
    data = defaultdict(int)
    for i in range(len(s)):
        data[s[i:i+10]] += 1

    ans = []
    for k, v in data.items():
        if v >= 2:
            ans.append(k)
    return ans        

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print("Repeated DNA Sequences", findRepeatedDnaSequences(s))    

def maxProduct(words):
        res = 0
        for i in range(len(words)):
            for j in range(i,len(words)):
                if not set(words[i]) & set(words[j]):
                    # print(set(words[i]), set(words[j]))
                    res = max(res,len(words[i])*len(words[j]) )
                else:print((words[i]), (words[j]))    
        return res          


words = ["abcw","baz","foo","bar","xtfn","abcdef"]
print("Maximum Product of Word Lengths", maxProduct(words))    

def majorityElement(nums):
    n = len(nums) // 3
    ans = set()
    i = 0
    size_ = len(nums)
    while i < size_:
        if nums[i] not in ans:
            if nums.count(nums[i]) > n:
                ans.add(nums[i])
                size_ = len(nums)
        i += 1        
    return list(ans)        
    pass

# nums = [3,2,3]
nums = [1,2]
# nums = [1]
print("Majority Element II", majorityElement(nums))    

def isPossible(nums):
    stack = []
    temp = []
    for i in range(len(nums)):
        temp.append(nums[i])
        if len(temp) >= 3:
            stack.append(temp.copy())
            temp.clear()

    if len(temp) >= 3:stack.append(temp)
    count = 0
    print(stack)
    for i in range(len(stack)):
        prev = None
        tag = True
        for j in stack[i]:
            if prev == None:
                prev = j
            if prev >= j:
                tag=False
                prev = j
            else:prev = j    

        if tag:
            count += 1        
    if count <=1:
        return False
    return True        

# nums = [1,2,3,4,4,5] 
nums = [1,2,3,3,4,5]
print("Split Array into Consecutive Subsequences",isPossible(nums))   
from collections import Counter
def isPossibleDivide(nums, k):

    data = Counter(nums)

    for i in sorted(nums):
        if i in data:
            for j in range(i,i+k):
                if j in data:
                    data[j] -=1 
                    if data[j] == 0:
                        del data[j]
                else:
                    return False
    return True                    

# nums = [1,2,3,3,4,4,5,6]
# k = 4
# nums = [3,2,1,2,3,4,3,4,5,9,10,11]
# k = 3
# nums = [1,2,3,4]
# k = 3
nums = [3,3,2,2,1,1]
k = 3
print("Divide Array in Sets of K Consecutive Numbers", isPossibleDivide(nums, k))    

def uniquePathsWithObstacles(obstacleGrid):
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        def dfs(i, j):
            if obstacleGrid[i][j]:      # hit an obstacle
                return 0
            if i == M-1 and j == N-1:   # reach the end
                return 1
            count = 0
            if i < M-1:
                count += dfs(i+1, j)    # go down
            if j < N-1:
                count += dfs(i, j+1)    # go right
            return count
        
        return dfs(0, 0)

def HelperUniquePath(i,j, arr,m,n):
    if arr[i][j]:
        return 0
    if i == m-1 and j == n-1:
        return 1 
    count = 0
    if i < m-1:
        count += HelperUniquePath(i+1,j,arr,m,n)
    if j < n-1:
        count += HelperUniquePath(i, j+1, arr,m,n)
    return count        

# obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
obstacleGrid = [[0,1],[0,0]]
print("Unique Paths II", uniquePathsWithObstacles(obstacleGrid))    

def sortedSum(a):
    # Write your code here
    ans = 0
    temp = []
    for i in range(len(a)):
        temp.append(a[i])
        temp.sort()
        ans2= 0
        for j in range(len(temp)):
            res = (j+1)*temp[j]
            ans2 += res
        ans += ans2
    return ans % 1000000007  

a = [9, 5, 8] 
print("sorted sum is", sortedSum(a))   

def minRefuelStops(target, startFuel, stations):
    maxreach = startFuel
    pq = []
    count = 0
    index = 0
    while index < len(stations) and stations[index][0]<=maxreach:
        pq.append(stations[index][1])
        index += 1

    while maxreach < target:
        if len(pq) <= 0:return -1
        pq.sort()
        maxreach += pq[-1]
        pq.pop()
        count += 1
    return count        

target = 100
startFuel = 1
stations = [[10,100]]
# target = 100
# startFuel = 10
# stations = [[10,60],[20,30],[30,30],[60,40]]
# target = 1
# startFuel = 1
# stations = []
# target = 100
# startFuel = 50
# stations = [[25,50],[50,25]]
# target = 100
# startFuel = 50
# stations = [[25,25],[50,50]]
print("Minimum Number of Refueling Stops", minRefuelStops(target, startFuel, stations))    

def partition(s):
        dp = []
        n = len(s)
        
        for i in range(n+1):
            dp.append([])
        dp[-1].append([])
    
        for i in range(n-1,-1,-1):
            for j in range(i+1,n+1):
                curr = s[i:j]
                
                if curr == curr[::-1]:  
                    for e in dp[j]:   
                        dp[i].append ([curr] + e)
                        
        return dp[0] 
    

def HelperPartition(s, idx, temp,ans):
    if idx >= len(s):
        # word_ = ''.join(temp)
        # if word_[::-1] == word_:
        #     if len(word_) >0:
        #      ans.append([word_])
        return

    temp.append(s[idx])
    HelperPartition(s, idx+1, temp, ans)
    temp.pop()
    HelperPartition(s, idx+1, temp, ans)    

s = "aab"
print("Palindrome Partitioning", partition(s))    

def wordBreak(s, wordict):
    dp = [False]*(len(s)+1)
    dp[0] = True 

    for i in range(1, len(s)+1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break 
    return dp[-1]              

# s = "catsandog"
# wordDict = ["cats","dog","sand","and","cat"]   
s = "leetcode"
wordDict = ["leet","code"] 
# s = "applepenapple"
# wordDict = ["apple","pen"]
# s = "cars"
# wordDict = ["car","ca","rs"]
# s = "aaaaaaa"
# wordDict = ["aaaa","aaa"]
print("Word Break", wordBreak(s, wordDict))

def numberOfBeams(bank):
    ans = 0
    temp = []
    security = "1"
    for i in range(len(bank)):
        if len(temp) <= 0:
            if security in bank[i]:
                temp.append(bank[i].count(security))
        else:
            if security in bank[i]:
                no_of_security = bank[i].count(security)
                prev_floor = temp[-1]
                res = prev_floor * no_of_security
                ans += res
                temp.append(no_of_security)
    return ans
                
# bank = ["011001","000000","010100","001000"]
# bank = ["000","111","000"]
bank = ["010101","001000","111111"]
print("Number of Laser Beams in a Bank", numberOfBeams(bank))    

def partitionLabels(S):
    result, last_seen, max_last_seen, count = [], {}, 0, 0
    for i, char in enumerate(S):
        last_seen[char] = i
    for i, char in enumerate(S):
        max_last_seen = max(max_last_seen, last_seen[char])
        count += 1
        if i == max_last_seen:
            result.append(count)
            count = 0
    return result

s = "ababcbacadefegdehijhklij"
print("partition labels", partitionLabels(s))

def maximumTop(nums,k):
    ans = -1
    count = 0
    des = k

    while True:
        if len(nums) < k:
            k = k // len(nums)
            des = k
        else:
            if abs(count - des) == 1:
                nums.insert(0, ans)
                break 
            else:
                print(nums)
                ans = max(ans, nums[0])
                del nums[0]
                count += 1
                k -= 1    
    return nums[0]            
# nums = [5,2,2,4,0,6]
# k = 4
# nums = [2]
# k = 1
nums = [2,3,4,5,6,8]
k = 4
# nums = [99,95,68,24,18]
# k = 69
print("Maximize the Topmost Element After K Moves", maximumTop(nums, k))

def canCompleteCircuit(gas, cost):
    start = 0
    current = 0

    if sum(gas) < sum(cost):
        return -1

    for i in range(len(gas)):
        current += gas[i] - cost[i]
        if current < 0:
            start = i+1
            current = 0
    return start            
       
# gas = [2,3,4]
# cost = [3,4,3] 
# gas = [1,2,3,4,5]
# cost = [3,4,5,1,2]   
gas = [1,3,5,6,7]
cost = [1,2,3,4,5] 
gas = [5,1,2,3,4]
cost = [4,4,1,5,1]
# gas = [3,1,1]
# cost = [1,2,2]

print("Gas Station", canCompleteCircuit(gas, cost))

def maxWidthOfVerticalArea(points):
    arr = sorted({x for x, y in points})       
    ans = 0
    n = len(arr)
    for i in range(1, n):
        res = arr[i] - arr[i-1]
        ans = max(ans, res)
    return ans    

# points = [[8,7],[9,9],[7,4],[9,7]]
points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
# points = [[4,2],[2,3],[4,5],[6,0]]
# points = [[4,6],[4,5],[6,0]]

print("Widest Vertical Area Between Two Points Containing No Points", maxWidthOfVerticalArea(points))

def arithmeticTriplets(nums, diff):
    i = 0
    n = len(nums)
    ans = 0
    for i in range(n):
        j = i 
        k = n-1 
        while j < k:
            res = nums[j] - nums[i]
            res2 = nums[k] - nums[j]
            if res == diff and res2 == diff:
                ans += 1
            j +=1 
            k -= 1


    return ans             

nums = [0,1,4,6,7,10]
diff = 3  
# nums = [4,5,6,7,8,9]
# diff = 2
print("Number of Arithmetic Triplets", arithmeticTriplets(nums, diff))  
from collections import Counter
def numIdenticalPairs(nums):
    data = {}
    n = len(nums)
    ans = 0
    for i in range(n):
        if nums[i] in data.values():
            res = 0
            for v in data.values():
                if v == nums[i]:
                    res += 1
            ans += res        
            data[i] = nums[i]
        else:
            data[i] = nums[i]    
    
    return ans 


# nums = [1,2,3,1,1,3]
# nums = [1,1,1,1]
nums = [1,2,3]
print("Number of Good Pairs", numIdenticalPairs(nums))  

def executeInstructions(startPos, s, n):
        result = []
        for idx in range(len(s)):
            count, row, col = 0, startPos[0],startPos[1]
            while  idx < len(s):
                if s[idx] == 'D':
                    row += 1
                    if row >= n:
                        break
                    count += 1
                elif s[idx] == 'U':
                    row -= 1
                    if row < 0:
                        break
                    count += 1
                elif s[idx] == 'R':
                    col += 1
                    if col >= n:
                        break
                    count += 1
                else:
                    col -= 1
                    if col < 0:
                        break
                    count += 1
                idx += 1
            result.append(count)
        return result

startPos = [0,1]
s = "RRDDLU" 
n = 3   
print(" Execution of All Suffix Instructions Staying in a Grid", executeInstructions(startPos, s, n))

def wateringPlants(plants, capacity):
    max_capacity = capacity
    forward_step = 0
    refill_step = 0
    n = len(plants)
    for i in range(n):
        if max_capacity < plants[i]:
            refill_step += i 
            forward_step += i+1
            max_capacity = capacity - plants[i]
        else: 
             forward_step += 1
             max_capacity -= plants[i]
    ans = refill_step + forward_step
    return ans              

# plants = [2,2,3,3]
# capacity = 5 
# plants = [1,1,1,4,2,3]
# capacity = 4 
plants = [7,7,7,7,7,7,7]
capacity = 8  
print("Watering Plants", wateringPlants(plants, capacity))

def maxCoins(piles):
    piles.sort()
    sum_ = 0 
    i = len(piles) - 2
    j = 0 
    while j < len(piles) / 3:
        sum_ += piles[i]
        i -= 2
        j += 1
    return sum_    

# piles = [2,4,1,2,7,8] 
piles = [9,8,7,6,5,1,2,3,4]
print("Maximum Number of Coins You Can Get", maxCoins(piles))   

def checkArithmeticSubarrays(nums, l,r):
    ans_arr = []
    n = len(l)
    for i in range(n):
        is_arthmatic = True
        arth_mat = nums[l[i]:r[i]+1]
        arth_mat.sort()
        ans = None
        for j in range(len(arth_mat)-1):
            res = arth_mat[j+1] - arth_mat[j] 
            if ans == None:
                ans=res
            else:
                if ans != res:
                    is_arthmatic = False
                    break
        ans_arr.append(is_arthmatic)              
    return ans_arr

# nums = [4,6,5,9,3,7]
# l = [0,0,2]
# r = [2,3,5]  
nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10]
l = [0,1,6,4,8,7]
r = [4,4,9,7,9,10]  
print("Arithmetic Subarrays", checkArithmeticSubarrays(nums, l,r))

def maximumSegmentSum(nums, removeQueries):
    ans = []
    n = len(removeQueries)
    nums.sort()
    for i in range(n):
        nums[removeQueries[i]] = 0
        a = [nums[j] for j in range(removeQueries[i], len(nums)-1) if nums[j+1] != 0]
        b = [nums[j] for j in range(removeQueries[i]) if nums[j+1] != 0]
        a = sum(a)
        b = sum(b)
        ans.append(max(a,b))
    return ans            

# nums = [1,2,5,6,1]
# removeQueries = [0,3,2,4,1]   
# nums = [3,2,11,1]
# removeQueries = [3,2,1,0]
nums = [500,822,202,707,298,484,311,680,901,319,343,340]
removeQueries = [6,4,0,5,2,3,10,8,7,9,1,11]

print("Maximum Segment Sum After Removals", maximumSegmentSum(nums, removeQueries)) 
from collections import Counter
def findLongestWord(s, dictionary):
    ans = ""
    max_ans = 0
    n = len(dictionary)
    data = Counter(s)
    for i in range(n):
        temp_count = 0
        word_fre = Counter(dictionary[i])
        for k,v in word_fre.items():
            if k in data:
                if data[k] >= v:
                    temp_count += v
                else:temp_count -= 1            
        if temp_count > max_ans:
            max_ans = temp_count
            ans = dictionary[i]
        elif temp_count == max_ans:
            if dictionary[i] < ans:
                ans = dictionary[i]

    return ans

s = "abpcplea"
dictionary = ["ale","apple","monkey","plea"] 
# s = "abpcplea"
# dictionary = ["b","a","c"] 
# s = "abpcplea"
# dictionary = ["ale","apple","monkey","plea", "abpcplaaa","abpcllllll","abccclllpppeeaaaa"]
# s = "aaa"
# dictionary = ["aaa","aa","a"]  
print("Longest Word in Dictionary through Deleting", findLongestWord(s, dictionary))

def minimumOperations(nums):
    count = 0
    n = len(nums)
    for i in range(2,n):
        if nums[i-2] == nums[i]:
            if nums[i] == nums[i-1]:
                nums[i-1] = 0
                count += 1
        else:
            nums[i] = nums[i-2]
            count += 1
    return count 

# nums = [3,1,3,2,4,3]
# nums = [2,2,2,2,2,2]
# nums = [1,2,2,2,2]
nums = [69,91,47,74,75,94,22,100,43,50,82,47,40,51,90,27,98,85,47,14,55,82,52,9,
        65,90,86,45,52,52,95,40,85,3,46,77,16,59,32,22,41,87,89,78,59,78,34,26,71,
        9,82,68,80,74,100,6,10,53,84,80,7,87,3,82,26,
        26,14,37,26,58,96,73,41,2,79,43,56,74,30,71,6,100,72,93,83,40,28,79,24]
print("Minimum Operations to Make the Array Alternating", minimumOperations(nums))    

def minMoves2(nums):
    nums.sort()
    ans = 0
    l = 0
    n = len(nums)
    r = n - 1 
    mid = l + (r-l) // 2
    ele = nums[mid]
    for i in range(n):
        if i == mid:continue  
        else:
            diff = abs(nums[i] - nums[mid])
            ans += diff
    return ans

# nums = [1,2,3]
# nums = [1,10,2,9]
nums = [0,1,2,3,4,6,7,8,9]
print(" Minimum Moves to Equal Array Elements II", minMoves2(nums))     

def largestDivisibleSubset(nums):
    ans = []
    n = len(nums)
    i = 0
    while i < n:
        temp = [nums[i]]
        j = i+1
        while j < n:
            if nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0:
                temp.append(nums[j])
                j += 1
            else:
                break  
        if len(temp) > 1 and len(temp) > len(ans):
            ans.clear()        
            ans = temp
        i += j 
    return ans        


# nums = [1,2,4,8]
# nums = [3,2,4,8,7,6]
nums = [1,2,3]
print("Largest Divisible Subset", largestDivisibleSubset(nums))    

def rotateMat(matrix):

    temp = matrix.copy()
    matrix.clear()
    for i in range(len(temp)):
        matrix.append([])

    for j in range(len(temp)):
       for k in range(len(temp)):
          matrix[j].insert(0, temp[k].pop(0))
    return matrix                

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print("Rotate Image", rotateMat(matrix))                


def insertOverlappping(intervals, newInterval):
    for i in range(len(intervals)):
        if intervals[i][1] >= newInterval[0]:
            intervals[i][1] = max(intervals[i][1], newInterval[1])
            intervals[i][0] = min(intervals[i][0], newInterval[0])
            break
        else:
           intervals.append(newInterval)    
   
    i = 0
    n = len(intervals)
    while i < n-1:
        if intervals[i][1] < intervals[i+1][0]:
            i += 1
            continue
        else:
            intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
            del intervals[i+1]
            n = len(intervals)    

    return intervals        
 
intervals = [[1,5]]
newInterval = [0,0] 
# intervals = [[1,5]]
# newInterval = [0,3]
# intervals = [[1,3],[6,9]]
# newInterval = [2,5]
# intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
# newInterval = [4,8]
# intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
# newInterval = [7,9]
# intervals = [[1,5]]
# newInterval = [6,8]
print("Insert Interval", insertOverlappping(intervals, newInterval))    

def minNumberOperations(target):
    res = 0
    prev = 0

    for i in target:
        res += max(0, i-prev)                
        prev = i 
    return res                 
    

# target = [3,1,1,2]
# target = [3,1,1,2]
# target = [1,2,3,2,1]
target = [3,1,5,4,2]
print("Minimum Number of Increments on Subarrays to Form a Target Array", minNumberOperations(target))    

def longestPalindrome(words):
    data = defaultdict(int)   
    ans = 0
    n = len(words)
    for i in range(n):
        if data[words[i][::-1]] > 0:
            data[words[i][::-1]] -= 1
            ans += 4
            if data[words[i][::-1]] == 0:
                del data[words[i][::-1]]
        else:
            data[words[i]] += 1    
    flag=False
    for word in data.keys(): 
        if data[word]>0 and len(set(word))==1: 
            flag=True
            break
    return ans+(2 if flag else 0)       

# words = ["lc","cl","gg"]
words = ["ab","ty","yt","lc","cl","ab"]
print("Longest Palindrome by Concatenating Two Letter Words", longestPalindrome(words))    

def minInsertions(s):
    if s == s[::-1]:return 0 
    n = len(s)
    dp = [[0 for i in range(n+1)] for i in range(n+1)]
    s2 = s[::-1]
    for i in range(0,len(dp)):
        for j in range(0,len(dp[0])):
            if i == 0 or j == 0:
                dp[i][j] = 0 
            elif s2[i-1] == s[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    ans = abs(n - dp[-1][-1])
    return ans                    


    pass 

# s = "zzazz"
s = "mbadm"
s = "leetcode"
s = "aniket"
s = "geek"
print("Minimum Insertion Steps to Make a String Palindrome", minInsertions(s))    

def reverseVowels(s):
    vowels = "aeiouAEIOU"
    s = list(s)
    i = 0
    j = len(s)-1
    
    while i < j:
        if s[i] in vowels and s[j] not in vowels:
            j -= 1
        elif s[i] not in vowels and s[j] in vowels:
            i += 1
        elif s[i] in vowels and s[j] in vowels:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i += 1
            j -= 1
        else:
            i+=1 
            j -= 1
    s = "".join(s)
    return s                   

s = "hello"
# s = "leetcode"
# s = "aniket"
print("Reverse Vowels of a String", reverseVowels(s))            

def InsertionSort(list1):
    for i in range(1, len(list1)): 
        value = list1[i]    
        j = i - 1  
        while j >= 0 and value < list1[j]:  
            list1[j + 1] = list1[j]  
            j -= 1  
        list1[j + 1] = value  
    return list1

head = [4,2,1,3]
print(" Insertion Sort List", InsertionSort(head))       

def nextGreaterElement(nums1, nums2):

        n = len(nums1)
        ans = []
        
        for i in range(n):
            if nums1[i] in nums2:
                ele =  nums1[i]
                idx = nums2.index(ele)
                tag = False
                greate_ele = None
                for j in range(idx, len(nums2)):
                    if nums2[j] > ele:
                        tag = True
                        greate_ele = nums2[j]
                        break
                if tag:
                    ans.append(greate_ele)
                else:
                    ans.append(-1)
        return ans  

# nums1 = [4,1,2]
# nums2 = [1,3,4,2] 
nums1 = [2,4]
nums2 = [1,2,3,4]
print("Next Greater Element I", nextGreaterElement(nums1, nums2))           

def checkPerfectNumber(num):
    sum_ = 0
    print(num)
    for i in range(1, num):
        if sum_ == num:
            print(sum_)
            return True
        if num % i == 0 and num != i:
            # print(i)
            sum_ += i 
    return False

num = 28 
num = 7
num = 2016
print("Perfect Number", checkPerfectNumber(num))  

def reverseWords(s):
    word = ""
    ans = ""
    for i in range(len(s)):
        if s[i] == " ":
            revers_ = word[::-1]    
            ans += revers_ + " "
            word = ""
        else:
            word += s[i]
    revers_ = word[::-1]
    ans += revers_  
    return ans

#"s'teL ekat edoCteeL tsetnoc"
# s = "Let's take LeetCode contest"
s = "God Ding"
print("Reverse Words in a String III", reverseWords(s))    

def addStrings(num1, num2):
    a = 0  
    b = 0 
    for i in num1: 
        a = a * 10 + (ord(i) - 48) 

    for j in num2:
        b = b * 10 + (ord(j) - 48)    

    ans = a + b 
    return str(ans)    


num1 = "11"
num2 = "123"
print(" Add Strings", addStrings(num1, num2))    
from collections import Counter
def chefandstring(string):
    x =  list(string)
    y = list(string)

    if len(string) > 1:
        x_ele = x.pop(0)
        y_ele = y.pop(-1)

        x.append(x_ele)
        y.insert(0,y_ele)   

        print(x,y)

    pass

s = "abcd"
s = "ab"
print("chef and string ", chefandstring(s))    

def maxSatisfaction(satisfaction):
        prefix_sum = 0
        cur_sum = 0
        max_sum = 0

        for num in sorted(satisfaction, reverse=True):
            prefix_sum += num
            cur_sum += prefix_sum
            print(max_sum, cur_sum, num)
            max_sum = max(max_sum, cur_sum)
            print(max_sum, cur_sum)
            print()

        return max_sum

# satisfaction = [-1,-8,0,5,-9]
satisfaction = [-1,-5,-3]
print("Reducing Dishes", maxSatisfaction(satisfaction))    

arr = [1, 3, 4, 6, 7, 8]

def minSubArrayLen(nums, target):
        n = len(nums)
        i = 0
        s = 0
        minlen = 999999

        for j in range(n):
            s += nums[j]
            while(s>=target):
                minlen = min(minlen, j-i+1)
                s -= nums[i]
                i+=1
                
        
        return 0 if minlen == 999999 else minlen
    

# target = 7
# nums = [2,3,1,2,4,3] 
target = 4
nums = [1,4,4]   
print("Minimum Size Subarray Sum", minSubArrayLen(nums, target))

def productExceptSelf(nums):
        zero_count = 0
        product = 1
        n = len(nums)
        ans = [0]*n
        zero_idx = None
        for i in range(n):
            if nums[i] == 0:
                zero_count += 1
                zero_idx = i
                if zero_count >= 2:
                    return ans
            else:
                product *= nums[i]
        
        if zero_count == 1:
            ans[zero_idx] = product
        else:
            for i in range(n):
                res = product // nums[i]
                ans[i] = res
        return ans 
     

nums = [-1,1,0,-3,3]
nums = [1,2,3,4]
nums = [-1,1,0,-3,3,0,0,12,4,5,6]
print("Product of Array Except Self", productExceptSelf(nums))    

def longestNiceSubarray(nums):
    count = 0

    for i in range(len(nums)-1):
        if nums[i] & nums[i+1] == 0:
            count += 1
    if count == 0:
        return 1
    return count

nums = [1,3,8,48,10]
# nums = [3,1,5,11,13]
print("longegst", longestNiceSubarray(nums))    

def smallestSumSubarray(arr):
    ans = 100000
    res = 0

    for i in arr:
        res += i 

        if res > i:
            res = i 

        ans = min(res, ans)
    return ans        

arr = [3,-4, 2,-3,-1, 7,-5]
print("Smallest sum contiguous subarray", smallestSumSubarray(arr))    

def longestIdealString(s, k):
    n = len(s)
    s2 = s[::-1]
    dp = [[0 for i in range(n)] for i in range(n)]
    
    ans = -10000

    for i in range(len(dp)):
        for j in range(len(dp[i])):
            if i == 0 or j == 0:
                dp[i][j] = 0

            res = abs(ord(s[i]) - ord(s2[j]))
            if res <= k and s[i] != s2[j]:
                
                dp[i][j] = dp[i-1][j-1] + 1
                ans = max(ans, dp[i][j])
            else:
                dp[i][j] = 0

    return ans


s = "acfgbd"
k = 2
# s = "abcd"
# k = 3
s = "pvjcci"
k = 4
print("Longest Ideal Subsequence", longestIdealString(s, k))    

def func(arr):
    if sorted(arr) == arr:
        return 0
    count = 0
    n = len(arr)
    stack = []
    
    for i in range(n):
        if len(stack) > 0:
            stack.append(arr[i])
        if  stack[-1] > arr[i]:
            j = i
            while j < n:
                if stack[-1] <= arr[j]:
                    stack.append(arr[j])
                    break
                else:
                    stack.pop() 
                        




    return count 
arr = [1,2,3,10,4,2,3,5]
arr = [5,4,3,2,1]
arr = [1,2,3]
arr = [1,2,3,10,0,7,8,9]
# print(" Shortest Subarray to be Removed to Make Array Sorted", func(arr))        

def isStackPermutation(a,b):
    stack = []
    j = 0 
    n = len(a)

    for i in range(n):
        stack.append(a[i])
        top_ele = stack[-1]

        if top_ele == b[j]:
            while True:
                if stack and stack[-1] == b[j]:
                    stack.pop()
                    j += 1
                else:break       
    
    if len(stack) > 0:
        return False    

    return True    


A = [1,2,3]
B = [3,1,2] 
A = [1,2,3]
B = [2,1,3]
A = [2, 4, 3, 1]
B = [3, 4, 1, 2]
A = [4, 3, 1, 7, 5, 3]
B = [3, 4, 3, 1, 5, 7]   
print("Stack Permutations", isStackPermutation(A,B))

def numberOfWeakCharacters(properties):
    properties.sort(key = lambda x:(x[0],x[1]))

    most_from_last = properties[-1][1]  #overall the most
    most_from_last_diff = 0             # the most that [0] is different
    prev_0 = properties[-1][0]
    result = 0
    
    for i in range(len(properties)-2, -1, -1):
        curr_0, curr_1 = properties[i][0], properties[i][1]
        if curr_0 != prev_0:#if different from the previous case
            if curr_1 < most_from_last:
                result += 1
                most_from_last_diff = most_from_last
            else:
                most_from_last_diff = most_from_last
                most_from_last = curr_1

        elif curr_0 == prev_0:#if the same as previous case
            if curr_1 < most_from_last_diff:
                result += 1
            elif curr_1 >= most_from_last:
                most_from_last = curr_1
        prev_0 = curr_0
        
    return result
properties = [[2,2],[3,3]]
# properties = [[5,5],[6,3],[3,6]]
properties = [[1,5],[10,4],[4,3]]
properties = [[7,7],[1,2],[9,7],[7,3],[3,10],[9,8],[8,10], [4,3],[1,5], [1,5]]
print("The Number of Weak Characters in the Game", numberOfWeakCharacters(properties))    

def maxProfit(prices,k):
    min_price = [999999999] * (k + 1)
    max_profit = [0] * (k + 1)

    for price in prices:
        for i in range(1, k + 1):
            temp = price - max_profit[i-1]
            if temp < min_price[i]: 
                min_price[i] = temp 
            temp = price - min_price[i]
            if temp > max_profit[i]:
                max_profit[i] = temp
    return max_profit[k]                        

k = 2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
prices = [2,4,1]  
k = 3
prices = [4,3,8,6,0,5]  
print("Best Time to Buy and Sell Stock IV", maxProfit(prices, k))

def countColor(n):
    arr = []
    for i in range(n+1):
        if i == 0:
            