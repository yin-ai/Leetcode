时间复杂度:O(MN)
空间复杂度:O(1)

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        left, right, top, bottom, res = 0, len(matrix[0])-1, 0, len(matrix)-1, []
        while True:
            for i in range(left, right+1): res.append(matrix[top][i])
            top += 1
            if top > bottom: break
            for i in range(top, bottom+1): res.append(matrix[i][right])
            right -= 1
            if left > right: break
            for i in range(right, left-1, -1): res.append(matrix[bottom][i])
            bottom-=1
            if top>bottom: break
            for i in range(bottom, top-1, -1): res.append(matrix[i][left])
            left+=1
            if left>right: break
        
        return res
            


        
        
