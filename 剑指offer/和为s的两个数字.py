’‘’
这是一道非常简单的题了。我分别采用了字典和双指针，解决了这道题
’‘’

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums: return []
        dict_ = {}
        for i in nums:
            if i not in dict_:
                dict_[target-i] = i
            else:
                return [i, dict_[i]] 
        return []
                
                
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        if not nums: return []
        
        l, r = 0, len(nums)-1
        while l<r:
            sum_ = nums[l] + nums[r]
            if sum_ == target:
                return [nums[l], nums[r]]
            if sum_ < target: l+=1
            if sum_ > target: r-=1
        return []
