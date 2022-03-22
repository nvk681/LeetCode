class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""
        if len(strs) == 1: return strs[0]
        
        strs.sort()
        first = strs[0]
        last = strs[-1]
        
        if last == first: return last
        if len(first) == 0: return ""
        if first[0] != last[0]:
            return ""
        lenght = 0
        while lenght < len(first) and lenght < len(last) and first[lenght] == last[lenght]:
            lenght += 1
        
        return first[:lenght]