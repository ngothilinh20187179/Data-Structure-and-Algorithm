# not allocate extra space for another list
# modify the input list in-place with O(1) extra memory.

# ko phân bổ thêm ko gian lưu trữ, sửa đổi trực tiếp mảng đầu vào

def remove_element(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i] # đẩy dần các số muốn xoá về cuối hàng
            k += 1 
        print(nums)
    while len(nums) > k:
        nums.pop()
    
    return k

nums = [1, 2, 3, 4, 5]
val = 3
print("Remove value", val, "that's located at the end of the list.")
print("BEFORE:", nums)
new_length = remove_element(nums, val)
print("AFTER:", nums, "\nNew length:", new_length)

# [1, 2, 4, 5] 
# length: 4