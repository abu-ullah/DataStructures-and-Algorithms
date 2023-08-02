class Stack:
    def __init__(self):
        self.stack = []
        
    def peek(self):
        if len(self.stack) == 0:
            return 'Empty Stack'
        return self.stack[len(self.stack) - 1]
        
    def push(self, value):
        self.stack.append(value)
        return self
    
    def pop(self):
        #del self.stack[len(self.stack) - 1]
        self.stack.pop()
        return self
    
    ## remove top node
    def printStack(self):
        if len(self.stack) == 0:
            print('Stack is empty')
        for i in range(len(self.stack)):
            print(self.stack[i])
    
myStack = Stack()

myStack.push(5)
myStack.push(10)
myStack.push(15)

myStack.printStack()
print('Peek: ', myStack.peek())

print("============ After pop() ====================")
myStack.pop()
myStack.printStack()
print('Peek: ', myStack.peek())