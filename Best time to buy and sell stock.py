class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_=0
        for i in range(len(prices)):
            buy=prices[i]
            for j in range(i+1,len(prices)):
                sell=prices[j]
                profit=prices[j]-prices[i]
                max_=max(max_,profit)
        return max_
