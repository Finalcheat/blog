title: 判断二叉树是否相同
date: 2016/03/07 14:01:05
tags:
- Tree
- Depth-first Search
categories:
- leetcode
- C++

---
## [Same Tree](https://leetcode.com/problems/same-tree/)
> Given two binary trees, write a function to check if they are equal or not.
> Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

### 实现思路
判断当前节点值是否相等，若相等则递归调用左右子树。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Same-Tree.cpp)
```
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
    public:
        bool isSameTree(TreeNode* p, TreeNode* q) {
            if (p == NULL && p == q) {
                return true;
            }
            if (p && q) {
                if (p->val != q->val) {
                    return false;
                } else {
                    return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
                }
            } else {
                return false;
            }
        }
};
```
