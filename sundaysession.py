
def sorting(arr):
    arr.sort(key = lambda x : x[1])
    return arr
arr = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print(sorting(arr))

def Fibonaci(n, dp):
    if n <= 1:return n

    if dp[n]!=-1:return dp[n]
    first = 0
    second = 0
 
    if (dp[n - 1] != -1):
        first = dp[n - 1]
    else:
        first = Fibonaci(n - 1, dp)
    if (dp[n - 2] != -1):
        second = dp[n - 2]
    else:
        second = Fibonaci(n - 2, dp)
    dp[n] = first + second
 
    # Memoization
    return dp[n] 
n = 5
dp = [-1 for i in range(n+1)]
# print(dp)
print(Fibonaci(n, dp))
from cmath import cos
from itertools import count
from pydoc import Helper
from socket import NI_NUMERICSERV
import sys
from this import d
def frogJump(arr):
    dp = [-1 for i in range(len(arr)+1)]
    return FrogHelper(len(arr)-1, arr, dp)
    

def FrogHelper(idx , arr, dp):
    if idx == 0: return 0

    if dp[idx] != -1:return dp[idx]

    left = FrogHelper(idx-1, arr, dp) + abs(arr[idx] - arr[idx-1])
    right = sys.maxsize
    if idx > 1:
        right = FrogHelper(idx-2, arr, dp) + abs(arr[idx] - arr[idx-2])

    dp[idx] = min(left, right)    
    return dp[idx]
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print("Frog jums", frogJump(arr))

def climbStairs(n):
    dp = [1,1] + [0]*n
    # return StairHelper(n)
    for i in range(2, n+1):
        dp[i] = dp[i-2] + dp[i-1]
    return dp[n]    

def StairHelper(n):
    if n < 0:return
    if n == 0:return 1
    if n == 1:return 1
    one = StairHelper(n-1) + StairHelper(n-2)
    return one
n = 84
print("climb Stairs", climbStairs(n))
 
def minCostClimbingStairs(cost):
    length = len(cost)
    dp = [0] * length
    dp[-2:] = cost[-2:]
    for i in reversed(range(length - 2)):
        dp[i] = cost[i] + min(dp[i + 2], dp[i+1])
    return(min(dp[0], dp[1]))   

cost = [1,100,1,1,1,100,1,1,100,1]

print("Min Cost Climbing Stairs", minCostClimbingStairs(cost))

def lengthOfLIS(nums):
    dp = [1]*len(nums)

    for i in range(1, len(nums)):
        max_ = 0
        for j in range(i):
            if nums[j] < nums[i]:
                if dp[j] > max_:
                    max_ = dp[j]

        dp[i] = max_+1 
    return max(dp)               

    # for i in range(len(nums)-2, -1,-1):
    #     print(nums[i],"i")
    #     for j in range(i+1, len(nums)):
    #         if nums[i] < nums[j]:
    #             dp[i] = max(dp[i], 1+dp[j])
    #     print(dp)        
    # return max(dp)          



# nums = [10,9,2,5,3,7,101,18]
# nums = [0,1,0,3,2,3]
nums = [7,7,7,7,7,7,7]
print("Longest Increasing Subsequence", lengthOfLIS(nums))

def subarraysDivByK(arr,k):
    hmap,total,result = {},0,0
    for num in arr:
        hmap[total] = hmap.get(total,0) + 1
        total += num
        total %= k
        if hmap.get(total):
            result += hmap[total]
    return result

nums = [4,5,0,-2,-3,1]
k = 5
print("Subarray Sums Divisible by K", subarraysDivByK(nums,k))

def subarraySum(nums,k):
    result = 0
    n = len(nums)
    data = {0:1}
    ans = 0
    for i in nums:
        result += i
        temp = result - k
        if temp in data:
            ans += data[temp]
        if result in data:
            data[result] += 1
        else:
            data[result] = 1
    return ans
         

# nums = [1,1,1]
# k = 2
# nums = [1,2,3]
# k = 3
# nums = [10 , 2, -2, -20, 10]
# k = -10
nums = [9, 4, 20, 3, 10, 5]
k = 33
print("Subarray Sum Equals K", subarraySum(nums,k))

def arrayChange(nums, operations):
    dic = {num: i for i, num in enumerate(nums)}
    for s, e in operations:
        i = dic[s]
        nums[i] = e
        dic[e] = i
        del dic[s]
    return nums            

nums = [1,2,4,6]
operations = [[1,3],[4,7],[6,1]]
# nums = [1,2]
# operations = [[1,3],[2,1],[3,2]]
print("Replace Elements in an Array", arrayChange(nums, operations))

from collections import defaultdict
def minSteps(s,t):
    data = {}

    for i in s:
        if i not in data:
            data[i] = 1
        else:
            data[i] += 1

    for i in t:
        if i in data and data[i] != 0:
            data[i] -= 1

    return sum(data.values())                    

# s = "bab"
# t = "aba"
# s = "leetcode"
# t = "practice"
s = "anagram"
t = "mangaar"
print("Minimum Number of Steps to Make Two Strings Anagram", minSteps(s,t))

def minAddToMakeValid(s):
        opening = count = 0
        for i in s:
            if i == '(': 
                opening += 1
            else:
                if opening: opening -= 1
                else: count += 1
        return count + opening

s = "((("
# s = "())"
print("Minimum Add to Make Parentheses Valid", minAddToMakeValid(s))


def minSubarray(arr, p):
    if sum(arr) % p ==0:return 0
    sum_= 0
    i ,j = 0, 0
    count = 0
    n = len(arr)
    while j < n:
        sum_ += arr[j]
        if sum_ % p ==0:
            ans = abs(count - n)
            return ans
        elif sum_ > p:
            while i < j:
                if sum_ % p == 0:
                    ans = abs(count - n)
                    return ans
                elif sum_ < p:
                    break
                else:
                    sum_ -= arr[i]
                    count -= 1

    pass

nums = [6,3,5,2]
p = 9
print(" Make Sum Divisible by P", minSubarray(arr, p))

def findRestaurant(list1, list2):
    ans = []
    dict1 = {res:i for i, res in enumerate(list1)}
    dict2 = {res:dict1[res]+1 for i, res in enumerate(list2) if res in dict1}
    MIN = float('inf')
    for k,v in dict2.items():
        if v < MIN:
            ans = [k]
            MIN = v
        elif v == MIN:
            ans.append(k)    

    return ans

# list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
# list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
# list2 = ["KFC","Shogun","Burger King"]
list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Burger King","Tapioca Express","Shogun"]
print(" Minimum Index Sum of Two Lists", findRestaurant(list1, list2))

def areNumbersAscending(s):
    n = 0
    l = s.split()

    for i in l:
        if i.isdigit():
            if int(i) <= n:return False
            n = int(i)
    return True                 

s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
# s = "hello world 5 x 5"
# s = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"
print("Check if Numbers Are Ascending in a Sentence", areNumbersAscending(s))