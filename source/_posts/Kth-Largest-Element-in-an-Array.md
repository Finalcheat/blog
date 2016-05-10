title: 数组中第k大的元素
create_time: 2016/05/10 20:48:07
tags:
- Heap
- Divide and Conquer
categories:
- leetcode
- C++

---
## [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
> Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
> For example,
> Given [3,2,1,5,6,4] and k = 2, return 5.
> Note: 
> You may assume k is always valid, 1 ≤ k ≤ array's length.

### 实现思路
> 两种解法:
> * 最简单的解法就是对整个数组排序，然后取第k个位置的元素即可。
> * 标准的做法是建立一个k大小的最大堆，遍历数组发现有比最大堆最小元素还大的给替换掉，然后重新调整最大堆以维持堆的性质。下面会用std::vector模拟，只是为了简单的说明解法，实际情况应该使用heap替换，否则性能比较差。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Kth-Largest-Element-in-an-Array.cpp)
```
class Solution {
    public:
        int findKthLargest(vector<int>& nums, int k) {
            // 简单解法，排序取第k项即可。
            std::sort(nums.begin(), nums.end(), std::greater<int>());
            return nums[k - 1];
        }
        
        int _findKthLargest(vector<int>& nums, int k) {
            // 标准做法，这里只是演示，并没有用堆，实际中应该使用heap替换掉std::vector
            std::vector<int> sortNum(k);
            std::copy(nums.begin(), nums.begin() + k, sortNum.begin());
            std::sort(sortNum.begin(), sortNum.end(), std::greater<int>());
            for (size_t i = k; i < nums.size(); ++i) {
                if (nums[i] > sortNum[k - 1]) {
                    // 发现有比"最大堆"最小元素还大的元素，替换掉
                    sortNum[k - 1] = nums[i];
                    // 重新调整"最大堆"使得它维持堆的性质
                    std::sort(sortNum.begin(), sortNum.end(), std::greater<int>());
                }
            }
            return sortNum[k - 1];
        }
};
```
