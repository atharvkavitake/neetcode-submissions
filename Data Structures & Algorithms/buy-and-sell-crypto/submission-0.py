class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        mini=prices[0]
        profit=0
        for i in prices:
            mini=min(mini,i)
            profit=max(profit,i-mini)
        return profit
        