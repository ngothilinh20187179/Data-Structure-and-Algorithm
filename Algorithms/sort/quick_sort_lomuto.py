######## Lomuto Partitioning biến thể

def quick_sort(list):
    quick_sort_helper(list, 0, len(list)-1)

# đệ quy sắp xếp danh sách nhỏ và lớn hơn privot
def quick_sort_helper(list, left_index, right_index):
    if left_index < right_index:
        pivot_index = pivot(list, left_index, right_index) # pivot index mới -> sau khi hoán đổi để chia list hai phần < và >
        print ("list", list) # list cũng đc sắp xếp lại (do reference, Hàm pivot() tác động đến list trong quick_sort_helper())
        quick_sort_helper(list, left_index, pivot_index-1)  
        quick_sort_helper(list, pivot_index+1, right_index)       
    return list

def swap(list, index1, index2):
    list[index1], list[index2] = list[index2], list[index1]

# hoán đổi pivot với phần tử tại swap_index để đặt nó vào đúng vị trí
def pivot(list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index+1, end_index+1):
        if list[i] < list[pivot_index]:
            swap_index += 1
            swap(list, swap_index, i)
    swap(list, pivot_index, swap_index)
    return swap_index

list = [4,6,1,7,3,2,5]

quick_sort(list)

print(list)



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6, 7]
 """

"""
    [4,6,1,7,3,2,5]
    pivot list -> [2, 1, 3, '4', 6, 7, 5], swap_index = 3
    
    quick_sort_helper [2, 1, 3] vs [6, 7, 5]
    pivot [2, 1, 3] -> swap(list, pivot_index, swap_index) -> [1, 2, 3]
    ...
"""