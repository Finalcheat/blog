title: 验证是否包含重复值
create_time: 2016/03/07 15:10:08
tags:
- leetcode
- C++
categories:
- leetcode

---
## [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
> Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

### 实现思路
对数组排序，排序后相同的值必定连在一起，遍历一遍验证即可。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Contains-Duplicate.cpp)
```
class Solution {
    public:
        bool containsDuplicate(vector<int>& nums) {
            std::sort(nums.begin(), nums.end());
            for (size_t i = 1; i < nums.size(); ++i) {
                if (nums[i] == nums[i - 1]) {
                    return true;
                }
            }
            return false;
        }
};
```
