'''
这道题是leetcode136题的变体，考点是位运算。
在那道题的基础上，有加一位数字，这就需要我们再进一次分组，这样分别找出这两个数字
'''

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        # 这里x代表的是第一轮两个只出现一次的数字的异或，a和b分别表示只出现一次的数字。
        mix_, num1, num2 = 0,0,0
        for num in nums:
            mix_ ^= num
        
        #找到两个只出现一次的数字第一次出现不同的位。因为两个数字之后不同的位，才会是1。因此和1做与运算。结果为1就说明不相同    
        div = 1    
        while not mix&div:
          div <<= 1
        
        #我们按照两个只出现一次的数字不同的那位，进行分组，分别找出相应的数字
        for num in nums:
          if num&div:
             num1 ^= num
          else:
             num2 ^= num
        return [num1, num2]
        
        
        
            
