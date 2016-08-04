title: 判断一个数是否是2的幂
date: 2016/04/04 13:06:35
tags:
- Math
- Bit Manipulation
categories:
- leetcode
- C++

---
## [Power of Two](https://leetcode.com/problems/power-of-two/)
> Given an integer, write a function to determine if it is a power of two.

### 实现思路
注意到2的整数次幂对应的二进制只含有1个1，所以判断1的个数是否为1即可。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Power-of-Two.cpp)
```
class Solution {
    public:
        bool isPowerOfTwo(int n) {
            if (n <= 0) {
                return false;
            }
            int oneNum = 0;
            while (n) {
                int bit = n & 1;
                oneNum += bit;
                if (oneNum > 1) {
                    return false;
                }
                n = n >> 1;
            }
            return oneNum == 1;
        }
};
```
