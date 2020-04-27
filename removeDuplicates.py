"""
Variable | Value
nums     | Type list
left     | 0
right    | 1
"""

def removeDuplicates(nums) -> int:
    left = 0
    right = 1

    while right < len(nums):
        if nums[left] == nums[right]:
            nums.remove(nums[right])
        else:
            left += 1
            right += 1
        
    return len(nums)

listWithDuplicates = [2,2,4,4,6,7,8]
print(removeDuplicates(nums=listWithDuplicates))