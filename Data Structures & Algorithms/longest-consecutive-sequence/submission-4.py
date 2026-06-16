class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 2 3 4 4 5 10 20
        nums.sort()
        print(nums)
        if not nums:
            return 0
        l = 0
        r = l+1
        temp = 1
        longest = 1
        while r < len(nums):
            if nums[r] == nums[l] + 1:
                temp += 1
                longest = max(temp, longest)
            elif nums[r] == nums[l]:
                pass
            else:
                l = r
                r += 1
                temp = 1
                continue
            l += 1
            r += 1
        return longest
