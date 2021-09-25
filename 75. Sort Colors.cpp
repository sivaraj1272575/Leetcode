class Solution {
public:
    void sortColors(vector<int>& nums) {
        int count[3] = {0};
        for(int i=0; i<nums.size(); i++)
            count[nums[i]] += 1;
        
        int j= 0, i=0;
        while(i < 3){
            if(count[i] == 0)
                i+=1;
            else{
                nums[j++] = i;
                count[i] -=1;
            }
        }
        
    }
};
