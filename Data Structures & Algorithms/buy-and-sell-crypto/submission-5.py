class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        maxProfit = 0

        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            if prices[r] - prices[l] > 0:
                maxProfit = max(maxProfit, prices[r] - prices[l])
        
        return maxProfit
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''profit = 0
        l, r = 0, 0

        while l <= r and r < len(prices):
            profit = max(profit, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
            r += 1
        
        return profit'''