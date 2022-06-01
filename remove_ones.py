class Solution:
    def removeOnes(self, grid) -> bool:
        row, col = len(grid), len(grid[0])
        for i in range(row):
            if grid[i][0] == 1:
                for j in range(col):
                    grid[i][j] = abs(1-grid[i][j])
        for j in range(col):
            if grid[0][j] == 1:
                for i in range(row):
                    grid[i][j] = abs(1-grid[i][j])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return False
        return True


s = Solution()
print(s.removeOnes([[0,1,0],[1,0,1],[0,1,0]]))
print(s.removeOnes([[1,1,0],[0,0,0],[0,0,0]]))
print(s.removeOnes([[0]]))