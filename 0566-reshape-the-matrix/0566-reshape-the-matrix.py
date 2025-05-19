class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row=len(mat)
        col=len(mat[0])

        if(row*col != r*c):
            return mat

        reshape=[num for row in mat for num in row]
        return [reshape[i*c:(i+1)*c] for i in range(r)]

        