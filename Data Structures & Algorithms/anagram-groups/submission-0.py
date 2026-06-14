class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        result = []
        # "act": ["act"]
        # "opst" : ["pots", "tops"]
        for s in strs:
            sort = ''.join(sorted(s))
            if sort not in group:
                group[sort] = [s]
            else:
                group[sort].append(s)
        for k,v in group.items():
            result.append(v)

        return result