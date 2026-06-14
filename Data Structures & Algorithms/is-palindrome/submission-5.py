class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i < j:
            while i < j and not isAlphaNum(s[i]):
                i += 1
            while i < j and not isAlphaNum(s[j]):
                j -= 1
            if (s[i].lower() != s[j].lower()):
                return False
            i += 1
            j -= 1
        return True

def isAlphaNum(s):
    if '0' <= s <= '9' or 'A' <= s <= 'Z' or 'a' <= s <= 'z':
        return True
    return False
