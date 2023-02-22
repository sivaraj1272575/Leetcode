class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if(len(piles) == h):
            return max(piles)
        low, high = 1, max(piles)
        ans = high

        def canEat(speed):
            temp = 0
            for i in piles:
                temp += math.ceil(i/speed)
                if temp > h:
                    return False
            
            return True


        while low <= high:
            speed = (low + high) // 2
            if canEat(speed):
                ans = min(ans, speed)
                high = speed - 1
            else:
                low = speed + 1
        
        return ans
