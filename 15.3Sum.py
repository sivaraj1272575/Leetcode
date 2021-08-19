class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(0,n):
            low = i+1
            high = n-1
            while low<high:
                if sum([nums[i],nums[low],nums[high]])<0:
                    low+=1
                elif sum([nums[i],nums[low],nums[high]])>0:
                    high-=1
                else:
                    if [nums[i],nums[low],nums[high]] not in ans:
                        ans.append([nums[i],nums[low],nums[high]])
                    low+=1
                    high-=1
        print(ans)
        return(ans)
