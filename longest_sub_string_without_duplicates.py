class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result, value, temp = 0, 0, []
        for i in s:
            if i in temp:
                result = result if result > value else value
                temp.append(i)
                temp = temp[temp.index(i)+1:]
                value = len(temp)
            else:
                temp.append(i)
                value += 1
        result = result if result > value else value
        return result


s = Solution()
print(s.lengthOfLongestSubstring("aq"))
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
