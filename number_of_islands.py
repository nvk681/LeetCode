class Solution:
    def numIslands(self, grid):
        is_land = 0
        list_of_parsing = []
        def dfs(grid):
            while len(list_of_parsing) > 0:
                temp_des = list_of_parsing.pop(0)
                i = temp_des[0]
                j = temp_des[1]
                if i+1 < len(grid) and grid[i+1][j] == "1":
                    grid[i+1][j] = '0'
                    list_of_parsing.append([i+1, j])
                if j+1 < len(grid[i]) and grid[i][j+1] == "1":
                    grid[i][j+1] = '0'
                    list_of_parsing.append([i, j+1])
                if i > 0 and grid[i-1][j] == "1":
                    grid[i-1][j] = '0'
                    list_of_parsing.append([i-1, j])
                if j > 0 and grid[i][j-1] == "1":
                    grid[i][j-1] = '0'
                    list_of_parsing.append([i, j-1])


        for index in range(len(grid)):
            for j_index in range(len(grid[index])):
                if grid[index][j_index] == "1":
                    grid[index][j_index] = '0'
                    list_of_parsing.append([index,j_index])
                    dfs(grid)
                    is_land += 1
        return is_land

