title: 单链表删除倒数第n个节点
create_time: 2016/03/18 15:22:34
tags:
- Linked List
- Two Pointers
categories:
- leetcode
- C++

---
## [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
> Given a linked list, remove the nth node from the end of list and return its head.
> For example,
> Given linked list: 1->2->3->4->5, and n = 2.
> After removing the second node from the end, the linked list becomes 1->2->3->5.

### 实现思路
两个指针，一个指针先走n步，然后两个指针同时前进，当先走的指针next为空的时候就找到了要删除的节点。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Remove-Nth-Node-From-End-of-List.cpp)
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
        ListNode* removeNthFromEnd(ListNode* head, int n) {
            if (head == NULL) {
                return NULL;
            }
            ListNode* node = head;
            while (n-- && node) {
                node = node->next;
            }
            ListNode* prevNode = head;
            while (node && node->next) {
                prevNode = prevNode->next;
                node = node->next;
            }
            ListNode* nextNode = prevNode->next;
            if (nextNode && node) {
                prevNode->next = nextNode->next;
                delete nextNode;
            } else {
                node = head;
                head = head->next;
                delete node;
            }
            return head;
        }
};
```
