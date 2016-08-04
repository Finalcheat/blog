title: 反转位
date: 2016/03/10 12:37:09
tags:
- Bit Manipulation
categories:
- leetcode
- C++

---
## [Reverse Bits](https://leetcode.com/problems/reverse-bits/)
> Reverse bits of a given 32 bits unsigned integer.
> For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), 
> return 964176192 (represented in binary as 00111001011110000010100101000000).

### 实现思路
反转位，思路是通过与1做&运算得出最右边的bit，然后不断右移，新数不断左移加上最右边的bit即可。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Reverse-Bits.cpp)
```
class Solution {
    public:
        uint32_t reverseBits(uint32_t n) {
            uint32_t result = 0;
            for (size_t i = 0; i < 32; ++i) {
                const int bit = n & 1;
                n = n >> 1;
                result = result << 1;
                result += bit;
            }
            return result;
        }
};
```
