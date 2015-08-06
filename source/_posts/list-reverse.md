title: 单链表反转
date: 2015/08/04 23:08:00
tags: 
- 链表
- C/C++
categories: C/C++

---
> 题目描述：输入一个单向链表，输出逆序反转后的链表
> 
> 分析：链表的转置是面试当中比较喜欢出的数据结构题了，算法也比较简单，遍历链表的同时调整指针指向就可以了。

<!-- more -->

## 节点定义
	typedef struct listNode
	{
	    int value;
	    struct listNode *next;
	} listNode;
	
## 创建链表
	listNode *createList()
	{
	    listNode *head = 0;
	    listNode *tail = 0;
	    const size_t len = 10;
	    for (size_t i = 0; i < len; ++i)
	    {
	        listNode *node = new listNode;
	        node->value = i;
	        node->next = 0;
	        if (i == 0)
	            head = tail = node;
	        else
	        {
	            tail->next = node;
	            tail = node;
	        }
	    }

	    return head;
	}
	
## 反转
	listNode *reverse(listNode *head)
	{
	    listNode *currentNode = 0;
	    listNode *nextNode = 0;
	    while (head)
	    {
	        nextNode = head->next;
	        head->next = currentNode;
	        currentNode = head;
	        head = nextNode;
	    }
	    return currentNode;
	}
	
## 输出
	void printList(listNode *head)
	{
	    while (head)
	    {
	        std::cout << head->value << " ";
	        head = head->next;
	    }
	    std::cout << std::endl;
	}
	
## 释放链表资源
	void freeList(listNode *head)
	{
	    listNode *freeNode = 0;
	    while (head)
	    {
	        freeNode = head;
	        head = head->next;
	        delete freeNode;
	    }
	}
	
## 测试
	int main()
	{
	    listNode *head = createList();
	    printList(head);
	    head = reverse(head);
	    print_list(head);
	    freeList(head);
	}