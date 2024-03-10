"""
https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/
"""


class Solution(object):
    # 148ms
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        max_profit = 0
        min_price = prices[0]
        # enumerate比for i更快
        for i, price in enumerate(prices):
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit
        # for i in range(1, len(prices)):
        #     min_price = min(min_price, prices[i])
        #     max_profit = max(max_profit, prices[i] - min_price)
        # return max_profit


if __name__ == '__main__':
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
