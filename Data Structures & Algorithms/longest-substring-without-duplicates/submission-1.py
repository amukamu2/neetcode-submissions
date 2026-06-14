class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1
        seen = set()
        longest = 0
        if len(s) == 1:
            return 1
        while r < len(s):
            if l == 0:
                seen.add(s[l])
            while r < len(s) and s[r] not in seen:
                seen.add(s[r])
                r += 1
            longest = max(len(seen), longest)
            while r < len(s) and s[r] in seen:
                seen.remove(s[l])
                l += 1
        return longest