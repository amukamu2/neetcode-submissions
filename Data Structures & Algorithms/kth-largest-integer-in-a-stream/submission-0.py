class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        num = []
        ans = 1
        for i in self.nums:
            num.append(i * -1)
        heapq.heapify(num)
        for a in range(self.k):
            ans = -heapq.heappop(num)
        return ans
        
        
