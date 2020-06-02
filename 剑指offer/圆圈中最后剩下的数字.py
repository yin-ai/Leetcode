'''
这道题首先我感觉使用栈来解决，但是复杂度有些高，容易造成超时。因此这道题得用公式法。
公式法：实现应该使用倒推的形式去解决这个问题
时间复杂度：O(n)
空间复杂度：O(1)
''‘
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        # if n=0. then f = 0
        f = 0
        for i in range(2, n+1):
            f = (f+m)%i
        return f
