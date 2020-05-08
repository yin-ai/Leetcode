# 从右下角向左上角查找，这样不会错过目标值。
# 采用try的形式来判断，若报错则说明越界或者matrix没有值。因此返回False
# 时间复杂度O(n)
# 空间复杂度O(1)
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix) - 1
        m = 0
        while(True):
            try:
                if matrix[n][m] > target:
                    n -= 1
                elif matrix[n][m] < target:
                    m += 1
                elif matrix[n][m] == target:
                    return True
            except:
                return False
