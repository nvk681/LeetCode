class Solution:
    def longestIncreasingPath(self, matrix) -> int:
        local_max, global_max = 0,0
        row_limit, col_limit = len(matrix), len(matrix[0])
        def get_lenght(i,j):
            # while
            pass
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                local_max = get_lenght(i,j)
                global_max = global_max if global_max > local_max else local_max
        