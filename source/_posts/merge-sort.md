title: 归并排序（Merge Sort）
date: 2015/08/04 10:44:00
tags: 
- 排序
- 算法
- C/C++
- Python
categories: 算法导论

---
>归并排序（英语：Merge Sort，或mergesort），是创建在归并操作上的一种有效的[排序算法](https://zh.wikipedia.org/wiki/%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95)，效率为O(n logn)。1945年由[约翰·冯·诺伊曼](https://zh.wikipedia.org/wiki/%E7%BA%A6%E7%BF%B0%C2%B7%E5%86%AF%C2%B7%E8%AF%BA%E4%BC%8A%E6%9B%BC)首次提出。该算法是采用[分治法](https://zh.wikipedia.org/wiki/%E5%88%86%E6%B2%BB%E6%B3%95)（Divide and Conquer）的一个非常典型的应用，且各层分治递归可以同时进行。

## 算法描述
归并操作的过程如下：

1. 申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列
2. 设定两个指针，最初位置分别为两个已经排序序列的起始位置
3. 比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置
4. 重复步骤3直到某一指针到达序列尾
5. 将另一序列剩下的所有元素直接复制到合并序列尾

## C/C++
	void merge(int *arr, unsigned int p, unsigned int q, unsigned int r)
	{
	    const unsigned int tmpArr1Len = q - p + 1;
	    int *tmpArr1 = new int[tmpArr1Len];
	    const unsigned int tmpArr2Len = r - q;
	    int *tmpArr2 = new int[tmpArr2Len];
	    for (unsigned int i = 0; i < tmpArr1Len; ++i)
	    {
	        tmpArr1[i] = arr[p + i];
	    }
	    for (unsigned int i = 0; i < tmpArr2Len; ++i)
	    {
	        tmpArr2[i] = arr[q + i + 1];
	    }
	    unsigned int arrIndex = p;
	    unsigned int tmpArr1Index = 0;
	    unsigned int tmpArr2Index = 0;
	    while (tmpArr1Index < tmpArr1Len && tmpArr2Index < tmpArr2Len)
	    {
	        if (tmpArr1[tmpArr1Index] < tmpArr2[tmpArr2Index])
	        {
	            arr[arrIndex] = tmpArr1[tmpArr1Index];
	            ++tmpArr1Index;
	        }
	        else
	        {
	            arr[arrIndex] = tmpArr2[tmpArr2Index];
	            ++tmpArr2Index;
	        }
	        ++arrIndex;
	    }

	    while (tmpArr1Index < tmpArr1Len)
	    {
	        arr[arrIndex] = tmpArr1[tmpArr1Index];
	        ++arrIndex;
	        ++tmpArr1Index;
	    }

	    while (tmpArr2Index < tmpArr2Len)
	    {
	        arr[arrIndex] = tmpArr2[tmpArr2Index];
	        ++arrIndex;
	        ++tmpArr2Index;
	    }

	    delete []tmpArr1;
	    delete []tmpArr2;
	}
	
	void mergeSort(int *arr, const unsigned int p, const unsigned int r)
	{
	    if (p < r)
	    {
	        int q = (p + r) / 2;
	        mergeSort(arr, p, q);
	        mergeSort(arr, q + 1, r);
	        merge(arr, p, q, r);
	    }
	}
	
## Python
	def merge(arr, p, q, r):
	    tmpArr1 = arr[p : (q + 1)]
	    tmpArr2 = arr[(q + 1) : (r + 1)]
	    tmpArr1Len = len(tmpArr1)
	    tmpArr2Len = len(tmpArr2)
	    arrIndex = p
	    tmpArr1Index = 0
	    tmpArr2Index = 0
	    while tmpArr1Index < tmpArr1Len and tmpArr2Index < tmpArr2Len:
	        if tmpArr1[tmpArr1Index] < tmpArr2[tmpArr2Index]:
	            arr[arrIndex] = tmpArr1[tmpArr1Index]
	            tmpArr1Index += 1
	        else:
	            arr[arrIndex] = tmpArr2[tmpArr2Index]
	            tmpArr2Index += 1
	        arrIndex += 1

	    while tmpArr1Index < tmpArr1Len:
	        arr[arrIndex] = tmpArr1[tmpArr1Index]
	        arrIndex += 1
	        tmpArr1Index += 1

	    while tmpArr2Index < tmpArr2Len:
	        arr[arrIndex] = tmpArr2[tmpArr2Index]
	        arrIndex += 1
	        tmpArr2Index += 1


	def mergeSort(arr, start, end):
	    if start < end:
	        middle = (start + end) / 2
	        mergeSort(arr, start, middle)
	        mergeSort(arr, middle + 1, end)
	        merge(arr, start, middle, end)
