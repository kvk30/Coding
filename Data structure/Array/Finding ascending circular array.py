#Function finds circular array
def findingCircularArray(Array):
    
    countException = 0
    
    #Circular function is only once exception
    for i in range(1,len(Array)):
        if Array[i-1] > Array[i]:
            countException += 1
    
    if countException == 1:
        return True
    else:
        return False

elementsInarray = input().split()
elementsInarray = list(map(int, elementsInarray))
checking = findingCircularArray(elementsInarray)
if(checking == True):
    print("Array is ascending circularly sorted")
else:
    print("Array not found to be a ascending circular sorted one.")
