# 这道题我认为的重点就是list和str的转换
# 时间复杂度O(n)
# 空间复杂度O(n)
class Solution:
    def replaceSpace(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)):
            if s[i] == ' ':
                s[i] = '%20'
        s = "".join(s)
        return s
