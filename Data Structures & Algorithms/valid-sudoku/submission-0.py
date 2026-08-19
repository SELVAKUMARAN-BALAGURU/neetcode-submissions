class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            temp = []
            for k in row:
                if k in temp and k!=".":
                    return False
                else:
                    temp.append(k)

        for col in range(9):
            temp = []
            for row in range(9):
                k = board[row][col]
                if k in temp and k!=".":
                    return False
                else:
                    temp.append(k)
        
        for start_row in range(0,9,3):
            for start_col in range(0,9,3):
                temp = []
                for row in range(start_row,start_row+3):
                    for col in range(start_col,start_col+3):
                        k = board[row][col]
                        if k in temp and k!=".":
                            return False
                        else:
                            temp.append(k)
        return True


             
        
        
        