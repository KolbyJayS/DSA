# Linked List

# User defined data structure
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# All reassignments are shallow copies. For a deep copy, create a new node instance and build from there

# Used in patters:
# Cycle Detection (Fast and Slow Pointer)
# Reverse List
# Dummy Head