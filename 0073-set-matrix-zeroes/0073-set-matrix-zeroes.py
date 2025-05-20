class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        col = len(matrix[0])
        row_zero = any(matrix[0][j] == 0 for j in range(col))
        col_zero = any(matrix[i][0] == 0 for i in range(row))
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:   
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, row):
            if matrix[i][0] == 0:
                for j in range(col):
                    matrix[i][j] = 0

        for j in range(1, col):
            if matrix[0][j] == 0:
                for i in range(row):
                    matrix[i][j] = 0
        if row_zero:
            for j in range(col):
                matrix[0][j] = 0
        if col_zero:
            for i in range(row):
                matrix[i][0] = 0

        
       