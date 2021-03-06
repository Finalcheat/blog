title: 二叉树路径
date: 2016/03/09 14:16:49
tags:
- leetcode
- Tree
- Depth-first Search
categories:
- leetcode
- C++

---
## [Path Sum](https://leetcode.com/problems/path-sum/)
> Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

### 实现思路
叉树的题目一般用递归来解决很方便。思路是判断当前节点的值与给定的sum值相等并且当前节点是叶节点是为真，否则递归调用左右子树

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Path-Sum.cpp)
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
        bool hasPathSum(TreeNode* root, int sum) {
            if (root == NULL) {
                return false;
            }

            // 当前节点值与给定的sum值相等并且是叶节点
            if (sum == root->val && (!root->left) && (!root->right)) {
                return true;
            }

            // 递归调用左右子树
            return hasPathSum(root->left, sum - root->val) || hasPathSum(root->right, sum - root->val);
        }
};
```
