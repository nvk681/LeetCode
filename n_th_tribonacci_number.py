memory_map = {}
def get_value(num):
    if num == 0:
        return 0
    if num in (1,2):
        return 1
    if num in memory_map:
        return memory_map[num]
    memory_map[num] = get_value(num-1)+get_value(num-2)+get_value(num-3)
    return memory_map[num]
class Solution:
    def tribonacci(self, n: int) -> int:
        return get_value(n)