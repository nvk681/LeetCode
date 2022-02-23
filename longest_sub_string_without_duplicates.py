class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        current_lenght, max_lenght = 0, 0
        pool_of_characters = []
        for i in s:
            if i not in pool_of_characters:
                pool_of_characters.append(i)
                current_lenght += 1
            else: 
                if max_lenght < current_lenght:
                    max_lenght = current_lenght
                while i in pool_of_characters:
                    pool_of_characters.pop(0)
                pool_of_characters.append(i)
                current_lenght = len(pool_of_characters)
        return max_lenght if max_lenght > current_lenght else current_lenght


s = Solution()
print(s.lengthOfLongestSubstring("aq"))
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
