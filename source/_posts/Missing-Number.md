title: 丢失的数字
create_time: 2016/03/08 19:13:02
tags:
- leetcode
- C++
categories:
- leetcode

---
## [Missing Number](https://leetcode.com/problems/missing-number/)
> Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
> For example,
> Given nums = [0, 1, 3] return 2.

### 实现思路
使用等差数列计算出总和，然后遍历减去数组上的数即可。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Missing-Number.cpp)
```
class Solution {
    public:
        int missingNumber(vector<int>& nums) {
            int sum = nums.size() * (nums.size() + 1) / 2;
            for (size_t i = 0; i < nums.size(); ++i) {
                sum -= nums[i];
            }
            return sum;
        }
};
```
