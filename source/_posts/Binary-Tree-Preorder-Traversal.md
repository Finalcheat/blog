title: 二叉树非递归前序遍历
create_time: 2016/03/08 19:22:35
tags:
- leetcode
- C++
categories:
- leetcode

---
## [Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)
> Given a binary tree, return the preorder traversal of its nodes' values.
> For example:
> Given binary tree {1,#,2,3},
> return [1,2,3].

### 实现思路
要求不能用递归，可以使用栈作为辅助，将左右子树压入栈中即可。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Binary-Tree-Preorder-Traversal.cpp)
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
        vector<int> preorderTraversal(TreeNode* root) {
            if (root == NULL) {
                return vector<int>();
            }
            std::stack<TreeNode*> s;
            s.push(root);
            std::vector<int> result;
            while (!s.empty()) {
                TreeNode * node = s.top();
                s.pop();
                result.push_back(node->val);
                if (node->right) {
                    s.push(node->right);
                }
                if (node->left) {
                    s.push(node->left);
                }
            }
            return result;
        }
};
```

