class Solution:
    def maxSatisfaction(self, s: List[int]) -> int:
        n = len(s)
        if(n < 1) :
            return 0
        s.sort(reverse = True)
        print(s)
        prefix = 0
        ans = 0
        for i in range(0, n):
            prefix += s[i]
            if prefix > 0:
                ans += prefix
            else:
                break
        
        return ans
