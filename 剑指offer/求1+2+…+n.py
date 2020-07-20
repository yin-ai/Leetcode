class Solution:
    def sumNums(self, n: int) -> int:
        sum_ = 0
        def helper(sum_, n):
            if n == 0: return sum_
            sum_ += n
            return helper(sum_, n-1)
        return helper(sum_, n)
