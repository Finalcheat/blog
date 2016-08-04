title: Excel表格列标题
date: 2016/03/07 14:50:57
tags:
- Math
categories:
- leetcode
- C++

---
## [Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number/)
> Given a column title as appear in an Excel sheet, return its corresponding column number.
> For example:
> A -> 1
> B -> 2
> C -> 3
> ...
> Z -> 26
> AA -> 27
> AB -> 28

### 实现思路
很简单，就像16进制转10进制的计算方法即可，只不过这个是26进制。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Excel-Sheet-Column-Number.cpp)
```
class Solution {
    public:
        int titleToNumber(string s) {
            int result = 0;
            int pos = 1;
            for (int i = s.size() - 1; i >= 0; --i) {
                result += (s[i] - 'A' + 1) * pos;
                pos *= 26;
            }
            return result;
        }
};
```
