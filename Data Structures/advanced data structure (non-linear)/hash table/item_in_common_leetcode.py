def item_in_common(list1,list2):
    dictionary = {}
    for i in list1:
        dictionary[i] = True
    for j in list2:
        if j in dictionary:
            return True
    return False

list1 = [1,3,5]
list2 = [2,4,5]


print(item_in_common(list1, list2))



"""
    EXPECTED OUTPUT:
    ----------------
    True

"""