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
    
    def SortAndMerge(self):
        ans = []
        temp = self.head
        while temp != None:
            ans.append(temp.data)
            temp = temp.next
        #1->2->3->4->5
        ans.sort()
        temp = self.head
        i = 0
        while i < len(ans):
            temp.data = ans[i]
            i += 1
            temp = temp.next


    def ViewNode(self):
        temp = self.head
        while temp!= None:
            print(temp.data)
            temp = temp.next

lists = LinkedList()
# arr = [3,5,2,4,1]
arr = [9,15,0]
for i in arr:
    node = Node(i)
    lists.InsertNode(node)

lists.SortAndMerge()
lists.ViewNode()


arr = [5,3,4,5,4,3,2,9]
res = 0
for i in arr:
    res = res ^ i
print(res)    