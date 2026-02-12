# Binary Trees
# Left value is less than current
# Right Value is greater than current
# Holds true for entire tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Uses DFS and BFS for Traversal