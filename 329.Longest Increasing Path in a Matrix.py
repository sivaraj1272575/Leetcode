class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.ans = 0
        def dfs(i,j):
            if self.dp[i][j]!=0:
                return self.dp[i][j]
            mx = 0
            for k in self.direction:
                x = i+k[0]
                y = j+k[1]
                if x>=0 and y>=0 and x<self.n and y<self.m and self.matrix[i][j]<self.matrix[x][y]:
                    val = dfs(x, y)
                    mx = max(mx, val)
            self.dp[i][j] = mx+1
            return self.dp[i][j]
            
        self.matrix = matrix    
        self.direction = [[-1, 0], [0, -1], [1, 0], [0, 1]]    
        self.n = len(matrix)
        self.m = len(matrix[0])
        self.dp = [[0 for i in range(self.m)] for j in range(self.n)]
        mx = 0
        for i in range(self.n):
            for j in range(self.m):
                mx = max(mx, dfs(i, j))
        return mx

        
