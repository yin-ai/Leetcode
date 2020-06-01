'''
这是一道简单的二叉树遍历问题
时间复杂度：O(N) 树的节点数
空间复杂度：O(D) 树的深度 
'''

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root: return
        
        root.left, root.right = root.right, root.left
        self.mirrorTree(root.left)
        self.mirrorTree(root.right)
        
        return root
