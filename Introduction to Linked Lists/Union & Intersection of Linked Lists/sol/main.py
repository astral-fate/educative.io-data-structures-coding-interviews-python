from LinkedList import LinkedList
from Node import Node


def intersection(list1, list2):

    result = LinkedList()
    current_node = list1.get_head()

    # Traversing list1 and searching in list2
    # insert in result if the value exists
    while current_node is not None:
        value = current_node.data
        if list2.search(value) is not None:
            result.insert_at_head(value)
        current_node = current_node.next_element

    # Remove duplicates if any
    result.remove_duplicates()
    return result


ilist1 = LinkedList()
ilist2 = LinkedList()

ilist1.insert_at_head(14)
ilist1.insert_at_head(22)
ilist1.insert_at_head(15)

ilist2.insert_at_head(21)
ilist2.insert_at_head(14)
ilist2.insert_at_head(15)

lst = intersection(ilist1, ilist2)
lst.print_list()
