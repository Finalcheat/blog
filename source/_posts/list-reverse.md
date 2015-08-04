title: 单链表反转
date: 2015/08/04 23:08:00
tags: 链表
categories: C/C++

---
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