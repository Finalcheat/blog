title: 二叉树前序遍历转成链表
date: 2016/05/31 21:23:09
tags:
- Tree
- Depth-first Search
categories:
- leetcode
- C++

---
## [Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)
> Given a binary tree, flatten it to a linked list in-place.
> For example,
> Given
>
<pre>
       1
      / \
     2   5
    / \   \
   3   4   6
</pre>
> 
> The flattened tree should look like:
<pre>
 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
</pre>

### 实现思路
前序遍历放到队列中，然后从队列中取出元素调整指针指向即可。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Flatten-Binary-Tree-to-Linked-List.cpp)
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
        void flatten(TreeNode* root) {
            if (!root) {
                return;
            }
            std::stack<TreeNode*> s;
            std::queue<TreeNode*> q;
            s.push(root);
            while (!s.empty()) {
                TreeNode* node = s.top();
                s.pop();
                if (node->right) {
                    s.push(node->right);
                }
                if (node->left) {
                    s.push(node->left);
                }
                q.push(node);
            }
            
            TreeNode* preNode = NULL;
            while (!q.empty()) {
                TreeNode* node = q.front();
                q.pop();
                node->left = NULL;
                node->right = NULL;
                if (preNode) {
                    preNode->right = node;
                }
                preNode = node;
            }
        }
};
```
