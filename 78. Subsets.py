class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return [[]]
        if len(nums)==1:
            return [[],nums]
        ans = [list()]
        print(ans)
        n =1
        for i in nums:
            count = n
            for j in range(n):
                s = ans[j].copy()
                s.append(i)
                print(s)
                ans.append(s.copy())
                count+=1
            n=count
        return ans
