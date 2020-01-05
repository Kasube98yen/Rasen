from collections import deque

# full scratchで作成した場合

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        result = self.stack[-1]
        del self.stack[-1]
        return result
    
def main():
    formula = input().split()
    stack = Stack()
    operator_list = ["+", "-", "*"] # 演算子リスト
    a, b = (0, 0) # popした値のTEMP

    for i in range(len(formula)):
        if formula[i] in operator_list:
            a = stack.pop()
            b = stack.pop()
            ans = eval(str(b) + formula[i] + str(a))
            stack.push(ans)
        else:
            stack.push(formula[i])

    print(stack.pop())

# dequeを使った場合

def main2():
    formula = input().split()
    stack = deque()
    operator_list = ["+", "-", "*"]
    a, b = (0, 0) # popした値のTEMP

    for i in range(len(formula)):
        if formula[i] in operator_list:
            a = stack.pop()
            b = stack.pop()
            ans = eval(str(b) + formula[i] + str(a))
            stack.append(ans)
        else:
            stack.append(formula[i])
    
    print(stack.pop())

# dequeはO(1)で、呼び出し回数10^5を超えるとarrayやlist実装より早いらしい

if __name__ == "__main__":
    main2()