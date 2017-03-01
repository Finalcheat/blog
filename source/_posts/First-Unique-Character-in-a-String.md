title: 字符串中第一个出现一次的字符
date: 2017/03/01 22:56:35
tags:
- Hash Table
categories:
- leetcode
- C++

---
## [First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string)
> Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
> Examples:
> s = "leetcode"
> return 0.
> s = "loveleetcode",
> return 2.
> Note: You may assume the string contain only lowercase letters.

### 实现思路
第一次遍历使用hashtable存储字符出现的次数，第二次遍历直接查找hashtable出现次数为1的字符，找到直接返回即可。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/First-Unique-Character-in-a-String.cpp)
```
class Solution {
    public:
        int firstUniqChar(string s) {
            std::unordered_map<char, int> u;
            for (size_t i = 0; i < s.size(); ++i) {
                ++u[s[i]];
            }
            for (size_t i = 0; i < s.size(); ++i) {
                if (u[s[i]] == 1) {
                    return i;
                }
            }
            return -1;
        }
};
```
