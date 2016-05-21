title: 两个数组的相同数字
create_time: 2016/05/21 17:19:06
tags:
- Binary Search
- Hash Table
- Two Pointers
- Sort
categories:
- leetcode
- C++

---
## [Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/)
> Given two arrays, write a function to compute their intersection.
> Example:
> Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
> Note:
> * Each element in the result must be unique.
> * The result can be in any order.

### 实现思路
将nums1数组转成hash table数据结构以便快速搜索，遍历nums2数组，若找到则插入新的hash table里面去，最后将hash table中的值拷贝到vector。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Intersection-of-Two-Arrays.cpp)
```
class Solution {
    public:
        vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
            std::unordered_set<int> numsHash;
            for (size_t i = 0; i < nums1.size(); ++i) {
                numsHash.insert(nums1[i]);
            }
            std::unordered_set<int> setResult;
            for (size_t i = 0; i < nums2.size(); ++i) {
                int num = nums2[i];
                if (numsHash.find(num) != numsHash.end()) {
                    setResult.insert(num);
                }
            }
            std::vector<int> result(setResult.size());
            std::copy(setResult.begin(), setResult.end(), result.begin());
            return result;
        }
};
```
