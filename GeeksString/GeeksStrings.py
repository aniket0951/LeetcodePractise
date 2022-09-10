from calendar import leapdays
from gettext import dpgettext
from re import M


def ImplementAtoi(string):
    ans = 0
    for i in range(len(string)):
        if string[i].isalpha():
            return -1
        else:
            ans = ans * 10 + (ord(string[i]) - ord('0'))
    return ans


# string = "123"
# string = "21a"
string = "-12"
print("String integer is Atoi", ImplementAtoi(string))


def MinimumIndexedCharacter(str1, patt):
    i = 0
    j = 0
    ans = []
    while i < len(str1) and j < len(patt):
        if str1[i] == patt[j]:
            ans.append(i)

        i += 1
        j += 1

    if len(ans) > 0:
        res = min(ans)
        return res
    return -1


# str = "geeksforgeeks"
# patt = "set"
# str = "adcffaet"
# patt = "onkl"
str = "hasjkhflaskdf"
patt = "sdlkjfshd"
print("Manimum indexed character is", MinimumIndexedCharacter(str, patt))


def EditDistance(str1, str2):
    m = len(str1)
    n = len(str2)
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

    # Fill d[][] in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],  # Insert
                                   dp[i - 1][j],  # Remove
                                   dp[i - 1][j - 1])  # Replace

    return dp[m][n]


# s = "geek"  
# t = "gesek"
# s = "gfg" 
# t = "gfg"
s = "ecfbefdcfca"
t = "badfcbebbf"
print("Edit distance is", EditDistance(s, t))


