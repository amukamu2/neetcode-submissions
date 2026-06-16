class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = []
        for i in stones:
            maxheap.append(-1*i)
        heapq.heapify(maxheap)
        while len(maxheap) > 1:
            stn1 = -heapq.heappop(maxheap)
            stn2 = -heapq.heappop(maxheap)
            print("2", maxheap)
            if (stn1 - stn2) > 0:
                weigh = (stn1 - stn2)*-1
                heapq.heappush(maxheap, weigh)
        if not maxheap:
            return 0
        return -heapq.heappop(maxheap)


