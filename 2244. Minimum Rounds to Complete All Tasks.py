class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        d = dict()
        for i in tasks:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        ans = 0
        for i in d:
            if d[i] == 1:
                return -1
            if d[i] % 3 == 0:
                ans += d[i] // 3
            else:
                ans += (d[i] // 3 + 1)
         return ans
      
