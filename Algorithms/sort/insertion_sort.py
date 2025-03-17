# The insertion sort
# Insert each item into its correct position within the sorted part
def insertion_sort(list):
    for i in range(1, len(list)):
        position = i
        currentValue = list[i]
        while position > 0 and list[position-1] > currentValue:
            list[position] = list[position - 1]
            position = position - 1
        list[position] = currentValue
        print(list)

unorderedList = [5, 3, 8, 4, 6]
insertion_sort(unorderedList)

# [5, 3, 8, 4, 6]
# run index 1 -> 4
# i = 1
    # position = 1
    # currentValue = 3
    # list[0] > currentValue (5 > 3)
        # list[1] = list[0] = 5
        # position = 0
    # list[0] = currentValue = 3
    # [3, 5, 8, 4, 6]
# i = 2
    # position = 2
    # currentValue = 8
    # list[1] > currentValue (5 > 8) (sai)
    # list[2] = currentValue = 8
    # [3, 5, 8, 4, 6]
# i = 3
    # position = 3
    # currentValue = 4
    # list[2] > currentValue (8 > 4)
        # list[3] = list[2] = 8
        # position = 2             ([3, 5, 8, '8', 6])
    # list[1] > currentValue (5 > 4)
        # list[2] = list[1] = 8
        # position = 1             ([3, 5, '5', 8, 6])
    # list[0] < currentValue (3 < 4)
    # list[1] = 4
    # [3, 4, 5, 8, 6]
# i = 4
    # position = 4
    # currentValue = 6
    # list[3] > currentValue (8 > 6)
        # list[4] = list[3]         ([3, 4, 5, 8, '8'])
        # position = 3
    # list[2] > currentValue (5 > 6)  (Sai. Vòng lặp while kết thúc)
    # list[3] = currentValue = 6
    # [3, 4, 5, 6, 8]