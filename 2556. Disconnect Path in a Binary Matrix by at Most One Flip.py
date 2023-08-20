class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        self.dirs = [(0, 1), (0,-1), (1,0),(-1,0)]
        self.m = len(grid)
        self.n = len(grid[0])

        def dfs(i, j, dist):
            if i<0 or j<0 or i>=self.m or j>=self.n or grid[i][j] == 0:
                return False
            if i == dist[0] and j == dist[1]:
                return True
            grid[i][j] = 0

            return dfs(i, j+1, dist) or dfs(i+1, j, dist)
        
        path1 = dfs(0, 0, (self.m-1, self.n-1))
        grid[0][0] = 1
        grid[self.m-1][self.n-1] = 1
        path2 = dfs(0, 0, (self.m-1, self.n-1))

        return True if (path1 == False or path2 == False) else False
