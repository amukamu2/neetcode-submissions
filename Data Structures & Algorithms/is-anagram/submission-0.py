class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = sorted(s.lower())
        t1 = sorted(t.lower())
        if s1 == t1:
            return True
        return False