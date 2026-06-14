class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        for i, val in enumerate(prices):
            for j in range(i+1, len(prices)):
                if prices[j] > val:
                    profit = prices[j] - val
                    maxP = max(profit, maxP)
        return maxP
