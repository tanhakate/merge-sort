def merge_sort(array):
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

    merge_sort(left)
    merge_sort(center)
    merge_sort(right)

    merge(left, center, right, array)


def merge(left, center, right, a):
    l = len(left)
    c = len(center)
    r = len(right)
    i = j = k = l = 0

    while (i < l and j < r and k < c):
        if left[i] <= right[j] and left[i] <= center[k]:
            a[l] = left[i]
            i += 1
        elif center[k] <= right[j] and center[k] <= left[i]:
            a[l] = center[k]
            k += 1
        else:
            a[l] = right[j]
            j += 1
        print(a[l])
        l += 1

    # one sublist is added to the original array and there are left overs
    # there can be leftovers only in one sublist

    while (i < l):
        a[l] = left[i]
        i += 1
        l += 1

    while (j < r):
        a[l] = right[j]
        j += 1
        l += 1

    while (k < c):
        a[l] = center[k]
        k += 1
        l += 1

my_array = [2,7,6,8,3,2,9,7,8]
merge_sort(my_array)
for i in my_array:
    print (i,)