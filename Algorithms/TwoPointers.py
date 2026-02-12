# Two Pointers : O(n)

# When to use :
# Sorted arrays
# Palindromes
# Pair sums

# General Template
l, r = 0, len(arr) - 1 # Initializae left and right pointer
while l < r:
    if condition: # if condition shrink from left
        l += 1
    else: # else shrink from right
        r -= 1
