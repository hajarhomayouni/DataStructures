class hashTable:
    def __init__(self, size):
        self.size=size
        self.table=[[] for i in range(size)]

    def hashFunc(self, key):
        return key%self.size

    def insert(self, key, value):
        index=self.hashFunc(key)
        self.table[index].append((key,value))

    def read(self, key):
        index=self.hashFunc(key)
        for (k, v) in self.table[index]:
            if k==key:
                return v

    def printTable(self):
        print self.table



ht=hashTable(10)
ht.insert(10 , 'Nepal')
ht.insert(25, 'USA')
ht.insert(20, 'India')
#ht.printTable()
print ht.read(10)




    
