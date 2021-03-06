title: 二叉搜索树第k小的元素
date: 2016/03/30 21:21:35
tags:
- Tree
- Binary Search
categories:
- leetcode
- C++

---
## [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
> Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
> Note: 
> You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
> Follow up:
> What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

### 实现思路
二叉搜索树的第k小的元素，其实就是二叉搜索树的中序遍历的第k个元素。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Kth-Smallest-Element-in-a-BST.cpp)
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
        int kthSmallest(TreeNode* root, int k) {
            std::stack<TreeNode*> s;
            TreeNode* node = root;
            while (node) {
                s.push(node);
                node = node->left;
            }
            int x = 1;
            while (!s.empty() && x <= k) {
                node = s.top();
                s.pop();
                x += 1;
                TreeNode* rightNode = node->right;
                while (rightNode) {
                    s.push(rightNode);
                    rightNode = rightNode->left;
                }
            }
            return node->val;
        }
};
```
