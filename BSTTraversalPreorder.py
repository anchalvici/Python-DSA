class Node:
    def __init__(self, v):
        self.data = v
        self.left = None
        self.right = None
 
# Preorder Traversal
def printPreOrder(node):
    if node is None:
        return
    # Visit Node
    print(node.data, end = " ")
 
    # Traverse left subtree
    printPreOrder(node.left)
 
    # Traverse right subtree
    printPreOrder(node.right)
 
# Driver code
if __name__ == "__main__":
    # Build the tree
    root = Node(100)
    root.left = Node(20)
    root.right = Node(200)
    root.left.left = Node(10)
    root.left.right = Node(30)
    root.right.left = Node(150)
    root.right.right = Node(300)
 
    # Function call
    print("Preorder Traversal: ", end = "")
    printPreOrder(root)