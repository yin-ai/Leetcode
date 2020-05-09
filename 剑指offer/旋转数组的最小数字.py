# 这道题其实使用常规遍历并不难，难点就是将复杂度降低。
# 因为这道题题目是半排序数组，所以联想到的就是二分法。这样
# 时间复杂度 O(logN)
# 空间复杂度 O(1)

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        l, r = 0, len(numbers)-1
        while l<r:
            # 使用位操作更快
            mid = (l+r) >> 1
            # 不能把中间值和左面的进行比较，这样可能会导致比较无效
            if numbers[mid] > numbers[r]: l = mid+1
            elif numbers[mid] < numbers[r]: r = mid
            else: r -= 1
            
        # l <= mid < r
        return numbers[l]
