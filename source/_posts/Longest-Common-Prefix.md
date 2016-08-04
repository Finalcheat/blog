title: 最长公共前缀字符
date: 2016/07/26 21:33:09
tags:
- String
categories:
- leetcode
- C++

---
## [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)
> Write a function to find the longest common prefix string amongst an array of strings.

### 实现思路
将第一个字符串的字符与其他字符串比较，遇到不相等的直接返回结果，否则增加当前字符到结果中。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Longest-Common-Prefix.cpp)
```
class Solution {
    public:
        string longestCommonPrefix(vector<string>& strs) {
            std::string result;
            if (strs.empty()) {
                return result;
            }
            const std::string& first_str = strs[0];
            for (size_t i = 0; i < first_str.size(); ++i) {
                for (size_t j = 1; j < strs.size(); ++j) {
                    if (i >= strs[j].size() || first_str[i] != strs[j][i]) {
                        return result;
                    }
                }
                result.push_back(first_str[i]);
            }
            return result;
        }
};
```
