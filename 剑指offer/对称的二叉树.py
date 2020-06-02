‘’‘
’‘’
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        first = []
        second = []
        
        def first(root):
            if root:
                first.append(root.val)
                first(root.left)
                second(root.right)
            else:
                first.append([])
            return first
        
        def second(root):
            if root:
                second.append(root.val)
                second(root.right)
                second(root.left)
            else:
                second([])
            return second

        return first(root) == second(root)
            
