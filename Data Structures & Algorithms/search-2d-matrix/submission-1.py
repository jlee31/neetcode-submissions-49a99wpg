class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        numRows = len(matrix[0])
        numCols = len(matrix)
        # second sol will use binary search 
        # since we know its sorted
        for i in range(numCols):
            if target in matrix[i]:
                return True
        return False