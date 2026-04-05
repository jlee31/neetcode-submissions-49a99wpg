class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        numCols = len(matrix[0])
        numRows = len(matrix)
        # ok the proper solution should use binary search
        # sicne we know its sorted
        l = 0
        r = numRows - 1
        theRow = 0

        # gotta identity the possible row its in
        while l < r:
            mid = (l + (r-l)//2)
            if target > matrix[mid][numCols-1]:
                l = mid + 1
                theRow = l
            elif target < matrix[mid][0]:
                r = mid
                theRow = l
            else:
                theRow = mid
                break 
        # now we check if target is there or not
        l = 0
        r = numCols - 1

        while l < r:
            mid = (l + (r-l)//2)
            if target == matrix[theRow][l]:
                return True
            if target > matrix[theRow][mid]:
                l = mid + 1
            else:
                r = mid

        return matrix[theRow][l] == target