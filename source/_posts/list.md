title: 双链表实现
create_time: 2016/03/17 21:17:56
tags:
- Linked List
categories:
- C++

---
## 简单实现双链表
下面给出部分代码以及解析，完整的代码见[这里](https://github.com/Finalcheat/Introduction-to-Algorithms/blob/master/src/list.cpp)

## 节点定义
```
template <typename T>
struct ListNode
{
    typedef ListNode<T>* PtNode;
    PtNode prev;
    PtNode next;
    T data;
};
```
节点有3个数据成员，分别是指向前节点的指针prev、指向后节点的指针next、以及节点的数据data。


## 迭代器定义
```
template <typename T>
struct ListNodeIterator
{
    typedef ListNodeIterator<T> iterator;
    typedef T* pointer;
    typedef T& reference;

    ListNodeIterator() : node(nullptr) {}
    ListNodeIterator(ListNode<T>* _node) : node(_node) {}
    ListNodeIterator(const ListNodeIterator& n) : node(n.node) {}

    bool operator==(const ListNodeIterator& n) { return this->node == n.node; }
    bool operator!=(const ListNodeIterator& n) { return this->node != n.node; }
    reference operator*() const { return node->data; }
    pointer operator->() const { return &(node->data); }
    iterator& operator++() { node = node->next; return *this; }
    iterator operator++(int) { iterator tmp = *this; ++*this; return tmp; }
    iterator& operator--() { node = node->prev; return *this; }
    iterator operator--(int) { iterator tmp = *this; --*this; return tmp; }

    ListNode<T>* node;
};
```
迭代器主要用于封装节点ListNode的操作，重载++、--等操作符使得迭代器的行为像指针一样操作。


## 链表定义
```
template <typename T>
class List
{
    public:
        typedef ListNodeIterator<T> iterator;

    public:
        List() : head(nullptr), tail(nullptr) {}
        List(const T& v) : head(nullptr), tail(nullptr) { insert(v); }
        ~List();

    public:
        ListNode<T>* search(const T& v);
        void insert(const T& v);
        void push(const T& v);
        void remove(const T& v);
        iterator begin() { return iterator(head); }
        iterator end() { return nullptr; }

    private:
        ListNode<T>* head;
        ListNode<T>* tail;
};
```
链表包含头尾节点的指针，同时定义了insert、push、remove等函数用于链表操作。begin、end返回头、尾节点的迭代器。


### search函数实现
> search函数搜索并返回值为v的节点，若找不到，则返回nullptr

```
template <typename T>
ListNode<T>* List<T>::search(const T& v)
{
    for (ListNode<T>* p = head; p != nullptr; p = p->next)
    {
        if (p->data == v)
            return p;
    }
    return nullptr;
}
```
链表的搜索很简单，从头结点开始遍历搜索即可。

### insert函数实现
> insert函数将v插入当前头节点前面，同时更新头节点指向

```
template <typename T>
void List<T>::insert(const T& v)
{
    // 生成新节点
    ListNode<T>* node = new ListNode<T>;
    node->data = v;
    node->prev = nullptr;
    node->next = nullptr;

    if (head == nullptr)
    {
        tail = head = node;
    }
    else
    {
        node->next = head;
        head->prev = node;
        head = node;
    }
}
```
两种情况
- 头结点为空，也就是当前链表一个节点也没有，令新生成的节点为头尾节点。
- 头结点不为空，令新生成的节点next值为头节点，头结点的prev值为新生成的节点，然后更新头结点指向为新生成节点。

### push函数实现
> push函数将v插入当前尾节点后面，同时更新尾节点指向

```
template <typename T>
void List<T>::push(const T& v)
{
    ListNode<T>* node = new ListNode<T>;
    node->data = v;
    node->prev = nullptr;
    node->next = nullptr;
    if (head == nullptr)
    {
        tail = head = node;
    }
    else
    {
        node->prev = tail;
        tail->next = node;
        tail = node;
    }
}
```
也是两种情况，跟insert基本一样，只不过更新操作的是尾节点tail。

### remove函数实现
> remove函数将节点值为v的删除

```
template <typename T>
void List<T>::remove(const T& v)
{
    ListNode<T>* node = List<T>::search(v);
    if (node != nullptr)
    {
        ListNode<T>* prev = node->prev;
        ListNode<T>* next = node->next;

        if (prev != nullptr)
            prev->next = next;
        else
        {
            // delete head node
            head = next;
        }

        if (next != nullptr)
            next->prev = prev;
        else
        {
            // delete tail node
            tail = prev;
        }

        delete node;
    }
}
```
先找到要删除的节点，然后调整被删除节点的前后节点的指针指向即可，要注意的是被删除节点前节点或者后节点为nullptr这种情况。

### 重载<<输出链表
```
template <typename T>
std::ostream& operator<<(std::ostream& os, List<T>& l)
{
    for (typename List<T>::iterator iter = l.begin(); iter != l.end(); ++iter)
    {
        os << *iter << " ";
    }
    return os;
}
```

### 简单使用测试
```
int main()
{
    List<int> l;
    const size_t num = 10;
    for (size_t i = 0; i < num; ++i)
    {
        l.insert(i);
        std::cout << i << " ";
    }
    std::cout << std::endl;

    l.remove(3);
    l.remove(9);
    l.remove(0);

    l.push(99);

    std::cout << l << std::endl;

    return 0;
}
```
编译执行输出
> c++ -std=c++11 list.cpp
> ./a.out
> 0 1 2 3 4 5 6 7 8 9
> 8 7 6 5 4 2 1 99
