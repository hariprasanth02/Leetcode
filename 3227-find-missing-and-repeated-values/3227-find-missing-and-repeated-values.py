class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
       n=len(grid)
       N = n*n
       exp_sum = (N*(N+1)) //2
       exp_sum_sq = (N*(N+1)*(2*N+1)) // 6
       act_sum = 0
       act_sum_sq = 0
       for row in grid:
        for num in row:
            act_sum += num
            act_sum_sq += num*num
       diff1 = act_sum - exp_sum
       diff2 = act_sum_sq - exp_sum_sq
       sum1 = diff2 // diff1
       a =(sum1+diff1)//2
       b = sum1-a
       return[a,b]
