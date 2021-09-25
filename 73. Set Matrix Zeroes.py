class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        col = list()
        row = list()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if(matrix[i][j]==0):
                    row.append(i)
                    col.append(j)
        for i in row:
            for j in range(len(matrix[i])):
                matrix[i][j] =0
        for i in col:
            for j in range(len(matrix)):
                matrix[j][i] = 0
