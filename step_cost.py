memory_map = {}
def get_min(array, index):
    if index in memory_map:
        return memory_map[index]
    index_1 = memory_map[index-1] if (index-1) in memory_map else get_min(array, index-1)
    memory_map[index-1] = index_1 
    if index < 2: 
        return index_1
    index_2 = memory_map[index-2] if (index-2) in memory_map else get_min(array, index-2)
    memory_map[index-2] = index_2
    memory_map[index] = array[index]+min(index_1, index_2) if index < len(array) else min(index_1, index_2)
    return memory_map[index]

def minCostClimbingStairs(cost) -> int:
    memory_map.clear()
    memory_map[0] = cost[0]
    memory_map[1] = cost[1]
    return get_min(cost, len(cost))

print(minCostClimbingStairs([0,2,2,1]))