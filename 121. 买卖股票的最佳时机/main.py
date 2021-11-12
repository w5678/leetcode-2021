"""
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
思路：
最简单的一种动态规划，今天的收益和昨天有关，昨天的收益和前天有关，前天的收益和前前天有关
1， 题目隐含了今天买可以今天卖，收益为0
2,  当前天的收益 = max(今天卖的收益 ，昨天拿到的收益)

"""
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices)<=1:
            return 0
        minp,maxp = prices[0],0
        for p in prices[1:]:
            minp =min(minp,p)#第i 天，我花最少的钱购入的股票
            maxp =max(maxp,p-minp)# 第i天，迄今为止我能获取的最高利润，可能今天的高，也可能是昨天的高
        return maxp


