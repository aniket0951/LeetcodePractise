from types import new_class


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def InsertNode(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            # new_node.prev = None
        else:
            new_node = Node(data)
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
            new_node.next = None
    
    def SortedDll(self, data):
        new_node = Node(data)
 
        if self.head is None:
            self.head = new_node
        
        elif self.head.data >= new_node.data:
            new_node.next = self.head
            new_node.next.prev = new_node
            self.head = new_node
        else:
            current = self.head
 
            while ((current.next is not None) and
                   (current.next.data < new_node.data)):
                current = current.next
            new_node.next = current.next
 
            if current.next is not None:
                new_node.next.prev = new_node
 
            current.next = new_node
            new_node.prev = current 

        return self.head        

    def ViewNode(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next        

linked = LinkedList()
linked.InsertNode(1)
linked.InsertNode(2)
linked.InsertNode(3)
linked.InsertNode(4)
linked.InsertNode(6)

data = linked.SortedDll(5)
temp = data
while temp:
    print(temp.data)
    temp = temp.next
# linked.ViewNode()