class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min = prices[0]
        profit = 0;

        for i in prices:
            if i < min: min = i
            profit = max(profit, i-min)
        return profit