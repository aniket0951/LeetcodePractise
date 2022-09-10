def consecutiveNumber(myList):
    if not myList:
        return 0

    numSet = set()
    result = 0
    for i in myList:
        numSet.add(i)

    for j in numSet:
        count = 1
        if j - 1 not in numSet:
            while j + 1 in numSet:
                count += 1
                j += 1

            result = max(result, count)
    return result


A = [2, 6, 1, 9, 4, 5, 3]
print("the consecutive number is", consecutiveNumber(A))


def minimumElement(myList):
    cunMin = myList[0]
    for i in myList:
        if cunMin > i:
            cunMin = i
    return cunMin


# A = [4, 5, 1, 2, 3]
A = [10, 20, 30, 40, 50, 5, 7]
print("minimum number in array is", minimumElement(A))


def maximumSumInConfig(myList, n):
    ans = 0
    sum = 0
    pro = 0
    for i in range(len(myList)):
        sum += myList[i]
        pro += myList[i] * i
    for i in range(len(myList)):
        pro = pro + sum - n * (myList[n - 1 - i])
        ans = max(ans, pro)
    return ans


A = [8, 3, 1, 2]
n = len(A)
print("maximum sum by rotating array", maximumSumInConfig(A, n))


def pascalTriangle(n):
    arr = [[0 for x in range(n)]
           for y in range(n)]
    for i in range(0, n):

        # Every line has number of
        # integers equal to line number
        for j in range(0, i + 1):

            # First and last values
            # in every row are 1
            if j == 0 or j == i:
                arr[i][j] = 1
                print(arr[i][j], end=" ")

            # Other values are sum of values
            # just above and left of above
            else:
                arr[i][j] = (arr[i - 1][j - 1] +
                             arr[i - 1][j])
                print(arr[i][j], end=" ")
        print("\n", end="")


n = 10


# print("pascal triangle", pascalTriangle(n))


def sumOfLinkList(list1, list2):
    list1.reverse()
    list2.reverse()
    a = set()
    emptyList = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            emptyList.append(list1[i] + list2[j])
    return emptyList


l1 = [2, 4, 3]
l2 = [5, 6, 4]
print("sum of two numbers in linked list is", sumOfLinkList(l1, l2))


def minimizeHeight(myList, k, n):
    cunMin = 0
    cunMax = 0
    myList.sort()
    result = myList[n - 1] - myList[0]

    for i in range(0, n):
        if myList[i] >= k:
            cunMax = max(myList[i - 1] + k, myList[n - 1] - k)
            cunMin = min(myList[0] + k, myList[i] - k)

            f_result = min(cunMin, cunMax)
            result = min(result, f_result)

    return result


# A = [3, 9, 12, 16, 20]
# k = 3
# A = [1, 5, 8, 10]
A = [2, 6, 3, 4, 7, 2, 10, 3, 2, 1]
k = 5
n = len(A)
print("differance between minimize height is", minimizeHeight(A, k, n))

def minOperations(arr, k):
    heap = []

    for i in arr:
        heap.append(i)

    count = 0
    while len(heap) > 1 and k > heap[-1]:
        min1 = heap[-1]
        heap.pop()
        min2 = heap[-1]
        heap.append(min1 + min2)
        count += 1

    if heap[-1] >=k:
        return count
    return -1           

    # arr.sort()
    # count = 0
    # ans = arr[0]
    # for i in range(1, len(arr)):
    #     if ans < k:
    #         ans += arr[i]
    #         count += 1
    #     elif ans >= k:
    #         if arr[i] < k:
    #             count += 1
    # return count                

arr = [7, 3, 7, 1, 8, 10, 1, 5, 6]
k_ = 7
# k_ = 6 
# arr = [1, 10, 12, 9, 2, 3]
# k_ = 4
# arr = [5, 4, 6, 4]
print("min operations in array addition", minOperations(arr, k_))
temp = []
def subsetSums(arr, l, r, sum):
 
    # Print current subset
    if l > r:
        if sum != 0:
            temp.append(sum)
        print(sum, end=" ")
        return
 
    # Subset including arr[l]
    subsetSums(arr, l + 1, r, sum + arr[l])
    # Subset excluding arr[l]
    subsetSums(arr, l + 1, r, sum)

arr = [2,6,4,1]
print(subsetSums(arr,0, len(arr)-1, 0))
temp.sort()
print(temp)