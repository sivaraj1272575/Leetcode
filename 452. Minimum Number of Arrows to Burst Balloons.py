class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
		if(len(points) <= 1):
			return len(points)
		first = True
		points = sorted(points)
		mn = mx = 0
		for i in points:
            # print(mn, mx, sep=' ')
            if mn> i[0] and mx<i[1]:
                continue
            elif mn<=i[0] and mx>=i[1] and not first:
                mn = i[0]
                mx = i[1]
            elif mx>=i[0] and mx<=i[1] and not first:
                mn = i[0]
            elif mn>=i[0] and mn<=i[1] and not first:
                mx = i[1]
            else:
                ans += 1
                mn = i[0]
                mx = i[1]
                first = False
        
        return ans
