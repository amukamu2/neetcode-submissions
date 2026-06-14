class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for number in nums:
            if number not in count:
                count[number] = 1
            else:
                count[number] += 1
        
        bucket = [[] for i in range(len(nums)+1)]

        for key, val in count.items():
            print(key, val)
            bucket[val].append(key)
        
        result = []
        for i in range(len(bucket)-1, 0, -1):
            for j in bucket[i]:
                result.append(j)
                if len(result) == k:
                    return result
        
        return result