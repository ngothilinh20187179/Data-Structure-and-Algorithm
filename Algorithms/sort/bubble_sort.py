# The bubble sort
# Compare adjacent items and exchange those
# Mỗi lần chạy lại vòng for là list mới bỏ đi phần tử cuối cùng

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
        print(lst)

unordered_list = [5, 3, 8, 4, 6]
bubble_sort(unordered_list)

print("-------")

# ít step hơn
def bubbleSort(list):
    stillExchange = True
    numberElements = len(list) - 1
    while numberElements > 0 and stillExchange:
        stillExchange = False
        for i in range(numberElements):
            if list[i] > list[i + 1]:
                stillExchange = True
                list[i], list[i + 1] = list[i + 1], list[i]
        numberElements = numberElements - 1
        print(list)

unorderedList = [5, 3, 8, 4, 6]
bubbleSort(unorderedList)