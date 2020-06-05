'''
这是一道典型的动态规划问题。
动态规划问题的核心内容就是状态转移方程。对于状态转移方程，我们首先要想的就是怎么定义状态。
对于这道回文子串的问题，首先想到的就是表示字符串s[i:j]是否是回文串：
所以这道题初步想到的状态是二维的状态：dp[i][j]。
其次是状态转移：dp[i][j] = dp[i+1][j-1] if s[i]==s[j]
'abaab'
状态转移知道了以后，得知道是如何遍历的, 并且还要首先考虑边界条件
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ''
        res = ''
        max_ = 0
        dp = [[0]*len(s) for _ in range(len(s))]
        for j in range(len(s)):
            for i in range(j+1):
              if s[i] == s[j] and (j-i<2 or dp[i+1][j-1]):
                   dp[i][j] = 1
              if dp[i][j] and max_ < j+1-i:
                  max_ = j+1-i
                  res = s[i:j+1]
        return res
                
