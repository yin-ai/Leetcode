'''
这是一道简单的题，但是这道题看了题解才知道要使用双指针。
时间复杂度：O(n)
空间复杂度：O(n)
'''

class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        l, r = 1, 2
        sum_ = 0
        res = []
        list_ = [(i+1) for i in range(target)]
        while l < r and r <= target:
            sum_ = (l+r)*(r-l+1)/2
            if sum_ < target: r+=1
            if sum_ == target:
                res.append(list_[l-1:r])
                l+=1
                r+=1
            if sum_ > target: l+=1
        return  res
