class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        arr_sum = 0
        mx_temp, mx = 0, -100000
        mn_temp, mn = 0, 100000
        
        for i in nums:
            arr_sum += i
            
            mx_temp += i
            mn_temp += i
            
            mx = max(mx, mx_temp)
            mn = min(mn, mn_temp)
            
            mx_temp = max(mx_temp, 0)
            mn_temp = min(mn_temp, 0)
        
        if mn == arr_sum:
            return mx
        else:
            return max(mx, arr_sum-mn)
        
