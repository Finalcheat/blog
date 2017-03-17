title: 找出二叉排序树中出现最多的元素
date: 2017/03/17 21:26:00
tags:
- Tree
categories:
- leetcode
- C++

---
## [Find Mode in Binary Search Tree](https://leetcode.com/problems/find-mode-in-binary-search-tree/)
> Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.
> Assume a BST is defined as follows:
> 1. The left subtree of a node contains only nodes with keys less than or equal to the node's key.
> 2. The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
> 3. Both the left and right subtrees must also be binary search trees.
> For example:
> Given BST [1,null,2,2],
<pre>
   1
    \
     2
    /
   2
</pre>
return [2].
Note: If a tree has more than one mode, you can return them in any order.
Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).

### 实现思路
中序遍历过程中记录当前元素出现次数与当前出现最多的次数，然后比较，相等则添加当前元素到结果中，大于的话则清空结果将当前元素添进结果中同时更新出现最多的次数。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Find-Mode-in-Binary-Search-Tree.cpp)
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
        vector<int> findMode(TreeNode* root) {
            int prevVal = -1;
            int maxCount = 0;
            int curCount = 0;
            vector<int> result;
            BSTSearch(root, prevVal, maxCount, curCount, result);
            return result;
        }

        void BSTSearch(TreeNode* node, int& prevVal, int& maxCount, int& curCount, vector<int>& result)
        {
            if (!node) {
                return;
            }

            BSTSearch(node->left, prevVal, maxCount, curCount, result);

            int val = node->val;
            if (val == prevVal) {
                ++curCount;
            } else {
                curCount = 1;
                prevVal = val;
            }
            if (curCount == maxCount) {
                result.push_back(val);
            } else if (curCount > maxCount) {
                result.clear();
                result.push_back(val);
                maxCount = curCount;
            }

            BSTSearch(node->right, prevVal, maxCount, curCount, result);
        }
};
```
