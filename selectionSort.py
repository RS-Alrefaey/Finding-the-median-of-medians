# This funaction will sort the data and find the median with Slection Sort Algorithm
def Median_Selection_Sort(A):
    import math
    Len = len(A)# O(1)
    # Traverse through all array elements
    for i in range(Len-1):# O(n)
        # Find the minimum element in remaining 
        # unsorted array
        min_i = i# O(1)
        for j in range(i+1, Len): # O(n)
            if(A[j] < A[min_i]): # O(1)
                A[j], A[min_i] = A[min_i], A[j] # O(1)
        # Swap the found minimum element with 
        # the first element
        if(min_i != i): # O(1)
            A[min_i], A[i] = A[i], A[min_i] # O(1)
 # Calculating median O(1)
    # if the data have an even number of elements we have to get the average of the 2 elements in the middle
    if( (Len % 2) == 0 ): # O(1)
        m1 = math.floor((Len)/2) # O(1)
        m2 = math.floor((Len-1)/2) # O(1)
        med = (A[m1] + A[m2])/2 # O(1)
    # otherwise we get the mid of them all
    else:
        med = A[math.floor((Len)/2)] # O(1)
    return med