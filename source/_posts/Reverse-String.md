title: 反转字符串
create_time: 2016/04/28 20:46:09
tags:
- Two Pointers
- String
categories:
- leetcode
- C++

---
## [Reverse String](https://leetcode.com/problems/reverse-string/)
> Write a function that takes a string as input and returns the string reversed.
> Example:
> Given s = "hello", return "olleh".

### 实现思路
很简单的循环，遍历字符串的一半交换即可。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Reverse-String.cpp)
```
class Solution {
    public:
        string reverseString(string s) {
            const size_t len = s.size();
            for (size_t i = 0; i < len / 2; ++i) {
                std::swap(s[i], s[len - i - 1]);
            }
            return s;
        }
};
```
