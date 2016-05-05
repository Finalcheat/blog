title: 判断一个数字是否是4的幂次方
create_time: 2016/05/05 21:07:36
tags:
- Bit Manipulation
categories:
- leetcode
- C++

---
## [Power of Four](https://leetcode.com/problems/power-of-four/)
> Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
> Example:
> Given num = 16, return true. Given num = 5, return false.

### 实现思路
循环除以4即可，注意判断边界条件。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Power-of-Four.cpp)
```
class Solution {
    public:
        bool isPowerOfFour(int num) {
            if (num <= 0) {
                return false;
            }
            while (num > 1) {
                if (num % 4 != 0) {
                    return false;
                }
                num /= 4;
            }
            return num == 1;
        }
};
```
