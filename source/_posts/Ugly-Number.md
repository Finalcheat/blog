title: 丑陋数
date: 2013/04/02 14:17:09
tags:
- Math
categories:
- leetcode
- C++

---
## [Ugly Number](https://leetcode.com/problems/ugly-number/)
> Write a program to check whether a given number is an ugly number.
> Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.
> Note that 1 is typically treated as an ugly number.

### 实现思路
丑陋数的定义是因子只有1、2、3、5，所以判断一个数是否是丑陋数只需要不断除以这些数即可。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Ugly-Number.cpp)
```
class Solution {
    public:
        bool isUgly(int num) {
            while (num > 3) {
                if (num % 2 == 0) {
                    num /= 2;
                } else if (num % 3 == 0) {
                    num /= 3;
                } else if (num % 5 == 0) {
                    num /= 5;
                } else {
                    return false;
                }
            }
            return !(num < 1);
        }
};
```
