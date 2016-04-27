title: 二叉树添加next指针
create_time: 2016/04/27 20:11:35
tags:
- Tree
- Depth-first Search
categories:
- leetcode
- C++

---
## [Populating Next Right Pointers in Each Node II](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/)
> Follow up for problem "Populating Next Right Pointers in Each Node".
> What if the given tree could be any binary tree? Would your previous solution still work?
> For example,
> Given the following binary tree,
> 
<pre>
          1
         /  \
        2    3
       / \    \
      4   5    7
</pre>
> 
> After calling your function, the tree should look like:
<pre>
          1 -> NULL
         /  \
        2 -> 3 -> NULL
       / \    \
      4-> 5 -> 7 -> NULL
</pre>

### 实现思路
使用队列作为辅助结构，用层次遍历的方法在循环中操作每层的节点，调整next指针指向。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Populating-Next-Right-Pointers-in-Each-Node-II.cpp)
```
/**
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  TreeLinkNode *left, *right, *next;
 *  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
 * };
 */
class Solution {
    public:
        void connect(TreeLinkNode *root) {
            if (root == NULL) {
                return;
            }
            std::queue<TreeLinkNode*> q;
            q.push(root);
            while (!q.empty()) {
                const size_t levelSize = q.size();
                TreeLinkNode* nextLinkNode = NULL;
                for (size_t i = 0; i < levelSize; ++i) {
                    TreeLinkNode* currentNode = q.front();
                    if (currentNode->right) {
                        q.push(currentNode->right);
                    }
                    if (currentNode->left) {
                        q.push(currentNode->left);
                    }
                    currentNode->next = nextLinkNode;
                    nextLinkNode = currentNode;
                    q.pop();
                }
            }
        }
};
```
