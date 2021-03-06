title: 数组中差值为k的数对
date: 2017/04/01 21:09:00
tags:
- Two Pointers
- Array
categories:
- leetcode
- C++

---
## [K-diff Pairs in an Array](https://leetcode.com/problems/k-diff-pairs-in-an-array/)
> Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.
> Example 1:
> <pre>
> Input: [3, 1, 4, 1, 5], k = 2
> Output: 2
> Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
> Although we have two 1s in the input, we should only return the number of unique pairs.
> </pre>
> Example 2:
> <pre>
> Input:[1, 2, 3, 4, 5], k = 1
> Output: 4
> Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
> </pre>
> Example 3:
> <pre>
> Input: [1, 3, 1, 5, 4], k = 0
> Output: 1
> Explanation: There is one 0-diff pair in the array, (1, 1).
> </pre>

### 实现思路
数组排序后用两个指针遍历对比，注意去重以及二分搜索即可。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/K-diff-Pairs-in-an-Array.cpp)
```
class Solution {
    public:
        int findPairs(vector<int>& nums, int k) {
            if (nums.empty()) {
                return 0;
            }
            std::sort(nums.begin(), nums.end());
            int count = 0;
            int prev = nums[0];
            bool find = false;
            for (vector<int>::iterator it = nums.begin(); it != nums.end(); ++it) {
                if (find && (*it == prev)) {
                    continue;
                }
                const int target = *it + k;
                prev = *it++;
                find = std::binary_search(it, nums.end(), target);
                --it;
                if (find) {
                    ++count;
                }
            }
            return count;
        }
};
```
