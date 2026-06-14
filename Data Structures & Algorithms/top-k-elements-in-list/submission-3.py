class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        l = []
        result = []
        for number in nums:
            freq[number] = 1 + freq.get(number, 0)
        
        for key, val in freq.items():
            l.append([val, key])
        
        l.sort()
        print(l)
        while len(result) < k:
            result.append(l.pop()[1])
        
        return result

    