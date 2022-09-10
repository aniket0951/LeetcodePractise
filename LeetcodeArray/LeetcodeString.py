from dataclasses import dataclass
from itertools import count
from xml.dom.minidom import Element


def ValidPalindrom(s):
        s = ''.join(ch for ch in s if ch.isalnum())
        s = "".join(s.split())
        s = s.lower()
        revS = s[::-1]  
        if revS == s:
            return True
        return False     

# s = "A man, a plan, a canal: Panama"
# s = "race a car"
# s = " "
s = "0P"
print("Is valid palindrom or not", ValidPalindrom(s))

def IsoMarphicString(s, t):
    hashMap ={}
    if len(s) != len(t):
        return False

    for idx, c in enumerate(s):
        if c not in hashMap:
            if t[idx] not in hashMap.values():
                hashMap[c] = t[idx]
            else:
                return False
        if hashMap[c] != t[idx]:
            return False
    return True
    pass

# s = "egg"
# t = "add"
# s = "foo"
# t = "bar"
# s = "paper"
# t = "title"
s = "bbbaaaba"
t = "aaabbbba"
print("Isomarphic string", IsoMarphicString(s,t))

def AnagramString(s,t):
    if len(s) != len(t):
        return False

    data = {}
    for i in s:
        if i in data:
            data[i] += 1
        else:
            data[i] = 1
    
    for j in t:
        if j in data:
            data[j] -= 1
            if data[j] < 0:
                return False 
 
    for v in data.values():
        if v > 0:
            return False
    return True    
    pass

s = "anagram"
t = "nagaram"
# s = "rat"
# t = "car"
print("Anagram string", AnagramString(s,t))

def WordPatter(pattern, s):
    if len(pattern) != len(s.split()):
        return False
    dictonary = {}
    s = s.split()
    for i in range(len(pattern)):
        if pattern[i] not in dictonary:
            if s[i] not in list(dictonary.values()):
                dictonary[pattern[i]] = s[i]
            else:
                return False
        else:
            if dictonary[pattern[i]] != s[i]:
                return False
    return True                        

pattern = "abba" 
s = "dog cat cat dog"
# pattern = "abba"
# s = "dog cat cat fish"
# pattern = "aaaa" 
# s = "dog cat cat dog"
# pattern = "aba"
# s = "dog cat cat"
print("Word pattern", WordPatter(pattern, s))

def FirstUniqueCharacterinaString(s): 
    from collections import Counter
    d = Counter(s)  
    print(d)
    data = {}

    for i in range(len(s)):
        if s[i] not in data:
            data[s[i]] = i
        else:
            data[s[i]] = -1
    print(data)
    for v in data.values():
        if v >= 0:
            return v

    return -1                               

# s = "leetcode"
# s = "loveleetcode"
# s = "aabb"
s = "aadadaad"
print("First Unique Character in a String", FirstUniqueCharacterinaString(s))

def FindDifferance(s,t):
    if len(s) <= 0:
        return t

    for i in t:
        if i not in s:
            return i    

# s = "abcd"
# t = "abcde"
s = ""
t = "y"
print("Differance between both string", FindDifferance(s, t))

def ValidParanthess(s):
        if len(s) % 2 != 0:
            return False
        dict = {'(' : ')', '[' : ']', '{' : '}'}
        stack = []
        for i in s:
            if i in dict.keys():
                stack.append(i)
            else:
                if stack == []:
                    return False
                a = stack.pop()
                if i!= dict[a]:
                    return False
        return stack == []

s = "()"
print("Valid paranthess ", ValidParanthess(s))

def countandsay(n):
      s,i = "1",1
      while i < n:
        new_s,idx = "",0
        while idx<len(s):
          c, counter = s[idx], 1
          while idx<len(s)-1 and s[idx+1]==c:
            idx+=1; counter+=1
          new_s+= (str(counter)+c); idx+=1
        s = new_s;  i+=1
      return s                 

n = 4
print("count and say", countandsay(n))

def PalindromPartitions(s):
    temp = [[i for i in s]]
    res = ""
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            res += str(s[i-1])
        else:
            res += str(s[i-1])
            temp.append([res])
            res = s[i]   
    temp.append(res)
    return temp

s = "aab"
print("Palindrome Partitioning", PalindromPartitions(s))

def IsSubsequence(s,t):
    i = 0
    j = 0
    
    ans = ""
    while j < len(t) and i < len(s):
        if s[i] == t[j]:
            ans += str(s[i])
            i += 1
            j += 1
        else:
            j += 1
    
    if s == ans:
        return True
    return False       

s = "abc"
t = "ahbgdc"
# s = "axc"
# t = "ahbgdc"
# s = "acb"
# t = "ahbgdc"
# s = "b"
# t = "abc"
print("Is subsequence ", IsSubsequence(s,t))

