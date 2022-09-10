def getMaxCountChar(count):
  maxCount = 0
  for i in range(26):
    if count[i] > maxCount:
        maxCount = count[i]
        maxChar = chr(i + ord('a'))

  return maxCount, maxChar

def rearrangeString(S):
  n = len(S)
  
  if not n:
      return False
    
  count = [0] * 26
  for char in S:
      count[ord(char) - ord('a')] += 1


  maxCount, maxChar = getMaxCountChar(count)

  if maxCount > (n + 1) // 2:
      return False

  res = [None] * n

  ind = 0

  while maxCount:
      res[ind] = maxChar
      ind += 2
      maxCount -= 1
      
  count[ord(maxChar) - ord('a')] = 0

  for i in range(26):
      while count[i] > 0:
          if ind >= n:
              ind = 1
          res[ind] = chr(i + ord('a') )
          ind += 2
          count[i] -= 1


  return ''.join(res)

# str = "geeksforgeeks"
str = "bbbbb"
print("Rearrange the character", rearrangeString(str))

def LongestPalindromInString(s):
       start = 0
       maxL = 1
       low = 0
       high = 0
       
       for i in range(1, len(s)):
           low = i-1
           high = i
           while low >=0 and high < len(s) and s[low] == s[high]:
               if (high -low + 1) > maxL:
                   start = low
                   maxL = high - low + 1
                   
               low -= 1
               high += 1
               
           low = i-1
           high = i+1
           while low >= 0 and high < len(s) and s[low] == s[high]:
               if (high - low + 1) > maxL:
                   start = low
                   maxL = high - low + 1
                   
               low -= 1
               high += 1
               
       return s[start: start+maxL]

s = "aaaabbaa"
print("Longest Palindrome in a String ", LongestPalindromInString(s)) 

from collections import deque
from pprint import pp
def PhoneDigits(arr):
    n = len(arr)
    phone = {
        2:['a','b','c'],
        3:['d','e','f'],
        4:['g','h','i'],
        5:['j','k','l'],
        6:['m','n','o'],
        7:['p','q','r','s'],
        8:['t','u','v'],
        9:['w','x','y','z'],
        0:['']
     }
        
    q = deque()
    q.append((0,''))
    ans = []

    while q:
        i,word = q.popleft()

        if i==n:
            ans.append(word)
            continue

        for letter in phone[arr[i]]:
            q.append((i+1,word+letter))
    return ans    

arr = [2, 3, 4]
print("Possible Words From Phone Digits", PhoneDigits(arr))

ini_str = "ABSG"
 
# Printing initial string
print("Initial string", ini_str)
 
# Finding all permutation
result = []
 
def permute(data, i, length):
    if i == length:
        result.append(''.join(data) )
    else:
        for j in range(i, length):
            # swap
            data[i], data[j] = data[j], data[i]
            permute(data, i + 1, length)
            data[i], data[j] = data[j], data[i] 
permute(list(ini_str), 0, len(ini_str))
print(result)

from collections import defaultdict
def MostFrequentInArrayOfString(arr):
    data = defaultdict(int)

    for i in arr:
        data[i] += 1
    
    max_freq = max(data.values())
    ans = []
    for k, v in data.items():
        if v == max_freq:
            ans.append(k)

    return ans[-1]            

arr = ["xejdcj", "xejdcj" ,"lvjpb" ,"tmyuiu", "lvjpb", "tmyuiu" ,"ovoba" ,"lvjpb" ,"lvjpb" ,"fqhyu" ,"fqhyu", "tmyuiu" ,"xejdcj", "tmyuiu", "fqhyu", "ovoba", "xejdcj"]
# arr = ["hello","world"]
# arr = ["geeks","for","geeks"]
# arr = ["rstax" ,"rstax" ,"gebi", "gebi" ,"rstax" ,"tgpj" ,"tgpj" ,"tgpj" ,"gebi" ,"rstax", "tgpj"]
print("Most freqency in array of string is", MostFrequentInArrayOfString(arr))

def Anagrams(words):
    res = []
    for i in range(len(words)):
        if words[i] not in res:
            res.append(words[i])
        j = i + 1
        tag = False
        while j < len(words):
            s = 0
            e = len(words[j]) - 1
            while e < len(words):
                if words[e] in words[i]:
                    tag = True
                else:
                    tag = False
                e += 1        

word = ["act","god","cat","dog","tac"]
# print("Anagram strings", Anagrams(word))
from collections import OrderedDict

