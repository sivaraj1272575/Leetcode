class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        low, high = 1, max(candies)
        ans = low

        def canAllocate(n):
            temp = 0
            for i in candies:
                temp += i//n
                if temp >= k:
                    return True
            
            return False
        
        while low <= high:
            mid = (low + high) //2
            if canAllocate(mid):
                ans = max(ans, mid)
                low = mid + 1
            else:
                high = mid - 1
        
        return ans
