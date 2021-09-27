class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        if m == 1 and n == 1:
            return 0
        visited = [[[0 for i in range(k+1)]for j in range(n)] for i in range(m)]
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        q = [[0, 0, k]]
        visited[0][0][k] = 1
        step = 0
        while q:
            k = len(q)
            for i in range(k):
                [cur_x, cur_y, cur_k] = q.pop(0)
                for x,y in dirs:
                    new_x, new_y = cur_x+x, cur_y+y
                    if 0<=new_x < m and 0<=new_y < n:
                        if new_x == m-1 and new_y==n-1:
                            return step+1
                        if(grid[new_x][new_y] == 1 and cur_k > 0 and visited[new_x][new_y][cur_k-1] == 0):
                            q.append([new_x, new_y, cur_k-1])
                            visited[new_x][new_y][cur_k-1] = 1
                        elif(grid[new_x][new_y] == 0 and visited[new_x][new_y][cur_k] == 0):
                            q.append([new_x, new_y, cur_k])
                            visited[new_x][new_y][cur_k] = 1
            step += 1
        return -1
                        
