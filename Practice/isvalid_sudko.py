from collections import defaultdict
def sudoko(board):

    rows  = defaultdict(set)
    cols = defaultdict(set)
    squares = defaultdict(set)
    for i in range(9) :
        for j in range(9):
            if board[i][j]!= ".":
                if  (board[i][j] not in rows[i]):

                    rows[i].add(board[i][j])  
                else :return False
            
                if(board[i][j] not in squares[i//3,j//3]):
                    squares[i//3,j//3].add(board[i][j])
                else :return False

        
            if board[j][i]!= '.':
                if(board[j][i] not in cols[i]):
                    cols[i].add(board[j][i])
                else: return False

    return True
board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

ans =sudoko(board)

print(ans)