title: 二叉树最小深度
date: 2016/03/24 15:29:09
tags:
- Tree
- Depth-first Search
- Breadth-first Search
categories:
- leetcode
- C++

---
## [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)
> Given a binary tree, find its minimum depth.
> The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

### 实现思路
递归解法。
以下情况:
- 节点为空，返回0
- 节点的左子树为空，返回1+右子树最小深度
- 节点的右子树为空，返回1+左子树最小深度
- 节点的左右子树非空，返回1+min(左子树最小深度, 右子树最小深度)

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Minimum-Depth-of-Binary-Tree.cpp)
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
        int minDepth(TreeNode* root) {
            if (root == NULL) {
                return 0;
            }
            if (root->left == NULL) {
                return 1 + minDepth(root->right);
            }
            if (root->right == NULL) {
                return 1 + minDepth(root->left);
            }
            return 1 + std::min(minDepth(root->left), minDepth(root->right));
        }
};
```
