# Binary Search
# O(logn)

# Works by splitting the array in a left and right portion based on middle pointer
# Only work on left or right portion depending on which meets needed condition
# Continue until needed value is found

# Common Question Types:
# Sorted Array
# Monotonic Function

# Standard Binary Search Template
def BST ():
    l, r = 0, len(arr)-1 # Initialize left and right pointer
    while l <= r: # Continuous loop until value is found or is proven it doesn't exist
        mid = (l + r)//2 # middle of l and r pointers
        if arr[mid] == target: # if value is found, return it
            return mid
        elif arr[mid] < target: # if target in right portion, disregard left portion
            l = mid + 1 
        else: # else if target in left portion, disregard right portion
            r = mid - 1