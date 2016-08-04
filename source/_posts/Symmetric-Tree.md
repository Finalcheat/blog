title: 判断二叉树是否对称
date: 2016/03/21 14:08:36
tags:
- Tree
- Depth-first Search
categories:
- leetcode
- C++

---
## [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)
> Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

### 实现思路
递归解法。
满足以下条件为真:
- 当前两个节点值相等。
- 左子树与右子树对称。
- 右子树与左子树对称。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Symmetric-Tree.cpp)
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
        bool isSymmetric(TreeNode* root) {
            if (root == NULL) {
                return true;
            } else {
                return isSymmetric(root->left, root->right);
            }
        }
        
    private:
        bool isSymmetric(TreeNode* left, TreeNode* right) {
            if (left == NULL) {
                return right == NULL;
            } else if (right == NULL) {
                return false;
            }
            if (left->val != right->val) {
                return false;
            } else {
                return isSymmetric(left->left, right->right) && isSymmetric(left->right, right->left);
            }
        }
};
```
