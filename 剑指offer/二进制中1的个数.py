# 看到这道题首先想到的就是位运算，因为位运算要比加减乘除计算的都快
# 时间复杂度 O(log2N)
# 空间复杂度 O(1)

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n&1
            n >>= 1
        return res
