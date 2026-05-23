class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0;
        for i in range(len(prices)):
            max=prices[i]
            for j in range(i+1,len(prices)):
                if(prices[j]>max):
                    max=prices[j]
            diff=max-prices[i]
            if(diff>profit):
                profit=diff

        return profit


       

       

        
        