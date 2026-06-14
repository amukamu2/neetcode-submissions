class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # -4 -1 -1 0 1 2
        # -4 -1 -1 0 1 2 5
        # -1 0 0 1
        nums.sort()
        result = []
        for i, val in enumerate(nums):
            complement = 0 - val
            left = 0
            right = len(nums) - 1
            while left < right:
                if left == i:
                    left += 1
                    continue
                if right == i:
                    right -= 1
                    continue
                sum2 = nums[left] + nums[right]
                if sum2 == complement:
                    triple = [nums[left], val, nums[right]]
                    triple.sort()
                    if triple not in result:
                        result.append(triple)
                if sum2 < complement:
                    left += 1
                elif sum2 > complement:
                    right -= 1
                else:
                    left += 1
                    right -= 1
        print(result)
        return result
        
        
        