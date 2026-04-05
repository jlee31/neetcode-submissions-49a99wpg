class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        numRows = len(matrix[0])
        numCols = len(matrix)
        # first lets write the brute force
        for row in range(numRows):
            for col in range(numCols):
                if matrix[col][row] == target:
                    return True
        return False