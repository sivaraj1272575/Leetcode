class Solution:
    def totalNQueens(self, n: int) -> int:
        arr = [-1]*n
        def check(k):
            for i in range(k):
                if arr[i]==arr[k] or abs(arr[i]-arr[k]) == abs(i-k):
                    return False
            return True
        
        count = 0
        k=0
        while k>=0:
            arr[k] = arr[k]+1
            while arr[k]<n and check(k)==False:
                arr[k] = arr[k]+1
            if arr[k] <n:
                if k == n-1:
                    count+=1
                else:
                    k = k+1
            else:
                arr[k]=-1
                k-=1
        return count
