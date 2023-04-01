# Radix sort 


# Using counting sort to sort the elements in the basis of significant places
def countingSort(array, place):
    #length of data 
    #O(1)
    size = len(array)
  
    #auxiliary array for assigning sorted data 
    #O(1)
    output = [0] * size #(n) will be the number of data 
    
    #This array is used for storing the count of the elements in the array. 
    #why 10? because each position can hold number of the range 0-9
    #O(1)
    count = [0] * 10 #(k) will be the number of bucket that will hold count of numbers

    # Calculate count of elements O(n)
    # digit position: ones / tens /hundred and so on
    #O(n)   size
    for i in range(0, size):
        index = array[i] // place   
        count[index % 10] += 1  

    # Calculate cumulative count
    #O(k) 
    for i in range(1, 10):
        count[i] += count[i - 1]

    
    # Find the index of each element of the original array in count array
    # place the elements in output array
    
    #O(n) 
    i = size - 1 #placing integers to it correcponding place in array in backward
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i] 
        count[index % 10] -= 1 #deacrement count by 1
        i -= 1 #deacrement by 1


    #filling original array with sorted data in output array
     #O(n)
    for i in range(0, size):
        array[i] = output[i]
 

# Main function to implement radix sort
def radixSort(array):
        
    # Get maximum element in data
    ##O(1)
    max_element = max(array)

    # Apply counting sort to sort elements based on place value.
    #O(maxDigit)
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10 #increasse the place by 10 each loop
        


