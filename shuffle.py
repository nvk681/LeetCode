import random

class Solution:

    def __init__(self, nums):
        self.nums = nums

    def reset(self):
        return list(self.nums)

    def shuffle(self):
        temp = list(self.nums)
        for i in range(len(temp)):
            index = random.randrange(i, len(temp))
            temp[index], temp[i] = temp[i], temp[index]
        return temp


# Your Solution object will be instantiated and called as such:
obj = Solution([1, 2, 3])
param_1 = obj.reset()
param_2 = obj.shuffle()