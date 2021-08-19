class Solution {
public:
    int maxCoins(vector<int>& nums) {
        int n = nums.size() + 2;
        if(n == 0)
            return 0;
        int dp[n][n];

        nums.push_back(1);
        nums.push_back(0);
        
        for(int i=n-1; i>0; i--){
            nums[i] = nums[i-1];
        }
        nums[0] = 1;
        
        for(int i=0; i<n; i++)
            for(int j=0; j<n; j++)
                dp[i][j] = 0;
        
        for(int size = 1; size < n-1; size++){
            for(int start = 1;start<n-size; start ++){
                int end = start + size - 1;
                for(int k = start; k<=end; k++){
                    dp[start][end] = max(dp[start][end] , dp[start][k-1] + dp[k+1][end] + nums[start-1]*nums[end+1]*nums[k]);
                }
            }
        }
        
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++)
                cout<<dp[i][j]<<'\t';
            cout<<endl;
        }
        return dp[1][n-2];
    }
};
