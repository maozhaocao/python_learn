"""
https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/description/
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        # dp[i][j] 第i天状态为j的最大利润
        n = len(prices)
        # 5个状态 未买 买1 卖1 买2 卖2
        dp = [-10000 for _ in range(5)]
        dp[0] = 0
        dp[1] = -prices[0]
        # 状态压缩
        for i in range(1, n):
            dp[0] = 0
            dp[1] = max(dp[1], dp[0] - prices[i])
            dp[2] = max(dp[2], dp[1] + prices[i])
            dp[3] = max(dp[3], dp[2] - prices[i])
            dp[4] = max(dp[4], dp[3] + prices[i])
        return max(dp[0], dp[2], dp[4])

    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        # dp[i][j] 第i天状态为j的最大利润
        n = len(prices)
        # 5个状态 未买 买1 卖1 买2 卖2
        dp = [[-10000 for _ in range(5)] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = 0
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + prices[i])
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] - prices[i])
            dp[i][4] = max(dp[i - 1][4], dp[i - 1][3] + prices[i])
        return max(dp[n - 1][0], dp[n - 1][2], dp[n - 1][4])


if __name__ == '__main__':
    print(Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
