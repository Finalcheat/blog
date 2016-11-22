title: 最佳时间买入卖出股票
date: 2016/04/29 21:52:45
tags:
- Array
- Dynamic Programming
categories:
- leetcode
- C++

---
## [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
> Say you have an array for which the ith element is the price of a given stock on day i.
> If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

### 实现思路
动态规划

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Best-Time-to-Buy-and-Sell-Stock.cpp)
```
class Solution {
    public:
        int maxProfit(vector<int>& prices) {
            const size_t len = prices.size();
            if (len <= 1) {
                return 0;
            }
            int result = prices[1] - prices[0];
            int minPrice = prices[0];
            for (size_t i = 2; i < len; ++i)
            {
                minPrice = std::min(prices[i - 1], minPrice);
                if (result < prices[i] - minPrice) {
                    result = prices[i] - minPrice;
                }
            }
            return result > 0 ? result : 0;
        }
};
```
