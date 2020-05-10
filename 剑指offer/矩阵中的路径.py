'''
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，
每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。
例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。
[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]
但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof
'''
# 这道题看了题解才知道怎么写
# 首先我觉着如果一道题没有好的思路那么就想一想暴力枚举。这道题其实就是在暴力枚举的基础上进行剪枝，即DFS+剪枝 == 回溯
# 确定回溯算法之后需要了解的就是回溯算法的框架：
# 1. 首先想一下边界条件
# 2. 其次想返回条件
# 3. 如何进入下一层
# 4. 回溯（还原， 返回）

# 时间复杂度 O(3^KMN)
# 空间复杂度 O(K)

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            # 边界
            if not 0<=i<len(board) or not 0<=j<len(board[0]) or not board[i][j] == word[k]: return False
            # 终止条件
            if k == len(word)-1: return True
            temp, board[i][j] = board[i][j], '*'
            # 核心
            res = dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or dfs(i, j+1, k+1) or dfs(i, j-1, k+1)
            # 还原
            board[i][j] = temp
            # 返回结果
            return res
            
        # 寻找第一个与word匹配的board[i][j]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0): return True
        
        return False
