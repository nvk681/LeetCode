class Solution:
    def minCost(self, costs) -> int:
        hash_map = {}
        def cal_culate_cost(index, selection):
            if str(index)+"_"+str(selection) in hash_map: return hash_map[str(index)+"_"+str(selection)]
            if index == len(costs): return 0
            result = float('inf')
            for sub_index in range(len(costs[index])):
                if sub_index != selection:
                    current = costs[index][sub_index]+cal_culate_cost(index+1, sub_index)
                    result = result if result < current else current
            # result = 0
            hash_map[str(index)+"_"+str(selection)] = result#str(index)+"_"+str(selection)
            return result
        
        return cal_culate_cost(0, None)
s = Solution()
print(s.minCost([[17,2,17],[16,16,5],[14,3,19]]))