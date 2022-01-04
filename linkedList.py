
class Node:
    def __init__ (self, value = None):
        self.value = value
        self.next = None
    

class linkedList:

    #Constructor initialising head and tail
    def __init__ (self):
        self.head = None
        self.tail = None
    
    #Making linkedList printable (sourced online)
    def __iter__ (self):
        node = self.head
        while node:
            yield node
            node = node.next
    

    def insert (self, value, location):
        newNode = Node(value)
        #No linked list then when we insert, newNode is both the head and tail
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        #Based on if linked list exists
        else:
            #Insertion at start of linked list
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            #Insertion at end of linked list
            elif location == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            #Insertion at given location (middle)
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next 
                tempNode.next = newNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail = newNode
    
        
    #Traversing a linked list
    def traversal (self):
        if self.head is None:
            print("No present linked list to traverse") 
        else:
            node = self.head
            while node is not None:
                print (node.value)
                node = node.next


    #Find a node 
    def find (self, value):
        if self.head is None:
            return "No present linked list to traverse"
        else:
            node = self.head
            while node is not None:
                if node.value == value:
                    return node.value
                node = node.next
            
            return "Value does not exist in linked list"
    
    #Deletion of elements in linked list
     #  Delete a node from Singly Linked List
    def deleteNode(self, location):
        if self.head is None:
            print("The SLL does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    def deleteAll (self):
        if self.head is None:
            return 'No linked list to delete'
        else:
            self.head = None
            self.tail = None


singlyLinkedList = linkedList()

print ([node.value for node in singlyLinkedList])

singlyLinkedList.insert(1,0)
singlyLinkedList.insert(2,1)
singlyLinkedList.insert(3,2)
singlyLinkedList.insert(4,3)
singlyLinkedList.insert(5,4)

print ([node.value for node in singlyLinkedList])

singlyLinkedList.deleteNode(-1)

print ([node.value for node in singlyLinkedList])

