"""
https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/
"""


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        # dp[i][j] 第i天状态为j的最大利润
        n = len(prices)
        # 2*k+1个状态 未买 买1 卖1 买2 卖2
        dp = [-10000 for _ in range(2 * k + 1)]
        dp[0] = 0
        dp[1] = -prices[0]
        # 状态压缩
        for i in range(1, n):
            for j in range(k):
                dp[2 * j + 1] = max(dp[2 * j + 1], dp[2 * j] - prices[i])
                dp[2 * j + 2] = max(dp[2 * j + 2], dp[2 * j + 1] + prices[i])
        # 截取步长=2
        return max(dp[::2])


if __name__ == '__main__':
    print(Solution().maxProfit(2, [3, 2, 6, 5, 0, 3]))
