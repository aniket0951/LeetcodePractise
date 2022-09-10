def Maximumnoof1srow(arr):
    count = 0
    ans = None 

    for i in range(len(arr)):
        res = 0
        for j in arr[i]:
            if j == 1:
                res += 1
        if res > count:
            count = res
            ans = i

    return ans        


# Mat = [[0, 1, 1, 1],
#          [0 ,0 ,1 ,1],
#          [0 ,0, 1, 1]]
Mat = [[0, 1],
         [1 ,1]
            ]
print("Maximum no of 1's rows", Maximumnoof1srow(Mat))         

def RotateMatrix(arr):
    temp = []
    for i in range(len(arr)):
        temp.append([])
    
    for i in range(len(arr)):
        for j in range(len(arr)):
            temp[i].insert(0, arr[j].pop(0))
    arr.clear()
    arr = temp
    return arr    

Mat=[[1,2,3],[4,5,6],[7,8,9]]
print("Rotate matrix element clock wise", RotateMatrix(Mat))

def SpiralMatrix(matrix):
    rowbegin = 0
    rowend = len(matrix)
    columnbegin = 0
    columnend = len(matrix[0])
    res = []

    while rowend > rowbegin and columnend > columnbegin:

        for i in range(columnbegin, columnend):
            res.append(matrix[rowbegin][i])

        for j in range(rowbegin+1, rowend-1):
            res.append(matrix[j][columnend-1])

        if rowend != rowbegin+1:
            for i in range(columnend-1, columnbegin-1, -1):
                res.append(matrix[rowend-1][i])

        if columnbegin != columnend+1:
            for i in range(rowend-2, rowbegin,-1):
                res.append(matrix[i][columnbegin])

        rowbegin += 1
        rowend -= 1
        columnbegin += 1
        columnend -= 1
    return res                            

mat = [[1,2,3],[4,5,6], [7,8,9]]
print("spiral matrix", SpiralMatrix(mat))

def kthSmallest(matrix, k):
    temp = []
    for i in range(len(matrix)):
        for j in matrix[i]:
            temp.append(j)
    temp.sort()
    ans = temp[k-1]
    return ans        
    pass

# mat =[[16, 28, 60, 64],
#          [22, 41, 63, 91],
#          [27, 50, 87, 93],
#          [36, 78, 87, 94 ]]
# k = 3

mat =[[10, 20, 30, 40],
      [15, 25, 35, 45],
      [24, 29, 37, 48],
      [32, 33, 39, 50]]
k = 7
print("Kth Smallest element in array is", kthSmallest(mat, k))

def maximumPath(matrix):
    ans = 0
    for i in range(len(matrix)):
        ans += max(matrix[i])

    return ans

# Matrix = [[348, 391],
#           [618, 193]]
Matrix = [[2, 2],
          [2, 2]]
print("maximum path in matrix", maximumPath(Matrix))     

def transposeMatrix(mat):
    n = len(mat)
    for i in range(n):
        for j in range(i):
            print(mat[j])
            temp = mat[i][j]
            mat[i][j] = mat[j][i]
            mat[j][i] = temp
    return mat

# mat = [[1, 2],
#        [-9, -2]]

mat = [[1, 1, 1, 1],
           [2, 2, 2, 2],
           [3, 3, 3, 3],
           [4, 4, 4, 4]]

print("transpose the matrix", transposeMatrix(mat))

def SortMat(mat):
    n = len(mat)
    temp = [[0] for i in mat]

    ans = []
    for i in range(n):
        for j in mat[i]:
            ans.append(j)

    ans.sort()
    i = 0 
    for k in range(n):
        for m in range(n):
            if i == len(ans):
                break

            mat[k][m] = ans[i]
            i += 1
    return mat    

Mat=[[10,20,30,40],
    [15,25,35,45],
    [27,29,37,48], 
    [32,33,39,50]]
print("Sort matrix is ", SortMat(Mat))    


