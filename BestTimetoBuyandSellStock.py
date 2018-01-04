#! /usr/bin/env python
"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
"""

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxdiff = 0
        minprice = prices[0]
        for i in prices[1:]:
            if i > minprice:
                if (i - minprice) > maxdiff:
                    maxdiff = i - minprice
            else:
                minprice = i
        return maxdiff

if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))
    print(s.maxProfit([7, 6, 4, 3, 1]))