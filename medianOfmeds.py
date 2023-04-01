#this function do the partitioning depends on pivot value
def partition(data, pivot):
    j = 0 # O(1)
    right = len(data) - 1 # O(1)
    i = 0 # O(1)
    while i <= right:  # O(n)
        if data[i] == pivot: # O(1)
            i += 1 # O(1)
        elif data[i] < pivot: # O(1)
            data[j], data[i] = data[i], data[j] # O(1)
            j += 1 # O(1)
            i += 1# O(1)
        else:
            data[right], data[i] = data[i], data[right] # O(1)
            right -= 1 # O(1)
    return j # O(1)

# the complexity of this function reach to # O(n)

#==============================================================================

#this is the main function of median_of_medians algorithm
# it is spliting the data array to lists of 5 element
#and find the median of each list and the the median of them
#then assign it as a pivot to da the partitioning 
#then decide if the pivot is the median or decide the direction
#of the next call 
    
def selectPivot(data, k):

    sublists = [data[i : i+5] for i in range(0, len(data), 5)]    # O(n/5) this is gathering each 5 element to one list
    
    sortedSublists = [sorted(sub) for sub in sublists]    # O(n/5) it sort each sublist created from previous step
    medians = [sub[len(sub) // 2] for sub in sortedSublists]     #O(n/5) it retrieve the median of each sublist

    # if # of sublists > 5 we will have recursive call with median list to get the median of them
    #otherwise we will choose the median of medians directly 
    
    #so selectPivot function may take #O(n/5) = #O(n)
    
    if len(medians) <= 5: #O(1)
        pivot = sorted(medians)[len(medians) // 2] #O(1)
    else:
        pivot = selectPivot(medians, len(medians) // 2) #O(7n/10)
        
    res = partition(data, pivot) #as we see it may takes O(n)
    
    if k == res: #O(1)
        return pivot #O(1)
    if k < res: #O(1)
        return selectPivot(data[0:res], k)  #O(7n/10)  
    else:
        return selectPivot(data[res+1:len(data)], k - res - 1) #O(7n/10)
    
    #the max complexity in this section = O(7n/10)
#==============================================================================
        
#here is the main call to implement the algorithm
        
def medianOfMedians(data, size): 
    #if there is no data return none
    if data is None or len(data) == 0: #O(1)
        return None #O(1)

    return selectPivot(data, size) #O(7n/10)
#==============================================================================

#so the complexity we may get is: 
#spliting + select pivot + partitioning 
# O(n/5) + O(7n/10) + O(n)  = O(n)
