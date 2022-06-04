class Solution:
    def productExceptSelf(self, nums: List[int]):
        ans = [1]*len(nums)
        for i in range(1, len(nums)):
            ans[i] = ans[i-1]*nums[i-1]
        rightProduct = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] = ans[i] * rightProduct
            rightProduct *= nums[i]
        return ans