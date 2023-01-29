class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            reminder = target - nums[i]
            coun = 0 if nums[i] != reminder else 1
            if nums.count(reminder) > coun:                   
                nums[i] = None
                return i, nums.index(reminder)