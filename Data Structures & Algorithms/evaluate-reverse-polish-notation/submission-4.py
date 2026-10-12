import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        for tok in tokens:

            if tok == "+":
                res = stack.pop() + stack.pop()
                stack.append(res)

            elif tok == "-":
                sub = stack.pop()
                res = stack.pop() - sub
                stack.append(res)

            elif tok == "*":
                res = stack.pop() * stack.pop()
                stack.append(res)

            elif tok == "/":
                divisor = stack.pop()
                res = math.trunc(stack.pop() / divisor)
                stack.append(res)
            else:
                stack.append(int(tok))

        return stack[-1]