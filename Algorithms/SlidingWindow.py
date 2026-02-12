# Sliding Window : O(n)

# When to use Variable Sliding Window:

# Subarray
# Substring
# Contiguous segment

# Variable Sliding Window Template

l = 0
for r in range(len(arr)): # Iterates through array by r pointer
    # expand window
    while invalid: # Shrinks from left when condition is invalid
        l += 1


# When to use Fixed Sliding Window 

# Subarray / substring of exact length k
# Max sum of size k
# Count condition in window of size k

# Fixed Sliding Window Template
if len(nums) < k:
    SomeResult # Edgecase for when k length is larger than given array or string length

# initialize first window
window_sum = sum(nums[:k]) 
result = window_sum

# slide window
for i in range(k, len(nums)): # Iterates from end of pre-initialized array to end of given array
    window_sum += nums[i]        # add right element
    window_sum -= nums[i - k]    # remove left element
    result = max(result, window_sum)  # modify as needed

