
from collections import Counter
from email import message
from itertools import count
from re import L


def sumOfArrayWithRecursion(n):
    if n == 1 or n== 0:
        return 1

    recu = sumOfArrayWithRecursion(n-1)
    ans = recu+n
    return ans

n = 5
print("Recursion sum is", sumOfArrayWithRecursion(n))

def powerofValue(val,pow):
    if(pow==0):
        return 1
    else:
        return(val*powerofValue(val,pow-1))  

pow = 5
val = 2
print("power of value", powerofValue(val,pow))

def PalindromString(string):
    start = 0
    end = len(string) -1
    return HelperOfPalindrome(string, start, end)

def HelperOfPalindrome(string, start, end):
    if start >= end:
        return "YES"

    if string[start] != string[end]:
        return "NO"

    return HelperOfPalindrome(string, start+1, end-1)        

# s = "abcba"
s = "noon"
print("String is Palindrom or not", PalindromString(s))

def ReverseArray(arr):
    start = 0
    end = len(arr) -1

    return HelperForReverseArray(arr, start, end)

def HelperForReverseArray(arr, start, end):
    if start >= end:
        return arr

    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp

    return HelperForReverseArray(arr, start+1, end-1)    

# arr = [1,2,3,4,5,6]
arr = [1,2,3,4,5]
print("Reverse the array using recusrion", ReverseArray(arr))

def SortArrayByRecusrsion(arr):
    i = 0
    j = 1
    if len(arr) <= 1:
        return arr
    return HelperSortArray(arr, i, j)    
    pass

def HelperSortArray(arr, i ,j):
    if len(arr) ==i :
        return arr
    if len(arr) == j:
        i += 1
        j = i+1

    elif arr[i] > arr[j]:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    else:
        j += 1    
    return HelperSortArray(arr, i, j)


# arr = [2,3,5,1,0]
arr = [34,12,67, 54, 100, 1,3]
print("Sort array by recursion", SortArrayByRecusrsion(arr))

def Recursivelyremovealladjacentduplicates(s):
    li = [x for x in s]
    hold = True
    ch = '0'
    for i in range(len(li)):
        if ch == li[i]:
            li[i] = ""
            li[i-1] = ""
            hold=False
        else:
            ch = li[i]
    s = "".join(li)
    if hold:
        return s 
    return Recursivelyremovealladjacentduplicates(s)               


S = "geeksforgeek"
print("Recursively remove all adjacent duplicates", Recursivelyremovealladjacentduplicates(S))

def PowerOfTwo(n):
    if(n==1):
        return True
    ans = 1    
    for i in range(0,n):
        ans = ans * 2
        if ans < n:
            continue
        if ans > n:
            return False
        if ans == n:
            return False
    
    return False            

n = 16
print("Power of two is n or not", PowerOfTwo(n))

def FibbonaciNumber(n):
    # Base Cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # recursive call
    rec1 = FibbonaciNumber(n-1)
    rec2 = FibbonaciNumber(n-2)
    
    # small calculation
    res = rec1 + rec2
    return res        
    

n = 6
print("Fibbonaci number is", FibbonaciNumber(n))

# stair problem
def CountWayToRichTop(n):
    
    if n == 1 or n == 2:
        return n

    rec1 = CountWayToRichTop(n-1)
    rec2 = CountWayToRichTop(n-2)

    res = rec1 + rec2
    return res    

n = 6
print("Count way to rich top", CountWayToRichTop(n))


def ReverseArray(arr):
    return ReverseHelp(arr, 0, len(arr) - 1)

def ReverseHelp(arr, i, j):
    if i > j:
        return arr

    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    i += 1
    j -= 1
    return ReverseHelp(arr, i, j)

arr = [1,2,3,4,5,6]
print("Reverse the array by using recursion", ReverseArray(arr))

def subsequence(arr):
    return HelperSubseq(0, [], arr, len(arr))

def HelperSubseq(idx, temp, arr, n):
    if idx >= n:
        for i in range(len(temp)):
            print(temp[i])
        if len(temp) <= 0:print("{}") 
        print()
    else:
        temp.append(arr[idx])
        HelperSubseq(idx+1, temp, arr, n)
        temp.pop()
        HelperSubseq(idx+1, temp, arr, n)        

arr = [1,2,2]
# print("sub-sequence is", subsequence(arr))

def StringSequ(string):
    return HelperStringSequ(0, [], string, len(string),0)
    pass
ans = []
def HelperStringSequ(idx, temp, string, n,count):
    if idx >= n:
        res = "".join(temp)
        ans.append(res)
        return
    else:
        temp.append(string[idx])
        count += HelperStringSequ(idx+1, temp, string, n,count)
        temp.pop()        
        count += HelperStringSequ(idx+1, temp, string, n, count)
        # count+= take + non_take
        return count

