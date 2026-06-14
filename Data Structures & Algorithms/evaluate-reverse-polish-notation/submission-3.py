class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in '+-*/':
                stack.append(int(i))
            else:
                pop1 = stack.pop()
                pop2 = stack.pop()
                if i == "+":
                    stack.append(pop1 + pop2)
                elif i == "-":
                    stack.append(pop2 - pop1)
                elif i == "*":
                    stack.append(pop1*pop2)
                else:
                    stack.append(int(pop2/pop1))
        if len(stack):
            return stack[0]
        else:
            return 0

                