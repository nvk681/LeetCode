def threeSum(nums):
        if len(nums) < 3: return []
        if len(nums) == 3: return [nums] if sum(nums) == 0 else []
        nums.sort()
        result = []
        for i in range(len(nums)-2):
            j = i+1
            while j < len(nums)-1:
                k = len(nums)-1
                while k>j:
                    total = nums[i]+nums[j]+nums[k]
                    if total == 0:
                        if [nums[i], nums[j], nums[k]] not in result:
                            result.append([nums[i], nums[j], nums[k]])
                            k -= 1
                            j += 1
                            break
                    if total > 0:
                        k -= 1
                        continue
                    if total < 0:
                        j += 1
                        continue
                    k -= 1
                j += 1
        return result

print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([0]))
print(threeSum([0, 0, 0]))
print(threeSum([]))