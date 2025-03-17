# The selection sort
# Find max item -> move to the last position of list

def selection_sort(list):
    limit = len(list) - 1
    for i in range(limit):
        positionMax = 0
        lastIndex = limit - i
        for j in range(lastIndex + 1):
            if list[j] > list[positionMax]: 
                positionMax = j
        # exchange
        if positionMax != lastIndex:
            list[lastIndex], list[positionMax] = list[positionMax], list[lastIndex]
    print(list)
        
unorderedList = [5,3,8,4,6]
selection_sort(unorderedList)