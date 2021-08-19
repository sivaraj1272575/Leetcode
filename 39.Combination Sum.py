class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(sm,lst,target,given,j):
            if sm==target:
                nonlocal ans
                ans.append(lst.copy())
            for i in range(j,len(given)):
                if sm+given[i] <= target:
                    backtrack(sm+given[i],lst+[given[i]],target,given,i)
        backtrack(0,[],target,candidates,0)
        print(ans)
        return ans
