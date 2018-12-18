class MinHeap:
    def __init__(self, treeArray=[]):
        self.treeArray=treeArray

    def insertNode(self, node):
        self.treeArray.append(node)
        nodeIndex=len(self.treeArray)-1
        parentIndex=int((nodeIndex-1)/2)
        while parentIndex>=0 and nodeIndex>0 and self.treeArray[nodeIndex]<self.treeArray[parentIndex]:
            temp=self.treeArray[parentIndex]
            self.treeArray[parentIndex]=self.treeArray[nodeIndex]
            self.treeArray[nodeIndex]=temp
            nodeIndex=parentIndex
            parentIndex=int((parentIndex-1)/2)

    def delNode(self):
        if len(self.treeArray)!=0:
            removedItem=self.treeArray[0]
            self.treeArray[0] = self.treeArray[len(self.treeArray)-1]
            del self.treeArray[-1]
            nodeIndex=0
            child1Index=2*(nodeIndex+1)
            child2Index=2*(nodeIndex+1)-1
            while nodeIndex<len(self.treeArray):
                if child1Index<len(self.treeArray) and self.treeArray[child1Index]<self.treeArray[nodeIndex]:
                    temp=self.treeArray[nodeIndex]
                    self.treeArray[nodeIndex]=self.treeArray[child1Index]
                    self.treeArray[child1Index]=temp
                    nodeIndex=child1Index
                    child1Index=2*(nodeIndex+1)
                elif child2Index<len(self.treeArray) and self.treeArray[child2Index]<self.treeArray[nodeIndex]:
                    temp=self.treeArray[nodeIndex]
                    self.treeArray[nodeIndex]=self.treeArray[child2Index]
                    self.treeArray[child2Index]=temp
                    nodeIndex=child2Index
                    child2Index=2*(nodeIndex+1)-1
                else:
                    break
            return removedItem

    def printTree(self):
        print self.treeArray


#Tests
mh=MinHeap()
mh.insertNode(9)
mh.printTree()
print "ADD"
print "************"
mh.insertNode(17)
mh.printTree()
print "************"
mh.insertNode(12)
mh.printTree()
print "************"
mh.insertNode(26)
mh.printTree()
print "************"
mh.insertNode(17)
mh.printTree()
print "************"
mh.insertNode(10)
mh.printTree()

print "Delete"
print "************"
mh.delNode()
mh.printTree()

print "************"
mh.delNode()
mh.printTree()

print "************"
mh.delNode()
mh.printTree()

print "************"
mh.delNode()
mh.printTree()

print "************"
mh.delNode()
mh.printTree()

print "************"
mh.delNode()
mh.printTree()

print "************"
mh.delNode()
mh.printTree()

        
        

            
            
            
            
        

        
