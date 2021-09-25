class Solution:
    def numTrees(self, n: int) -> int:
        k = 2*n+1
        dp = [0 for i in range(k)]
        dp[0] = 1
        for i in range(1,k):
            dp[i] = dp[i-1]*i
        print(dp)
        return dp[2*n]//(dp[n]*dp[n+1])
