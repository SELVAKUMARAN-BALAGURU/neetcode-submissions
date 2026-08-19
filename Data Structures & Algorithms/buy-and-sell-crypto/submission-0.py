class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxprofit = []
        for i in range(n):
            for j in range(i+1,n):
                if prices[j]-prices[i]>prices[i]:
                    maxprofit.append(prices[j]-prices[i])
                else:
                    continue
        print(maxprofit)
        if len(maxprofit)>=1:
            return max(maxprofit)
        else:
            return 0
        