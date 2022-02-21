class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for index in range(len(nums)):
            hash_map[nums[index]] = index
        for i in range(len(nums)): 
                 if (target - nums[i]) in hash_map and i != hash_map[target - nums[i]]:
                     return [i, hash_map[target - nums[i]]]
        return []