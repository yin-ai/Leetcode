# 这个没有搞懂考点在哪里，就是普通的删除节点
# 时间复杂度: O(N)
# 空间复杂度: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val: return head.next
        cur = head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
                return head
            cur = cur.next
