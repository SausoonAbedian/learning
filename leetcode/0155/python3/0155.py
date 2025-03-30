class MinStack:

    def __init__(self):
        self.value_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.value_stack.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        elif self.min_stack[-1] > val:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.value_stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.value_stack[-1]

    def get_min(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
assert min_stack.get_min() == -3
min_stack.pop()
assert min_stack.top() == 0
assert min_stack.get_min() == -2
