from __future__ import barry_as_FLUFL
from itertools import count
from tkinter.messagebox import NO


class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None

    #insert new node
    def insertLast(self, value):
        newnode = node(value)
        if self.start == None:
            self.start = newnode
        else:
            temp = self.start
            while temp.next!=None:
                temp = temp.next
            temp.next = newnode   

    # delete first node of list 
    def deletFirst(self):
        if self.start == None:
            print("Linked list is empty")
        else:
            self.start = self.start.next   

    # itereate from linkedlist
    def viewList(self):
        if self.start == None:
            print("List is empty")
        else:
            temp = self.start
            while temp!=None:
                print(temp.data)
                temp = temp.next

    # sort list by ascending order 
    def sortList(self):
        sortedList = []
        if self.start == None:
            print("List is empty")
        else:
            # temp = self.start
            # while temp != None:
            #     sortedList.append(temp.data)
            #     temp = temp.next
            temp = self.start
            print(temp[0])
        sortedList.sort()
        return sortedList        


myList = LinkedList()
# myList.insertLast(40)
# myList.insertLast(30)
# myList.insertLast(20)
# myList.insertLast(10)
lists = [[1,4,5],[1,3,4],[2,6]]
myList.insertLast(lists)

myList.viewList()


class Node2:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList2:
    def __init__(self):
        self.head = None
    
    def listlength(self):
        current = self.head
        length = 0

        while current != None:
            length += 1
            current = current.next
        return length    

    def InsertNewNode(self, newnode):
        if self.head == None:
            self.head = newnode
        else:
            currentNode = self.head

            while currentNode.next!= None:
                currentNode = currentNode.next

            currentNode.next = newnode

    def InsertHeadNode(self, value):
        if self.head == None:
            self.head = value
        else:
            temp = self.head
            self.head = value
            self.head.next = temp

            del temp            
    
    def InsertNodeInEnd(self, value):
        if self.head == None:
            self.head = value
        else:
            temp = self.head

            while temp.next != None:
                temp = temp.next

            temp.next = value        
    
    def InsertNodeAt(self, value, position):
        if position < 0 or position > self.listlength():
            print("Position Not Valid")
            return
        current = self.head
        count = 0
        while True:
            if count == position:
                temp.next = value
                temp.next.next = current
                break
            else:
                temp = current
                current = current.next
                count +=1

    def DeleteLastNode(self):
        temp = self.head

        while temp.next is not None:
            prev = temp
            temp = temp.next
        prev.next = None    

    def DeleteNodeAt(self, position):
        current = self.head
        count = 0

        while True:
            if count == position:
                prev.next = current.next
                current.next = None
                break
            prev = current
            current = current.next
            count += 1
    
    def ViewNodes(self):
        if self.head == None:
            print("List is empty")
        else:
            temp = self.head
            while temp!=None:
                print(temp.data)
                temp = temp.next               

nodes = Node2("Magandas")
nodes2 = Node2("Ajinath")
nodes3 = Node2("Aniket")
nodes4 = Node2("Suryawanshi")
nodes5 = Node2("Koudane")
nodes6 = Node2("Karjat")
lists = LinkedList2()
lists.InsertNewNode(nodes)
lists.InsertNewNode(nodes2)
lists.InsertNewNode(nodes3)
lists.InsertHeadNode(nodes4)
lists.InsertNodeInEnd(nodes5)
lists.InsertNodeAt(nodes6, 1)
lists.DeleteLastNode()
lists.DeleteNodeAt(2)
lists.ViewNodes()
