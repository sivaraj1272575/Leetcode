class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        arr = [-1]*n
        ans = []
        def check(k):
            for i in range(k):
                if arr[k] == arr[i] or abs(i-k)==abs(arr[i]-arr[k]):
                    return False
            return True
        
        k=0
        while k>=0:
            arr[k] = arr[k]+1
            while arr[k]<n and check(k)==False:
                arr[k] = arr[k]+1
            if arr[k] < n:
                if k == n-1:
                    ans.append(arr.copy())
                else:
                    k = k+1
            
            else:
                arr[k] = -1
                k = k-1
        qnlst = []
        for i in ans:
            t = list()
            for j in i:
                s = '.'*j+'Q'+'.'*(n-j-1)
                t.append(s)
            qnlst.append(t)
        return qnlst
