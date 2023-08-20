class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        self.dirs = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        def bfs(i):
            temp = [[0 for i in range(col)] for j in range(row)]
            visited = set()
            for j in range(i):
                temp[cells[j][0]-1][cells[j][1]-1] = 1
            q = []
            for j in range(col):
                if temp[0][j] == 0:
                    q.append((0, j))
                    visited.add((0, j))
            
            while q:
                ele = q.pop(0)
                if ele[0] == row - 1:
                    return True
                for dirs in self.dirs:
                    x, y = dirs[0] + ele[0], dirs[1] + ele[1]
                    if x >= 0 and x<row and y >= 0 and y<col and (x,y) not in visited and temp[x][y]==0:
                        q.append((x, y))
                        visited.add((x, y))
            return False
        
        left, right = 0, len(cells)
        res = -1
        while (left <= right):
            mid = (left + right) //2
            if bfs(mid):
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res
