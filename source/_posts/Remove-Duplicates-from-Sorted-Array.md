title: 从已排序的数组中删除重复的元素
create_time: 2016/05/06 20:35:09
tags:
- Array
- Two Pointers
categories:
- leetcode
- C++

---
## [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
> Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
> Do not allocate extra space for another array, you must do this in place with constant memory.
> For example,
> Given input array nums = [1,1,2],
> Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

### 实现思路
遍历的时候将元素覆盖到前面，重复的跳过，所以需要一个变量判断当前元素是否是重复。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Remove-Duplicates-from-Sorted-Array.cpp)
```
class Solution {
    public:
        int removeDuplicates(vector<int>& nums) {
            if (nums.empty()) {
                return 0;
            }
            int num = nums[0];
            int index = 1;
            for (size_t i = 1; i < nums.size(); ++i) {
                if (nums[i] != num) {
                    nums[index] = nums[i];
                    ++index;
                    num = nums[i];
                }
            }
            return index;
        }
};
```
