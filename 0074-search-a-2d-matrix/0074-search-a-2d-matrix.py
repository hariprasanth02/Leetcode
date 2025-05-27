from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:  # Handle empty matrix case
            return False

        m, n = len(matrix), len(matrix[0])  # Number of rows and columns
        left, right = 0, m * n - 1  # Treat matrix as a virtual 1D sorted array

        while left <= right:
            mid = (left + right) // 2
            row, col = divmod(mid, n)  # Corrected divisor to `n` (number of columns)

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False