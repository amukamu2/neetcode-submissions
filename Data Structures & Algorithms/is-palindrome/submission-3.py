class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i < j:
            while i < j and not (s[i].isalpha() or s[i].isdigit()):
                print(i, s[i])
                i += 1
            while i < j and not (s[j].isalpha() or s[j].isdigit()):
                print(j, s[j])
                j -= 1
            if (s[i].lower() != s[j].lower()):
                return False
            i += 1
            j -= 1
        return True

# ...,