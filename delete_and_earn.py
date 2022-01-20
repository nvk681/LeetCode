def del_item(arr, index): 
    item = arr.pop(index)
    if (item+1) in arr: 
        arr.remove(item+1)
    if (item-1) in arr:
        arr.remove(item-1)
    return arr

def deleteAndEarnr(nums):
    if len(nums) == 1:
        return nums[0]
    same_values = all(elem == nums[0] for elem in nums)
    if same_values:
        return sum(nums)
    max_value = 0
    for index in range(len(nums)):
        current_value = nums[index]
        new_array = nums.copy()
        new_array = del_item(new_array, index)
        current_value += deleteAndEarnr(new_array)
        max_value = current_value if current_value > max_value else max_value
    return max_value

print(deleteAndEarnr([3,4,2]))
print(deleteAndEarnr([2,2,3,3,3,4]))
# print(deleteAndEarnr())