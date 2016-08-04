title: 找出数组中出现一次的数字
date: 2016/03/06 15:42:19
tags:
- Hash Table
- Bit Manipulation
categories:
- leetcode
- C++

---
## [Single Number](https://leetcode.com/problems/single-number/)
> Given an array of integers, every element appears twice except for one. Find that single one.

### 实现思路
利用两个相同的数做异或操作为0，0跟任意数异或得到其本身的特点解决此题。

### [code](https://github.com/Finalcheat/leetcode/blob/master/src/Single-Number.cpp)
```
class Solution {
    public:
        int singleNumber(vector<int>& nums) {
            int result = 0;
            for (size_t i = 0; i < nums.size(); ++i) {
                result ^= nums[i];
            }
            return result;
        }
};
```
