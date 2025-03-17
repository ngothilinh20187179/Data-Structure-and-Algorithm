
def find_pairs(arr1, arr2, target):
    set_arr1 = set(arr1)
    set_arr2 = set(arr2)
    pairs = []
    for num in set_arr2:
        if target - num in set_arr1:
            pairs.append((target - num, num))
    return pairs



arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)



"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""