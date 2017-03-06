title: Fizz Buzz
date: 2017/03/06 21:18:00
tags:
- String
categories:
- leetcode
- C++

---
## [Fizz Buzz](https://leetcode.com/problems/fizz-buzz/)
> Write a program that outputs the string representation of numbers from 1 to n.
> But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
> Example:
<pre>
n = 15,
Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
</pre>

### 实现思路
很简单的一道题目，循环中判断是否被3，5整除然后输出对应的FizzBuzz即可。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Fizz-Buzz.cpp)
```
class Solution {
    public:
        vector<string> fizzBuzz(int n) {
            vector<string> result;
            for (int i = 1; i <= n; ++i) {
                string s;
                if (i % 3 == 0) {
                    s = "Fizz";
                }
                if (i % 5 == 0) {
                    s += "Buzz";
                }
                if (i % 3 && i % 5) {
                    s = std::to_string(i);
                }
                result.push_back(s);
            }
            return result;
        }
};
```
