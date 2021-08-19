class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        job = list(zip(startTime, endTime, profit))
        job.sort(key = lambda x:x[1])
        
        n = len(job)
        dp = [0 for i in range(n)]
        dp[0] = job[0][2]
        
        for i in range(1, n):
            k = 0
            for j in range(i-1, -1, -1):
                if job[j][1] <= job[i][0]:
                    k = dp[j]
                    break
            dp[i] = max(dp[i-1], k + job[i][2])
        
        return dp[-1]
