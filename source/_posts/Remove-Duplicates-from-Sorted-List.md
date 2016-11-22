title: 已排序的链表中删除重复的节点
date: 2016/03/09 14:01:06
tags:
- Linked List
categories:
- leetcode
- C++

---
## [Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)
> Given a sorted linked list, delete all duplicates such that each element appear only once.
> For example,
> Given 1->1->2, return 1->2.
> Given 1->1->2->3->3, return 1->2->3.

### 实现思路
遍历链表，比较前后节点的值是否相同，相同的话删除同时调节链表指针指向。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Remove-Duplicates-from-Sorted-List.cpp)
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
        ListNode* deleteDuplicates(ListNode* head) {
            if (!head) {
                return NULL;
            }
            ListNode* l = head;
            ListNode* node = head;
            while (node) {
                ListNode* nextNode = node->next;
                if (!nextNode) {
                    break;
                }
                if (node->val == nextNode->val) {
                    // delete
                    node->next = nextNode->next;
                    delete nextNode;
                } else {
                    node = nextNode;
                }
            }
            return l;
        }
};
```
