title: 二叉树的层平均值
date: 2017/10/18 22:25:00
tags:
- Tree
categories:
- leetcode
- C++

---
## [Average of Levels in Binary Tree](https://leetcode.com/problems/average-of-levels-in-binary-tree/description/)
> Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
> Example 1:
> <pre>
> Input:
>     3
>    / \
>   9  20
>     /  \
>    15   7
> Output: [3, 14.5, 11]
> Explanation:
> The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
> </pre>

### 实现思路
二叉树层序遍历求平均值即可，注意溢出。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Average-of-Levels-in-Binary-Tree.cpp)
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
        vector<double> averageOfLevels(TreeNode* root) {
            vector<double> result;
            std::queue<TreeNode*> levelNodes;
            levelNodes.push(root);
            while (!levelNodes.empty()) {
                int len = levelNodes.size();
                int64_t sum = 0;
                int count = 0;
                for (size_t i = 0; i < len; ++i) {
                    TreeNode* node = levelNodes.front();
                    sum += node->val;
                    ++count;
                    if (node->left) {
                        levelNodes.push(node->left);
                    }
                    if (node->right) {
                        levelNodes.push(node->right);
                    }
                    levelNodes.pop();
                }
                result.push_back((double)sum / count);
            }
            return result;
        }
};
```
