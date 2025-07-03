class TwoStacks:
    def __init__(self,size):
        self.size = size
        self.arr = [None] * size
        self.top1 = -1
        self.top2 = size

    def push1(self,value):
        if self.top1 + 1  < self.top2:
            self.top1 += 1
            self.arr[self.top1] = value
        else:
            print('Stack overflow in stack1')
    def push2(self,value):
        if self.top2 - 1 > self.top1:
            self.top2 -= 1
            self.arr[self.top2] = value
        else:
            print('Stack overflow in stack2')
    def pop1(self):
        if self.top1 >= 0:
            value =self.arr[self.top1]
            self.top1 -= 1
            return value
        else:
            print("Stack Underflow in stack1")
            return None
    def pop2(self):
        if self.top2 < self.size:
            value = self.arr[self.top2]
            self.top2 += 1
            return value
        else:
            print('Stack Underflow in stack1')
            return None
s = TwoStacks(10)
s.push1(1)
s.push1(2)
s.push2(9)
s.push2(8)
print(s.pop1())
print(s.pop2())

"""
class TwoStacks:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size
        self.top1 = -1  # Stack1 starts from beginning
        self.top2 = size  # Stack2 starts from end

    def push1(self, value):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.array[self.top1] = value
        else:
            raise OverflowError("Stack Overflow in Stack 1")

    def push2(self, value):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.array[self.top2] = value
        else:
            raise OverflowError("Stack Overflow in Stack 2")

    def pop1(self):
        if self.top1 >= 0:
            value = self.array[self.top1]
            self.top1 -= 1
            return value
        else:
            raise IndexError("Stack Underflow in Stack 1")

    def pop2(self):
        if self.top2 < self.size:
            value = self.array[self.top2]
            self.top2 += 1
            return value
        else:
            raise IndexError("Stack Underflow in Stack 2")

    def display(self):
        print("Stack 1:", self.array[:self.top1+1])
        print("Stack 2:", self.array[self.top2:])


# 🔧 Example Usage:
stacks = TwoStacks(10)
stacks.push1(1)
stacks.push1(2)
stacks.push2(9)
stacks.push2(8)
stacks.display()

print("Popped from Stack 1:", stacks.pop1())
print("Popped from Stack 2:", stacks.pop2())
stacks.display()

"""