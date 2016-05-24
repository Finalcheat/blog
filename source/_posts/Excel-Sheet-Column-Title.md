title: Excel列标题
create_time: 2016/05/24 21:16:15
tags:
- Math
categories:
- leetcode
- C++

---
## [Excel Sheet Column Title](https://leetcode.com/problems/excel-sheet-column-title/)
> Given a positive integer, return its corresponding column title as appear in an Excel sheet.
> For example:
> 1 -> A
> 2 -> B
> 3 -> C
> ...
> 26 -> Z
> 27 -> AA
> 28 -> AB 

### 实现思路
不断除以26即可，注意余数为0的情况。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Excel-Sheet-Column-Title.cpp)
```
class Solution {
    public:
        string convertToTitle(int n) {
            std::string result;
            while (n) {
                const int num = n % 26;
                char c;
                if (num > 0) {
                    c = 'A' + num - 1;
                } else {
                    c = 'Z';
                    --n;
                }
                result.insert(0, 1, c);
                n = n / 26;
            }
            return result;
        }
};
```
