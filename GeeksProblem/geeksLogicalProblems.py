"""
find a frequency of particular value in array
"""


def findFrequencyInArray(myList, number):
    counter = 0
    for i in myList:
        if i == number:
            counter = counter + 1
    return counter


A = [1, 1, 1, 1, 1, 1, 2]
N = 2
print("the frequency of given integer number is", findFrequencyInArray(A, N))


def sortArrayWithAscendingArray(myList):
    for i in range(len(myList)):
        for j in range(i + 1, len(myList)):
            if myList[i] > myList[j]:
                temp = myList[i]
                myList[i] = myList[j]
                myList[j] = temp

    return myList


A = [0, 2, 1, 2, 0]
print("array is sorting with ascending order", sortArrayWithAscendingArray(A))


def subArrSum(myList, n, s):
    if n <= 0:
        return [-1]
    subArraySum = 0
    startIndex = 0

    for i in range(n):
        subArraySum += myList[i]
        while subArraySum > s:
            # remove the startIndex from the sum till subArraySum < s
            subArraySum -= myList[startIndex]
            startIndex += 1
        # check whether subArraySum equals s
        if subArraySum == s:
            print("remove subArraySum", subArraySum)
            return [startIndex + 1, i + 1]
    return [-1]


N = 5
S = 12
A = [1, 2, 3, 7, 5]
# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Sum of array of s is", subArrSum(A, N, S))


def negativeElementEndOfArray(arr):
    # Create an empty array to store result
    temp = [0 for k in range(len(arr))]
    # Traversal array and store +ve element in
    # temp array
    j = 0  # index of temp
    for i in range(len(arr)):
        if arr[i] >= 0:
            temp[j] = arr[i]
            j += 1

    # Store -ve element in temp array
    for i in range(len(arr)):
        if arr[i] < 0:
            temp[j] = arr[i]
            j += 1

    # Copy contents of temp[] to arr[]
    for k in range(len(arr)):
        arr[k] = temp[k]
    return arr


A = [-5, 7, -3, -4, 9, 10, -1, 11]
print("the negative element are placed in end of array", negativeElementEndOfArray(A))


def findUnionNumber(listA, listB, n):
    emptyList = []

    for i in listA:
        for j in listB:
            if i == j:
                listB.remove(i)
                break
        emptyList.append(i)
    emptyList = emptyList + listB
    return len(emptyList)


A = [1, 2, 3, 4, 5]
B = [1, 2, 3, 6]
print("the same element take one time and return the number of arrays", findUnionNumber(A, B, 5))


def arrayRotationByOnePositionClockWise(mylist):
    x = mylist[len(mylist) - 1]
    for i in range(len(mylist) - 1, 0, -1):
        mylist[i] = mylist[i - 1]

    mylist[0] = x
    return mylist


A = [9, 8, 7, 6, 4, 2, 1, 3]
print("array rotation by one position in clock wise", arrayRotationByOnePositionClockWise(A))


def findMissingElement(myList):
    for i in range(len(myList)):
        for j in range(i + 1, len(myList)):
            if myList[i] >= myList[j]:
                temp = myList[i]
                myList[i] = myList[j]
                myList[j] = temp

        x = 1
        missingNum = 0

        for k in range(len(myList)):
            for m in range(k + 1, len(myList)):
                if myList[k] + x != myList[m]:
                    missingNum = myList[k] + x

    return missingNum


A = [111, 112, 113, 114, 115, 117]
print("finding the missing number of array is", findMissingElement(A))


def arraySumOfTwo(myList, k):
    counter = 0
    for i in range(len(myList)):
        for j in range(i + 1, len(myList)):
            if myList[i] + myList[j] == k:
                counter = counter + 1

    return counter


A = [1, 1, 1, 1]
k = 2
print("The number of pairs of elements in the array whose sum is equal to K is", arraySumOfTwo(A, k))


def findDuplicateElements(myList):
    emptyList = []
    for i in range(len(myList)):
        for j in range(i + 1, len(myList)):
            if myList[i] == myList[j]:
                emptyList.append(myList[i])

    if emptyList:
        finalList = []
        for i in range(len(emptyList)):
            for j in range(i + 1, len(emptyList)):
                if emptyList[i] >= emptyList[j]:
                    temp = emptyList[i]
                    emptyList[i] = emptyList[j]
                    emptyList[j] = temp
        for num in emptyList:
            if num not in finalList:
                finalList.append(num)
        return finalList
    else:
        return [-1]
    pass


A = [13, 9, 25, 1, 1, 0, 22, 13, 22, 20, 3, 8, 11, 25, 10, 3, 15, 11, 19, 20, 2, 4, 25, 14, 23, 14]
print("the duplicate numbers occurring in array is", findDuplicateElements(A))


def findThreeDuplicateValue(listA, listB, listC):
    emptyList = []
    finalList = []
    for i in listA:
        for j in listB:
            for k in listC:
                if i == j and j == k:
                    emptyList.append(i)

    for n in emptyList:
        if n not in finalList:
            finalList.append(n)
    return finalList


A = [1, 5, 10, 20, 40, 80]
B = [6, 7, 20, 80, 50, 100]
C = [3, 4, 15, 20, 30, 50, 70, 80, 120]
print("the same element in all three array is", findThreeDuplicateValue(A, B, C))


