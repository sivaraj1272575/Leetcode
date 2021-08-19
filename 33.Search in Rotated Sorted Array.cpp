class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0, h=nums.size()-1;
        int mid;
        
        while(l <= h){
            mid = (l + h)/2;
            if(nums[mid] == target)
                return mid;
            if(nums[mid] >= nums[l]){
                if(target <= nums[mid] && target >= nums[l])
                    h = mid - 1;
                else
                    l = mid + 1;
            }
            else{
                if(target <= nums[h] && target >= nums[mid])
                    l = mid + 1;
                else
                    h = mid - 1;
            }
            
        }
        return -1;
    }
};
