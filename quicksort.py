def partition(arr, low, high):
	i = (low-1)		 # index of smaller element constant-time
	pivot = arr[high]	 # pivot constant-time

	for j in range(low, high):
		# If current element is smaller than or
		# equal to pivot
		if arr[j] <= pivot: #O(n)
			# increment index of smaller element
			i = i+1 #constant-time
			arr[i], arr[j] = arr[j], arr[i]
	arr[i+1], arr[high] = arr[high], arr[i+1] #constant-time
	return (i+1) #constant-time
#O(n)



def quickSort(arr, low, high):
	if len(arr) == 1:
		return arr
	if low < high: #constant-time
		# pi is partitioning index, arr[p] is now
		# at right place
		pi = partition(arr, low, high) #O(n)
		quickSort(arr, low, pi-1) # Sort left of partitioned # n-1
		quickSort(arr, pi+1, high) # Sort right  of partitioned  #n
        
        
# = O(n-1)+O(n)       
# Worst case O(n^2)

