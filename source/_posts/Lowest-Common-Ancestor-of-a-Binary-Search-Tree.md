title: 二叉搜索树最近公共祖先
date: 2016/06/01 20:20:01
tags:
- Tree
categories:
- leetcode
- C++

---
## [Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)
> Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
> According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”
>
<pre>
>       _______6______
>      /              \
>   ___2__          ___8__
>  /      \        /      \
>  0      _4       7       9
>        /  \
>        3   5
</pre>
>
> For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

### 实现思路
递归解法，三种情况:
* 两节点在当前节点的两边，LCA就是当前节点
* p节点的值比当前节点的值小，LCA在当前节点的左子树
* p节点的值比当前节点的值大，LCA在当前节点的右子树

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Lowest-Common-Ancestor-of-a-Binary-Search-Tree.cpp)
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
        TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
            if ((p->val - root->val) * (root->val - q->val) >= 0) {
                return root;
            } else if (p->val < root->val) {
                return lowestCommonAncestor(root->left, p, q);
            } else {
                return lowestCommonAncestor(root->right, p, q);
            }
        }
};
```
