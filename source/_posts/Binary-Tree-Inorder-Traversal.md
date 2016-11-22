title: 二叉树中序遍历(非递归)
date: 2016/03/11 13:59:56
tags:
- Tree
- Stack
- Hash Table
categories:
- leetcode
- C++

---
## [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
> Given a binary tree, return the inorder traversal of its nodes' values.
> For example:
> Given binary tree {1,#,2,3},
> return [1,3,2].

### 实现思路
用栈作辅助，一直向左走并且将节点压栈，直到为空然后出栈得到父节点，接着向右走即可完成中序遍历。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Binary-Tree-Inorder-Traversal.cpp)
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
        vector<int> inorderTraversal(TreeNode* root) {
            if (root == NULL) {
                return vector<int>();
            }
            vector<int> result;
            std::stack<TreeNode*> s;
            TreeNode* node = root;
            while (node != NULL || !s.empty()) {
                if (node) {
                    s.push(node);
                    node = node->left;
                } else {
                    node = s.top();
                    s.pop();
                    result.push_back(node->val);
                    node = node->right;
                }
            }
            return result;
        }
};
```
