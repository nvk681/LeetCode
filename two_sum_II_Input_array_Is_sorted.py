class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers)-1
        while end > start:
            result = numbers[start]+numbers[end]
            if result == target:
                return [start+1, end+1]
            if result < target:
                start += 1
            if result > target:
                end -= 1
        return []