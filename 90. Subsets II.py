class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(arr,lst,start,n):
            nonlocal ans
            ans.append(lst)
            for i in range(start,n):
                if i!=start and arr[i] == arr[i-1]:
                    continue
                backtrack(arr,lst+[arr[i]],i+1,n)
        
        nums.sort()
        backtrack(nums,[],0,len(nums))
        print(ans)
        return ans
