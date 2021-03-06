title: 最佳时间买入卖出股票II
date: 2016/04/01 21:34:56
tags:
- Array
- Greedy
categories:
- leetcode
- C++

---
## [Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)
> Say you have an array for which the ith element is the price of a given stock on day i.
> Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

### 实现思路
贪心算法，计算相邻时间差的价格，大于0则计入最后的收益中。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Best-Time-to-Buy-and-Sell-Stock-II.cpp)
```
class Solution {
    public:
        int maxProfit(vector<int>& prices) {
            int result = 0;
            for (size_t i = 1; i < prices.size(); ++i) {
                const int diff = prices[i] - prices[i - 1];
                if (diff > 0) {
                    result += diff;
                }
            }
            return result;
        }
};
```
