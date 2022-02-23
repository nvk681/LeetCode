class Solution:
    def maxArea(self, height) -> int:
        start, end = 0, len(height)-1
        area = 0
        while start != end:
            area = area if area > (min(height[start], height[end]))* (end - start) else (min(height[start], height[end]))* (end - start)
            if height[start] < height[end]:
               start += 1
            else: 
                end -= 1
        return area

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
print(s.maxArea([1,1]))
# print( == s.maxArea())
# print( == s.maxArea())
