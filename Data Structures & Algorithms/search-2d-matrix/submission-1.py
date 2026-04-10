class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])
        def find_row():
            lo, hi = 0, m-1
            while lo <= hi:
                mid = (lo + hi) //2
                if matrix[mid][0] <= target <= matrix[mid][-1]:
                    return mid
                if matrix[mid][0] > target:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return -1
        row = find_row()
        if row == -1:
            return False
        i, j = 0, n-1
        while i <= j:
            mid = (i+j)//2
            if target == matrix[row][mid]:
                return True
            if target < matrix[row][mid]:
                j = mid- 1
            else:
                i = mid + 1
        return False