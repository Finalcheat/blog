title: 赎金条
date: 2017/03/04 14:33:50
tags:
- String
- Hash Table
categories:
- leetcode
- C++

---
## [Ransom Note](https://leetcode.com/problems/ransom-note/)
> Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
> Each letter in the magazine string can only be used once in your ransom note.
> Note:
> You may assume that both strings contain only lowercase letters.
> canConstruct("a", "b") -> false
> canConstruct("aa", "ab") -> false
> canConstruct("aa", "aab") -> true

### 实现思路
使用hashtable记录出现的字符以及对应的次数，然后遍历验证即可。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Ransom-Note.cpp)
```
class Solution {
    public:
        bool canConstruct(string ransomNote, string magazine) {
            std::unordered_map<char, int> u;
            for (size_t i = 0; i < magazine.size(); ++i) {
                ++u[magazine[i]];
            }
            for (size_t i = 0; i < ransomNote.size(); ++i) {
                std::unordered_map<char, int>::iterator it = u.find(ransomNote[i]);
                if (it == u.end() || it->second <= 0) {
                    return false;
                }
                --it->second;
            }
            return true;
        }
};
```