s = "aniket"
# print("string sub-sequences", StringSequ(s))

def canJump(arr):
    jumps = arr[0]
    if len(arr) <=1:return True
    if jumps == 0:return False
    i = 1
    for i in range(1, len(arr)):
        jumps -= 1
        if i == len(arr)-1 and jumps == 0:return True
        elif jumps == 0 and arr[i] == 0:return False
        else:jumps = arr[i]
    return True      
        

# nums = [2,3,1,1,4]
nums = [3,2,1,0,4]  
# nums = [0,1]
# nums = [0]
# nums = [2,1,0,0]
# nums = [2,0,0]
# nums = [3,0,8,2,0,0,1]

print("can jump", canJump(nums))

def largestWordCount(msg, sender):
    data = dict()
    best = 0
    for w,s in zip(msg, sender):
        count = 0
        count += len(w.split(" "))
        if s in data:
            data[s] += count
        else:
            data[s] = count    
        best = max(best, data[s])
    
    possibles = []
    for k,v in data.items():
        if v == best:
            possibles.append(k)
    return sorted(possibles)[-1] 

# messages = ["Hello userTwooo","Hi userThree","Wonderful day Alice","Nice day userThree"]
# senders = ["Alice","userTwo","userThree","Alice"]
# messages = ["How is leetcode for everyone","Leetcode is useful for practice"]
# senders = ["Bob","Charlie"]
messages =  ["tP x M VC h lmD","D X XF w V","sh m Pgl","pN pa","C SL m G Pn v","K z UL B W ee","Yf yo n V U Za f np","j J sk f qr e v t","L Q cJ c J Z jp E","Be a aO","nI c Gb k Y C QS N","Yi Bts","gp No g s VR","py A S sNf","ZS H Bi De dj dsh","ep MA KI Q Ou"]
senders =  ["OXlq","IFGaW","XQPeWJRszU","Gb","HArIr","Gb","FnZd","FnZd","HArIr","OXlq","IFGaW","XQPeWJRszU","EMoUs","Gb","EMoUs","EMoUs"]

print("largestWordCount", largestWordCount(messages, senders))

def countBits(n):
    dp = [0,1]
    for i in range(2,n+1):
        a = dp[i//2] + dp[i%2]
        print(a)
        dp.append(a)

    return dp    

n = 5
print("Counting Bits", countBits(n))

def subsets(arr):
    ans = []
    HelperSubset(arr, 0, [],ans)
    ans.sort()
    return ans

def HelperSubset(arr, idx, temp, ans):
    if idx >= len(arr):
        res = []
        [res.append(i) for i in temp]
        res.sort()  
        if res not in ans:
            ans.append(res) 
        return 
    else:
        temp.append(arr[idx])    
        HelperSubset(arr, idx+1, temp, ans)
        temp.pop()
        HelperSubset(arr, idx+1, temp, ans)

# nums = [1,2,2]
nums = [4,4,4,1,4]
print("subsets of array",subsets(nums))

def reverseWords(string):
    string = string.strip()
    ans = []
    word = ""
    for i in range(len(string)):
        if string[i] == " ":
            ans.insert(0, word)
            word = ""
        else:word+=string[i]
    ans.insert(0, word)
    ans = " ".join(ans)
    return ans    

# s = "the sky is blue"
# s = "  hello world  "
s = "a good   example"
print("Reverse Words in a String", reverseWords(s))

def largestNumber(arr):
    ans = str(arr[0])
    for i in range(1, len(arr)):
        res1 = ans + str(arr[i])
        res2 = str(arr[i]) + ans
        ans = str(max(res1, res2))
    return ans    

# nums = [10,2]
nums = [3,30,34,5,9]
print("larget number form in array is", largestNumber(nums))
from collections import defaultdict
def diagonalSort(mat):
    dct = defaultdict(list)
    row,columns=len(mat),len(mat[0])
    for i in range(row):
        for j in range(columns):
            dct[i-j].append(mat[i][j])
    for i in dict(dct):
        dct[i].sort(reverse=True)
    
    for i in range(row):
        for j in range(columns):
            mat[i][j]=dct[i-j].pop()
    return mat

mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
print("Sort the Matrix Diagonally", diagonalSort(mat))

def sortArrayByParityII(arr):
    even = [i for i in arr if i %2==0]
    odd = [i for i in arr if i % 2 !=0]

    for j in range(len(arr)):
        if j % 2 == 0:
            arr[j] = even[0]
            even.pop(0)
        else:
            arr[j] = odd[0]
            odd.pop(0)    
    return arr
nums = [4,2,5,7]
print("Sort Array By Parity II", sortArrayByParityII(nums))
print(4-6)