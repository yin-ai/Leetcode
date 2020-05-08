# 这题的解题思路就是前序遍历的第一个是根节点，巧的是这个根节点正好可以将中序遍历分成：左子树|根节点|右子树
# 更巧的是中序遍历左右子树的个数在前序遍历中是：根节点|左子树|右子树
# 所以这道题采用分治法，将前序和中序分成左子树和右子树分别递归求解
# 时间复杂度 O(n) （采用主定理计算）
# 空间复杂度 O(n)

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 出口
        if not preorder: return
        # 中序遍历中根节点的索引
        index = inorder.index(preorder[0])
        
        head = TreeNode(preorder[0])
        # 分治法将前序和中序分成左子树和右子树分别求解
        head.left = self.buildTree(preorder[1:index+1], inorder[:index])
        head.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        
        return head
