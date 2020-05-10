# 首先想到的就是分治的思想
# 时间复杂度 O(log2N)
# 空间复杂度 O(1)
# 一个数值的整数次方可以分解成 (x^2)^n/2的形式


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0: return 1
        if n<0: x, n = 1/x, -n
        res=1
        while n:
          if n&1: res *= x
          x *= x
          n >>=1
        return res
          
