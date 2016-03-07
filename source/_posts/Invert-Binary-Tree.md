title: 反转二叉树
create_time: 2016/03/06 12:14:01
tags:
- leetcode
- C++
categories:
- leetcode

---
## [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)
> Invert a binary tree.
> This problem was inspired by this original tweet by Max Howell:
> Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so fuck off.(^_^)

### 实现思路
将左右子树位置调换，然后对左右子树递归调用即可。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Invert-Binary-Tree.cpp)
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
        TreeNode* invertTree(TreeNode* root) {
            if (root == NULL) {
                return NULL;
            }
            TreeNode* leftNode = root->left;
            TreeNode* rightNode = root->right;
            root->left = rightNode;
            root->right = leftNode;
            invertTree(leftNode);
            invertTree(rightNode);
            return root;
        }
};
```
