class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        # index = row * num_cols + col
        for row in range(n):
            s = set()
            # checking row
            for col in range(n):
                if board[row][col] != '.':
                    if board[row][col] in s:
                        return False
                    s.add(board[row][col])

        for col in range(n):
            s2 = set()
            # checking col
            
            for row in range(n):
                if board[row][col] != '.':
                    if board[row][col] in s2: 
                        return False
                    s2.add(board[row][col])
                
        # checking the 9 grids
        for i in range(3):
            for j in range(3):
                s3 = set()
                for row in range(3):
                    for col in range(3):
                        if board[3*i + row][3*j + col] != '.':
                            if board[3*i + row][3*j + col] in s3:
                                return False
                            s3.add(board[3*i + row][3*j + col])

        
        return True #all passes