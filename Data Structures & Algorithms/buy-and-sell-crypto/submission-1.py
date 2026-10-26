class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l = 0 
        r= l+1 
        max_profit = 0 
        while l < n-1 and r <= n-1 : 
            if prices[l] >= prices[r]:
                l = r 
                r = l+1         
            else :
                p = prices[r] - prices[l]
                max_profit = max(max_profit,p)
                r = r+1 
                
        return max_profit  




        