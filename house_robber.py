class Solution:
    def rob(self, nums: List[int]) -> int:
        for i in range(2, len(nums)):
            if i >= 3:
                nums[i] = nums[i]+max(nums[i-2],nums[i-3])
            else: 
                nums[i] = nums[i]+nums[i-2]
        if nums[len(nums)-1] > nums[len(nums)-2]:
            return nums[len(nums)-1]
        else: 
            return nums[len(nums)-2]