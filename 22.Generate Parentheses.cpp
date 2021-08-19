class Solution {
public:
    
    vector<string> ans;
    
    void helper(string s, int l, int r, int n){
        if(l == n && r== n){
            ans.push_back(s);
        }
        if(l < n){
            helper(s+'(', l+1, r, n);
        }if(r < l){
            helper(s+')', l, r+1, n);
        }
    }
    
    vector<string> generateParenthesis(int n) {
        helper("", 0, 0, n);
        return ans;
    }
};
