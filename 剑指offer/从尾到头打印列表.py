# 这个从一开始想用insert()方法，但是insert()方法的时间复杂度为O(n)，于是最后还是选择了append()方法。进行两次遍历
# 时间复杂度O(n)
# 空间复杂度O(n)

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        stack = []
        res = []
        while head:
            stack.append(head.val)
            head = head.next
            
        while stack:
            res.append(stack.pop())

        return res
