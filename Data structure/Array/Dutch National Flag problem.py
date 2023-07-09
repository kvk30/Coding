#In this code we explore the dutch national flag problem and python solution
def sort012(array):
    lowIndex = 0
    midIndex = 0
    highIndex = len(array) - 1
    while midIndex <= highIndex:
        if array[midIndex] == 0:
            # swap with element at index 'low' and increment both indices.
            array[lowIndex], array[midIndex] = array[midIndex], array[lowIndex]
            lowIndex += 1
            midIndex += 1
        elif array[midIndex] == 1:
            # simply move to nexßt position in sorted part of list (i.e., right side).
            midIndex += 1
        else:
            # swap with element at index 'high' and decrease highIndex.
            array[midIndex], array[highIndex] = array[highIndex], array[midIndex]
            highIndex -= 1
    return array

"""
numberElements = int(input())
elementsInArray = []
for i in range(numberElements):
    elements = int(input())
    elementsInArray.append(elements)
elementsInArray = sort012(elementsInArray)
print(elementsInArray)
""" 

elementsInArray = input().split()
elementsInArray = list(map(int, elementsInArray))
elementsInArray = sort012(elementsInArray)
print(elementsInArray)