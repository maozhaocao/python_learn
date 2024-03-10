"""
https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
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
        # 多加一个冷冻期的状态
        dp = [[-10000 for _ in range(3)] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            dp[i][2] = max(dp[i][2], dp[i - 1][1] + prices[i])
        return max(dp[n - 1][0], dp[n - 1][2])


if __name__ == '__main__':
    print(Solution().maxProfit([1, 2, 3, 0, 2]))
