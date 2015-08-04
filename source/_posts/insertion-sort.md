title: 插入排序（Insertion Sort)
date: 2015/08/03 23:20:00
tags: 排序
categories: 算法导论

---
>[插入排序（Insertion Sort）](https://zh.wikipedia.org/wiki/%E6%8F%92%E5%85%A5%E6%8E%92%E5%BA%8F)是一种简单直观的排序算法。它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。插入排序在实现上，通常采用in-place排序（即只需用到O(1)的额外空间的排序），因而在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。

## 算法描述
一般来说，插入排序都采用in-place在数组上实现。具体算法描述如下：

1. 从第一个元素开始，该元素可以认为已经被排序
2. 取出下一个元素，在已经排序的元素序列中从后向前扫描
3. 如果该元素（已排序）大于新元素，将该元素移到下一位置
4. 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
5. 将新元素插入到该位置后
6. 重复步骤2~5

如果比较操作的代价比交换操作大的话，可以采用[二分查找法](https://zh.wikipedia.org/wiki/%E6%8A%98%E5%8D%8A%E6%90%9C%E7%B4%A2%E7%AE%97%E6%B3%95)来减少比较操作的数目。该算法可以认为是插入排序的一个变种，称为二分查找插入排序。




## 算法导论中的伪代码

	INSERTION_SORT(A)
		for j = 2 to A.length
			key = A[j]
			// Insert A[j] into the sorted sequence A[1..j-1]
			i = j - 1
			while i > 0 and A[i] > key
				A[i + 1] = A[i]
				i = i - 1
			A[i + 1] = key
			
			
## C/C++

	void insertionSort(int *arr, const unsigned int length)
	{
		for (unsigned int i = 1; i < length; ++i)
    	{
    		const int key = arr[i];
        	int j = i - 1;
        	while (j >= 0 && arr[j] > key)
        	{
            	arr[j + 1] = arr[j];
            	--j;
        	}
        	arr[j + 1] = key;
    	}
	}
	
	
## Python

	def insertionSort(arr):
		length = len(arr)
    	for i in range(1, length):
        	key = arr[i]
        	j = i - 1
        	while j >= 0 and arr[j] > key:
            	arr[j + 1] = arr[j]
            	j = j - 1
        	arr[j + 1] = key
      



