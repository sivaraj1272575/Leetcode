class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int diff = INT_MAX, num = 0;
        int j, k, threesum;
        int n = nums.size();
        for(int i=0;i<n;i++){
            j = i+1;
            k = n-1;
            while(j < k){
                threesum = nums[i] + nums[j] + nums[k];
                if(abs(target-threesum) < diff){
                    diff = abs(target-threesum);
                    num = threesum;
                }
                if(threesum > target){
                    k --;
                }
                else{
                    j ++;
                }
            }
        }
        return num;
    }
};
