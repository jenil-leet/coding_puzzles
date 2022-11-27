class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_till_now = float("inf")
        highest_profit = 0        
        for price in prices:
            lowest_till_now = min(lowest_till_now, price)
            highest_profit = max(highest_profit, price - lowest_till_now)
        return(highest_profit)            