class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l = 0
        r = len(matrix[0]) * len(matrix) -1

        while l <= r:

            mid = int((r - l)/2) + l

            row_size = len(matrix[0])

            row = mid // row_size
            column = mid % row_size

            number = matrix[row][column]

            if number == target: return True
            if number < target:
                l = mid+1
            else:
                r = mid-1

        return False
        