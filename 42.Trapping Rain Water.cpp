class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        if(n <= 2)
            return 0;
        
        int left[n], right[n];
        
        left[0] = -1;
        right[n-1] = -1;
        
        for(int i=n-2; i>=0; i--)
            right[i] = max(right[i+1], height[i+1]);
        
        for(int i=1; i<n; i++)
            left[i] = max(left[i-1], height[i-1]);
        
       
        
        int ans = 0;
        for(int i=0; i<n; i++){
            if(left[i] > 0 && right[i] > 0){
                int mn = min(left[i], right[i]);
                if(mn - height[i] > 0)
                    ans += mn-height[i];
            }
        }
        return ans;
        
    }
};
