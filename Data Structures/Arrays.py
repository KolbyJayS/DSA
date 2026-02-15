# Arrays

arr = [] # default initialization
arr = [1,2,3] # value initialization
arr = [0] * 20 # Inititalize with size 20, 0 at each index
arr = [[0] * 4 for i in range(4)] # Initialize a 2d array (4x4)

arr[2] # Returns element at index 2
arr.append(10) # Appends to end of array O(1)
arr.pop() # removes and returns top element of array O(1)
arr.pop(1) # removes ith element of array O(n)
arr.sort() # sorts array in non-decreasing order O(nlogn)
arr.sort(key=lambda x: len(x)) # Custom Sort which sorts by length of string
arr.reverse() # Reverses the array in place O(n)
len(arr) # Returns the length of the array
arr[0:2] # Slicing/Sublist (First inclusive, second non-inclusive)
for i, n in enumerate(arr): # Gives both index and element at given index
    print(i, n)


# Commonly Used in these Patterns

## Prefix sum
## Two pointers
## Sorting + sweep
## Hashing for lookup
