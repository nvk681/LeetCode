def rob(nums):
    if len(nums) > 2:
        nums[2] = nums[2]+nums[0]
    for i in range(3, len(nums)):
        nums[i] = nums[i]+max(nums[i-2],nums[i-3])
    
    if nums[len(nums)-1] > nums[len(nums)-2]:
        return nums[len(nums)-1]
    else: 
        return nums[len(nums)-2]


print(rob([1,2,3,1]))
print(rob([2,7,9,3,1]))
print(rob([0]))
# print(rob([]))