# 青蛙跳台阶的问题本质上就是斐波那契数列问题
# 因为求青蛙在第三个台阶的时候，我们可以想象成青蛙在第二个台阶和青蛙在第一个台阶的情况 即 f(n)=f(n-1)+f(n-2)
# 所以解法与菲波那切数列的解法相同
# 时间复杂度： O(n)
# 空间复杂度： O(1)

class Solution:
    def numWays(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n):
          a, b = b, a+b
        
        return a % 1000000007
