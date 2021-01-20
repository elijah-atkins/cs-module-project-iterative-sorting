index = 0
def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found



# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    #establish lowest and highest id in array
    lowest_id = 0
    highest_id = len(arr) - 1
    #set middle id, using integer division to keep value an integer and valid id
    middle_id = (highest_id + lowest_id) // 2

    while lowest_id <= highest_id:
        #find value of arr item in middle_id
        guess = arr[middle_id]
        #compare guess to target
        if guess is target:
            #if guess is correct return the current id
            return middle_id
        #if guess is greater than target set highest id to middle minus one
        if guess > target:
            highest_id = middle_id -1
        #if guess is less than target set lowest id to middle plus one
        if guess < target:
            lowest_id = middle_id + 1
        #set new middle_id to middle_id of unknown range
        middle_id = ((lowest_id + highest_id) // 2)
        
    return -1  # not found

