class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0,1
        count = {}
        res = 0

        for r,val in enumerate(s):
            count[val] = 1 + count.get(val, 0)

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        return res

