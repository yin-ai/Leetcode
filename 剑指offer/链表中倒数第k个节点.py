# 依旧是一道双指针的问题
# 使用指针拉开距离
# 时间复杂度 O(N)
# 空间复杂度 O(1)

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        first = head 
        for _ in range(k):
            first = first.next
        while first:
            first = first.next
            head = head.next
        return head
