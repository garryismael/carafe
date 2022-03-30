# Python3 program for the above approach
 
# Structure of an N ary tree node
class Node:
    def __init__(self, x):
        self.data = x
        self.child = []
 
# Function to print the root to leaf
# path of the given N-ary Tree
def printPath(vec):
     
    # Print elements in the vector
    for ele in vec:
        print(ele, end = " ")
        
    print()
 
# Utility function to print all
# root to leaf paths of an Nary Tree
def printAllRootToLeafPaths(root):
     
    global vec
     
    # If root is null
    if (not root):
        return
 
    # Insert current node's
    # data into the vector
    vec.append(root.data)
 
    # If current node is a leaf node
    if (len(root.child) == 0):
 
        # Print the path
        printPath(vec)
 
        # Pop the leaf node
        # and return
        vec.pop()
        return
 
    # Recur for all children of
    # the current node
    for i in range(len(root.child)):
 
        # Recursive Function Call
        printAllRootToLeafPaths(root.child[i])
         
    vec.pop()   
 
# Function to print root to leaf path
def printRootToLeafPaths(root):
     
    global vec
     
    # If root is null, return
    if (not root):
        return
 
    # Utility function call
    printAllRootToLeafPaths(root)
 
# Driver Code
if __name__ == '__main__':
     
    # Given N-Ary tree
    vec = []
    root = Node(1)
    root.child.append(Node(2))
    root.child.append(Node(3))
    root.child[0].child.append(Node(4))
    root.child[1].child.append(Node(5))
    root.child[1].child.append(Node(6))
    root.child[1].child[1].child.append(Node(7))
    root.child[1].child[1].child.append(Node(8))
 
    # Function Call
    printRootToLeafPaths(root)
 
# This code is contributed by mohit kumar 29