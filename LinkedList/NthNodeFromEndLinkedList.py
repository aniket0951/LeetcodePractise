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
    
    def NthNodeFromEnd(self, n):
        length = 0
        temp = self.head
        while temp!=None:
            length += 1
            temp = temp.next

        res = length - n
        temp = self.head
        for i in range(res):
            temp = temp.next

        print(temp.data)        

    def ViewNode(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

a = [1,2,3,4,5,6,7,8,9]
lists = LinkedList()
for i in a:
    node = Node(i)
    lists.InsertNode(node)

lists.NthNodeFromEnd(2)
lists.ViewNode()    

a = 6 // 2
print(a)