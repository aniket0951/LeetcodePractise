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
    
    def DetectLoopInList(self):
        slow = self.head
        fast = self.head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False        

    def ViewNode(self):
        temp = self.head

        while temp!=None:
            print(temp.data)
            temp = temp.next

head = [1,3,4]
lists = LinkedList()
for i in head:
    node = Node(i)
    lists.InsertNode(node)

data = lists.DetectLoopInList()
print(data)
lists.ViewNode()    