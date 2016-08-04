title: 求x的n次方
date: 2016/05/16 21:01:09

---
## [Pow(x, n)](https://leetcode.com/problems/powx-n/)
> Implement pow(x, n).

### 实现思路
求x的n次方，用递归解法，注意n是负数的情况。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Pow.cpp)
```
class Solution {
    public:
        double myPow(double x, int n) {
            if (n == 0) {
                return 1;
            } else if (n == 1) {
                return x;
            }
            double value = pow(x, abs(n / 2));  
            if (n > 0) {
                if (n % 2 == 0) {
                    return value * value;
                } else {
                    return value * value * x;
                }
            }
            else {  
                if (n % 2 == 0) {
                    return 1.0 / (value * value);
                } else {
                    return 1.0 / (value * value * x);
                }
            }
            return value;
        }
};
```
