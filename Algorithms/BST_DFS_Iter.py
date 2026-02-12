# Binary Search Tree : Depth First Search : Iterative (O(n))

# Explores one branch in its entirety before moving to the next branch
# Is stack based. Hence either the call stack is used ( Recursion ), or an explicit stack ( Iterative )

# Split into 3 types which affect the order of which the tree is traversed

# Preorder (Root -> Left -> Right) (Left to Right)
# This processes current node immediately, then go through entire left subtree, then right subtree
# Use Cases:
# Serialize Tree
# Copy/Clone Tree
# Construct Expression Trees
# Prefix Evaluation

def dfs_PreOrder(root):
    if not root: # Empty bst edge case check
        return
    
    stack = [root] # Initialize Stack with root of bst

    while stack: # Loop until entire BST has been traversed
        node = stack.pop() # Take node from top of stack

        # Process current node here

        if node.right:
            stack.append(node.right) # If right node exists, add to stack
        if node.left:
            stack.append(node.left) # If left node exists, add to stack


# Inorder (Left -> Root -> Right) (Left to Right, From Bottom)
# Search entire left subtree, then root, then right subtree. Returns BST nodes in ascending order
# Use Cases:
# Validate BST
# Get Sorted Values from BST
# Kth Smallest in BST

def dfs_InOrder(root):
    stack = [] # Initialize Stack
    cur = root # 
    
    while stack or cur: # Loop until entire BST has been traversed
        while cur: # Append entire Left Tree from Root
            stack.append(cur) 
            cur = cur.left


# Postorder (Left -> Right -> Root) (Left to Right, Bottom to Top)
# Process child nodes before root node
# Use Cases:
# Delete/Free Tree
# Compute subtree Properties (Height,Sum,Diameter)
# Bottom-up DP on trees



