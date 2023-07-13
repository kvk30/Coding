def mergeSortedArrays(Array1, Array2):
    for indexArray2 in range(len(Array2)-1, -1, -1):
        
        lastElemeneArray1 = Array1[len(Array1)-1]
        iteratorArray1 = len(Array1)-2
        
        #Finding least element in first array and using insert sorting

        while(iteratorArray1 >= 0 and Array1[iteratorArray1] > Array1[indexArray2]):
            Array1[iteratorArray1+1] = Array1[iteratorArray1]
            iteratorArray1 -= 1

        if(lastElemeneArray1 > Array2[indexArray2]):
            Array1[iteratorArray1+1] = Array2[indexArray2]
            Array2[indexArray2] = lastElemeneArray1

Array1 = [1, 5, 9, 10, 15, 20]
Array2 = [2, 3, 8, 13]

mergeSortedArrays(Array1, Array2)
for i in Array1:
    print(i)
for i in Array2:
    print(i)

#if(Array1[])
#range has arguments -> start, stop, step.
#for i in range(4,-1):
#    print(i)