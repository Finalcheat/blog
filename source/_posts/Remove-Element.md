title: 删除元素
create_time: 2016-05-01
tags:
- Array
- Two Pointers
categories:
- leetcode
- C++

---
## [Remove Element](https://leetcode.com/problems/remove-element/)
> Given an array and a value, remove all instances of that value in place and return the new length.
> Do not allocate extra space for another array, you must do this in place with constant memory.
> The order of elements can be changed. It doesn't matter what you leave beyond the new length.
> Example:
> Given input array nums = [3,2,2,3], val = 3
> Your function should return length = 2, with the first two elements of nums being 2.

### 实现思路
循环遍历将不等于val的元素拷贝到新位置newIndex，最后newIndex的值就是“新数组”的长度。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Remove-Element.cpp)
```
class Solution {
    public:
        int removeElement(vector<int>& nums, int val) {
            size_t newIndex = 0;
            for (size_t i = 0; i < nums.size(); ++i) {
                if (nums[i] != val) {
                    nums[newIndex] = nums[i];
                    ++newIndex;
                }
            }
            return newIndex;
        }
};
```
