class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=1:
            return 0
        dp = [-1]*n
        dp[0] = 0
        for i in range(0,n):
            j = i+1
            while j<n and j<=nums[i]+i:
                if dp[j] == -1:
                    dp[j] = dp[i]+1
                else:
                    dp[j] = min(dp[j], dp[i]+1)
                j+=1
        return dp[n-1]
