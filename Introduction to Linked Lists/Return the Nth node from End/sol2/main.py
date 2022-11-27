from LinkedList import LinkedList
from Node import Node


def find_nth(lst, n):

    if lst.is_empty():
        return -1

    nth_node = lst.get_head()  # This iterator will reach the Nth node
    end_node = lst.get_head()  # This iterator will reach the end of the list

    count = 0
    while count < n:
        if end_node is None:
            return -1
        end_node = end_node.next_element
        count += 1

    while end_node is not None:
        end_node = end_node.next_element
        nth_node = nth_node.next_element

    return nth_node.data


lst = LinkedList()
lst.insert_at_head(21)
lst.insert_at_head(14)
lst.insert_at_head(7)
lst.insert_at_head(8)
lst.insert_at_head(22)
lst.insert_at_head(15)

lst.print_list()

print(find_nth(lst, 19))
print(find_nth(lst, 5))
