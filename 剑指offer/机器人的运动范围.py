# 这里又是一道回溯法的问题
# 在这道题中我总结了这种题的一般解法：
# 一是DFS+剪枝， 二是BFS+剪枝
# 首先第一类算法：
#--------------------
# DFS算法流程(递归方式): 
# 1. 选择递归参数: 首先要判断一道题中需要递归的参数是什么
# 2. 判断终止条件: 这个函数以什么条件终止
# 3. 在这层需要做的工作
# 4. 递推工作: 如何利用参数进行下一步递推
# 5. 回溯返回值

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def sum_(i):
            sum_ = 0
            while i > 0:
                sum_ += i % 10
                i = i // 10
            return sum_
            
        def dfs(i, j, visited):
            s = sum_(i)+sum_(j)
            if not 0<=i<m or not 0<=j<n or ((i, j) in visited) or s>k: return 0
            visited.add((i, j))
            dfs(i+1, j, visited)
            dfs(i, j+1, visited)
            return len(visited)

        visited = set()
        return dfs(0, 0, visited)
