from LinkedList import LinkedList
from Node import Node
# Access HeadNode => list.getHead()
# Check length => list.length()
# Check if list is empty => list.isEmpty()
# Node class  { int data ; Node nextElement;}


def find_mid(lst):
    if lst.is_empty():
        return None

    node = lst.get_head()
    mid = 0
    if lst.length() % 2 == 0:
        mid = lst.length()//2
    else:
        mid = lst.length()//2 + 1

    for i in range(mid - 1):
        node = node.next_element

    return node.data


lst = LinkedList()
lst.insert_at_head(22)
lst.insert_at_head(21)
lst.insert_at_head(10)
lst.insert_at_head(14)
lst.insert_at_head(7)

lst.print_list()
print(find_mid(lst))
