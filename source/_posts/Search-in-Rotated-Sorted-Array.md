title: 搜索旋转数组的元素
date: 2016/05/11 20:54:02

---
## [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
> Suppose a sorted array is rotated at some pivot unknown to you beforehand.
> (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
> You are given a target value to search. If found in the array return its index, otherwise return -1.
> You may assume no duplicate exists in the array.

### 实现思路
二分查找的思想，主要思路是判断[start, middle]、[middle, end]两个区间中哪个区间没有旋转过(也就是那段区间还是有序的)，然后调整start、end指向，注意好边界情况。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Search-in-Rotated-Sorted-Array.cpp)
```
class Solution {
    public:
        int search(vector<int>& nums, int target) {
            int begin = 0;
            int end = nums.size() - 1;
            while (begin <= end) {
                int middle = (begin + end) / 2;
                if (nums[middle] == target) {
                    return middle;
                } 
                
                if (nums[middle] < nums[end]) {  
                    if (nums[middle] < target && target <= nums[end]) {
                        begin = middle + 1;
                    } else {
                        end = middle - 1;
                    }
                } else {  
                    if (nums[begin] <= target && target < nums[middle]) {
                        end = middle - 1;
                    } else {
                        begin = middle + 1;
                    }
                }  
            }
            return -1;
        }
};
```
