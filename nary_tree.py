class Node:
    def __init__(self, value):
        self.value=value
        self.child=[]


class naryTree:
    def __init__(self, root):
        self.root=root

    def mirrorHelper(self):
        self.mirror(self.root)

    def mirror(self, node):
        for c in node.child:
                self.mirror(c)
        node.child=reversed(node.child)
        return
            


    def BFS(self, queue):
        if len(queue)>0:
            node= queue.pop(0)
            print node.value
            for c in node.child:
                queue.append(c)
            self.BFS(queue)

    def DFS(self, stack):        
        if len(stack)>0:
            node= stack.pop()
            print node.value
            for c in node.child:
                stack.append(c)
            self.DFS(stack)



#main
root = Node(10) 
root.child.append(Node(2)) 
root.child.append(Node(34)) 
root.child.append(Node(56)) 
root.child.append(Node(100)) 
root.child[2].child.append(Node(1)) 
root.child[3].child.append(Node(7)) 
root.child[3].child.append(Node(8)) 
root.child[3].child.append(Node(9))

tree=naryTree(root)


print tree.BFS([root])
print "****************"
print tree.DFS([root])

tree.mirrorHelper()
print "************"
print tree.BFS([root])

