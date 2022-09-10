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
    
    def MiddleOfLinkedList(self):
        length = 0
        temp = self.head
        while temp != None:
            temp = temp.next
            length += 1

        res = length // 2

        temp = self.head
        for i in range(res):
            temp = temp.next
        return temp        

    def ViewNode(self):
        temp = self.head
        while temp!=None:
            print(temp.data)
            temp = temp.next                            

head = [1,2,3,4,5]
lists = LinkedList()
for i in range(len(head)):
    node = Node(head[i])
    lists.InsertNode(node)

data = lists.MiddleOfLinkedList()
temp = data
while temp!=None:
    print('list after middle',temp.data)
    temp = temp.next
lists.ViewNode()    

a = '101'
dec_number= int(a, 2)
print('a jsnjjj',dec_number)