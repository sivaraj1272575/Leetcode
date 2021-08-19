class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i=0
        while(i<len(nums) and nums[i]!=target):
            i+=1
        if(i>=len(nums)):
            return [-1,-1]
        else:
            j=i+1
            while(j<len(nums) and nums[j]==target ):
                j+=1
            return [i,j-1]
