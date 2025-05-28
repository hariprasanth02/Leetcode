class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # if not in matrix then:
        #     return 0
        n=len(matrix)
        # res = [[0]*n  for _ in range(len(matrix[0]))]
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        for row in matrix:
            row.reverse()   
        return matrix