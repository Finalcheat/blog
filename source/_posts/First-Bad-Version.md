title: 第一个坏的版本
create_time: 2016/05/26 22:07:08
tags:
- Binary Search
categories:
- leetcode
- C++

---
## [First Bad Version](https://leetcode.com/problems/first-bad-version/)
> You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
> Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
> You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

实现思路
二分查找的思路解题即可。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/First-Bad-Version.cpp)
```
// Forward declaration of isBadVersion API.
bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        if (n == 1) {
            return 1;
        }
        int begin = 1;
        int end = n;
        while (begin < end) {
            int middle = begin + (end - begin) / 2;
            if (isBadVersion(middle)) {
                end = middle;
            } else {
                begin = middle + 1;
            }
        }
        return end;
    }
};
```
