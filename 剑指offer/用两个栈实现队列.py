# 这个刚开始没有读懂题，其实这个添加和创建队列的时候是返回null的，只有删除操作的时候是返回-1或者要删除的那个元素
# 然后这个题明确指出要有两个栈，所以这个题的解题点就是用一个栈辅助另一个栈实现队列
# 时间复杂度 append O(1) delate O(n)
# 空间复杂度 O(n)

class CQueue:

    def __init__(self):
        self.cqueue = []
        self.helper = []

    def appendTail(self, value: int) -> None:
        self.cqueue.append(value)
   
    def deleteHead(self) -> int:
        if not self.helper: 
            while self.cqueue:
                self.helper.append(self.cqueue.pop())

        return self.helper.pop() if self.helper else -1
