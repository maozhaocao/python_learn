"""
https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/
"""


class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        # dp[i][j] 第i天状态为j的最大利润
        n = len(prices)
        dp = [-10000 for _ in range(2)]
        dp[0] = 0
        dp[1] = -prices[0] - fee
        for i in range(1, n):
            dp[0] = max(dp[0], dp[1] + prices[i])
            dp[1] = max(dp[1], dp[0] - prices[i] - fee)
        return dp[0]


if __name__ == '__main__':
    print(Solution().maxProfit([1, 3, 2, 8, 4, 9], 2))
