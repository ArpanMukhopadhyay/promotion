class Node:
    def __init__ (self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

class Queue:
    def __init__ (self):
        self.linkedList = LinkedList()
    
    def enqueue (self, value):
        newNode = Node(value)
        if self.linkedList.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.linkedList.tail.next = newNode
            self.linkedList.tail = None

    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False
    
    def dequeue (self, value):
        if self.isEmpty():
            return
        else:
            tempNode = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.head = None
                self.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next

            return tempNode    
            
    def peek(self):
        if self.isEmpty():
            return "There is not any node in the Queue"
        else:
            return self.linkedList.head

    def delete (self):
        self.linkedList.head = None
        self.linkedList.tail = None