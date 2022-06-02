class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums) 
        nums.reverse()
        start, end = 0, k-1
        while start < end:
            nums[end], nums[start] = nums[start], nums[end]
            end -= 1
            start += 1
        start, end = k, len(nums)-1
        while start < end:
            nums[end], nums[start] = nums[start], nums[end]
            end -= 1
            start += 1