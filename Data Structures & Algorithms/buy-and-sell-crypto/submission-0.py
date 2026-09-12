class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minPrice = prices[0]

        for i in range(1, len(prices)):
            minPrice = min(minPrice, prices[i])
            profit = max(profit, prices[i] - minPrice)
        
        return profit