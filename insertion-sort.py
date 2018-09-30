def insertion_sort(array):
    for i in range (1,len(array)):

        currentvalue = array[i]
        position = i

        while position>0 and currentvalue<array[position-1]:

            array[position] = array[position-1]
            position = position - 1

        array[position] = currentvalue

myArray = [54,26,93,17,77,31,44,55,20]
insertion_sort(myArray)
print(myArray)

