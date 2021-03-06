title: 交换链表中的两个节点
date: 2016/04/06 21:02:07
tags:
- Linked List
categories:
- leetcode
- C++

---
## [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)
> Given a linked list, swap every two adjacent nodes and return its head.
> For example,
> Given 1->2->3->4, you should return the list as 2->1->4->3.
> Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

### 实现思路
遍历链表，同时用两个指针，一个记录新表头，一个记录已处理的表尾用于链接未处理的节点。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Swap-Nodes-in-Pairs.cpp)
```
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
    public:
        ListNode* swapPairs(ListNode* head) {
            if (!head || !head->next) {
                return head;
            }
            ListNode* newHead = NULL;
            ListNode* tailNode = NULL;
            while (head) {
                ListNode* nextNode = head->next;
                if (!nextNode) {
                    break;
                }
                head->next = nextNode->next;
                nextNode->next = head;
                
                if (tailNode) {
                    tailNode->next = nextNode;
                    tailNode = head;
                } else {
                    tailNode = head;
                    newHead = nextNode;
                }
                head = head->next;
            }
            return newHead;
        }
};
```
