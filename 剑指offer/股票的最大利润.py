class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        low_prices = prices[0]
        max_ = 0
        for i in range(1, len(prices)):
            low_prices = min(low_prices, prices[i])
            max_ = max(max_, prices[i]-low_prices)
        return max_
