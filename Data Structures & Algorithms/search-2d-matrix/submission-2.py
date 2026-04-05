class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        numCols = len(matrix[0])
        numRows = len(matrix)
        # first lets write the brute force
        for row in range(numCols):
            for col in range(numRows):
                if matrix[col][row] == target:
                    return True
        return False

        # time is o(n * m)
        # space is o(1)