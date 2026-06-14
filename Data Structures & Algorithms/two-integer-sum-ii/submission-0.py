class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i, val in enumerate(numbers):
            diff = target - val
            if val not in d:
                d[val] = i + 1
            if diff in d and d[diff] != i + 1:
                return [d[diff], i + 1]
        return []