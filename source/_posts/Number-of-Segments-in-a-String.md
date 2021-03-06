title: 字符串分段数量
date: 2017/03/05 21:42:00
tags:
- String
categories:
- leetcode
- C++

---
## [Number of Segments in a String](https://leetcode.com/problems/number-of-segments-in-a-string/)
> Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.
> Please note that the string does not contain any non-printable characters.
> Example:
> Input: "Hello, my name is John"
> Output: 5

### 实现思路
用空白字符进行分割，遇到空白字符跳过，否则数量+1同时跳过所有非空白字符。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Number-of-Segments-in-a-String.cpp)
```
class Solution {
    public:
        int countSegments(string s) {
            int count = 0;
            for (size_t i = 0; i < s.size(); ++i) {
                if (s[i] == ' ') {
                    continue;
                }
                ++count;
                while (i < s.size() &&  s[i] != ' ') {
                    ++i;
                }
            }
            return count;
        }
};
```
