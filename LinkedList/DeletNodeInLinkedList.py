from this import s


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def InsertNodes(self, val):
        if self.head == None:
            self.head = val
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = val
    
    def DeleteNode(self, val):
        current = self.head
        count = 0

        while True:
            if count == val:
                prev.next = current.next
                current.next = None
                break
            prev = current
            current = current.next
            count += 1               

    def ViewNodes(self):
        temp = self.head
        while True:
            print(temp.data)
            if temp.next == None:
                break
            temp = temp.next

# head, val = [4,5,1,9],  5 
head, val = [4,5,1,9],  1
lists = LinkedList()
for i in range(len(head)):
    node = Node(head[i])
    lists.InsertNodes(node)

lists.DeleteNode(val)
lists.ViewNodes()

