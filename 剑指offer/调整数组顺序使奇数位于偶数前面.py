# 这道题首先就能想到是双指针的问题

# 时间复杂度: O(N)
# 空间复杂度: O(1)

class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums)-1
        while l < r:
            if not nums[l]&1 and nums[r]&1:
                nums[l], nums[r] = nums[r], nums[l]
            if nums[l]&1: l+=1
            if not nums[r]&1: r-=1

        return nums
