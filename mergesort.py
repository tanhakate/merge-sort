def merge_sort(array):
    n = len(array)
    if n<2:
        midpoint = n/2
        left = [0]*midpoint
        right = [0]*midpoint

        for i in range (0,midpoint-1):
            left = array [:i]

        for j in range (midpoint,n-1):
            right = array [j:]

        merge_sort(left)

        merge_sort(right)

        merge(left,right,array)

def merge(left,right,a):
    l = length(left)
    r = lenght(right)
    i = j = k = 0
    while i<l and j <r and k < len(a):
        if l[i]>=r[j]:
            a[k] = r[j]
            j += 1
        elif l[i]<r[j]:
            a[k] = l[i]
            l += 1
        k+=1
        
    # one sublist is added to the original array and there are left overs
    # there can be leftovers only in one sublist

    while i<l: #if there are leftovers in l
        A[k] = l[i]
        i+= 1
        k+=1

    while j<r: # if there are leftover in r
        A[k] = r[j]
        j+= 1
        k+=1

    return (a)
