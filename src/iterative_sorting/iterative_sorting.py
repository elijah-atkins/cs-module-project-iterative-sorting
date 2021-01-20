# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    #storing array_length as variable to avoid multiple calls to len(arr)
    array_length = len(arr)
    #Run selection sort loop one time for each item in the array
    for current_index in range(array_length):
        #set index of smallest value starting from loop iteration count
        smallest_index = current_index
        #check unsorted portion of array for next lowest value
        for unsorted in range(current_index + 1, array_length):
            if arr[smallest_index] > arr[unsorted]:
                #change smallest_index to index of new lowest value found
                smallest_index = unsorted
        #swapper storage for current unsorted item
        swapper = arr[current_index]
        #put lowest value found in unsorted into arr current index
        arr[current_index] = arr[smallest_index]
        #put value in swapper to index lowest value was pulled from
        arr[smallest_index] = swapper

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    #storing array_length as variable to avoid multiple calls to len(arr)
    array_length = len(arr) - 1
    #Run bubble sort loop one time for each item in the array
    for _ in range(0, array_length):
        #run loop for every item in the array
        for current_index in range(0, array_length):
            #check if the current item is higher than the item to its right
            if (arr[current_index] > arr[current_index + 1]):
                #run swap 
                #save current value in temp swapper
                swapper = arr[current_index]
                #save item in current value as item to its right
                arr[current_index] = arr[current_index + 1]
                #save item in swapper with array item to right of current
                arr[current_index + 1] = swapper
    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here
    #if array is empty or only has one item return the unaltered array
    if not arr or len(arr) == 1:
        return arr
    #return error if given negative numbers
    if min(arr) < 0:
        return 'Error, negative numbers not allowed in Count Sort'
    #set maximum to value of higest item in array plus one to create bucket
    #from zero to higest number in array
    maximum = max(arr) + 1
    #creating an array of zeros to keep track of the number of times each value appears
    bucket = [0 for i in range(0, maximum)]
    
    #count how many times each value comes up by increasing it's tally in the bucket
    for value_index in range(0, len(arr)):
        bucket[arr[value_index]] += 1
    #set starting index value
    sorted_index = 0
    #cycle through each digit in bucket
    for digit in range(0, len(bucket)):
        #get number of occurances from current array digit
        number_of_occurances = bucket[digit]
        #if there are any occurances of digit in the bucket drop it in the 
        #array once for each occurance
        while number_of_occurances > 0:
            arr[sorted_index] = digit
            sorted_index += 1
            number_of_occurances -= 1
    return arr
