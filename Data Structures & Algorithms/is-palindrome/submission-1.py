class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for string in s:
            if string.isalpha() or string.isdigit():
                new_s += string
        re = new_s[::-1]
        print(re.lower(), new_s.lower())
        return re.lower() == new_s.lower()