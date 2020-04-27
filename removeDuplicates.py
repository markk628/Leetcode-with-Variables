"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Variable | Value
nums     | Type list
left     | 0
right    | 1

Restated
    - Return the length of a sorted array after removing duplicate values. Don't make a new list.

Questions
    - Are the values consecutive because if then I could just return the last value + 1

Assumptions
    - Assuming values are not consecutive
        * [1,4,7,8] insead of [1,2,3,4,5,6,7,8]

Thinking Out Loud
    Make two pointers that are right with values 0 and 1 respectively
    While right is less than the length of the list
        Compare both pointers
            if they are equal remove one of them
            else add 1 to each
    return the length of the new list

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