class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxP, mPoss = 0, float('inf')

        for price in prices:
            if price < mPoss:
                mPoss = price
            else:
                maxP = max(maxP, price - mPoss)
        return maxP


print(Solution.maxProfit(Solution, [2, 5, 8, 3, 15]))
