title: 交替位的二进制数
date: 2017/10/21 22:13:00
tags:
- Bit Manipulation
categories:
- leetcode
- C++

---
## [Binary Number with Alternating Bits](https://leetcode.com/problems/binary-number-with-alternating-bits/description/)
> Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.
> Example 1:
> <pre>
> Input: 5
> Output: True
> Explanation:
> The binary representation of 5 is: 101
> </pre>
> Example 2:
> <pre>
> Input: 7
> Output: False
> Explanation:
> The binary representation of 7 is: 111.
> </pre>
> Example 3:
> <pre>
> Input: 11
> Output: False
> Explanation:
> The binary representation of 11 is: 1011.
> </pre>
> Example 4:
> <pre>
> Input: 10
> Output: True
> Explanation:
> The binary representation of 10 is: 1010.
> </pre>

### 实现思路
取二进制位过程中判断即可。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Binary-Number-with-Alternating-Bits.cpp)
```
class Solution {
    public:
        bool hasAlternatingBits(int n) {
            int bit = n % 2;
            n /= 2;
            while (n > 0) {
                bit = !bit;
                if (n % 2 != bit) {
                    return false;
                }
                n /= 2;
            }
            return true;
        }
};
```
