class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
        
    def peek(self):
        return self.first
    
    def enqueue(self, value):
        newNode = Node(value)
        if self.first == None:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode    

        self.length += 1
        return self
        
    def dequeue(self):
        if self.length == 0:
            return 'Empty queue'
        if self.first == self.last:
            self.first = None
            self.last = None
        
        self.first = self.first.next
        self.length -= 1
        return self
    
    def printQueue(self):
        if self.length == 0: 
            print("Empty Queue")
            return
        else:    
            first = self.first
            print("Peek: ", first.value)
            for node in range(self.length - 1):
                if first.value == None:
                    return
                else:
                    first = first.next
                    print(first.value)
                    
myQueue = Queue()

myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
myQueue.enqueue(4)

myQueue.printQueue()

print('======== After Dequeue() ============')
myQueue.dequeue()
myQueue.printQueue()

print('Peek: ', myQueue.peek().value)
