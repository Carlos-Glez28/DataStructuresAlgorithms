class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def add(self, data):
        newNode = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = newNode

    def size(self):
        cur = self.head
        length = 0
        while cur.next != None:
            cur = cur.next
            length += 1
        return length

    def delete(self, idx):
        curIdx = 0
        cur = self.head
        if idx >= self.size():
            raise Exception("ERROR: 'Delete' Index out of bounds")
        while True:
            prev = cur
            cur = cur.next
            if idx == curIdx:
                prev.next = cur.next
                return
            curIdx += 1


    def get(self, idx):
        curIdx = 0
        cur = self.head
        if idx >= self.size():
            raise Exception("ERROR: 'Get' Index out of bounds")
        while True:
            cur = cur.next
            if idx == curIdx:
                return cur.data
            curIdx += 1

    def print(self):
        elements = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elements.append(cur.data)
        print(elements)


list = LinkedList()
list.add(2)
list.add(3)
list.print()
print(list.get(0))
list.print()
