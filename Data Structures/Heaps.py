# Heaps

import heapq

# Min Heap by Default (Top Element is minimum)
heap = [] # Initialize an Array
heapq.heappush(heap,x) # Pushes x onto heap : O(logn)
heapq.heappop(heap) # pops top element from heap (in this case the min) : O(logn)
heapq.heapify(heap) # Given a non-empty list, turns list into min heap : O(n)
heap[0] # Returns top value from heap (in this case the min)

# Max Heap (As if 3.14) (Else: Just turn all members of array into negative corrospondents)

# convert to negative
nums = [-x for x in nums]

# heap_max methods
heap = [] # Initialize an Array
heapq.heappush_max(heap,x) # Pushes x onto heap : O(logn)
heapq.heappop_max(heap) # pops top element from heap (in this case the max) : O(logn)
heapq.heapify_max(heap) # Given a non-empty list, turns list into max heap : O(n)
heap[0] # Returns top value from heap (in this case the max)
