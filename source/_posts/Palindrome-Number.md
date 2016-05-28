title: 回文数
create_time: 2016/05/28 20:25:01
tags:
- Math
categories:
- leetcode
- C++

---
## [Palindrome Number](https://leetcode.com/problems/palindrome-number/)
Determine whether an integer is a palindrome. Do this without extra space.

### 实现思路
反转数字，然后判断是否相等即可。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Palindrome-Number.cpp)
```
class Solution {
    public:
        bool isPalindrome(int x) {
            if (x < 0) {
                return false;
            }
            int reverseNum = 0;
            int num = x;
            while (num) {
                const int n = num % 10;
                reverseNum = reverseNum * 10 + n;
                num = num / 10;
            }
            return reverseNum == x;
        }
};
```
