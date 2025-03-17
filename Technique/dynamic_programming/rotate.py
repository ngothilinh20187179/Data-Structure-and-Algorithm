
def rotate(nums, k):
    n = len(nums)
    if n == 0 or k == 0:
        return

    k = k % n  # Handle cases where k > n
    
    nums.reverse() # [7, 6, 5, 4, 3, 2, 1]

    nums[:k] = reversed(nums[:k]) # [5, 6, 7, 4, 3, 2, 1]

    nums[k:] = reversed(nums[k:]) # [5, 6, 7, 1, 2, 3, 4]
    


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
print("Rotated array:", nums)


"""
    EXPECTED OUTPUT:
    ----------------
    Rotated array: [5, 6, 7, 1, 2, 3, 4]

"""