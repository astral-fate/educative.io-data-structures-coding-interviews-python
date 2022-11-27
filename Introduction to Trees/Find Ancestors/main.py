from Node import Node
from BinarySearchTree import BinarySearchTree


def findAncestors(root, k):
    if not root:
        return None
    ancestors = []
    current = root

    while current is not None:
        if k > current.val:
            ancestors.append(current.val)
            current = current.rightChild
        elif k < current.val:
            ancestors.append(current.val)
            current = current.leftChild
        else:
            return ancestors[::-1]
    return []
