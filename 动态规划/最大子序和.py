'''
时间复杂度：O(n)
空间复杂度：O(n)
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = [0]*len(nums)
        dp[0] = nums[0]
        max_ = nums[0]
        for i in range(1, len(nums)):
            if dp[i-1] < 0:
                dp[i] = nums[i]
            else:
                dp[i] = nums[i]+dp[i-1] 
            if max_ < dp[i]:
                max_ = dp[i]

        return max_
