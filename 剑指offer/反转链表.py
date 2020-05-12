# 首先这和上一道题一样是一个双指针的问题

# 时间复杂度： O(n)
# 空间复杂度： O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 首先定义一个反链表头指针
        rev = None
        while head:
          temp = head.next
          # 我们首先想到的是将指针指向前一个节点
          head.next = pre
          # 然后更新前一个节点
          pre = head
          # 然后更新head(head = head.next) 但是head.next已经变了，所以要提前存起来
          head = temp
        return rev
 
 
 # 当然我们还可以利用python的语言特性，用一行直接就道题前面的四句话
 class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 首先定义一个反链表头指针
        rev = None
        while head:
            # 使用一行就能将他们完成，很是方便
            head.next, pre, head = pre, head, head.next
        return rev
