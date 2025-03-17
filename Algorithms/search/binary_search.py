# divide and conquer
def binarySearch(orderedList, item):
    if len(orderedList) == 0:
        return False
    else :
        low = 0
        hight = len(orderedList) - 1 # -> error if empty list
        found = False
        while low <= hight and not found:
            midIndex = (low + hight) // 2 # -> / maybe return float, // -> return int
            midValue = orderedList[midIndex]
            if midValue == item:
                found = True
            elif midValue < item:
                low = midIndex + 1
            else:
                hight = midIndex - 1
        return found

orderedList = []
print("Found ?", binarySearch(orderedList, 2))
orderedList = [1,2,3,4,5,6,7,8]
print("Found ?", binarySearch(orderedList, 2))

# Recursion
# Moi lan lai tao list moi co the ton bo nho
def binarySearchRecursion(orderedList, item):
    if len(orderedList) == 0:
        return False
    else:
        midIndex = len(orderedList) // 2
        midValue = orderedList[midIndex]
        if midValue == item:
            return True
        elif midValue < item:
            return binarySearchRecursion(orderedList[midIndex+1:], item)
        else:
            return binarySearchRecursion(orderedList[:midIndex], item)

orderedListSecond = [1,2,3,4,5,6,7,8]
print("Found ?", binarySearchRecursion(orderedListSecond, 2))