class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}
        
    def get(self, index):
        return self.data[index]
    
    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.length
    
    def pop(self):
        if self.length == 0:
            print("Array is empty")

        itemToDelete = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return itemToDelete
        
    def shiftItems(self, index):
        self.length -= 1
        for i in range(index, self.length - 1):
            self.data[index] = self.data[index + 1]
        del self.data[self.length - 1]
        self.length -= 1
    
    def delete(self, index):
        item = self.data[index]
        self.shiftItems(index)
        return item
        
    def __repr__(self):
        return f"MyArray: {{length: {self.length}, data: {self.data}}}"

newArray = MyArray()
newArray.push("you")
newArray.push("are")
newArray.push("nice")

print(newArray.get(0))  # Output: 0
print(newArray.get(1))  # Output: 1

print(newArray)

newArray.delete(1)
print(newArray)