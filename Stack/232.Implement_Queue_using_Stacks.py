# https://leetcode.com/problems/implement-queue-using-stacks

class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek()
        return self.output.pop()

    def peek(self) -> int:
        if not self.output:
            for i in range(len(self.input)):
                intput_pop = self.input.pop()
                self.output.append(intput_pop)
        return self.output[-1]

    def empty(self) -> bool:
        if not self.input and not self.output: return True
        else: return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()