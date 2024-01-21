"""
Date: Jan 21 2024
Last Revision: N/A
General Notes: 
- 44ms runtime (19.33%) and 16.68MB (57.44%)
- Not a fan of the problem, but I guess it's a good way to practice queues.
Solution Notes:
- Place all values in queue1
- When pop or top is called, move all values except the last one to queue2 and store the last value to return later.
"""

class MyStack:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        self.queue1.append(x)
        return

    def pop(self) -> int:
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))

        ans = self.queue1.pop(0)

        self.queue1, self.queue2 = self.queue2, self.queue1

        return ans

    def top(self) -> int:
        
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))

        ans = self.queue1.pop(0)
        self.queue2.append(ans)

        self.queue1, self.queue2 = self.queue2, self.queue1

        return ans

    def empty(self) -> bool:
        return len(self.queue1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
