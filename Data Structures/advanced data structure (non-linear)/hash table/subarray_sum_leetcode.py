def subarray_sum(nums, target):
    sum_adjacent_numbers = 0
    dict_sum_adjacent_numbers = {}

    for index, num in enumerate(nums):
        sum_adjacent_numbers += num
        rest = sum_adjacent_numbers - target
        if rest == 0:
            return [0, index]
        elif rest in dict_sum_adjacent_numbers:
            return [dict_sum_adjacent_numbers[rest] + 1, index]
        dict_sum_adjacent_numbers[sum_adjacent_numbers] = index
    return []

# cộng dần các số liền nhau và push vào dictionary với index tăng dần
# nếu = target thì lấy mảng index từ đầu tới chỗ = target
# nếu trừ target được hiệu tồn tại trong dictionary thì lấy index từ sau phần đó tới hiện tại

nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )

nums = []
target = 0
print ( subarray_sum(nums, target) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""
