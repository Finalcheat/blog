title: 设置矩阵零值
create_time: 2016/06/02 20:34:56
tags:
- Array
categories:
- leetcode
- C++

---
## [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

### 实现思路
使用额外的空间保存要设置零值的行列，然后遍历一遍查找即可。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Set-Matrix-Zeroes.cpp)
```
class Solution {
    public:
        void setZeroes(vector<vector<int>>& matrix) {
            vector<bool> rows(matrix.size());
            vector<bool> columns(matrix[0].size());
            for (size_t i = 0; i < matrix.size(); ++i) {
                for (size_t j = 0; j < matrix[i].size(); ++j) {
                    if (matrix[i][j] == 0) {
                        rows[i] = true;
                        columns[j] = true;
                    }
                }
            }
            for (size_t i = 0; i < matrix.size(); ++i) {
                for (size_t j = 0; j < matrix[i].size(); ++j) {
                    if (rows[i] || columns[j]) {
                        matrix[i][j] = 0;
                    }
                }
            }
        }
};
```
