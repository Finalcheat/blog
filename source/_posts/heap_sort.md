title: 堆
create_time: 2015/08/13 21:20:00
tags:
- 算法
- C/C++
- 排序
- 堆
- 数据结构
categories:
- 算法导论

---
>堆是计算机科学中一类特殊的数据结构的统称。堆通常是一个可以被看做一棵树的数组对象。在队列中，调度程序反复提取队列中第一个作业并运行，因为实际情况中某些时间较短的任务将等待很长时间才能结束，或者某些不短小，但具有重要性的作业，同样应当具有优先权。堆即为解决此类问题设计的一种数据结构

## 基本操作
#### 父节点
```cpp
	inline int _parent(const int i)
	{
	    return i / 2 - 1;
	}
```
#### 左孩子
```cpp
	inline int _left(const int i)
	{
	    return i * 2 + 1;
	}
```
#### 右孩子
```cpp
	inline int _right(const int i)
	{
	    return i * 2 + 2;
	}
```

### 维护堆的性质
```cpp
	void max_heapify(int *arr, const int len, const int i)
	{
	    int left = _left(i);
	    int right = _right(i);
	    int larget = i;
	    if (left < len && arr[left] > arr[i])
	        larget = left;
	    if (right < len && arr[right] > arr[larget])
	        larget = right;
	    if (larget != i)
	    {
	        int tmp = arr[larget];
	        arr[larget] = arr[i];
	        arr[i] = tmp;
	        max_heapify(arr, len, larget);
	    }
	}
```
### 建堆
```cpp
	void build_max_heap(int *arr, const int len)
	{
	    for (int i = len / 2; i >= 0; --i)
	        max_heapify(arr, len, i);
	}
```
### 堆排序
```cpp
	void heap_sort(int *arr, int len)
	{
	    build_max_heap(arr, len);
	    for (int i = len - 1; i > 0; --i)
	    {
	        int tmp = arr[0];
	        arr[0] = arr[i];
	        arr[i] = tmp;
	        max_heapify(arr, --len, 0);
	    }
	}
```