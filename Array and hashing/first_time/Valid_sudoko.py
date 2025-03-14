#we will use hashset
import collections
def valid_sudoko(board):

    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)

    squares = collections.defaultdict(set)   # key in this case is (r/3 , c/3)


    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":

                continue

            if(board[r][c] in rows[r] or 
               board[r][c] in cols[c] or 
               board[r][c] in squares[(r//3,c//3)]):
                
                return False
            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[(r//3, c//3)].add(board[r][c])
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


ans = valid_sudoko(board)
print