def findPositionOfFirstDuplicate(myList, n):
    max = 0
    for x in range(n):
        if myList[x] > max:
            max = myList[x]

    temp = [0 for i in range(max + 1)]

    for x in range(n):
        num = myList[x]
        temp[num] += 1

    for x in range(n):
        num = myList[x]
        if temp[num] > 1:
            return x

    return -1  # if no repeating element found

    pass


A = [1, 5, 3, 4, 3, 5, 6]
n = len(A)
print("the first duplicate element position is", findPositionOfFirstDuplicate(A, n))


def findNonRepeatingNumb(myList):
    emptyList = []
    for i in myList:
        if i != i + 1:
            break
        emptyList.append(i)
    print(emptyList)

    for i in range(len(myList)):
        j = 0
        while j < len(myList):
            if i != j and myList[i] == myList[j]:
                break
            j += 1
        if j == len(myList):
            return myList[i]

    return -1


A = [-1, -17, -12, 8, 16, -17, -13, -14, -3, -6, -5, -11, -10, -12, -5, 19, -17, -5, -1, 12]
print("the non repeating number is", findNonRepeatingNumb(A))


def findLongestSubSequenceOfString(a, sec, c, m, n,o):
    L = [[[0 for i in range(o + 1)] for j in range(n + 1)]
         for k in range(m + 1)]

    ''' Following steps build L[m+1][n+1][o+1] in
    bottom up fashion. Note that L[i][j][k]
    contains length of LCS of X[0..i-1] and
    Y[0..j-1] and Z[0.....k-1] '''
    for i in range(m + 1):
        for j in range(n + 1):
            for k in range(o + 1):
                if i == 0 or j == 0 or k == 0:
                    L[i][j][k] = 0

                elif (a[i - 1] == sec[j - 1] and
                      a[i - 1] == c[k - 1]):
                    L[i][j][k] = L[i - 1][j - 1][k - 1] + 1

                else:
                    L[i][j][k] = max(max(L[i - 1][j][k],
                                         L[i][j - 1][k]),
                                     L[i][j][k - 1])

    # L[m][n][o] contains length of LCS for
    # X[0..n-1] and Y[0..m-1] and Z[0..o-1]
    return L[m][n][o]
    return L[m][n][o]


A = "geeksa"
B = "geeksafor"
C = "geeksforgeeks"
m = len(A)
n = len(B)
o = len(C)
print("the longest common sub sequence is", findLongestSubSequenceOfString(A, B, C, m,n,o))


def SumofMiddleElementsoftwosortedarrays(arr1, arr2):
    temp = arr1 + arr2
    temp.sort()

    l = 0
    r = len(temp) - 1

    first_mid = l + (r-l) // 2
    first_mid_ele = temp[first_mid]

    temp.remove(temp[first_mid])

    sec_mid = l + (r-l) //2
    sec_mid_ele = temp[sec_mid]

    ans = first_mid_ele + sec_mid_ele

    return ans


# Ar1 = [1, 2, 4, 6, 10]
# Ar2 = [4, 5, 6, 9, 12]

Ar1 = [1, 12, 15, 26, 38]
Ar2 = [2, 13, 17, 30, 45]

print("Sum of Middle Elements of two sorted arrays", SumofMiddleElementsoftwosortedarrays(Ar1, Ar2))


def OverLappingIntervals(arr):
    arr.sort(key = lambda x : x[0])
    
    st = []

    for i in range(len(arr)):
        cm = arr[i]

        if i == 0:
            st.append(cm)
        else:

            lm = st[-1]

            if lm[1] < cm[0]:
                st.append(cm)
            else:
                st.pop()
                mm = [lm[0], max(lm[1], cm[1])]
                st.append(mm)

    return st                

Intervals = [[1,3],[2,4],[6,8],[9,10]]
print("Over lapping inteval is", OverLappingIntervals(Intervals))

def Knegation(arr, k):
    arr.sort()
    ans = 0
    for i in range(len(arr)):
        if arr[i] < 0 and k > 0:
            arr[i] = abs(arr[i])
            k -= 1
    print(arr)
    for i in arr:
        ans += i

    x = min(arr)
    if k and 1:
        ans -= 2*x 

    return ans               

# K = 1
# arr = [1, 2, -3, 4, 5]

K = 5
arr = [5, -2, 5, -4, 5, -12, 5, 5, 5, 20]
# K = 5
# arr = [1,2,3,4,5]
print("Maximize sum after K negations", Knegation(arr, K))

def SetBitCount(arr):
    func = lambda e:bin(e).count('1')
    arr.sort(reverse=True,key = func)
    return arr

# arr = [1, 2, 3, 4, 5, 6]
arr = [5, 2, 3, 9, 4, 6, 7, 15, 32  ]
print("Reverse the array by binary representation", SetBitCount(arr))

def PaireswithSpecificdifferance(arr, k):
    temp = []
    output = 0
    for i in range(1, len(arr)):
        res = abs(arr[i] - arr[i-1])
        if res < k:
            temp.append([arr[i], arr[i-1]])
            ans = arr[i] + arr[i-1]
            output += ans
    print(temp)
    return output       

arr = [3, 5, 10, 15, 17, 12, 9]
k = 4
print("Pairs with specific difference ", PaireswithSpecificdifferance(arr, k))