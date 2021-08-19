class Solution(object):
    def maxArea(self, height):
        i = 0
        j = len(height)-1
        arr = height
        dist = j-i
        max_area = 0
        while(i<j):
            area = min(arr[j],arr[i])*dist
            if(max_area<area):
                max_area = area
            if arr[i]<arr[j]:
                i+=1
            else:
                j-=1
            dist -=1
        print(max_area)
        return max_area
