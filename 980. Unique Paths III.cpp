class Solution {
public:
    int uniquePathsIII(vector<vector<int>>& grid) {
        int sx, sy, zero = 0;
        for(int i=0; i<grid.size(); i++){
            for(int j=0; j<grid[i].size(); j++){
                if(grid[i][j] == 0)
                    zero += 1;
                if(grid[i][j] == 1){
                    sx = i;
                    sy = j;
                }
            }
        }

        return dfs(grid, sx, sy, zero);
    }

    int dfs(vector<vector<int>> grid, int x, int y, int zero){
        // for(int i=0; i<grid.size(); i++){
        //     for(int j =0; j<grid[0].size(); j++){
        //         cout << grid[i][j];
        //     }
        // }
        if(x < 0 || x >= grid.size() || y<0 || y>=grid[0].size() || grid[x][y]==-1){
            return 0;
        }
        if(grid[x][y] == 2){
            return zero == -1;
        }
        grid[x][y] = -1;
        zero -= 1;
        int paths = dfs(grid, x+1, y, zero) + dfs(grid, x-1, y, zero) + dfs(grid, x, y+1, zero) + dfs(grid, x, y-1, zero);
        grid[x][y] = 0;
        zero += 1;
        return paths;
    }
};
