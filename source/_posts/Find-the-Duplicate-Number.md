title: 重复的数字
date: 2016/04/30 16:30:56
tags:
- Binary Search
- Array
- Two Pointers
categories:
- leetcode
- C++

---
## [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)
> Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.
> Note:
> * You must not modify the array (assume the array is read only).
> * You must use only constant, O(1) extra space.
> * Your runtime complexity should be less than O(n2).
> * There is only one duplicate number in the array, but it could be repeated more than once.

### 实现思路
[鸽巢原理](https://zh.wikipedia.org/wiki/%E9%B4%BF%E5%B7%A2%E5%8E%9F%E7%90%86)，然后利用二分查找的思想搜索。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Find-the-Duplicate-Number.cpp)
```
class Solution {
    public:
        int findDuplicate(vector<int>& nums) {
            int min = 0;
            int max = nums.size() - 1;
            while (min <= max) {
                int middle = min + (max - min) / 2;
                int count = 0;
                for (size_t i = 0; i < nums.size(); ++i) {
                    if (nums[i] <= middle) {
                        ++count;
                    }
                }
                if (count > middle) {
                    max = middle - 1;
                } else {
                    min = middle + 1;
                }
            }
            return min;
        }
};
```
