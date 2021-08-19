class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.length();
        if(n<=1){
            return s;
        }
        int dp[n][n];
        int st,en;
        st = en = 0;
        for(int i=0;i<n;i++)
            for(int j=0;j<n;j++)
                if(i==j)
                    dp[i][j] = 1;
                else
                    dp[i][j] = 0;
            
        for(int i=0;i<n-1;i++)
            if(s[i] == s[i+1]){
                dp[i][i+1] = 2;
                st = i;
                en = i+1;
            }
        
        
        for(int i=2; i<n ;i++){
            for(int j=0;j<n-i;j++){
                if(s[j]==s[j+i] && dp[j+1][j+i-1] > 0)
                    dp[j][j+i] = 2 + dp[j+1][j+i-1];
                else
                    dp[j][j+i] = 0;
                
                if(dp[j][j+i] > dp[st][en]){
                    st = j;
                    en = j+i;
                }
                //dp[j][j+i] = 1;
                    
            }
        }
        
        /*for(int i=0;i<n;i++){
            for(int j=0;j<n;j++)
                cout<<dp[i][j]<<' ';
            cout<<endl;
        }*/

        
        return s.substr(st, (en-st+1));
    }
};
