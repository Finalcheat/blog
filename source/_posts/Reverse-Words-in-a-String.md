title: 字符串反转单词
date: 2016/06/21 21:38:37
tags:
- String
categories:
- leetcode
- C++

---
## [Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/)
> Given an input string, reverse the string word by word.
> For example,
> Given s = "the sky is blue",
> return "blue is sky the".
> Update (2015-02-12):
> For C programmers: Try to solve it in-place in O(1) space.
> Clarification:
> * What constitutes a word?
> A sequence of non-space characters constitutes a word.
> * Could the input string contain leading or trailing spaces?
> Yes. However, your reversed string should not contain leading or trailing spaces.
> * How about multiple spaces between two words?
> Reduce them to a single space in the reversed string.

### 实现思路
遍历过程找到单词的起始和结束位置，然后将单词提取出来，注意字符串首尾有空格以及单词间多个空格的情况。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Reverse-Words-in-a-String.cpp)
```
class Solution {
    public:
        void reverseWords(string &s) {
            auto startIt = s.rbegin();
            auto endIt = s.rbegin();
            std::string result;
            while (startIt != s.rend()) {
                while (startIt != s.rend() && *startIt == ' ') {
                    ++startIt;
                }
                endIt = std::find(startIt, s.rend(), ' ');
                if (startIt != endIt) {
                    std::reverse(startIt, endIt);
                    result += std::string(startIt, endIt);
                    result += " ";
                }
                startIt = endIt;
            }
            if (!result.empty()) {
                result.resize(result.size() - 1);
            }
            s = result;
        }
};
```
