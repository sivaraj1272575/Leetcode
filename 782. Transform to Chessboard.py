class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        N = len(board)
        no_of_ones_row, no_of_ones_col = 0, 0
        col_moves, row_moves = 0, 0
        
        for i in range(N):
            for j in range(N):
                if (board[0][0] ^ board[i][0]) ^ (board[i][j] ^ board[0][j]) == 1:
                    return -1
        
        for i in range(N):
            no_of_ones_row += board[0][i]
            no_of_ones_col += board[i][0]
            
            if board[i][0] == i%2:
                row_moves += 1
            if board[0][i] == i%2:
                col_moves += 1
        
        if no_of_ones_row <N//2 or no_of_ones_row > (N+1)//2:
            return -1
        if no_of_ones_col <N//2 or no_of_ones_col > (N+1)//2:
            return -1
        
        if N%2 == 1:
            if col_moves % 2 == 1:
                col_moves = N - col_moves
            if row_moves % 2 == 1:
                row_moves = N - row_moves
        else:
            col_moves = min(col_moves, N-col_moves)
            row_moves = min(row_moves, N-row_moves)
        
        return (row_moves + col_moves)//2
