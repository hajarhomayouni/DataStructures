class Node:
    def __init__(self, value=None):
        self.value=value
        self.right=None
        self.left=None
        

class textEditor:
    def __init__(self, node=None):
        self.head=node
        self.cursor=node
        self.operations=[]

    def moveCursorLeft(self):
        self.cursor=self.cursor.left
        self.operations.append("moveLeft")

    def moveCursorRight(self):
        self.cursor=self.cursor.right
        self.operations.append("moveRight")

    def insertCharacter(self, char, append=True):
       
        node=Node(char)
        if append==True:
            self.operations.append("add "+char)
        if self.cursor==None:
            self.cursor=node
            self.head=node
        elif self.cursor.right==None:
            #print self.cursor.value
            self.cursor.right=node
            node.left=self.cursor
            self.cursor=node
        elif self.cursor.left==None:
            node.right=self.cursor
            self.cursor.left=node
            self.cursor=node
            self.head=node
        elif self.cursor.right!=None and self.cursor.left!=None:
            #print self.cursor.value
            #temp=self.cursor
            self.cursor.left.right=node
            node.left=self.cursor.left
            node.right=self.cursor
            self.cursor.left=node

    def backspace(self, append=True):
        value=None
        if self.cursor==None:
            value= None
        elif self.cursor.left==None and self.cursor.right==None:
            value= self.cursor.value
        elif self.cursor.right==None:
            self.cursor.left.right=None
            value=self.cursor.value
            self.cursor=self.cursor.left
        elif self.cursor.left==None:
            value=None
        else:
            temp=self.cursor.right
            self.cursor.left.right=self.cursor.right
            self.cursor.right.left=self.cursor.left
            self.cursor=temp
        if value!=None and append==True:
            self.operations.append("del "+value)

    def undo(self):
        operation=self.operations.pop()
        print operation
        if "moveLeft" in operation:
            self.cursor=self.cursor.right
        elif "moveRight" in operation:
            self.cursor=self.cursor.left
        elif "add" in operation:
            self.backspace(append=False)
        elif "del" in operation:
            self.insertCharacter(operation[-1],append=False)

    def printAll(self):
        current=self.head
        values=""
        while current!=None:
            values+= current.value
            current=current.right
        print values
        


t=textEditor()
t.insertCharacter('a')
t.printAll()

t.insertCharacter('b')
t.printAll()

t.insertCharacter('c')
t.printAll()


t.backspace()


t.printAll()

t.undo()
t.printAll()
t.undo()
t.printAll()

            

        
            
            
            

        
        
