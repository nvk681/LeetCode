def rob(nums):
        for i in range(2, len(nums)):
            if i >= 3:
                nums[i] = nums[i]+max(nums[i-2],nums[i-3])
            else: 
                nums[i] = nums[i]+nums[i-2]
        if nums[len(nums)-1] > nums[len(nums)-2]:
            return nums[len(nums)-1]
        else: 
            return nums[len(nums)-2]

print(rob([1,2,3,1]))
print(rob([2,7,9,3,1]))
print(rob([0]))
# print(rob([]))