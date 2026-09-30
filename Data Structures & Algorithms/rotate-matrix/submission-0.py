class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r # since n x n matrix

                # save top left variable
                temp = matrix[top][l + i]

                # reverse order of rotation so only one temp variable 
                matrix[top][l + i] = matrix[bottom - i][l]

                matrix[bottom - i][l] = matrix[bottom][r - i]

                matrix[bottom][r - i] = matrix[top + i][r]

                matrix[top + i][r] = temp

            l += 1
            r -= 1

        