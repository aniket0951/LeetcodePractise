def RowWithMax(myList, m):
    ans = -1
    j = m - 1

    for i in range(len(myList)):
        while j >= 0:
            if myList[i][j] == 1:
                j -= 1
                ans = i
            else:
                break
    return ans


# A = [[0, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1],[0, 0, 0, 0]]
# m = 4
A = [[0, 0], [1, 1]]
m = 2
print("the two-D array row max is", RowWithMax(A, m))


def ArraySubsetOfAnotherArray(list1, lis2):
    list1.sort()
    lis2.sort()
    is_sunSet = False
    for i in range(len(lis2)):
        if lis2[i] in list1:
            is_sunSet = True
        if lis2[i] not in list1:
            return "No"
    if is_sunSet:
        return "Yes"


# list1 = [11, 1, 13, 21, 3, 7]
# list2 = [11, 3, 7, 1]
# list1 = [10, 5, 2, 23, 19]
# list2 = [19, 5, 3]
list1 = [1, 2, 3, 4, 8, 9, 5, 27, 92, 69, 11, 12]
list2 = [63, 11, 12, 1, 2, 3]
print("array subset of another array is",
      ArraySubsetOfAnotherArray(list1, list2))


def MajorityElement(myList):
    cunMajor = myList[0]
    count = 0
    maxEle = 0
    for i in range(len(myList)):
        if myList[i] == cunMajor:
            count += 1
            maxEle = myList[i]
        if myList[i] != cunMajor:
            cunMajor = myList[i]
            count = 0

    return maxEle


# A = [1, 2, 3]
A = [3, 1, 3, 3, 2]
print("the majority element is", MajorityElement(A))


