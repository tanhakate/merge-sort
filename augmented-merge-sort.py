import math

def merge_sort(array, certain_length):
    n = len(array) #calculate the length of the array

    if len(array) < certain_length: #if the length of the array is below the specified length, use insertion sort to sort the array
        insertion_sort(array)
        return

    if (n < 2):
        return #if the length of the array is less than two, skip the recursion

    if(n==2): #if the length of the subarray is equal to 2, switch places if the elements are out of order
        if array[0]<array[1]:
            return
        else:
            temp = array[0] #if the second element is smaller than the first element, use a temporary variable to store the value of the first element, insert the second element onto the first position and then insert the first element onto the second position
            array[0] = array[1]
            array[1] = temp
            return

    mid = math.ceil(n /3) # find the length of the array which is 1/3rd of the total array
    left = [0] * mid #create three empty arrays of size mid 
    center = [0] * mid
    right = [0] * (n - 2 * mid) #the third array contains all the remaining elements from index position 2*mid onwards, in case the total length of our array is not a multiple of three 

    for i in range(0, mid): 
        left[i] = array[i] #pass indices from the main list into the left sublist from the first index up till the 1/3 index

    for j in range(mid, 2 * mid):
        center[j - mid] = array[j] #pass indices from the main list into the right sublist from the 1/3 index up till the 2/3 index 

    for k in range(2 * mid, n):
        right[k - 2 * mid] = array[k] #pass indices from the main list into the center sublist from the 2/3 index to the end of the list

    if len(left) < certain_length: #check if either of the subarrays are below the previously specified length, in which case invoke insertion sortion
        insertion_sort(left)
    else: merge_sort(left,certain_length) #otherwise, recursively call merge_sort on the subarrays

    if len(center) < certain_length:
        insertion_sort(center)
    else: merge_sort(center,certain_length)

    if len(right) < certain_length:
        insertion_sort(right)
    else: merge_sort(right,certain_length)

    merge(left, center, right, array) #pass the subarrays into the merge function once we have recursively divided the main arrays in smaller and smaller sublists. 
    #The merge method will return an array with all the sublists sorted. As we traverse up throough the sublists, this will continue for larger and larger subarrays until we have merged the sorted main array. 


def merge(left, center, right, a):
    l = len(left) #calculate length of left subarray
    c = len(center) #calculate length of center subarray
    r = len(right) #calcualte length of right subarray
    i = j = k = z = 0 #z is index of the original array a, whereas i,k & j are the indices of left, center and right subarrays respectively

    while (i < l and j < r and k < c): #while the indices of all the subarrays are less than the length of the subarrays, we compare the element i of each subarray with the jth and kth element of the center and right subarrays. 
        #Note that after the first iteration on the base condition (n=3), the length of one of the subarrays will be equal to the value of the index. We have fully traversed one of the subarrays, therefore we will no longer go into this while loop.
        if left[i] <= right[j] and left[i] <= center[k]: #If the left array has the minimum value, we add it to the array a.
            a[z] = left[i]
            i += 1 #increase the index value of the left array i.e. compare the i+1 element in the subarry with the jth and kth elements of the other arrays.
        elif center[k] <= right[j] and center[k] <= left[i]: #Otherwise if the center array has the minimum value, we add it to the array a
            a[z] = center[k]
            k += 1 #increase the index value of the center array i.e. compare the k+1 element in the subarry with the ith and jth elements of the other arrays.
        else:
            a[z] = right[j] #If the right array has the minimum value, we add it to the array a.
            j += 1 #increase the index value of the right array i.e. compare the j+1 element in the subarry with the ith and kth elements of the other arrays.

        z += 1 #After an iteration in the while loop, we have added an element to array a. Therefore, we will increase the index by one since now we have to fill in the next sorted element. 

#The following while loops concern cases where the second and third subarry have remaining values
    while (k<c and j<r): 
        if center[k]<= right[j]:
            a[z] = center[k] #If the center array has the minimum value, add it to the array a and increase the value of its index.
            k += 1
        else:
            a[z] = right[j] #If the right array has the minimum value, add it to the array a and increase the value of its index.
            j += 1
            
        z += 1 #After an iteration in the while loop, we have added an element to array a. Therefore, we will increase the index by one since now we have to fill in the next sorted element. 


#The following while loops concern cases where the left and right subarry have remaining values
    while(i<l and j<r):
        if left[i] <= right[j]:
            a[z] = left[i] #If the left array has the minimum value, add it to the array a and increase the value of its index
            i += 1
        else:
            a[z] = right[j] #If the right array has the minimum value, add it to the array a and increase the value of its index
            j += 1
            
        z += 1 #After an iteration in the while loop, we have added an element to array a. Therefore, we will increase the index by one since now we have to fill in the next sorted element. 
        
#The following while loops concern cases where the left and center subarry have remaining values
    while (i < l and k < c):
        if left[i] <= center[k]:
            a[z] = left[i] #If the left array has the minimum value, add it to the array a and increase the value of its index
            i += 1
        else:
            a[z] = center[k] #If the center array has the minimum value, add it to the array a and increase the value of its index
            k += 1

        z += 1 #After an iteration in the while loop, we have added an element to array a. Therefore, we will increase the index by one since now we have to fill in the next sorted element. 

#The following while loops concern cases where only a single subarray has remaining values i.e. there are leftovers in one subarray. Note that the leftovers are already sorted since the merge operation begins from the base case. 

    while (i < l):
        a[z] = left[i] #If left array has remaining values, iteratively add the leftovers elements from the left array. 
        i += 1
        z += 1 #After adding a new element onto the main array a, increase the index number. 

    while (k < c):
        a[z] = center[k] #If center array has remaining values, iteratively add the leftovers elements from the left array.
        k += 1
        z += 1 #After adding a new element onto the main array a, increase the index number. 


    while (j < r):
        a[z] = right[j] #If right array has remaining values, iteratively add the leftovers elements from the left array.
        j += 1
        z += 1 #After adding a new element onto the main array a, increase the index number. 
        
def insertion_sort(array):

    for i in range (1,len(array)):

        currentvalue = array[i]
        
        position = i

        while position>0 and currentvalue<array[position-1]: # run the while loop as long as the element in the previous position is greater than current value
            array[position] = array[position-1] # if the previous element is greater than the element in the current position, move the previous element to the current position
            position = position - 1
            
        array[position] = currentvalue #inserting the current value into the position after which all elements are greater
        
        
import random
my_array = random.sample(range(100), 10) #generate a random list with 10 elements under range 100
print(my_array)
merge_sort(my_array, 4) #merge_sort the list, applying insertion sort when the length of the subarry is less than 4
print(my_array)

