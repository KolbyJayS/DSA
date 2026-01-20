# A binary search tree is a data structure made up of nodes, where the left node is always less than the current
# and the right node is always greater.
# Think of it like binary search. The top node is our center value, the start point. Go left, and your at the center
# value of the next left and right nodes, all of which are less than the root. Go right for the opposite

# import the deque module to use as a queue
from collections import deque

class Node:
    # Object definition for a node in the binary search tree
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
    # Function for initializing an binary search tree given a list of values
    def insert(self,nodes):
        for value in nodes:
            if not self.root:
                self.root = Node(value)
                continue
            
            curr = self.root
            while True:
                if value < curr.value:    
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = Node(value)
                        break
                else:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = Node(value)
                        break

class BST_BFS:
    # Functions for the BST : Breadth First Search
    # Given a list, initialize a binary search tree with the list's values
    def __init__(self):    
        self.root = None

    def bfs(self):
        # Ensure that the binary search tree isn't empty
        if not self.root:
            return

        # Initialize the queue (deque)
        queue = deque([self.root])
        

        # Loop through the tree. Left -> Right, Top -> Bottom
        while queue:
            # Get the node from the front of the queue
            curr = queue.popleft()

            # Here you can do whatever you want with the given node (curr)
            print(curr.value)

            # Append the child nodes to the queue, from left to right to ensure that left is always first in the queue
            if curr.left:    
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

bst = BinarySearchTree()
bst.insert([4, 2, 1, 3, 6, 5, 7])
bst.bfs()






        