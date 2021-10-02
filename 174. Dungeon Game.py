class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0][0] = dungeon[0][0]
        
        if(dungeon[m-1][n-1] > 0):
            dp[m-1][n-1] = 0
        else:
            dp[m-1][n-1] = dungeon[m-1][n-1]
        
        for i in range(n-2, -1, -1):
            dp[m-1][i] = dungeon[m-1][i] + dp[m-1][i+1]
            if dp[m-1][i] > 0:
                dp[m-1][i] = 0
            
        for i in range(m-2, -1, -1):
            dp[i][n-1] = dungeon[i][n-1] + dp[i+1][n-1]
            if dp[i][n-1] > 0:
                dp[i][n-1] = 0
        
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])+dungeon[i][j]
                if dp[i][j] > 0:
                    dp[i][j] = 0
        
        
        
        # for i in dp:
        #     for j in i:
        #         print(j, end = '\t')
        #     print()
        
        return abs(dp[0][0])+1
