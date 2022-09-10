from re import I, L


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self) -> None:
        self.head = None

    def InsertNode(self, val):
        if self.head == None:
            self.head = val
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = val
    
    def CheckListPalindrom(self):
        
        current = self.head
        rever = self.ReverseList()
        while current != None:
            if current.data != rever.data:
                return 0
            current = current.next
            rever = rever.next    
        return 1

    def ReverseList(self):
        current = self.head
        prev = None
        while current != None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev    
    
    def AddTwoDecimalNumberSumWithLinkedList(self, first, sec):
        data = self.get_sum_two(first, sec)  
        print(data)     
    
    @staticmethod
    def get_sum_two(first, sec):
        a = sum(first) + sum(sec)
        b = sum(sec)
        print("ans",b+a)
        return a
    def ViewNode(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

# arr = [1,2,1]
arr = [1,2,3,4]
linked = LinkedList()
for i in arr:
    node = Node(i)
    linked.InsertNode(node)

data = linked.CheckListPalindrom()
first = [4,5]
sec = [3,4,5]
addition = linked.AddTwoDecimalNumberSumWithLinkedList(first, sec)
print(addition)
print(data)


# sort list by 0s,1s,2s
class SegregateList:
    def __init__(self):
        self.head = None

    def InsertNode(self, val):
        if self.head == None:
            self.head = val
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = val
    
    def segregate(self):
        l = list()
        temp = self.head

        while temp!= None:
            l.append(temp.data)
            temp = temp.next

        l.sort()
        temp = self.head
        i = 0

        while temp!= None and i <= len(l):
            temp.data = l[i]
            temp = temp.next
            i += 1

        return self.head    

    def ViewNode(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

# arr = [1,2,2,1,2,0,2,2]
# seg = SegregateList()
# for i in arr:
#     node = Node(i)
#     seg.InsertNode(node)

# data = seg.segregate()
# temp = data
# while temp != None:
#     print(temp.data)
#     temp = temp.next
    
# seg.ViewNode()

class DelNode:
    def __init__(self) -> None:
        self.head = None


    def InsertNode(self, val):
        if self.head == None:
            self.head = val
        else:
            temp = self.head
            while temp.next!=None:
                temp = temp.next
            temp.next = val            
    
    def delnodes(self, x):
        count = 0
        res = x -1
        
        temp = self.head
        while temp != None:
            count += 1
            if count == res:
                temp.next = temp.next.next
            else:
                temp = temp.next

        return self.head            
    
    def SortedDLL(self, x):
        if self.head == None:
            node = Node(x)
            return node
        else:
            temp = self.head
            while temp != None:
                if temp.next.data > x:
                    node = Node(x)
                    next = temp.next
                    temp.next = node
                    # node.next = next
                temp = temp.next
            return temp           

    def ViewNode(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

# arr = [1,5,2,9]
# arr = [1,3,4]
arr = [3,5,8,10,12]
x = 9
dlelist = DelNode()
for i in arr:
    node = Node(i)
    dlelist.InsertNode(node)

# data = dlelist.delnodes(3)
# temp = data
# while temp != None:
#     print(temp.data)
#     temp = temp.next


# dlelist.ViewNode()

class MergeLists:
    def __init__(self):
        self.head = None  

    def InsertNode(self,val):
        if self.head == None:
            self.head = val
        else:
            temp = self.head
            while temp.next != None:
                  temp = temp.next
            temp.next  = val        
    
    def MergeSortedList(self):
        data = self.head
        print("data",data)
        return data

    def ViewNode(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

arr = [[1,2,3],[4 ,5],[5, 6],[7,8]]
mergelist = MergeLists()
for i in arr:
    node = Node(i)
    mergelist.InsertNode(node)

data = mergelist.MergeSortedList()
# temp = data
# while temp != None:
#     print(temp.data)
#     temp = temp.next
# mergelist.ViewNode()

class SortedDLL:
    def __init__(self) -> None:
        self.head = None

    def InsertNode(self, val):
        if self.head == None:
            self.head = val
        else:
            temp = self.head
            while temp.next!=None:
                temp = temp.next
            temp.next = val  

    def InsertIntoDLL(self, x):
        node = Node(x)

        temp = self.head
        prev = None
        current = None
        while temp!= None:
            current = prev.next
            if temp.data > x and prev.data < x:
                prev.next = node
                temp = current
            temp = temp.next

        return self.head        
    
    def slowfast(self):
        slow = 0
        fast = 0
        temp = self.head
        print(temp[0].data)
        # while True:
        #     if slow == fast:

    def RemoveDuplicates(self):
        arr = []
        temp = self.head
        
        while temp != None:
            if temp.data not in arr:
                arr.append(temp.data)
            temp = temp.next

        i = 0
        self.head = None
        for i in range(len(arr)):
            x = Node(arr[i])
            self.InsertNode(x)

        return self.head           

    def Viewnode(self):
        temp = self.head
        while temp!= None:
            print(temp.data)
            temp = temp.next

arr = [2,2,2,2,2]
sortedddl = SortedDLL()
for i in arr:
    node = Node(i)
    sortedddl.InsertNode(node)


data = sortedddl.RemoveDuplicates()
# temp = data
# while temp!= None:
#     print(temp.data)
#     temp = temp.next
# data = sortedddl.InsertIntoDLL(9)
# sortedddl.slowfast()
# sortedddl.Viewnode()

class RemoveDuplicateLinked:
    def __init__(self) -> None:
        self.head = None

    def InsertNode(self, val):
        if self.head == None:
            self.head = val
        else:
            temp = self.head
            while temp.next!=None:
                temp = temp.next
            temp.next = val  
    
    def Removeduplicates(self):
        temp = self.head
        while temp.next!=None:
            next_node = temp.next
            if temp.data == next_node.data:
                temp.next = next_node.next
            else:
               temp = temp.next
        return self.head            

    def Viewnode(self):
        temp = self.head
        while temp!= None:
            print(temp.data)
            temp = temp.next        

# arr = [2,2,4,5] 
arr = [2,2,2,2,2] 
lists = RemoveDuplicateLinked()
for i in arr:
    node = Node(i)
    lists.InsertNode(node)

lists.Removeduplicates()
lists.Viewnode()
from collections import defaultdict, Counter

s = "hqghumeaylnlfdxfircvscxggbwkfnqduxwfnfozvs"
data = defaultdict(int)
  
arr = [[0,0]] * len(s)
for i in range(len(s)):
    if s[i] in arr[i][0]:
        print("element repetead")
    else:
        arr[i].append([s[i], 1])    

print(arr)

# print(a)