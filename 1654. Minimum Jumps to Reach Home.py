class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, target: int) -> int:
        forbidden = set(forbidden)
        pos = 0
        q = [(0, '')]
        ans = 0
        while q:
            size = len(q)
            # if(ans == 121):
            #     print(q)
            for i in range(size):
                pos, dirs = q.pop(0)
                if pos == target:
                    return ans
                x, y = pos + a, pos - b
                if x not in forbidden and x <= 100000 and x >= 0:
                    forbidden.add(x)
                    q.append((x, 'f'))
                if dirs != 'b' and y not in forbidden and y >= 0:
                    # forbidden.add(y)
                    q.append((y, 'b'))
            ans += 1
        return -1 
