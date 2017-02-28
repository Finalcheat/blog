title: 查找二叉树中每一层的最大值
date: 2017/02/28 20:28:35
tags:
- Tree
- Depth-first Search
- Breadth-first Search
categories:
- leetcode
- C++

---
## [Find Largest Value in Each Tree Row](https://leetcode.com/problems/find-largest-value-in-each-tree-row/)
> You need to find the largest value in each row of a binary tree.
> Example:
> Input: 
<pre>
           1
          / \
         3   2
        / \   \
       5   3   9
</pre>
> Output: [1, 3, 9]

### 实现思路
二叉树层序遍历过程中找最大值即可。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Find-Largest-Value-in-Each-Tree-Row.cpp)
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
        vector<int> largestValues(TreeNode* root) {
            if (!root) {
                return vector<int>();
            }
            std::queue<TreeNode*> q;
            q.push(root);
            vector<int> result;
            while (!q.empty()) {
                const size_t levelLen = q.size();
                TreeNode* node = q.front();
                int levelMax = node->val;
                q.pop();
                if (node->left) {
                    q.push(node->left);
                }
                if (node->right) {
                    q.push(node->right);
                }
                for (size_t i = 1; i < levelLen; ++i) {
                    node = q.front();
                    q.pop();
                    if (node->val > levelMax) {
                        levelMax = node->val;
                    }
                    if (node->left) {
                        q.push(node->left);
                    }
                    if (node->right) {
                        q.push(node->right);
                    }
                }
                result.push_back(levelMax);
            }
            return result;
        }
};
```