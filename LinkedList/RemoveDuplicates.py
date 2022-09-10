from copy import copy
from re import L


class Node:
    def __init__(self, data):
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
    
    def RemoveDuplicateElement(self):
        dumm = LinkedList()
        dumm.next = self.head
        prev = dumm
        temp = self.head
        while temp != None:
            if temp.data == temp.next.data:
                while temp.next != None and temp.data== temp.next.data:
                    temp = temp.next
                prev.next = temp.next
            else:
                prev = temp.next

            temp = temp.next
        return dumm                 

    def ViewNode(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

head = [1,1,1,2,3]
lists = LinkedList()
for i in range(len(head)):
    node = Node(head[i])
    lists.InsertNode(node)

lists.ViewNode()
# lists.RemoveDuplicateElement()

a = [1,2,6,12]
b = [12,6,2,1]
print(a == b)
print(set(a) == set(b))

def f(x, l=[]):
    for i in range(x):
        l.append(i * i)
    print(l)
f(2)
f(3, [3,2,1])
f(3)   


x = ['ab', 'cd']
print(list(map(len, x)))

print(2**(3**2), (2**3)**2, (2**3)**3)

l = [1,2,3,4,5]
m = map(lambda x : 2**x, l)

print(list(m))

z = set('abc')
z.add('san')
z.update(set(['p', 'q']))
print(z)

print("Welcome to TURING".capitalize())

print([i.lower() for i in "TURING"])

sata = [1,2]
new = sata.copy()
print(new)
new = copy(sata)
print(new)
new = list(sata)
print(new)

data = [10,20,30,40,50]
data.pop()
print(data)
data.pop(2)
print(data)

import re
res = re.findall('Welcome to turing','Welcome', 1)
print(res)

class Welcome:
    def __init__(self, name) -> None:
        self.name = name

    def say_hellow(self):
        print('Welcome to ', self.name)

cw = Welcome('Turing')
cw.say_hellow()

a =[1,2,3,4]
b = [sum(a[0:x+1]) for x in range(0, len(a))]
print(b)

def func1():
    x = 50
    return x

func1()
print(x) 

def add(c,k):
    c.test = c.test + 1
    k = k+1

class Plus:
    def __init__(self):
        self.test = 0
def main():
    p = Plus()
    index = 0

    for i in range(0,25):
        add(p, index)
    print("p.test", p.test)
    print("index=", index)

data = [1,2,3]
def incr(x):
    return x+1
print(list(map(incr, data)))          

data  = ["2","3", "C"]
res = []
for i in range(len(data)):
    if data[i].isdigit():
        res.append(data[i])
    if data[i] == "C":
        res.remove(data[i-1])    
print(res)   

def Test(ops):
    while True:
        if '()' in ops:
            ops = ops.replace('()', '')
        elif '{}' in ops:
            ops = ops.replace('{}', '')
        elif '[]' in ops:
            ops = ops.replace('[]', '')
        else:
            return not ops            
print(Test('{[()]}{]{}}'))