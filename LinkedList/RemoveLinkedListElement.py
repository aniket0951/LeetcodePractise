class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):        
        self.head = None

    def InsertNodes(self, value):
        if self.head == None:
            self.head = value

        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next

            temp.next = value
    
    def RemoveEelementFromList(self, val):
        if self.head == None:
            print([])
            return
        else:
            temp = self.head
            if temp.data == val:
                temp = temp.next
            prev = LinkedList()
            while True:
                if temp.data == val:
                    prev.next = temp.next
                    temp = temp.next
                else:
                    prev = temp
                    temp = temp.next
                if temp.next == None:
                    if temp.data == val:
                        prev.next = temp.next
                        break

        return self.head

    def ViewNodes(self):
        if self.head == None:
            print("Linked List empty")
            return
        else:
            temp = self.head

            while True:
                print(temp.data)
                if temp.next == None:
                    break
                temp = temp.next

# head, val  = [1,2,6,3,4,5,6],  6  
# head, val = [],  1   
head, val = [7,7,7,7],   7
lists = LinkedList()                              
for i in range(len(head)):
    node = Node(head[i])
    lists.InsertNodes(node)

lists.RemoveEelementFromList(val)
lists.ViewNodes()