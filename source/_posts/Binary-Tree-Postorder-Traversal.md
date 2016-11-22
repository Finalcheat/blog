title: 二叉树后序遍历
date: 2016/04/25 20:51:08
tags:
- Tree
- Stack
categories:
- leetcode
- C++

---
## [Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)
> Given a binary tree, return the postorder traversal of its nodes' values.
> For example:
> Given binary tree {1,#,2,3},
> 
<pre>
   1
    \
     2
    /
   3
</pre>
> 
> return [3,2,1].

### 实现思路
递归解析即可，非递归解决比较绕。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Binary-Tree-Postorder-Traversal.cpp)
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
        vector<int> postorderTraversal(TreeNode* root) {
            std::vector<int> result;
            _postorderTraversal(root, result);
            return result;
        }
    private:
        void _postorderTraversal(TreeNode* node, std::vector<int>& result) {
            if (!node) {
                return;
            }
            _postorderTraversal(node->left, result);
            _postorderTraversal(node->right, result);
            result.push_back(node->val);
        }
};
```
