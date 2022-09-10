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
    
    def GetDecimalVal(self):
        s = ""
        temp = self.head
        while temp!=None:
            s += str(temp.data)
            temp = temp.next

        dec_val = int(s,2)
        return dec_val    

    def ViewNode(self):
        temp = self.head
        while temp!= None:
            print(temp.data)
            temp = temp.next

# head = [1,0,1]
head = [0]
lists = LinkedList()
for i in range(len(head)):
    node = Node(head[i])
    lists.InsertNode(node)

dec = lists.GetDecimalVal()
print("decimal value of list is", dec)
lists.ViewNode()                            

print(15-11)