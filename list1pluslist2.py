def list_plus(list1, list2):
    list_sum = []
    if len(list1) > len(list2):
        for j in range(len(list1)-len(list2)):
            list2.append(0)
    elif len(list2) > len(list1):
        for j in range(len(list2)-len(list1)):
            list1.append(0)    
    for i in  range(len(list1)):
        list_sum.append(list1[i] + list2[i])
    return list_sum
  
l1 = [99,100,101,33]
l2 = [101,101,333,139,22,33333,9999]

print(list_plus(l1,l2))