def RotateArrayInClockWise(arr):
    left = arr[len(arr) - 1]
    n = len(arr)
    for i in range(n-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = left
    return arr


arr = [1, 2, 3, 4, 5]
print("Array rotation is", RotateArrayInClockWise(arr))


def CountPairOfMaxSum(arr, k):
    n = len(arr)
    unordered_map = {}
    count = 0
    for i in range(n):
        b = k - arr[i]
        if b in unordered_map:
            count += unordered_map[b]
        if arr[i] in unordered_map:
            unordered_map[arr[i]] += 1
        else:
            unordered_map[arr[i]] = 1

    return count


# arr = [1, 1, 1, 1]
# k = 2
arr = [1, 5, 7, 1]
k = 6
print("Count pair of sum is", CountPairOfMaxSum(arr, k))


def FirstRepeatingElement(arr):
    n = len(arr)
    max = 0
    for x in range(n):
        if (arr[x] > max):
            max = arr[x]

    temp = [0 for i in range(max + 1)]  # the idea is to use
    # temporary array as hashmap
    # Arrays.fill(temp, 0)

    for x in range(n):
        num = arr[x]
        temp[num] += 1

    for x in range(n):
        num = arr[x]
        if (temp[num] > 1):
            return x

    return -1


# arr = [1, 5, 3, 4, 3, 5, 6]
arr = [7, 4, 0, 9, 4, 8, 8, 2, 4, 5, 5, 1]
print("First repeating element is", FirstRepeatingElement(arr))


def FirstNonRepeatingElement(arr):
    data = dict()

    for i in range(len(arr)):
        if arr[i] in data:
            data[arr[i]] += 1
        else:
            data[arr[i]] = 1

    for k, v in data.items():
        if v == 1:
            return k

    return 0


# arr = [-1, 2, -1, 3, 2]
arr = [-1, -17, -12, 8, 16, -17, -13, -14, -3, -
    6, -5, -11, -10, -12, -5, 19, -17, -5, -1, 12]
print("first non repeating element is", FirstNonRepeatingElement(arr))


def CheckIfTwoStringsAreKanagramsOrNot(str1, str2, k):

    if len(str1) != len(str2):
        return 0
    data = dict()

    for i in str1:
        if i in data:
            data[i] += 1
        else: data[i] = 1

    for j in str2:
        if j in data and data[j] > 0:
            data[j] -= 1

    count = 0

    for m in data.values():
        count += m

    if count <= k:
        return 1
    else: return 0


# str1, str2 = "fodr", "gork"
# k = 2
str1, str2 = "ukdbgygrsjlaukwsgc", "memdwhetaewfahkc"
k = 14
print("Check if two strings are k-anagrams or not",
      CheckIfTwoStringsAreKanagramsOrNot(str1, str2, k))


def ProductArrayPuzzle(arr):

    emptylist = []
    for i in range(len(arr)):
        new_arr = arr
        ans = 1
        for j in range(len(new_arr)):
            if arr[i] != new_arr[j]:
                ans = ans * new_arr[j]

        emptylist.append(ans)
    return emptylist


# arr = [10, 3, 5, 6, 2]
arr = [7, 8, 6, 4, 6, 7, 3, 10, 2, 3, 8, 1, 10, 4, 7, 1,
    7, 3, 7, 2, 9, 8, 10, 3, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1]
print("Product array puzzle is", ProductArrayPuzzle(arr))


def KadanesAlgorithm(arr):
        a = arr    
        max_so_far =a[0]
        curr_max = a[0]
        
        for i in range(1,len(a)):
            curr_max = max(a[i], curr_max + a[i])
            max_so_far = max(max_so_far,curr_max)
            
        return max_so_far                      

# arr = [1,2,3,-2,5]
# arr = [-1,-2,-3,-4]
# arr = [-4, -5, -5, -3]
arr = [-83, -66, 100, -77, 79, -98, -60, -47, 70, -6, -22, 98, -17, -100, -1, -99, 62, -91, -54, -90, -96, 67, 37, -60, -61]
print("Kadanes Algorithm is", KadanesAlgorithm(arr))

def MaximumProductSubarray(arr):
    maxele = arr[0]
    minele = arr[0]
    result = arr[0]

    for i in range(1, len(arr)):
        if arr[i] == 0:
            minele = 1
            maxele = 1
        else:
            temp = maxele * arr[i]
            temp2 = minele * arr[i]

            maxele = max(temp, temp2)
            maxele = max(maxele, arr[i])

            minele = min(temp, temp2)
            minele = min(minele, arr[i])

            result = max(result, maxele)

    return result        


# arr = [6, -3, -10, 0, 2]
arr = [2, 3, 4, 5, -1, 0]
print("Maximum product subarray is", MaximumProductSubarray(arr))

def SubarrayWithSum(arr, sum):
    cur_sum = arr[0]
    start = 0
    j = 1

    while True:
        cur_sum = cur_sum + arr[j]
        if cur_sum == sum:
            return start+1, j+1
        elif cur_sum < sum:
            j += 1
        elif cur_sum > sum:
            start += 1
            cur_sum = arr[start]
            j = start + 1
    return -1                

# S = 12
# A = [1,2,3,7,5]
S = 15
A = [1,2,3,4,5,6,7,8,9,10]
print("Subarray with sum is", SubarrayWithSum(A, S))

def PairOfSum(arr1, arr2, x):
    b_set = set()
    ans = []

    for num in arr2:
        b_set.add(num)
    
    arr1.sort()

    for j in arr1:
        if x - j in b_set:
            ans.append([j, x-j])
    return ans        
        

A = [1, 2, 4, 5, 7]
B = [5, 6, 3, 4, 8] 
X = 9 
# A = [-1, -2, 4, -6, 5, 7]
# B = [6, 3, 4, 0] 
# X = 8 
print("Pair of all sum pairs", PairOfSum(A, B, X)) 

def SwappingPairSum(arr1, arr2):
    a = arr1
    b = arr2
    asum = sum(a)
    bsum= sum(b)
    for x in set(a):
           for y in set(b):
               newsuma= asum - x + y
               newsumb = bsum -y + x
               if newsuma==newsumb:
                print(x,y, newsuma, newsumb)
                return 1 
               
    return -1
A = [4, 1, 2, 1, 1, 2]
B = [3, 6, 3, 3]
# A = [5, 7, 4, 6]
# B = [1, 2, 3, 8]
# A = [10, 10, 10, 10]
# B = [5, 5, 5, 5]
# A = [874, 332, 825, 430, 330, 168]
# B = [1206, 1255, 498]
print("Swapping pair make sum equal", SwappingPairSum(A, B))

def CountConversion(arr):
    i = 0
    j = 1
    ans = 0
    while i < len(arr):
        if j == len(arr):
            i += 1
            j = i+1

        elif arr[i] > arr[j]:
            ans += 1
            j += 1
        else:
            j += 1
    return ans    

# arr = [2, 4, 1, 3, 5]
# arr = [2, 3, 4, 5, 6]
arr = [10, 10, 10]
print("Count conversion of array is", CountConversion(arr))

def IsSubSet(arr1, arr2):
    a_set = set(arr1)
    b_set = set(arr2)

    for i in b_set:
        if i not in a_set:
            return "NO"

    return "YES"  

# a1 = [11, 1, 13, 21, 3, 7]
# a2 = [11, 3, 7, 1]
# a1 = [10, 5, 2, 23, 19]
# a2 = [19, 5, 3]
a1 = [1, 2, 3, 4, 5, 6]
a2 = [1, 2, 4]
print("Is a1 is subset of a2", IsSubSet(a1, a2))

def StockAndBuy(arr):
    buy = arr[0]
    ans = 0
    for i in range(1, len(arr)):
        res = arr[i] - buy
        if res < 0:
            buy = arr[i]
        if res > 0:
            ans = max(ans, res)
    if ans > 0:
        return 1
    return 0            

arr = [100,180,260,310,40,535,695]
# arr = [4,2,2,2,4]
print("Stock buy and sell", StockAndBuy(arr))
import collections
def MaximumOfAllSubarraysOfSizek(arr, k):
    p=[]
    n = len(arr)
    q=collections.deque(arr[0:k])
    print(q)
    p.append(max(q))
    for i in range(k-1,n-1):
        q.popleft()
        q.append(arr[i+1])
        p.append(max(q))
    return p           

# arr = [1 ,2 ,3 ,1 ,4 ,5 ,2 ,3, 6]
# k = 3
arr = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
k = 4
print("Maximum of all subarrays of size k is", MaximumOfAllSubarraysOfSizek(arr, k))

def ZeroSumSubArray(arr):
    n = len(arr)
    hashMap = {}
    out = []
    
    sum1 = 0
    for i in range(n):
        sum1 += arr[i]

        if sum1 == 0:
            out.append((0, i))
        al = []
        
        if sum1 in hashMap:
            al = hashMap.get(sum1)
            for it in range(len(al)):
                out.append((al[it] + 1, i))
        al.append(i)
        hashMap[sum1] = al
    return len(out)

# arr = [0,0,5,5,0,0]
arr = [6,-1,-3,4,-2,2,4,6,-12,-7]
print("Zero sum sub-array is", ZeroSumSubArray(arr))

def LargestNumberformedfromanArray(arr):
    i = 0
    j = 1

    while i < len(arr):
        if j == len(arr):
            i += 1
            j = i+1
            continue
        else:
            ij_el = (str(arr[i]), str(arr[j]))
            ji_el = (str(arr[j]), str(arr[i]))
            first_ele = "".join(ij_el)
            sec_el = "".join(ji_el)

            if sec_el > first_ele:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

            j += 1    
    ans = "".join(str(i) for i in arr)
    return ans
    

arr = [3, 30, 34, 5, 9]
print("Largest number formed for an array", LargestNumberformedfromanArray(arr))

def MaximumSumofArrofI(arr):
    arr.sort()
    ans = 0
    for i in range(len(arr)):
        res = arr[i] * i
        ans += res
    
    return ans
    pass

arr = [5, 3, 2, 4, 1]
print("Maximum sum of arr[i]* i is ", MaximumSumofArrofI(arr))

def ArrangeTheArray(arr):
    neg = []
    pos = []

    for i in arr:
        if i < 0:
            neg.append(i)
        else:
            pos.append(i)

    i = 0
    while i < len(neg):
        arr[i] = neg[i]
        i += 1
    j = 0
    while j < len(pos):
        arr[i] = pos[j]
        j += 1
        i += 1
    return arr        

arr = [-3, 3, -2, 2]
print("Arrange the array", ArrangeTheArray(arr))

def SticklerThif(arr):
    n = len(arr)

    if n <=1:
        return arr[0]    

    dp = [i  for i in arr]

    dp[0] = arr[0]
    dp[1] = max(arr[1], arr[0])

    for i in range(2, n):
        dp[i] = max(arr[i] + dp[i-2], dp[i-1])

    return dp[n-1]

# arr = [5,5,10,100,10,5]
arr = [1,2,3]
print("stickler thif is", SticklerThif(arr))


def SmallestSubArraySumgreaterX(arr, x):
    a = arr
    c=1000000000
    left=0
    sum1=0
    n=len(a)
    for i in range(n):
        sum1+=a[i]
           
        while sum1>x:
            c=min(c,i-left+1)
            sum1-=a[left]
            left+=1
    return c


# A = [1, 4, 45, 6, 0, 19]
# xsum  =  51
A = [1, 3, 4, 7, 10, 10, 8, 10]
xsum = 10
print("Smallest subarray with sum greater than x ", SmallestSubArraySumgreaterX(A, xsum))


def FirestNegativeInEveryWindow(arr, k):
    a = [arr[x:x+k] for x in range(0,len(arr))]
    temp = []

    for i in a:
        flag=  False
        if len(i) == k:
            for j in i:
                if j < 0:
                    flag = True
                    temp.append(j)
                    break
            if not flag:
                temp.append(0)  

    return temp          

# arr = [-8, 2, 3, -6, 10]
# k_in = 2
arr = [12, -1, -7, 8, -15, 30, 16, 28]
k_in = 3
print("First negative integer in every window of size k ", FirestNegativeInEveryWindow(arr, k_in))

def LargestSubarraywith0sum(arr):
    ans = 0
    temp = []
    for i in arr:
        res = ans + i
        if res <=0:
            ans = res
            temp.append(i)
        else:
            continue
    return len(temp)
    

arr = [15,-2,2,-8,1,7,10,23]
print("Largest subarray with 0 sum", LargestSubarraywith0sum(arr))