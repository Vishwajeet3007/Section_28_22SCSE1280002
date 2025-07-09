from collections import deque

class StackUsingQueues:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        # Step 1: Push to q2
        self.q2.append(x)
        # Step 2: Move all from q1 to q2
        while self.q1:
            self.q2.append(self.q1.popleft())
        # Step 3: Swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if not self.q1:
            return None
        return self.q1.popleft()

    def top(self):
        if not self.q1:
            return None
        return self.q1[0]

    def empty(self):
        return not self.q1
s = StackUsingQueues()
s.push(10)
s.push(20)
s.push(30)

print(s.top())   # Output: 30
print(s.pop())   # Output: 30
print(s.top())   # Output: 20
print(s.empty()) # Output: False
