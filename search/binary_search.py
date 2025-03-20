def binary_search(nums, target):
    left, right = 0, len(nums) -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if target > nums[mid]:
            left = mid + 1
        elif target < nums[mid]:
            right = mid - 1
        else:
            return mid

numbers = [1, 3, 5, 7, 9, 11]
print(binary_search(numbers, 7))