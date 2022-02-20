from collections import Counter 

def deleteAndEarn(nums):
        nums_counter = Counter(nums)
        prev = -1
        avoid = using = 0
        for i in sorted(nums_counter):
            if i - 1 != prev:
                avoid, using = max(avoid, using), i * nums_counter[i] + max(avoid, using)
            else:
                avoid, using = max(avoid, using), i*nums_counter[i]+avoid
            prev = i
        return max(avoid, using)

# def deleteAndEarn(nums):
#         nums = collections.Counter(nums)
#         usage , avoid =  0, 0
#         previous = None
#         for index in sorted(nums):
#             if previous == index - 1:
#                 avoid, usage = max(usage, avoid), avoid+index*nums[index]
#             else: 
#                 avoid, usage = max(usage, avoid), max(avoid, usage)+index*nums[index]
#             previous = index
#         return max(avoid, usage)
# print(deleteAndEarn([3,1]))
# print(deleteAndEarn([3,4,2]))
# print(deleteAndEarn([2,2,3,3,3,4]))
print(deleteAndEarn([1,6,3,3,8,4,8,10,1,3]))