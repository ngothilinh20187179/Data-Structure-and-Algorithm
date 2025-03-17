# Hoare Partitioning Scheme


def quickSort(list):
    quickSortHelper(list, 0, len(list) - 1)

def quickSortHelper(list, first_index, last_index):
    if first_index < last_index:
        splitpoint = partition(list, first_index, last_index)
        quickSortHelper(list, first_index, splitpoint - 1)
        quickSortHelper(list, splitpoint + 1, last_index)

def partition(list, first, last):
    pivotvalue = list[first]
    leftmark = first + 1
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and list[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        while rightmark >= leftmark and list[rightmark] >= pivotvalue:
            rightmark = rightmark - 1
        if rightmark < leftmark:
            done = True # giao nhau
        else:
            list[leftmark], list[rightmark] = list[rightmark], list[leftmark]
    list[first], list[rightmark] = list[rightmark], list[first]

    return rightmark

list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(list)
print(list)

""" 
    Chọn phần tử chốt (pivot) (đầu tiên của list)
    chạy leftmark từ trái sang phải list ->-> stop khi > pivot
    chạy rightmark phải sang trái list ->-> stop khi < pivot
    -> hoán đổi giá trị
    nếu leftmark và rightmark chạy giao nhau thì hoán pivot với split point (rightmark)
    đệ quy
"""
