from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = dummy = ListNode(0)
        if list1 is None:
            return list2
        if list2 is None:
            return list1
             

list1 = [1,2,4]
list2 = [1,3,4]

solution = Solution()
solution.mergeTwoLists(list1, list2)


class ListNode2:
    def __init__(self, value):
        self.value = value
        self.next = None

class TwoNumberLinkedList:

    def AddTwoNumbers(self, l1, l2):
        sum = 0
        
        s = ListNode2(l1)
        print(s.value)
        s2 = ListNode2(l2)
        print(s2.value)
        while l1 and l2:
            sum += (s.value + s2.value)
            s = s.next
            s2 = s2.next
            print(sum)


twolist = TwoNumberLinkedList()
l1, l2  = [2,4,3], [5,6,4]
# twolist.AddTwoNumbers(l1, l2)            


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def InsertNode(self, value):
        if self.head == None:
            self.head = value
        else:
            current = self.head

            while current.next != None:
                current = current.next

            current.next = value  

    def RemoveDuplicateElements(self):
        current = self.head
        if current == None:
            return None
        while current.next != None:
            next_node = current.next
            if next_node.data == current.data:
                current.next = next_node.next
            else:
                current = current.next    
        

    def View(self):
        current = self.head

        while current != None:
            print(current.data)
            current = current.next    

# node = Node(1)
# node1 = Node(1)
# node2 = Node(2)
node4 = Node(1)
node5 = Node(1)
node6 = Node(2)
node7 = Node(3)
node8 = Node(3)
lists = LinkedList()
# lists.InsertNode(node)
# lists.InsertNode(node1)
# lists.InsertNode(node2)
lists.InsertNode(node4)
lists.InsertNode(node5)
lists.InsertNode(node6)
lists.InsertNode(node7)
lists.InsertNode(node8)
lists.RemoveDuplicateElements()   
lists.View()             