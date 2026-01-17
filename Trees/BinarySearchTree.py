# A binary search tree is a commonly used data structure built up of nodes, with each node having at most 2 child nodes.
# The properties are simple. The left side of a node is always smaller values. The right is always larger.

# binary search tree implementation
class Node:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None

class BST_Methods:

    # Method for inserting a new node onto a BST : Recursive
    def insertRecur(root,key):
        # If tree is empty, return a new node
        if not root:
            return Node(key)
        
        # Otherwise, make way down the tree
        if key < root.value:
            root.left = insertRecur(root.left,key)
        else:
            root.right = insertRecur(root.right,key)

        # Return the unchanged node pointer
        return root
    
    # Method for inserting a new node onto a BST : Iterative
    def insertIter(root,key):
        temp = Node(key)
        
        # If tree is empty
        if not root:
            return Node(key)
        
        # Find the node which will be the new node's parent
        curr = root
        while curr:
            if curr.value > key and curr.left:
                curr = curr.left 
            elif curr.value < key and curr.right:
                curr = curr.right
            else:
                break
            
        # If key is smaller than key, make it left child. If greater, make right child
        if curr.value > key:
            curr.left = temp
        else:
            curr.right = temp
        
        return root
    

    # Method for searching for a specific node in a tree : Recursive
    def searchRecur(root,key):
        # Empty root node, key not present in tree
        if not root:
            return False
        
        # If key == node value, found node
        if root.value == key:
            return root

        # If key is smaller, search left. If key is bigger, search right. If Equal, found key
        if root.value < key:
            return searchRecur(root.right,key)
        else:
            return searchRecur(root.left,key)
    
    # Method for search for a specific node : Iterative
    def searchIter(root,key):
        curr = root

        while curr:
            # if node value == key, found Node
            if curr.value == key:
                return True

            # If node value > key, search left. If node value < key, search right    
            if curr.value < key:
                curr = curr.right
            else:
                curr = curr.left
        
        return curr
    

    #Method for deletion of a specific node : Recursive
    def delNodeRecur(root,key):
        if not root:
            return root
        # find parent node     
        if root.value > key:
            root.left = delNodeRecur(root.left, key)
        elif root.value < key:
            root.right = delNodeRecur(root.right,key)
        else: # found node to be deleted

            # If node with 0 or 1 child node
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            # Node has 2 children
            # Get successor
            succ = getSuccesor(root)
            # change value of root node to successor (replace it with successor)
            root.value = succ.value
            # Delete successor original node
            root.right = delNodeRecur(root.right,succ.data)

    # Helper function for finding successor (smallest in right subtree)
    def getSuccesor(curr):
        curr = curr.right
        while curr and curr.left:
            curr = curr.left
        return curr

    
    # BST Depth First Search Traversals
    # Recursive
    # Inorder : Gives the nodes in non-decreasing order of the values | Left Tree, Visit Root, Right Tree
    def inOrder(root):
        if root:
            # Traverse left subtree
            printInorder(root.left)

            # Visit node
            print(root.value,end=" ")

            # Traverse right subtree
            printInorder(root.right)


    # postOrder : Used to delete a tree from leaf to root | Left Tree, Right Tree, Root
    def postOrder(root):
        if root:
            # Traverse the left subtree
            postOrder(root.left)
            # Traverse the right subtree
            postOrder(root.right)
            # Return to the node
            print(root.value,end=" ")

    # preOrder : Used to create a copy of a tree | Root, Left Tree, Right Tree
    def preOrder(root):
        if root:
            # Visit the node
            print(root.value,end=" ")
            # Traverse the left subtree
            preOrder(root.left)
            # Traverse the right subtree
            preOrder(root.right)
    
    # Iterative
    # inOrder
    def inOrder(root):
        curr = root
        stack = []
        result = []
        # loop until whole tree has been traversed
        while curr or len(stack) > 0: 
            # traverse left subtree
            while curr:
                stack.append(curr)
                curr = curr.left

            # No more left, append all left subtree in order
            curr = stack.pop()
            result.append(curr.value)

            # move to right subtree
            curr = curr.right
        return result

        

    # postOrder
    def postOrderIterative(root):
         

    # preOrder
    def preOrderIterative(root):
        stack = [root]
        output = []

        while stack:
            node = stack.pop()
            result.append(node.value)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result

    # BST Breadth First Search Traversals
    # Recursive 
           
    


        