class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1  
        if n < 0:
            x = 1 / x
            n = -n
        power_one = self.myPow(x, n // 2)
        return power_one * power_one if n % 2 == 0 else x * power_one * power_one