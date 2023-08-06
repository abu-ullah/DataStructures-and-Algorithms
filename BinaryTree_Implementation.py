class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        newNode = Node(value)
        
        if self.root is None:
            self.root = newNode
            return self
        else:
            currentNode = self.root
            while True:
                if value < currentNode.value:
                    if currentNode.left is None:
                        currentNode.left = newNode
                        return self
                    currentNode = currentNode.left
                else:
                    if currentNode.right is None:
                        currentNode.right = newNode
                        return self
                    currentNode = currentNode.right
            
    def lookup(self, value):
        if self.root is None:
            print('No root node found')
            return
        
        currentNode = self.root
        while currentNode is not None:
            if value == currentNode.value:
                return currentNode 
            elif value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
        return False
    
    def remove(self, value):
        ### If Tree is empty
        if self.root is None:
            return False
        
        ### Else
        ### We need reference of current and prev node
        currentNode = self.root
        parentNode = None
        
        while currentNode:
            if value < currentNode.value:
                parent = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            ## Match Found -> Remove Node
            elif value == currentNode.value:
                ## Check if current node has a right child
                if currentNode.right is None:
                    pass
                elif currentNode.right.left is None:
                    pass
                
                            
    
    def print_tree(self):
        def print_inorder(node):
            if node is not None:
                print_inorder(node.left)
                print(node.value, end=" ")
                print_inorder(node.right)

        print_inorder(self.root)
        print()
    
myTree = BinarySearchTree()

myTree.insert(9)
myTree.insert(4)
myTree.insert(20)
myTree.insert(15)
myTree.insert(170)
myTree.insert(1)        
myTree.insert(6)

myTree.print_tree()

print('Lookup(20): ', myTree.lookup(20).value)
print('Lookup(9): ', myTree.lookup(9).value)
print('Lookup(4): ', myTree.lookup(4).value)
print('Lookup(56): ', myTree.lookup(56))