

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        # for i in range(len(nums)):
            # hashmap[nums[i]] = i    
        for i in range(len(nums)):
                need = target - nums[i]
                if need in hashmap and hashmap[need] != i:
                    return [i, hashmap[need]]
                hashmap[nums[i]] = i 