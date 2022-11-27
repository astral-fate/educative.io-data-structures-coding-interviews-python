from LinkedList import LinkedList
from Node import Node


def union(list1, list2):
    # Return other List if one of them is empty
    if (list1.is_empty()):
        return list2
    elif (list2.is_empty()):
        return list1

    start = list1.get_head()

    # Traverse the first list till the tail
    while start.next_element:
        start = start.next_element

    # Link last element of first list to the first element of second list
    start.next_element = list2.get_head()
    list1.remove_duplicates()
    return list1


ulist1 = LinkedList()
ulist2 = LinkedList()
ulist1.insert_at_head(8)
ulist1.insert_at_head(22)
ulist1.insert_at_head(15)

print("List 1")
ulist1.print_list()

ulist2.insert_at_head(21)
ulist2.insert_at_head(14)
ulist2.insert_at_head(7)

print("List 2")
ulist2.print_list()

new_list = union(ulist1,ulist2)

print("Union of list 1 and 2")
new_list.print_list()
