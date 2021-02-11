# Problem STatement
"""
Q.30  Write a function that combines two lists by alternatingly taking elements,
 e.g. [a,b,c], [1,2,3,4] → [a,1,b,2,c,3,4] (assuming both lists can be of varying lengths)
"""

def combine_alter_list_ele(lst1, lst2):
    dummy_lst = list()
    for i in range(min([len(lst1),len(lst2)])):
        dummy_lst.append(lst1[i])
        dummy_lst.append(lst2[i])
    if lst1 > lst2:
        for i in lst1[len(lst2):]:
            dummy_lst.append(i)
    else:
        for i in lst2[len(lst1):]:
            dummy_lst.append(i)
    return dummy_lst

lst1 = [44,55,66,77,88]
lst2 = [11,22,33]
print(lst1,'and', lst2)
print(combine_alter_list_ele(lst1,lst2))

        
        
    


    