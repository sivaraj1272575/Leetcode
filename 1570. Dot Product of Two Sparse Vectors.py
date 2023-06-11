class SparseVector:
    def __init__(self, nums: List[int]):
        self.num = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        if len(self.num) == len(vec.num):
            for i in range(len(self.num)):
                ans += self.num[i]*vec.num[i]
        return ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
