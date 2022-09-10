

from curses.ascii import isalpha

from email.policy import strict



def ReduceLowerCase(string):
    data = dict()

    for i in string:
        if i in data:
            data[i] += 1
        else:
            data[i] = 1

        if data[i] == 2:
            data.pop(i, None)

    ans = ""
    print(data)
    for j in data.keys():
        ans += j

    if not ans:
        return "Empty String"
    return ans


# s = "aaabccddd"
# s = "aa"
"tqauhujtmxnsbzpykwlvpfyqijvdhuhirdmuxiobyvxupqwydkpbxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh"
s = "zztqooauhujtmxnsbzpykwlvpfyqijvdhuhiroodmuxiobyvwwxupqwydkpeebxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh"
print("Reduce the lower string", ReduceLowerCase(s))


def ReverseArrayElements(arr):

    for i in range(len(arr)-1, -1, -1):
        pass


arr = [1, 2, 3, 4]
print("reverse array element is", ReverseArrayElements(arr))


def SortArray(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

    return arr


arr = [1, 5, 3, 2]
print("Sort array output is", SortArray(arr))


def lowerAndUpperCase(string):
    ans = ""
    for i in string:
        if i.isupper():
            i = i.lower()
            ans += i
        elif i.islower():
            i = i.upper()
            ans += i
        else:
            ans += i

    return ans
    pass


string = "HackerRank.com presents Pythonist 2"
print("Lower to Upper and Upper to Lower case ", lowerAndUpperCase(string))


def StringChecker(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return string


s = 'abracadabra'
position = 5
character = 'k'
print("Replacing the new character into the giving position",
      StringChecker(s, position, character))


def numberOfStringOccuers(string, sub_string):
    count = 0
    for i in range(len(string)):
        for j in range(len(sub_string)):
            if string[i+j] == sub_string[j] and j == (len(sub_string)-1):
                count = count+1
            if string[i+j] != sub_string[j]:
                break
        if i == len(string)-len(sub_string):
            break
    return count


string = "ABCDCDC"
sub_string = "CDC"
print("number of string occuers", numberOfStringOccuers(string, sub_string))


def StringFormatChecker(string):

    for i in string:
        if i.isalnum():
            print(True)

        elif i.isalpha():
            print(True)

        elif i.isdigit():
            print(True)

        elif i.islower():
            print(True)

        elif i.isupper():
            print(True)
        else:
            print(False)


string = "qA2"
print("string format checker is", StringFormatChecker(string))


def LonelyInteger(arr):
    data = dict()

    for i in range(len(arr)):
        if arr[i] in data:
            data[arr[i]] += 1
        else:
            data[arr[i]] = 1

    for j in data.keys():
        if data[j] == 1:
            return j


arr = [1, 1, 2]
print("lonely integer is", LonelyInteger(arr))


def ElementOccurKtime(arr, k):
    data = dict()
    if k == 1:
        return arr[0]
    for i in range(len(arr)):
        if arr[i] in data:
            data[arr[i]] += 1
            if data[arr[i]] == k:
                return arr[i]

        else:
            data[arr[i]] = 1


# arr = [1, 7, 4, 3, 4, 8, 7]
# k = 2
arr = [3, 1, 2]
k = 1
print("First element to occur k times", ElementOccurKtime(arr, k))


def CompressString(string):
    count = 0
    ans = []
    list1 = []
    list1[:0] = string
    string = list1
    first = string[0]

    for i in range(len(list1)):
        if list1[i] == first:
            count += 1
        if list1[i] != first:
            res = (count, list1[i])
            ans.append(res)
            count = 0
        first = list1[i]
    return ans


string = "1222311"
print("Comprese string is", CompressString(string))


def CaserChifer(string, k):
    orignal = "abcdefghijklmnopqrstuvwxyz"
    temp = []

    for char in string:
        temp.append(ord(char))

    for i in range(len(temp)):
        # upper-case 65-90
        if 65 <= temp[i] <= 90:
            temp[i] = (65 + (temp[i] - 65 + k) % 26)
        # lower case 97-122
        if 97 <= temp[i] <= 122:
            temp[i] = (95 + (temp[i] - 95 + k) % 26)
    return "".join(map(chr, temp))


string = "middle-Outz"
k = 2
print("caser chifer solution", CaserChifer(string, k))


def FizzBizz(n):
    result = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(str(i))


n = 15
print("Fizz Bizz number is", FizzBizz(n))


def MagicalMatrix(s):
    pre = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
    ]

    t = []
    
    for i in pre:
        res = 0
        for j , k in zip(i, s):
            for x,y in zip(j,k):
                res += max([x,y]) - min([x,y])
        t.append(res)
    return min(t)            

s = [[4, 8, 2], [4, 5, 7], [6, 1, 6]]
print("Magical matrix is", MagicalMatrix(s))

def RecursiveDigitSum(n,k):
    ans = ""
    while k>0:
        ans += n
        k -=1

    list1=[]
    list1[:0]=ans

    ans_sum = 0
    for i in range(len(list1)):
        ans_sum += int(list1[i])

    while True:
        if len(str(ans_sum)) <=1:
            break
        elif len(str(ans_sum)) > 1:
            list1 = []
            list1[:0] = str(ans_sum)
            ans_sum = 0
            for i in range(len(list1)):
                ans_sum += int(list1[i])

    return ans_sum          

n = "9875"
k = 4
print("recursive sum is", RecursiveDigitSum(n,k)) 


def DesignerPDF(hieght, word):
    alpha = list(map(chr, range(97, 123)))
    
    high = 0

    for i in word:
        if i in alpha:
            ind = alpha.index(i)
            if ind < len(height) + 1:
                high = max(high, height[ind])        
    ans = high * len(word)
    return ans
    pass

height = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
word = "zaba"
print("Disigner pwd is", DesignerPDF(height, word))

def BeautifulDaysAtTheMovies(i, j ,k):
    count = 0
    for m in range(i, j+1):
        rever = str(m)[::-1]
        ans = (m - int(rever))
        if ans % k == 0:
            count += 1
    return count        
i,j,k = 20, 23, 6
print("Beautiful days at the movies is", BeautifulDaysAtTheMovies(i,j,k))
arr = [1,2,3,4,5]
B
B
B
B
B
B
B
B
B
B

print("Aniket  suryawanshi 123")
