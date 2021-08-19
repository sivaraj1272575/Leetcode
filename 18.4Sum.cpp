class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector< vector<int>> ans;
        
        if(nums.size() == 0)
            return ans;
        sort(nums.begin(), nums.end());
        
        int n = nums.size();
        
        int i, j, k, l, rem;
        for(i=0; i<n; i++){
            for(j=i+1; j<n; j++){
                rem = target - (nums[i] + nums[j]);
                cout << rem <<' ';
                k = j+1;
                l = n-1;
                while(k < l){
                    if(nums[k] + nums[l] < rem)
                        k ++;
                    else if(nums[k] + nums[l] > rem)
                        l --;
                    else{
                        vector<int> temp;
                        
                        temp.push_back(nums[i]);
                        temp.push_back(nums[j]);
                        temp.push_back(nums[k]);
                        temp.push_back(nums[l]);
                        
                        while(k<l && temp[3] == nums[l])
                            l--;
                        while(k<l && temp[2] == nums[k])
                            k++;
                        ans.push_back(temp);
                    }
                    
                }
                while(j+1<n && nums[j] == nums[j+1])
                    j++;
            }
            while(i+1<n && nums[i] == nums[i+1])
                i++;
        }
        
        return ans;
        
    }
};
