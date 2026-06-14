class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i] # diff = 4
            if diff in seen:
                return [seen[diff], i]
            seen[nums[i]] = i