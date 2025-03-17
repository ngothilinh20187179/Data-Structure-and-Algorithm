def sequentialSearch(list, item): 
    index = 0
    found = False
    while not found and index < len(list):
        if list[index] == item:
            print("How many comparisons ?", index + 1)
            found = True
        else :
            index += 1
    return found

numberList = [0,1,2,3,6,3,8,12,9]            
print("Found number ?", sequentialSearch(numberList, 12))

# compare - ordered list
def sequentialSearchOrderedList(list, item):
    index = 0
    found = False
    stop = False
    while index < len(list) and not stop and not found:
        if list[index] == item:
            found = True
            print("How many comparisons ?", index + 1)
        else:
            if list[index] > item:
                stop = True
            else:
                index += 1
    return found

orderedNumberList = [1,2,3,4,5,6,7,8,9,10]
print("Found number in ordered list ?", sequentialSearchOrderedList(orderedNumberList, 10))