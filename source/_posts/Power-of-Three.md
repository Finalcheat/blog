title: 判断一个数是否是3的幂
date: 2016/04/05 20:32:08
tags:
- Math
categories:
- leetcode
- C++

---
## [Power of Three](https://leetcode.com/problems/power-of-three/)
> Given an integer, write a function to determine if it is a power of three.

### 实现思路
不断除以3即可，不能整除的肯定不是3的幂。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Power-of-Three.cpp)
```
class Solution {
    public:
        bool isPowerOfThree(int n) {
            if (n <= 0) {
                return false;
            }
            while (n != 1) {
                if (n % 3 != 0) {
                    return false;
                }
                n /= 3;
            }
            return true;
        }
};
```
