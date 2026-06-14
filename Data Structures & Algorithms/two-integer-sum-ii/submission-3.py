class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, nums in enumerate(numbers):
            complement = target - nums
            left = i + 1
            right = len(numbers) - 1
            while left <= right:
                mid = (left+right) // 2
                if (numbers[mid] == complement):
                    return [i+1, mid+1]
                if (numbers[mid] < complement):
                    left = mid + 1
                if (numbers[mid] > complement):
                    right = mid - 1
