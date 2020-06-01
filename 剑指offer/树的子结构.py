‘’‘
这个题也是采用递归的手法
时间复杂度为：O(MN) (其中M是A的节点数量，N是B节点的数量)
空间复杂度为：O(M)
’‘’
class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def helper(A, B):
          if not B: return True
          if not A or A.val != B.val: return False
          return helper(A.left, B.left) and helper(A.right, B.right)
          
        if not A or not B: return False
        if helper(A, B): return True
        return self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
          
        
