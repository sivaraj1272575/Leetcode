class Solution:
    def countAndSay(self, n: int) -> str:
        def count1(val):
            d = dict()
            order = []
            i=0
            temp = 0
            newstring=""
            while i<len(val):
                temp = 0
                s = val[i]
                while i<len(val) and s==val[i]:
                    temp+=1
                    i+=1
                newstring += str(temp)+s
            return newstring
        ans="1"
        for i in range(2,n+1):
            ans = count1(ans)
        return ans
