def findRunnerUp(myList):
    first = second = 0
    for i in range(len(myList)):
        if myList[i] > first:
            second = first
            first = myList[i]
        elif myList[i] > second and myList[i] != first:
            second = myList[i]

    print(second)


A = [2, 3, 6, 6, 5]
print("the runner up is", findRunnerUp(A))


def distinctPair(arr, k):
    count = 0
    emptyList = []
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):

            if arr[i] - arr[j] == k or arr[j] - arr[i] == k:
                if arr[i] and arr[j] not in emptyList:
                    emptyList.append(arr[i])
                    emptyList.append(arr[j])
                    count += 1
                else:
                    continue

    return count


k = 1
A = [1, 1, 2, 2]
print("distinct between list is the", distinctPair(A, k))


def leadersInArray(myList):
    emptyList = []
    greateInt = 0
    for i in range(len(myList)):
        for j in range(i + 1, len(myList)):
            if myList[j] > myList[i]:
                emptyList.append(myList[j])
            if myList[i] > myList[j]:
                emptyList.append(myList[i])

    return emptyList


# A = [6, 7, 4, 2, 5, 3]
A = [11, 10, 9, 8]
print("the leader of right side is", leadersInArray(A))

print(2 + -3 + 1)


def findingSubArraySum(myList):
    n_sum = 0
    # s = set()
    s = []
    for i in range(len(myList)):
        n_sum += myList[i]
        if n_sum == 0 or n_sum in s:
            return "YES"
        s.append(n_sum)
    return False


A = [4, 2, -3, 1, 6]
# A = [4, 2, 0, 1, 6]
print("the subArray's sum is 0", findingSubArraySum(A))


def maximumSumOfArray(myList):
    sum = 0
    max = myList[0]

    for i in range(len(myList)):
        sum += myList[i]
        if sum > max:
            max = sum
        if sum < 0:
            sum = 0
    return max


# A = [1, 2, 3, -2, 5]
A = [-1, -2, -3, -4]
print("maximum sum of sub array", maximumSumOfArray(A))


def findMaximumFactorial(facNumb):
    # factorial = 1
    # for i in range(1, facNumb + 1):
    #     factorial *= i
    # return factorial
    resInt = 1
    resStr = ""
    res = []
    for i in range(1, facNumb + 1):
        resInt *= i
    resStr = str(resInt)
    for i in resStr:
        res.append(int(i))
    return res


# A = 5
A = 10
print("the maximum factorial is", findMaximumFactorial(A))


def maximumProductSubArray(myList):
    sum = myList[0]
    cunMax = myList[0]
    cunMin = myList[0]
    for i in range(1,len(myList)):
        if myList[i] == 0:
            cunMax  = 1
            cunMin = 1
            continue
        temp = myList[i] * cunMax
        temp2 = myList[i] * cunMin

        cunMax = max(temp, temp2)
        cunMax = max(cunMax, myList[i])

        cunMin = min(temp,temp2)
        cunMin = min(cunMin, myList[i])

        sum = max(sum, cunMax)

    return sum


# A = [6, -3, -10, 0, 2]
# A = [2, 3, 4, 5, -1, 0]
A = [8, -2, -2, 0, 8, 0, -6, -8, -6, -1]
# A = [-8, 5, 3, 1, 6]
print("maximum sum of product sub array is", maximumProductSubArray(A))