def LongestCommonSubstring(s1, s2):
    n = len(s1)
    m = len(s2)

    dp = [[0 for _ in range(m + 1)] for i in range(n + 1)]
    res = 0
    for i in range(n + 1):
        for j in range(m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                res = max(res, dp[i][j])
            else:
                dp[i][j] = 0
    return res


# S1 = "ABCDGH"
# S2 = "ACDGHR"
# S1 = "adac"
# S2 = "adadac"
# S1 = "ABC" 
# S2 = "ACB"
# S1 = "ABCD"
# S2 = "ABC"
S1 = "ABC"
S2 = "AC"
print("Longest Common Substring is", LongestCommonSubstring(S1, S2))


def LongestPalindromeinaString(str1):
    str2 = str1[::-1]
    i = 0
    j = 0
    ans = ""

    while i < len(str1):
        if str1[i] == str2[j]:
            ans += str1[i]
            i += 1
            j += 1
        else:
            i += 1
    if len(ans) > 1:
        return ans
    return str1[0]


# S = "aaaabbaa"
S = "abc"
print("Longest palindrom in a string is", LongestPalindromeinaString(S))


def CheckStringIsIsogram(s):
    if any(s.count(i) > 1 for i in s):
        return False
    return True


# S = "machine"
S = "geeks"
print(CheckStringIsIsogram(S))


def FirstLetterOfString(s):
    ans = ""
    cur_word = ""
    for i in s:
        if i == " ":
            ans += cur_word[0]
            cur_word = ""
        else:
            cur_word += i

    if len(cur_word) > 0:
        ans += cur_word[0]
    return ans


S = "geeks for geeks"
print("first letters of string is", FirstLetterOfString(S))


def SecondMostRepeated(arr):
    data = dict()
    for i in arr:
        if i in data:
            data[i] += 1
        else:
            data[i] = 1
    first = max(list(data.values()))
    sec = 0
    for v in data.values():
        if v != first:
            sec = max(sec, v)
    return sec


arr = ["aaa", "bbb", "ccc", "bbb", "aaa", "aaa"]
print("Second most repeated element", SecondMostRepeated(arr))


def RemoveConsecutiveChar(string):
    ans = ""
    ans += string[0]
    for i in range(1, len(string)):
        if string[i] != string[i - 1]:
            ans += string[i]

    return ans


# S = "aabb"
S = "aabaa"
print("Remove Consecutive Characters ", RemoveConsecutiveChar(S))


def IsomorphicString(str1, str2):
    if len(str1) == len(str2):
        d1, d2 = {}, {}
        for c1, c2 in zip(str1, str2):
            if (c1 in d1 and d1[c1] != c2) or (c2 in d2 and d2[c2] != c1):
                return False
            d1[c1] = c2
            d2[c2] = c1
        return True
    else:
        return False

    # str1 = "aab"


# str2 = "xxy"
# str1 = "aab"
# str2 = "xyz"
str1 = "aba"
str2 = "xyy"
print("two strings are isomorphic or not", IsomorphicString(str1, str2))


def GameWithString(s, k):
    s = sorted(s)
    a = len(s) - k
    print(len(s))
    s = s[:a]

    print(len(s))
    data = {}

    for i in s:
        if i in data:
            data[i] += 1
        else:
            data[i] = 1

    ans = 0
    for v in data.values():
        squere = v * v
        ans += squere
    return ans


# s = "abccc"
# k = 1
# s = "aabcbcbcabcc"
# k = 3
s = "fxnsmkasmlerxxoxhfwviluzttqqotdwrsqfcsxrddicaxahewemjyleudukxzgqrzvvrtmvwvxzuxiyvnngna"
k = 21
print("Game with string is", GameWithString(s, k))


def MaxDifferance0and1(s):
    ans = -1
    num = 0
    for i in s:
        if i == "0":
            num += 1
        else:
            num -= 1
        ans = max(ans, num)
        if num < 0:
            num = 0
    return ans


S = "11000010001"
print("Max differance in os and 1s", MaxDifferance0and1(S))


def LongestKUniqueCharSubstring(s, k):
    i = 0
    j = 0
    data = {}

    while i < len(s):
        if s[i] in data:
            data[s[i]] += 1
        else:
            data[s[i]] = 1

        i += 1
        if len(data) > k:
            while j < i:

                data[s[j]] -= 1
                if data[s[j]] == 0:
                    del data[s[j]]
                j += 1
                if len(data) <= k:
                    break
    print(data)
    if len(data) != k:
        return -1
    else:
        ans = sum(data.values())
        return ans

    # S = "aabacbebebe"


# K = 3
# S = "aaaa"
# K = 2
# S = "gbwkfnqduxwfn"
# K = 15
S = "wcysyycqpev"
K = 6
print("Longest K unique characters substring", LongestKUniqueCharSubstring(S, K))


def findLongestWordInDict(data, s):
    cur = ""

    for word in sorted(data):
        i = j = 0

        while i < len(s) and j < len(word):
            if word[j] == s[i]:
                j += 1

            i += 1

        if j == len(word) and len(word) > len(cur):
            cur = word

    return cur


# d = {"ale", "apple", "monkey", "plea"}
# ss = "abpcplea"
d = {"a", "b", "c"}
ss = "abpcplea"
print("Longest word in dictionary is", findLongestWordInDict(d, ss))


def CountPS(S):
    count = 0
    i = 0
    j = i + 1
    while i < len(S):
        if j == len(S):
            i += 1
            j = i + 1
        else:
            temp = S[:j]
            res = temp[::-1]
            if temp == res:
                count += 1
                i += 1
                j = i + 1
            else:
                j += 1
    return count


# str = "abaab"
# str = "abbaeae"
# str = "a"
str = "aaaaa"
print("Count Palindrome Sub-Strings of a String", CountPS(str))
from collections import defaultdict, Counter
def RepetedFirst(string):

    d = Counter(string)

    for i in string:
        if d[i] > 1:
            return i

    print(d)
    return -1
# S = "geeksforgeeks"
S = "abcde"
print(RepetedFirst(S))

def lcs(m,n, s1,s2):
    dp = [[0 for i in range(m+1)]for i in range(n+1)]
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif s2[i-1] == s1[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[-1][-1]                          

str1 = "ABCDGH"
m = len(str1)
str2 = "AEDFHR"
n = len(str2)
# str1 = "ABC"
# str2 = "AC"
# m = len(str1) 
# n = len(str2)
print("LCS of string is", lcs(m,n,str1, str2))

# ["MyCalendar", "book", "book", "book"]
# [[], [10, 20], [15, 25], [20, 30]]
# Output
# [null, true, false, true]

# Explanation
# MyCalendar myCalendar = new MyCalendar();
# myCalendar.book(10, 20); // return True
# myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
# myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, 
# but not including 20.

class MyCalendar:
    ans = []
    def __init__(self):
        self.cal = []

    def book(self, start: int, end: int) -> bool:
        if len(self.cal) <= 0:
            self.cal.append([start, end])
            print(True)
            return True
        else:
            lasttime = self.cal[-1]
            #[10,20]
            if start > lasttime[1]:
                self.cal.append([start, end])
                print(False)
                return False
            if lasttime[1] >= start:
                self.cal.append([start, end])
                print(True)
                return True    

calende = MyCalendar()
calende.book(10, 20)
calende.book(15, 25)