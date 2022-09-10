from curses import noecho


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def InsertNode(self, value):
        if self.head == None:
            self.head = value
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next

            temp.next = value

    def InterationTwoLists(self, list1, list2):
        data1 = set()
        data2 = set()
        for i in range(len(list1)):
            node = Node(list1[i])
            temp = node
            while True:
                # print(temp.data)
                data1.add(temp)
                if temp.next == None:
                    break
                temp = temp.next        

        for j in range(len(list2)):
            node = Node(list2[j])
            temp = node
            while True:
                # print(temp.data)
                if temp in data1:
                    print(temp.data)
                    return 
                if temp.next == None:
                    break
                temp = temp.next      



    def ViewNodes(self):
        if self.head == None:
            print("Linked List Empty")
            return
        else:
            temp = self.head

            while True:
                print(temp.data)
                if temp.next == None:
                    break
                temp = temp.next

a = [4,1,8,4,5]
b = [5,6,1,8,4,5]
linked = LinkedList()
# for i in range(len(a)):
#     node = Node(a[i])
#     linked.InsertNode(node)
# list2 = LinkedList()
# for j in range(len(b)):
#     node = Node(b[j])
#     list2.InsertNode(node)

# linked.ViewNodes() 
linked.InterationTwoLists(a, b)