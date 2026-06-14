class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = [0]*26
        count2 = [0]*26
        if len(s1) > len(s2):
            return False
        for i, val in enumerate(s1):
            count1[ord(val) - ord("a")] += 1
        k = len(s1) # length of the window
        l = 0
        r = 0
        while r < len(s2):
            while r < k + l:
                count2[ord(s2[r])-ord("a")] += 1
                r += 1
            if count1 == count2:
                return True
            count2[ord(s2[l]) - ord("a")] -= 1
            l += 1
        return False

# lecabee
