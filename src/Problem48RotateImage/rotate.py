from typing import List


class Solution:
    def __init__(self, matrix):
        self.matrix = matrix
        pass

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        i = 0
        j = 0
        tmp1 = matrix[(n-1)-j][i]

        counter = 0
        while counter < n**2:
            matrix[i][j] = matrix[(n-1)-j][i] if counter == 0 else tmp2
            print(f"at {i},{j} matrix[{i}][{j}] is {matrix[i][j]}")
            tmp2 = matrix[i][j]

            tmp_i = i
            i = j
            j = (n-1)-tmp_i
            counter += 1
        return


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
solution = Solution(matrix)
solution.rotate(matrix)
print(solution.matrix)

matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
solution = Solution(matrix)
solution.rotate(matrix)
print(solution.matrix)
