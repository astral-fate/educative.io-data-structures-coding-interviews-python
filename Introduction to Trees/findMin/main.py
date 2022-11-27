from Node import Node
from BinarySearchTree import BinarySearchTree


def findMin(root):
    if root is None:  # check for None
        return None
    while root.leftChild:  # Traverse until the last child
        root = root.leftChild
    return root.val  # return the last child


BST = BinarySearchTree(6)
BST.insert(20)
BST.insert(-1)

print(findMin(BST.root))
