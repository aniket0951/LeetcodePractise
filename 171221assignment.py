'''
Amol sir Assignment on 17/12/21
'''

A = [9, 4, 2, 7, 6]
stringValue = "S16ghj2jk"


def sortArrayAscendingOrder(myList):
    for i in range(0, len(myList)):
        for j in range(i + 1, len(myList)):
            if myList[i] > myList[j]:
                temp = myList[i]
                myList[i] = myList[j]
                myList[j] = temp
    return myList


def sortArrayDescendingOrder(myList):
    for i in range(0, len(myList)):
        for j in range(i + 1, len(myList)):
            if myList[i] < myList[j]:
                temp = myList[i]
                myList[i] = myList[j]
                myList[j] = temp
    return myList


def findIntegerFromList(name):
    finalNumbers = []
    for word in name.split():
        numbers = word
        for j in numbers:
            if j.isdigit():
                finalNumbers.append(int(j))

    return finalNumbers


def secondSmallestNumber(myList):
    emptyList = []
    while myList:
        minNum = myList[0]
        for i in myList:
            if i < minNum:
                minNum = i
        emptyList.append(minNum)
        myList.remove(minNum)
    secondNum = emptyList[1]
    return secondNum


print("Ascending order of list is", sortArrayAscendingOrder(A))
print("Descending order of list is", sortArrayDescendingOrder(A))
print("the integer number from string value is", findIntegerFromList(stringValue))
print("second smallest number in array is", secondSmallestNumber(A))
