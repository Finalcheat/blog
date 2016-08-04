title: 验证变位词
date: 2016/03/07 14:20:01
tags:
- Hash Table
- Sort
categories:
- leetcode
- C++

---
## [Valid Anagram](https://leetcode.com/problems/valid-anagram/)
> Given two strings s and t, write a function to determine if t is an anagram of s.
> For example,
> s = "anagram", t = "nagaram", return true.
> s = "rat", t = "car", return false.
> Note:
> You may assume the string contains only lowercase alphabets.

### 实现思路
对字符串进行排序，然后遍历比较是否相等即可。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Valid-Anagram.cpp)
```
class Solution {
    public:
        bool isAnagram(string s, string t) {
            if (s.size() != t.size()) {
                return false;
            }
            std::sort(s.begin(), s.end());
            std::sort(t.begin(), t.end());
            for (size_t i = 0; i < s.size(); ++i) {
                if (s[i] != t[i]) {
                    return false;
                }
            }
            return true;
        }
};
```
