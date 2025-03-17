
def remove_duplicates(sorted_list):
    if not sorted_list:
        return 0
    unique_index = 1  # Index to place the next unique element
    for i in range(1, len(sorted_list)):
        if sorted_list[i] != sorted_list[i - 1]:
            sorted_list[unique_index] = sorted_list[i]
            unique_index += 1
    return unique_index
    


# Test case 1: Empty list
test1 = []
print(f"Test 1 Before: {test1}")
result1 = remove_duplicates(test1)
print(f"Test 1 After: {test1[:result1]}")
print(f"New Length: {result1}")
print("------")

# Test case 4: List with some duplicates
test4 = [1, 1, 2, 2, 3, 4, 5, 5]
print(f"Test 4 Before: {test4}")
result4 = remove_duplicates(test4)
print(f"Test 4 After: {test4[:result4]}")
print(f"New Length: {result4}")
print("------")


'''
[1, 1, 2, 2, 3, 4, 5, 5]
-> [1, 2, 3, 4, 5, 4, 5, 5]
-> [1, 2, 3, 4]

unique_index = 1 -> value: 1
i = 1 -> 1 = 1 -> ['1', '1', 2, 2, 3, 4, 5, 5] (no changes)
i = 2 -> 2 != 1 -> [1, '2', '2', 2, 3, 4, 5, 5]
unique_index = 2
i = 3 -> 2 = 2 -> [1, 2, '2', '2', 3, 4, 5, 5] (no changes)
i = 4 -> 3 != 2 ->  [1, 2, '3', 2, '3', 4, 5, 5]
unique_index = 3
i = 5 -> 4 != 3 -> [1, 2, 3, '4', 3, '4', 5, 5]
unique_index = 4
i = 6 -> 5 != 3 -> [1, 2, 3, 4, '5', 4, '5', 5]
unique_index = 5
i = 7 -> 5 = 5 -> [1, 2, 3, 4, 5, 4, 5, 5] (no changes)
'''