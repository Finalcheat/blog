title: 二叉树根到叶节点的路径和
date: 2016/04/24 14:45:56
tags:
- Tree
- Depth-first Search
categories:
- leetcode
- C++

---
## [Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/)
> Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
> An example is the root-to-leaf path 1->2->3 which represents the number 123.
> Find the total sum of all root-to-leaf numbers.
> For example,
> 
<pre>
    1
   / \
  2   3
</pre>
> 
> The root-to-leaf path 1->2 represents the number 12.
> The root-to-leaf path 1->3 represents the number 13.
> Return the sum = 12 + 13 = 25.

### 实现思路
递归，每向下子树节点遍历的时候将数字*10，当遍历到节点为叶节点时结束递归。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Sum-Root-to-Leaf-Numbers.cpp)
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
        int sumNumbers(TreeNode* root) {
            int result = 0;
            return _sumNumbers(root, result);
        }
    private:
        int _sumNumbers(TreeNode* node, int result) {
            if (!node) {
                return 0;
            }
            if (!node->left && !node->right) {
                return result * 10 + node->val;
            }
            result = result * 10 + node->val;
            return _sumNumbers(node->left, result) + _sumNumbers(node->right, result);
        }
};
```
