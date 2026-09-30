class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # flag for first row needing to be zeroed
        rowZero = False

        # num of columns, num of rows
        COL, ROW = len(matrix[0]), len(matrix)

        for i in range(ROW):
            for j in range(COL):
                if matrix[i][j] == 0:
                    if i == 0:
                        rowZero = True
                        break

                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # zero flagged rows
        for i in range(1, ROW):
            if matrix[i][0] == 0:
                matrix[i] = [0] * COL

        # zero flagged columns
        for j in range(COL):
            if matrix[0][j] == 0:
                for i in range(ROW):
                    matrix[i][j] = 0

        # now can zero out first row since columns zeroed
        matrix[0] = [0] * COL if rowZero else matrix[0]
