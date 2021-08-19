class Solution {
public:
    int longestValidParentheses(string s) {
        //Approach-1
        /*stack<int> stack;
        stack.push(-1);
        int mx = 0;
        for(int i=0;s[i];i++){
            if(s[i]=='(')
                stack.push(i);
            else{
                stack.pop();
                if(stack.empty())
                    stack.push(i);
                else
                    mx = max(mx, abs(i-stack.top()));
            }
        }
        return mx;*/
        int o,c,mx;
        o = c = mx = 0;
        for(int i=0;s[i];i++){
            if(s[i]=='(')
                o+=1;
            else
                c+=1;
            if(o == c)
                mx = max(mx, o+c);
            else if(c>o)
                c = o = 0;
        }
        c = o = 0;
        for(int i=s.length()-1;i>=0;i--){
            if(s[i]=='(')
                o+=1;
            else
                c+=1;
            if(o==c)
                mx = max(mx, o+c);
            else if(o>c)
                c = o = 0;
        }
        return mx;
    }
};
