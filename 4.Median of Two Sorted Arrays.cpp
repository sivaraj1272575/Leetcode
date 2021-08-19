class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if(nums1.size() > nums2.size())
            return findMedianSortedArrays(nums2, nums1);
        
        int x = nums1.size();
        int y = nums2.size();
        
        int low = 0;
        int high = nums1.size();
        
        int combined = nums1.size() + nums2.size();
        
        while(low <= high){
            int midX = (low + high) / 2;
            int midY = (combined + 1) /2 - midX;
            
            int leftX = (midX == 0) ? INT_MIN : nums1[midX-1];
            int rightX = (midX == x) ? INT_MAX : nums1[midX];
            
            int leftY = (midY == 0) ? INT_MIN : nums2[midY-1];
            int rightY = (midY == y) ? INT_MAX : nums2[midY];
            
            if(leftY <= rightX && leftX<=rightY){
                if(combined%2 == 0)
                    return (double)(max(leftX, leftY) + min(rightX, rightY))/2;
                else
                    return (double)(max(leftX, leftY));
            }
            else if(leftX > rightY)
                high = midX - 1;
            else
                low = midX + 1;
        }
        return 0;
    }
};
