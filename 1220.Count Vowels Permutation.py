class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = [[0 for i in range(5)] for i in range(n)]
        for i in range(5):
            dp[0][i] = 1
        ans = 5
        for i in range(1, n):
            dp[i][0] = dp[i-1][1]
            dp[i][1] = dp[i-1][0] + dp[i-1][2]
            dp[i][2] = dp[i-1][0] + dp[i-1][1] + dp[i-1][3] + dp[i-1][4]
            dp[i][3] = dp[i-1][2] + dp[i-1][4]
            dp[i][4] = dp[i-1][0]
            ans = dp[i][0] + dp[i][1] + dp[i][2] + dp[i][3] + dp[i][4]
        return ((ans)%1000000007)
