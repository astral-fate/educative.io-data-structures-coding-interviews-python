from Node import Node
from BinarySearchTree import BinarySearchTree


def findMin(root):
    if root is None:  # check if root exists
        return None
    elif root.leftChild is None:  # check if left child exists
        return root.val  # return if not left child
    else:
        return findMin(root.leftChild)  # recurse onto the left child


BST = BinarySearchTree(6)
BST.insert(20)
BST.insert(-1)

print(findMin(BST.root))
