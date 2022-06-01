class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = list(nums)
        sorted_nums.sort()
        hash_map = {}
        result = []
        for i in nums:
            if i in hash_map:
                result.append(hash_map[i])
                continue
            temp = 0
            while sorted_nums[temp] < i:
                temp += 1
            hash_map[i] = temp
            result.append(hash_map[i])
        return result