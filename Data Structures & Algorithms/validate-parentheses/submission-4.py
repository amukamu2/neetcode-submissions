class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        op = {'{':'}', '(':')', '[':']'}
        for i in s:
            if i in op:
                stack.append(i)
            if i in op.values():
                if stack == []:
                    return False
                if op[stack.pop()] != i:
                    return False
        if stack != []:
            return False
        return True