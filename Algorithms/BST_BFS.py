# Binary Search Tree : Breadth First Search (O(n))

# Traverses the tree level by level from top to bottom
# Uses a queue. In python, commonly uses a deque imported from collections
# Order (Root -> Left Child -> Right Child -> Repeat)
# Use Cases:
# Min Depth
# Average of Levels
# Shortest Path

# BFS Template

from collections import deque

def bfs(root):
    if not root: # Edge case for empty tree
        return
    
    q = deque([root]) # Initialize queue with root node of BST

    while q: # Until all of the BST has been search
        node = q.popleft()
        # Process current node here

        if node.left:
            q.append(node.left) # Append left node to queue if there is one
        if node.right:
            q.append(node.right) # Append right node to queue if there is one
