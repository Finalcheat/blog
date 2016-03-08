title: 二进制中1的个数
create_time: 2016/03/08 19:33:25
tags:
- leetcode
- C++
categories:
- leetcode

---
## [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)
> Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).
> For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.

### 实现思路
利用与1作&操作可得出最右bit的特性，通过不断右移即可算出1的个数

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Number-of-1-Bits.cpp)
```
class Solution {
    public:
        int hammingWeight(uint32_t n) {
            int count = 0;
            while (n) {
                count += n & 1;
                n >>= 1;
            }
            return count;
        }
};
```
