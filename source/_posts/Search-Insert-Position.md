title: 搜索插入的位置
create_time: 2016/03/10 13:44:05
tags:
- Array
- Binary Search
categories:
- leetcode
- C++

---
## [Search Insert Position](https://leetcode.com/problems/search-insert-position/)
> Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
> You may assume no duplicates in the array.
> Here are few examples.
> [1,3,5,6], 5 → 2
> [1,3,5,6], 2 → 1
> [1,3,5,6], 7 → 4
> [1,3,5,6], 0 → 0

### 实现思路
数组已排序，用二分搜索即可。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Search-Insert-Position.cpp)
```
class Solution {
    public:
        int searchInsert(vector<int>& nums, int target) {
            int begin = 0;
            int end = nums.size() - 1;
            while (begin <= end) {
                const int middle = (begin + end) / 2;
                if (nums[middle] < target) {
                    begin = middle + 1;
                } else {
                    end = middle - 1;
                }
            }
            return begin;
        }
};
```
