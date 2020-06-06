'''
这个题的解题点就是对二叉树使用回溯法
首先想的是如何对二叉树进行遍历，其次是如何保留路径

对于回溯法的步骤：
  首先是参数：哪些参数递归
  其次是：终止条件
  然后是：递推关系
'''
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def helper(root, sum):
            if not root: return
            path.append(root.val)
            sum -= root.val
            if sum == 0 and not root.left and not root.right:
                res.append(list(path))
            helper(root.left, sum)
            helper(root.right, sum)
            path.pop()
        path, res = [], []
        helper(root, sum)
        return res
        
