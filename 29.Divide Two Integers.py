class Solution:
    def divide(self, x, y):
        ans = 0
        xx, yy = abs(x), abs(y)
        for i in range(32, -1, -1):
            if xx >= (yy<<i):
                xx -= (yy<<i)
                ans += (1<<i)
        
        if (x>0 and y<0) or (x<0 and y>0): 
            ans = -ans
        
        return min(2**31-1, max(-2**31, ans))
