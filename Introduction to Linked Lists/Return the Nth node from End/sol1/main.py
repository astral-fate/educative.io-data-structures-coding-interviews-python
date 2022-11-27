from LinkedList import LinkedList
from Node import Node


def find_nth(lst, n):
    if (lst.is_empty()):
        return -1

    # Find Length of list
    length = lst.length() - 1

    # Find the Node which is at (len - n + 1) position from start
    current_node = lst.get_head()

    position = length - n + 1

    if position < 0 or position > length:
        return -1

    count = 0

    while count is not position:
        current_node = current_node.next_element
        count += 1

    if current_node:
        return current_node.data
    return -1


lst = LinkedList()
lst.insert_at_head(21)
lst.insert_at_head(14)
lst.insert_at_head(7)
lst.insert_at_head(8)
lst.insert_at_head(22)
lst.insert_at_head(15)


lst.print_list()
print(find_nth(lst, 5))
print(find_nth(lst, 1))
print(find_nth(lst, 10))