def TestFunc(mat):

    # for row in range(len(mat)):
    #     col = 0
    #     while col < len(mat[row]):
    #         if mat[row][col] < 0:
    #             mat[row][col] = abs(mat[row][col])
    #         else:
    #             mat[row][col] = -mat[row][col]    
    #         col += 1
       
    ## sort matrix in decending order
    top = 0
    bottom = len(mat)-1
 
    left = 0
    right = len(mat[0])-1
 
    while left < right and top < bottom:
 
        # Store the first element of next row,
        # this element will replace first element of
        # current row
        prev = mat[top+1][left]
 
        # Move elements of top row one step right
        for i in range(left, right+1):
            curr = mat[top][i]
            mat[top][i] = prev
            prev = curr
 
        top += 1
 
        # Move elements of rightmost column one step downwards
        for i in range(top, bottom+1):
            curr = mat[i][right]
            mat[i][right] = prev
            prev = curr
 
        right -= 1
 
        # Move elements of bottom row one step left
        for i in range(right, left-1, -1):
            curr = mat[bottom][i]
            mat[bottom][i] = prev
            prev = curr
 
        bottom -= 1
 
        # Move elements of leftmost column one step upwards
        for i in range(bottom, top-1, -1):
            curr = mat[i][left]
            mat[i][left] = prev
            prev = curr
 
        left += 1
 
    return mat
Mat=[[1,2,3],[4,5,6],[7,8,9]]
print("Test function run", TestFunc(Mat))
def ReverseTheMat(mat):

    for i in range(len(mat)):
        top = 0
        bottom = len(mat) -1
        while top < bottom:
            temp = mat[top][i]
            mat[top][i] = mat[bottom][i]
            mat[bottom][i] = temp

            top += 1
            bottom -= 1

    return mat

Mat=[[1,2,3],[4,5,6],[7,8,9]]
print("Reverse the matrix", ReverseTheMat(Mat))

def CheckEvenOdd(mat):
    top = 0
    even_count = 0
    odd_count = 0
    while top < len(mat):
        for i in range(len(mat)):
            if mat[top][i] % 2 ==0:
                even_count += 1
            else:
                odd_count += 1   
        top += 1 

    return f"even number in array {even_count} and odd numbers {odd_count}"       

Mat=[[1,2,3],[4,5,6],[7,8,9]]
print("Check even or odd", CheckEvenOdd(Mat))

def setZeros(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    rowindx = set()
    colindx = set()

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                rowindx.add(i)
                colindx.add(j)


    for i in range(rows):
        for j in range(cols):
            if i in rowindx or j in colindx:
                matrix[i][j] = 0     

    return matrix                


matrix = [[1,1,1],[1,0,1],[1,1,1]]
print("Set Matrix Zeroes", setZeros(matrix))

def searchMatrix(mat, target):
    flag = False
    for i in range(len(mat)):
        for j in mat[i]:
            if j == target:
                flag = True
                break

        if flag:
            return flag
    return flag    

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# target = 13
# matrix = [[1]]
# target = 1
# matrix = [[1,3]]
# target = 3
# matrix = [[1],[3]]
# target = 1
print("Search a 2D Matrix", searchMatrix(matrix, target))
from collections import defaultdict
def exist(mat, word):
    
    data = defaultdict(int)

    for i in word:
        data[i] += 1

    for i in range(len(mat)):
        for j in mat[i]:
            if j in data:
                j = "0"
                data[j] -= 1

                if data[j] == 0:
                    del data[j]

        if len(data) == 0:
            return True
    print(mat)
    return False                               

# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "ABCCED"
# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "ABCB"

board = [["a","b"],["c","d"]]
word = "abcd"
print(" Word Search", exist(board, word))

def transeformMatrix(mat):
    top = 0
    end = len(mat) - 1

    left = 0
    right = len(mat[0]) - 1
    ans = []
    while left < right and top < end:
        for i in range(top, end):
            ans.append(mat[top][i])

        for j in range(top+1, end-1):
            ans.append(mat[j][right-1])
        
        if end != top+1:
            for j in range(right-1, left-1,-1):
                ans.append(mat[end-1][i])

        if left != right+1:
            for i in range(end-2, top-1):
                ans.append(mat[i][left])        

        top += 1
        end -= 1
        left += 1
        right -= 1
    return ans            

    pass

mat = [[1,2,3],[4,5,6], [7,8,9]]
print("trance form matrix", transeformMatrix(mat))

def repeatedRows(matrix, r, c):
    
    arr = [[-123]*c] * r
    ans = []
    arr[0]= matrix[0]
    for i in range(1, len(matrix)):
        if matrix[i] in arr:
            ans.append(i)
            arr[i] = matrix[i]
        else:
            arr[i] = matrix[i]  
    return ans


# matrix = [[1, 0, 0],
#           [1, 0, 0],
#           [1, 0, 0],
#           [0, 0, 0]]
# R = 4
# C = 3
R = 2
C = 2
matrix = [[1, 0],
          [1, 0]]
print("Row are duplicates", repeatedRows(matrix, R,C))