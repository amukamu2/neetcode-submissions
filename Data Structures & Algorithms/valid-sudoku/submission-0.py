class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = len(board)
        col = len(board[0])
        square = {(0,0): set(), (0,1): set(), (0,2): set(), (1,0): set(), (1,1): set(), (1,2): set(), (2,0): set(), (2,1): set(), (2,2): set()}
        for i in range(row):
            ro = set()
            co = set()
            for j in range(col):
                r = board[i][j]
                c = board[j][i]
                if r != ".":
                    if r not in ro:
                        ro.add(r)
                    else:
                        return False
                if c != ".":
                    if c not in co:
                        co.add(c)
                    else:
                        return False
                s_row = int(i/3)
                s_col = int(j/3)
                key = (s_row, s_col)
                if r != ".":
                    if r not in square[key]:
                        square[key].add(r)
                    else:
                        return False
        print(square)
        return True
