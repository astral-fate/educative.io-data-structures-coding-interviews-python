from Node import Node
from BinarySearchTree import BinarySearchTree


# Check console to see input tree
def findKNodes(root, k):
    res = []
    findK(root, k, res)
    return res

# Helper recursive function to traverse tree and append all
# the nodes at "k" distance into "res" list


def findK(root, k, res):
    if root is None:
        return
    if k == 0:
        res.append(root.val)
    else:
        # Decrement k at each step till you reach at the leaf node
        # or when k == 0 then append the Node's data into result string
        findK(root.leftChild, k - 1, res)
        findK(root.rightChild, k - 1, res)

    pass
