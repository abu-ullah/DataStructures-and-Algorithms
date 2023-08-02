class HashTable:
    def __init__(self, size=50):
        self.size = size
        self.data = [None] * size
        
    def _hash(self, key):
        hash_value = 0
        for i in range(len(key)):
            hash_value = (hash_value + ord(key[i]) * i) % self.size
        return hash_value
        
    def set(self, key, value):
        address = self._hash(key)
        if self.data[address] is None:
            self.data[address] = []
        self.data[address].append([key, value])
        print(self.data)
        
    def get(self, key):
        address = self._hash(key)
        currentBucket = self.data[address]
        print(currentBucket)
        if currentBucket:
            for pair in self.data[address]:
                if pair[0] == key:
                    return pair[1]
        print("Key not found in the Hash Table")
        
    def keys(self):
        keysArray = []
        for bucket in self.data:
            if bucket:
                keysArray.append(bucket[0][0])
        return keysArray
        
myHashTable = HashTable(50)
print(myHashTable.size)

myHashTable.set('grapes', 78)
myHashTable.set('banana', 20)
myHashTable.set('apples', 54)
myHashTable.set('grapes', 36)
myHashTable.set('oranges', 16)

print(myHashTable.get('banana'))
print(myHashTable.keys())
