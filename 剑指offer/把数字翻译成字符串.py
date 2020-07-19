时间复杂度：O(N)
空间复杂度：O(N)

class Solution:
    def translateNum(self, num: int) -> int:
        a, b = 1, 1
        s = str(num)
        for i in range(2, len(s)+1):
            a, b = (a+b if '10'<= s[i-2:i]<='25' else a), a
        
        return a
