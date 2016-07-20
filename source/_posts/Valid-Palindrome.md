title: 验证字符串是否是回文
create_time: 2016/07/20 22:45:09
tags:
- Two Pointers
- String
categories:
- leetcode
- C++

---
## [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
> Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
> For example,
> "A man, a plan, a canal: Panama" is a palindrome.
> "race a car" is not a palindrome.
> Note:
> Have you consider that the string might be empty? This is a good question to ask during an interview.
> For the purpose of this problem, we define empty string as valid palindrome.

### 实现思路
用两个指针分别从首尾扫描，遇到不符合回文的直接返回false，否则指针移动继续检验，最后结束返回true

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Valid-Palindrome.cpp)
```
class Solution {
    public:
        bool isPalindrome(string s) {
            int begin = 0;
            int end = s.size() - 1;
            while (true) {
                while (begin <= end && !isAlphanumericCharacters(s[begin])) {
                    ++begin;
                }
                while (begin <= end && !isAlphanumericCharacters(s[end])) {
                    --end;
                }
                if (begin >= end) {
                    break;
                } else if (tolower(s[begin]) == tolower(s[end])) {
                    ++begin;
                    --end;
                } else {
                    return false;
                }
            }
            return true;
        }
    private:
        bool isAlphanumericCharacters(const char c) {
            return (c >= '0' && c <= '9') || (c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z');
        }
};
```
