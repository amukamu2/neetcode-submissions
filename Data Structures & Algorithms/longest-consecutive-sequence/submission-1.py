class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums.sort() # n log n
        curr = nums[0]
        i = 0
        longest = 0
        streak = 0
        while i < len(nums):
            if curr != nums[i]:
                streak = 0
                curr = nums[i]
            while i < len(nums) and nums[i] == curr:
                i+=1
            streak += 1
            curr += 1
            longest = max(longest, streak)
        return longest