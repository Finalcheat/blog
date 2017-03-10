title: 二进制相加
date: 2017/03/10 20:47:25
tags:
- Math
- String
categories:
- leetcode
- C++

---
## [Add Binary](https://leetcode.com/problems/add-binary/)
> Given two binary strings, return their sum (also a binary string).
> For example,
> a = "11"
> b = "1"
> Return "100".

### 实现思路
从后往前遍历相加即可，注意结果长度的判断以及进位的处理即可。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Add-Binary.cpp)
```
class Solution {
    public:
        string addBinary(string a, string b) {
            int aLen = a.size();
            int bLen = b.size();
            int cLen = std::max(aLen, bLen);
            string result(cLen, '0');
            int carry = 0;
            while (aLen > 0 || bLen > 0) {
                int num1 = 0;
                if (aLen > 0) {
                    num1 = a[--aLen] - '0';
                }
                int num2 = 0;
                if (bLen > 0) {
                    num2 = b[--bLen] - '0';
                }
                int sum = num1 + num2 + carry;
                carry = sum / 2;
                result[--cLen] = sum % 2 + '0';
            }
            if (carry) {
                return std::to_string(carry) + result;
            }
            return result;
        }
};
```