def countMin(string):
        Str = string
        rev = Str[::-1]
        n = len(Str)
        dp = [[0]*(n + 1) for i in range(n+1)]
        
        for i in range(n+1):
            for j in range(n+1):
                if i*j == 0:
                    continue
                
                elif Str[n-j] == rev[n-i]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                    
                    
        return n - dp[i][j]

# string = "abcd"
# string = "aa"
string = "geeks"
# string = "anasdad"
print("Form a palindrome", countMin(string))

def minRepeats(a,b):
        len_a = len(a)
        len_b = len(b)
     
        for i in range(0, len_a):
             
            if a[i] == b[0]:
                k = i
                count = 1
                for j in range(0, len_b):
                     
                    # we are reiterating over A again and
                    # again for each value of B
                    # Resetting A pointer back to 0 as B
                    # is not empty yet
                    if k >= len_a:
                        k = 0
                        count = count + 1
                         
                    # Resetting A means count
                    # needs to be increased
                    if a[k] != b[j]:
                        break
                    k = k + 1
                     
                # k is iterating over A
                else:
                    return count
        return -1

A = "abcd"
B = "cdabcdab"
print("Minimum times A has to be repeated such that B is a substring of it", minRepeats(A,B))

def findTime(s1,s2):
    if len(s2) <= 1:
        return s1.index(s2)
    ans = 0
    i = 0
    for j in s2:
        idx = s1.index(j)
        res = abs(i-idx)
        ans += res
        i = idx
    return ans

# S1 = "abcdefghijklmnopqrstuvwxyz"
# S2 = "cba"
S1 = "zyxwvutsrqponmlkjihgfedcba"
S2 = "a"
print("A Special Keyboard", findTime(S1, S2))

def findMaximumNum(s, k):

    maximum = int(s)

    for i in range(0, len(s) - 1):
      maxc = s[i]
      if k == 0:
        break
      for j in range(i + 1, len(s)):

         if int(s[j]) > int(maxc):
            maxc = s[j]

      if maxc != s[i]:
        k -= 1
        idx = s[i + 1:].rfind(maxc) + i + 1
        ll = list(s)
        ll[i], ll[idx] = ll[idx], ll[i]
        s = ''.join(ll)
        maximum = max(int(s), maximum)
       
    return maximum                

str = "1234567"
k = 4
# k = 3
# str = "3435335"
# str = "1034"
# k = 2
print("Largest number in K swaps", findMaximumNum(str,k))
from collections import OrderedDict
def Anagrams(words):
    d = OrderedDict()
    for i in words:
        w = ''.join(sorted(i))
        if w in d:
            d[w].append(i)
        else:
            d[w] = []
            d[w].append(i)
    ans = []
    for v in d.values():
        for i in v:
            ans.append(i)       
    return ans       


words = ["act","god","cat","dog","tac"]
print("Print Anagrams Together", Anagrams(words))

def allPossibleSubsequences(s):
    data = OrderedDict()
    vowels = ('a','e', 'i','o','u')
    for i in range(len(s)):
        if s[i] in vowels:
            if s[i] not in data:
                data[s[i]] = []
            j = i + 1
            temp = ""
            while j < len(s):
                if s[j] not in vowels:
                    temp +=  s[j]
                    if temp not in data[s[i]]:
                        res = ''.join(sorted(temp))
                        data[s[i]].append(res)
                    # temp = ""
                else:temp += s[j]
                j += 1

    ans = []
    for v in data.values():
        for k in v:
            ans.append(k)
        
    if s[0] in vowels and s[-1] not in vowels:
        ans.append(s)   
    return ans     

# S = "abc"
# S = "aab"
S = "xabcef"
print("String Subsequence Game", allPossibleSubsequences(S))

def longestPalinSubseq(s1):
    s2 = s1[::-1]
    
    x = len(s1)
    y = len(s2)

    if x == 0 and y == 0:
        return 0

    dp = [[0 for i in range(x+1)] for i in range(y+1)] 
    ans = 0
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif s2[i-1] == s1[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
                ans = max(ans, dp[i][j])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return ans                

# s1 = "bbabcbcab"
s1 = "abcd"
print("longest palindrom subsequence", longestPalinSubseq(s1))

n = 927
a = bin(n)
a = a[2:]
print(a)
ans = 0
curr_ones = 0
for i in range(len(a)):
    if a[i] == "1":
        curr_ones += 1
    else:
        ans = max(ans, curr_ones)
        curr_ones = 0

if curr_ones != 0:
    ans = max(ans, curr_ones)
    
print(ans)            