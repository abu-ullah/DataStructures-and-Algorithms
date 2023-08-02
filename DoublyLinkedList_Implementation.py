class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1
    
    def append(self, value):
        newNode = Node(value)
        newNode.prev = self.tail
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1
        return self
        
    def prepend(self, value):
        newHead = Node(value)
        newHead.next = self.head
        self.head.prev = newHead
        self.head = newHead
        self.length += 1
        return self
    
    def traverseToIndex(self, index):
        counter = 0
        currentNode = self.head
        while counter != index - 1:
            currentNode = currentNode.next
            counter += 1
        return currentNode
        
    def insert(self, index, value):
        if index >= self.length:
            self.append(value)
        elif index == 0:
            self.prepend(value)
        else:
            newNode = Node(value)
            currentNode = self.traverseToIndex(index)
            newNode.next = currentNode.next
            newNode.prev = currentNode
            currentNode.next.prev = newNode
            currentNode.next = newNode
        
        self.length += 1
        return self
    
    def remove(self, index):
        prevNode = self.traverseToIndex(index)
        unwantedNode = prevNode.next
        prevNode.next = unwantedNode.next
        
        self.length -= 1
        return self
    
    def print_linked_list(self):
        current = self.head
        while current is not None:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
        print('Length: ', self.length)
    
myLinkedList = DoublyLinkedList(10)

myLinkedList.append(5)
myLinkedList.append(16)
myLinkedList.append(34)
myLinkedList.prepend(1)

myLinkedList.insert(2, 99)
myLinkedList.insert(20, 88)

myLinkedList.print_linked_list()

myLinkedList.remove(2)

myLinkedList.print_linked_list()