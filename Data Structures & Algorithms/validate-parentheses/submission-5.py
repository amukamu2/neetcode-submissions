class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        op = {'{':'}', '(':')', '[':']'}
        for i in s:
            if i in op.values():
                print(i, stack)
                if stack and (op[stack[-1]] == i):
                    stack.pop()
                    continue
                else:
                    return False
            stack.append(i)
        if stack == []:
            return True
        print(stack)
        return False