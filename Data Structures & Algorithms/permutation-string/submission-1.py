class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1) # length of the window
        l = 0
        r = l + k - 1# r=3
        while r < len(s2):
            cut = s2[l:r+1]
            print(cut)
            if sorted(cut) == sorted(s1):
                print("true")
                return True
            r += 1
            l += 1
        return False
            
