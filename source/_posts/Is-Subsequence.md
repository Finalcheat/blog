title: 判断字符串子序列
date: 2017/03/30 20:42:00
tags:
- String
- Two Pointers
categories:
- leetcode
- C++

---
## [Is Subsequence](https://leetcode.com/problems/is-subsequence/)
> Given a string s and a string t, check if s is subsequence of t.
> You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).
> A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).
> Example 1:
> s = "abc", t = "ahbgdc"
> Return true.
> Example 2:
> s = "axc", t = "ahbgdc"
> Return false.

### 实现思路
设置两个指针分别指向两个字符串遍历搜索即可。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Is-Subsequence.cpp)
```
class Solution {
    public:
        bool isSubsequence(string s, string t) {
            size_t prev = -1;
            for (size_t i = 0; i < s.size(); ++i) {
                prev = t.find_first_of(s[i], prev + 1);
                if (prev == string::npos) {
                    return false;
                }
            }
            return true;
        }
};
```
