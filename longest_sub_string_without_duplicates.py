class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        l = list(s)
        temp = list()
        max_lenght = 0
        for i in l:
            if i in temp:
                current_lenght = len(temp)
                max_lenght = max_lenght if current_lenght < max_lenght else current_lenght 
                while i in temp:
                    temp.pop(0)
                temp.append(i)
            else : 
                temp.append(i)
        return max_lenght

s = Solution()
s.lengthOfLongestSubstring("aq")