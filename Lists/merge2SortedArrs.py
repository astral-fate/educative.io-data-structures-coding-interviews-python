def merge_lists(lst1, lst2):
    ind1 = 0
    ind2 = 0
    while(ind1 < len(lst1) and ind2 < len(lst2)):
        if(lst1[ind1] > lst2[ind2]):
            lst1.insert(ind1, lst2[ind2])
            ind1 += 1
            ind2 += 1
        else:
            ind1 += 1

    if(ind2 < len(lst2)):
        lst1.extend(lst2[ind2:])
    return lst1



#solve it using bubble sort

def sort_and_merge(array1):
  # Use bubble sort to sort array1
  n = len(array1)
  for i in range(n):
    for j in range(0, len(array1)-1):
      if array1[j] > array1[j + 1]:
        temp = array1[j]
        array1[j] = array1[j + 1]
        array1[j + 1] = temp
        
    return array1
    
    
    
list1=[1,4,6,7,2]
print(sort_and_merge(list1))
