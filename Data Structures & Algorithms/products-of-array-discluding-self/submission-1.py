class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prefix = 1
        postfix = 1
        for i in nums:
            result.append(prefix)
            prefix = prefix*i
            
        for j in range(len(nums)-1,-1,-1):
            result[j] = result[j]*postfix
            postfix = postfix*nums[j]
        
        print(result)
        return result

        # [1,1,2,8]
        # [48,24,12,8]
