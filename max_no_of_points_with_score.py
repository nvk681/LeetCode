def find_max(values, row, col):
    if row >= len(values):
        return 0
    max_value = 0
    for i in range(len(values[row])):
        current = (values[row][i])-abs(i-col)+find_max(values, row+1, i)
        max_value = current if max_value is None or max_value < current else max_value
    return max_value

class Solution:
    def maxPoints(self, points) -> int:
        max_value = None
        for i in range(len(points[0])):
            current = points[0][i]+find_max(points, 1, i)
            max_value = current if max_value is None or max_value < current else max_value
        return max_value

s = Solution()
print(s.maxPoints([[1,2,3],[1,5,1],[3,1,1]]))