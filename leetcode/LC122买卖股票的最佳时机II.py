"""
https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/description/
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
        dp = [[-10000 for _ in range(2)] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[n - 1][0]


if __name__ == '__main__':
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
