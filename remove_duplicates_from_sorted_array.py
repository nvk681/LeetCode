class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        while index < len(nums)-1:
            if nums[index] == nums[index+1]:
                del nums[index+1]
                continue
            index += 1
        return len(nums)