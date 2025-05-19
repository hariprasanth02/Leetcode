class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []
        m=len(matrix)
        n=len(matrix[0])
        transposed_matrix = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                transposed_matrix[j][i]=matrix[i][j]
        return transposed_matrix

        