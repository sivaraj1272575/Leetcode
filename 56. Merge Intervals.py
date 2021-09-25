class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def merge(low,mid,high,intervals):
            l = low
            m = mid+1
            arr = []
            while l<=mid and m<=high:
                if intervals[l][0]<intervals[m][0]:
                    arr.append(intervals[l])
                    l+=1
                else:
                    arr.append(intervals[m])
                    m+=1
            while l<=mid:
                arr.append(intervals[l])
                l+=1
            while m<=high:
                arr.append(intervals[m])
                m+=1
            k = 0
            for i in range(low,high+1):
                intervals[i]=arr[k]
                k+=1
                
        
        def mergesort(l,h,intervals):
            if l<h:
                m = (l+h)//2
                mergesort(l,m,intervals)
                mergesort(m+1,h,intervals)
                merge(l,m,h,intervals)
        
        n = len(intervals)
        
        if n==0:
            return []
        mergesort(0,n-1,intervals)
        stack = []
        stack.append(intervals[0])
        for i in range(1,n):
            if stack[-1][1]>=intervals[i][0]:
                stack[-1][1] = max(stack[-1][1],intervals[i][1])
            else:
                stack.append(intervals[i])
        return stack
            
