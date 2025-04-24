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