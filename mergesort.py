def merge_sort(array):
    n = len(array)
    if (n < 2):
        return

    midpoint = int(n / 2)
    left = [0] * midpoint
    right = [0] * (n - midpoint)

    for i in range(0, midpoint):  # adding each of the elements separately
        left[i] = array[i]

    for j in range(midpoint, n):
        right[j - midpoint] = array[j]

    merge_sort(left)

    merge_sort(right)

    merge(left, right, array)


def merge(left, right, a):
    l = len(left)
    r = len(right)
    i = j = k = 0
    while (i < l and j < r):
        if left[i] >= right[j]:

            a[k] = right[j]
            j += 1
        else:
            a[k] = left[i]
            i += 1
        k += 1
    # one sublist is added to the original array and there are left overs
    # there can be leftovers only in one sublist

    while (i < l):
        a[k] = left[i]
        i += 1
        k += 1

    while (j < r):
        a[k] = right[j]
        j += 1
        k += 1

my_array = [2,7,6,8,3,2]
y = merge_sort(my_array)
for i in my_array:
    print (i,)
3-way-code.py
