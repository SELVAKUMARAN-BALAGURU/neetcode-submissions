class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxprofit = -99999
        for i in range(n):
            for j in range(i+1,n):
                if prices[j]>prices[i]:
                    profit = prices[j]-prices[i]
                    if profit>maxprofit:
                        maxprofit = profit
                    else:
                        continue
                else:
                    continue
        print(maxprofit)
        if maxprofit == -99999:
            return 0
        return maxprofit