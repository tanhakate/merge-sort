def merge_sort(array, certain_length):
    n = len(array)
    if (n < 3):
        return

    mid = int(n // 3)
    left = [0] * mid
    center = [0] * mid
    right = [0] * (n - 2 * mid)

    for i in range(0, mid):
        left[i] = array[i]

    for j in range(mid, 2 * mid):
        center[j - mid] = array[j]

    for k in range(2 * mid, n):
        right[k - 2 * mid] = array[k]

    if len(left) < certain_length:
        insertion_sort(left)
    else: merge_sort(left)

    if len(center) < certain_length:
        insertion_sort(left)
    else: merge_sort(center)

    if len(right) < certain_length:
        insertion_sort(right)
    else: merge_sort(right)

    merge(left, center, right, array)


def merge(left, center, right, a):
    l = len(left)
    c = len(center)
    r = len(right)
    i = j = k = z = 0 #z is index of the original list

    while (i < l and j < r and k < c): #After first iteration, l = 1, therefore we will no longer go into this while loop
        if left[i] <= right[j] and left[i] <= center[k]:
            a[z] = left[i]
            i += 1
        elif center[k] <= right[j] and center[k] <= left[i]:
            a[z] = center[k]
            k += 1
        else:
            a[z] = right[j]
            j += 1

        z += 1

#cases where the second and third sublists have remaining values
    while (k<c and j<r):
        if center[k]<= right[j]:
            a[z] = center[k]
            k += 1
        else:
            a[z] = right[j]
            j += 1
        z += 1

# cases where the first and third sublists have remaining values

    while(i<l and j<r):
        if left[i] <= right[j]:
            a[z] = left[i]
            i += 1
        else:
            a[z] = left[j]
            j += 1
        z += 1
    # cases where the first and second sublists have remaining values

    while (i < l and k < c):
        if left[i] <= center[k]:
            a[z] = left[i]
            i += 1
        else:
            a[z] = center[k]
            k += 1

        z += 1

    # one sublist is added to the original array and there are left overs
    # there can be leftovers only in one sublist

    while (i < l):
        a[z] = left[i]
        i += 1
        z += 1

    while (k < c):
        a[z] = center[k]
        k += 1
        z += 1

    while (j < r):
        a[z] = right[j]
        j += 1
        z += 1

def insertion_sort(array):

    for i in range (1,len(array)):

        currentvalue = array[i]
        position = i

        while position>0 and currentvalue<array[position-1]: # run the while loop as long as the element in the previous position is greater than current value
            array[position] = array[position-1] # if the previous element is greater than the element in the current position, move the previous element to the current position
            position = position - 1
        array[position] = currentvalue #inserting the current value into the position after which all elements are greater

my_array = [2,7,6,8,3,2,9,7,8,11,3,2,6,7,12,33,4,29,1]
merge_sort(my_array, 4)
print(my_array)