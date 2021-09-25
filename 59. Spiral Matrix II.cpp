class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> mat;
        for(int i=0; i<n; i++){
            vector<int> temp(n, 0);
            mat.push_back(temp);
        }
        
        int top=0,down=n-1,left=0,right=n-1;
        int k = 1, dir = 0;
        
        while(top <= down && left <= right){
            if(dir == 0){
                for(int i=left; i<=right; i++){
                    mat[top][i] = k;
                    k+=1;
                }
                top += 1;
            }else if(dir == 1){
                for(int i=top ;i<=down; i++){
                    mat[i][right] = k;
                    k+=1;
                }
                right -= 1;
            }else if(dir == 2){
                for(int i=right; i>=left; i--){
                    mat[down][i] = k;
                    k+=1;
                }
                down -= 1;
            }else{
                for(int i=down; i>=top; i--){
                    mat[i][left] = k;
                    k+=1;
                }
                left += 1;
            }
            dir = (dir + 1)%4;
        }
        return mat;
    }
};
