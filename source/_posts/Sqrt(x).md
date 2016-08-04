title: 求x的平方根
date: 2016/05/15 15:21:56
tags:
- Binary Search
- Math
categories:
- leetcode
- C++

---
## [Sqrt(x)](https://leetcode.com/problems/sqrtx/)
> Implement int sqrt(int x).
> Compute and return the square root of x.

### 实现思路
[牛顿迭代法](https://en.wikipedia.org/wiki/Newton%27s_method)

### Code
```
class Solution {
    public:
        int mySqrt(int x) {
            if (x == 0) {
                return 0;
            }
            double prev = 0;
            double result = 1;
            while (result != prev)
            {
                prev = result;
                result = (result + x / result) / 2;
            }
            return int(result);
        }
};
```
