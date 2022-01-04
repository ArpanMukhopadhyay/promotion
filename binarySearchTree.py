import queueLinked as queue

class BSTNode:
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None
    

#Insertion into a binary search tree
def insertNode (rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    
    elif nodeValue <= rootNode.data:
        if rootNode.left is None:
            rootNode.left = BSTNode (nodeValue)
        else:
            insertNode(rootNode.left, nodeValue)
    
    else:
        if rootNode.right is None:
            rootNode.right = BSTNode (nodeValue)
        else:
            insertNode (rootNode.right, nodeValue)

    return "Node has been successfully inserted"

#PreOrder Traversal (DFS)
def preOrderTraversal (rootNode):
    if not rootNode:
        return
    else:
        print (rootNode)
        preOrderTraversal(rootNode.left)
        preOrderTraversal(rootNode.right)

#In Order Traversal (DFS)
def inOrderTraversal (rootNode):
    if not rootNode:
        return
    else:
        inOrderTraversal(rootNode.left)
        print(rootNode)
        inOrderTraversal(rootNode.right)

#PostOrder Traversal (DFS)
def postOrderTraversal (rootNode):
    if not rootNode:
        return
    else:
        postOrderTraversal(rootNode.left)
        postOrderTraversal (rootNode.right)
        print(rootNode)

#Level Order Traversal (BFS)

def levelOrderTraversal (rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print (root.value.data)
            if (root.value.left is not None):
                customQueue.put(root.value.left)
            if (root.value.right is not None):
                customQueue.put(root.value.right)


def search (rootNode, value):
    if rootNode == value:
        return value
    elif value < rootNode.data:
        if rootNode.left.data == value:
            return value
        else:
            search (rootNode.left, value)
    else:
        if rootNode.right.data == value:
            return value
        else:
            search (rootNode.right, value)



newBST = BSTNode(None)
insertNode(newBST, 80)
insertNode(newBST,40)
insertNode(newBST,100)
insertNode(newBST, 20)
insertNode(newBST,50)
insertNode(newBST,60)
insertNode(newBST,90)
insertNode(newBST,10)
insertNode(newBST,30)

levelOrderTraversal(newBST)