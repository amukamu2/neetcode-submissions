class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        op = {'{':'}', '(':')', '[':']'}
        for i in s:
            if i in op.values():
                if stack and (op[stack[-1]] == i):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if stack == []:
            return True
        return False