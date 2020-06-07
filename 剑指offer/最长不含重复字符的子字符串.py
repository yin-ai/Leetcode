‘’‘
这道题是中等难度，本着想用动态规划的思想，但是有一些不一样，最终还看了题解
’‘’


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        dict_ = {}
        cur, max_ = 0, 0
        for i in range(len(s)):
            if s[i] not in dict_ or i-dict_[s[i]] > cur:
                cur+=1
            else:
                cur = i - dict_[s[i]]
            dict_[s[i]] = i
            max_ = max(max_, cur)
            
        return max_
