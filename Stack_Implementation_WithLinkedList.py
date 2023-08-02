class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
    
    ## see very top Node 
    def peek(self):
        if self.isEmpty():
            return 'Empty Stack'
        return self.top
        
    ## push to top Node
    def push(self, value):
        newNode = Node(value)
        if self.isEmpty():
            self.bottom = newNode
            self.top = self.bottom
        else:
            self.top.next = newNode
            self.top = newNode
            
        self.length += 1
        return self
        
    ## remove top node
    def pop(self):
        if self.isEmpty():
            return 'Empty Stack'
        if self.top == self.bottom:
            self.bottom = None
        
        ## holdingPointer = self.top
        self.top = self.top.next
        self.length -= 1
        return self
        
    def isEmpty(self):
        if self.length == 0:
            return True
        return False
                
    def printStack(self):
        if self.isEmpty(): 
            print("Empty Stack")
            return
        else:    
            first = self.bottom
            print("Bottom: ", first.value)
            for node in range(self.length - 1):
                if first.value == None:
                    return
                else:
                    first = first.next
                    print(first.value)

myStack = Stack()

myStack.printStack()
myStack.push(5)
myStack.push(10)
myStack.push(15)
myStack.push(20)

myStack.pop()
myStack.printStack()