# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    #storing array_length as variable to avoid multiple calls to len(arr)
    array_length = len(arr)
    #Run sort loop one time for each item in the array

    
    for current_index in range(array_length):
        #set index of smallest value starting from loop iteration count
        smallest_index = current_index
        #check unsorted portion of array for next lowest value
        for item in range(current_index + 1, array_length):
            if arr[smallest_index] > arr[item]:
                #change smallest_index to index of new lowest value found
                smallest_index = item
        #swapper storage for current item
        swapper = arr[current_index]
        #put lowest value found in current index
        arr[current_index] = arr[smallest_index]
        #put value in swapper to index lowest value was pulled from
        arr[smallest_index] = swapper

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    for i in range(0, len(arr) - 1):
        for num in range(0, len(arr) - 1):
            if (arr[num] > arr[num + 1]):
                x = arr[num]
                arr[num] = arr[num + 1]
                arr[num + 1] = x
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
    if not arr or len(arr) == 1:
        return arr
    if min(arr) < 0:
        return 'Error, negative numbers not allowed in Count Sort'

    largest = max(arr) + 1
    elements = [0 for i in range(0, largest)]

    for i in range(0, len(arr)):
        elements[arr[i]] += 1

    sorted_index = 0
    for i in range(0, len(elements)):
        num = elements[i]
        while num > 0:
            arr[sorted_index] = i
            sorted_index += 1
            num -= 1
    return arr
