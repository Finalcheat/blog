title: 二叉树最大深度
create_time: 2016/03/06 16:01:57
tags:
- leetcode
- C++
categories:
- leetcode

---
## [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
> Given a binary tree, find its maximum depth.
> The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

### 实现思路
使用递归解法最简单，二叉树的最大深度等于1+左右子树中的最大深度

### [code](https://github.com/Finalcheat/leetcode/blob/master/src/Maximum-Depth-Of-Binary-Tree.cpp)
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
        int maxDepth(TreeNode* root) {
            if (root == NULL) {
                return 0;
            }
            return 1 + std::max(maxDepth(root->left), maxDepth(root->right));
        }
};
```
