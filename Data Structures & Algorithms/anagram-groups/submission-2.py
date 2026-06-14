class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for s in strs:
            alpha = [0]*26
            for char in s:
                alpha[ord(char) - ord("a")] += 1
            key = tuple(alpha)
            group[key].append(s)
        return list(group.values())