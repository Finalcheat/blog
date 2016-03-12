title: 加数字
create_time: 2016/03/07 14:45:45
tags:
- Math
categories:
- leetcode
- C++

---
## [Add Digits](https://leetcode.com/problems/add-digits/)
> Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
> For example:
> Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

### 实现思路
数学问题，详情请看[wiki](https://en.wikipedia.org/wiki/Digital_root)

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Add-Digits.cpp)
```
class Solution {
    public:
        int addDigits(int num) {
            return (num - 1) % 9 + 1;
        }
};
```
