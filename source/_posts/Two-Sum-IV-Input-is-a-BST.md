title: 两个数的和IV-输入是排序二叉树
date: 2017/11/05 20:13:00
tags:
- Tree
categories:
- leetcode
- C++

---
## [Two Sum IV - Input is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/)
> Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.
> Example 1:
> <pre>
> Input:
>     5
>    / \
>   3   6
>  / \   \
> 2   4   7
> Target = 9
> Output: True
> </pre>
> Example 2:
> <pre>
> Input:
>     5
>    / \
>   3   6
>  / \   \
> 2   4   7
> Target = 28
> Output: False
> </pre>

### 实现思路
使用set作为辅助结构，遍历二叉树过程中判断k与节点的差值是否在set中，若是则为true，否则为false并插入节点值到set中然后继续遍历左右子树。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Two-Sum-IV-Input-is-a-BST.cpp)
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
        bool findTarget(TreeNode* root, int k) {
            std::set<int> s;
            return findTarget(root, s, k);
        }

    private:
        bool findTarget(TreeNode* node, std::set<int>& s, const int k) {
            if (node) {
                const int val = node->val;
                auto iter = s.find(k - val);
                if (iter != s.end()) {
                    return true;
                } else {
                    s.insert(val);
                    return findTarget(node->left, s, k) || findTarget(node->right, s, k);
                }
            } else {
                return false;
            }
        }
};
```
