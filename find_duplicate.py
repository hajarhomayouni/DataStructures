def getNextElement(element, elements):
    return elements[element-1]
    
def getNextIndext(element, elements):
    return element-1
    
# [2 3 1 4 5 3 4]
def find_duplicates(elements):
    #1. find the indext of an element in the cycle
    indext=0
    for i in range(len(elements)):
        element=getNextElement(elements[i], elements)
        indext=getNextIndext(elements[i], elements)
        
    #print (indext)
    
    #2. find the size of circle
    size=1
    startPoint=elements[indext]
    #print(getNextElement(elements[indext], elements))
    while startPoint!=getNextElement(elements[indext], elements):
        indext=getNextIndext(elements[indext], elements)
        size=size+1
        
    print(size)
    
    #3. find the first element in the circle
    pointer1=pointer2=len(elements)-1
    for i in range(size):
        pointer2=getNextIndext(elements[pointer2],elements)
        
    print (pointer1)
    print (pointer2)
    
    
    while elements[pointer1]!=elements[pointer2]:
        pointer1=getNextIndext(elements[pointer1],elements)
        print (pointer1)
        pointer2=getNextIndext(elements[pointer2],elements)
        print(pointer2)

    print (elements[pointer1])
    
find_duplicates([3,1,2,2])

        
        
    
    
        
        


