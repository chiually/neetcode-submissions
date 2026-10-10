class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        # find which row the target is in
        row = None
        while top <= bottom:
            # get middle row
            mid = (top + bottom) // 2

            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                bottom = mid - 1
            else: 
                top = mid + 1

        row = matrix[min(top, bottom)]

        # search the row for the target
        while left <= right:
            # get middle row
            mid = (left + right) // 2

            if row[mid] == target:
                return True
            elif row[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False

        