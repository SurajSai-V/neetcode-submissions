class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen = set()
            for j in range(9):
                c = board[i][j]
                if c == ".":
                    continue
                elif c in seen:
                    return False
                seen.add(c)
        for i in range(9):
            seen = set()
            for j in range(9):
                c = board[j][i]
                if c == ".":
                    continue
                elif c in seen:
                    return False
                seen.add(c)
        for x in range(0,9,3):
            for y in range(0,9,3):
                seen = set()
                for i in range(x,x+3):
                    for j in range(y,y+3):
                        if board[i][j] ==".":
                            continue
                        elif board[i][j] in seen:
                            return False
                        seen.add(board[i][j])
        return True