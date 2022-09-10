from tempfile import tempdir


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
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
    
    def ReverseList(self):
        current = self.head
        prev = None

        while current!=None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        return prev    

    def ViewNode(self):
        temp = self.head

        while True:
            print(temp.data)
            if temp.next == None:
                break
            temp = temp.next

# head = [1,2,3,4,5]
# lists = LinkedList()

# for i in range(len(head)):
#     node = Node(head[i])
#     lists.InsertNode(node)

# lists.ReverseList()
# lists.ViewNode()


class RotateLinkedList:
    def __init__(self):
        self.head = None


    def InsertNode(self, value):
        if self.head == None:
            self.head = value
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next

            temp.next = value
 
    # def RotateList(self, k):
    #     current = self.head
    #     prev = None

    #     while current!=None:
    #         temp = current.next
    #         current.next = prev
    #         prev = current
    #         current = temp

    #     return prev  

    def RotateList(self, k):
        if self.head == None:
            return None
        
        first = self.head
        second = self.head
        leng = 0
        
        while first is not None:
            first = first.next
            leng += 1
            
        rotate = k % leng
        
        if rotate == 0:
            return self.head
        
        first = self.head
        while rotate>0:
            second = second.next
            rotate -= 1 
        while second.next is not None:
            first = first.next
            second = second.next

        start = first.next
        second.next = self.head
        first.next = None
        
        return start   

    def ViewNodes(self):
        temp = self.head

        while temp != None:
            print(temp.data)
            temp = temp.next

head = [1,2,3,4,5]
rotateList = RotateLinkedList()
for i in head:
    node = Node(i)
    rotateList.InsertNode(node)

data = rotateList.RotateList(2)
temp = data
while temp != None:
    print(temp.data)
    temp = temp.next

print(data)
# rotateList.ViewNodes()