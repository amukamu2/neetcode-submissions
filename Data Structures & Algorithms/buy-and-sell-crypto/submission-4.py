class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window
        left = 0
        right = left + 1
        maxP = 0
        while right < len(prices):
            profit = prices[right] - prices[left]
            if profit > 0:
                maxP = max(profit, maxP)
            else:
                left = right
            right += 1
        return maxP

