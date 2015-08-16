title: 计数排序
create_time: 2015/08/16 14:53:00
tags:
- 算法
- C/C++
- 排序
- 计数
- 线性时间
categories:
- 算法导论

---
>[计数排序](https://zh.wikipedia.org/wiki/%E8%AE%A1%E6%95%B0%E6%8E%92%E5%BA%8F)（Counting sort）是一种稳定的线性时间排序算法。计数排序使用一个额外的数组C，其中第i个元素是待排序数组A中值等于i的元素的个数。然后根据数组C来将A中的元素排到正确的位置

### 计数排序的特征
>计数排序假设$n$个输入元素中的每一个都是在$0$到$k$区间内的一个整数，其中$k$为某个整数。当$k=O(n)$时，排序的运行时间为$O(n)$。
>
>计数排序的基本思想是：对每一个输入元素$x$，确定小于$x$的元素个数。利用这一信息就可以直接把$x$放到它在输出数组中的位置上了。例如，如有有17个元素小于$x$，则$x$就应该在第18个输出位置上。当有几个元素相同时，这一方案要略做修改。因为不能把它们放在同一输出位置上。
>
>在计数排序算法的代码中，假设输入是一个数组$A[1..n]$，$A.length=n$。我们还需要两个数组：$B[1..n]$存放排序的输出，$C[0..k]$提供临时存储空间。

#### 伪代码
	COUNTING-SORT(A, B, k)
		let C[O..K] be a new array
		for i = 0 to k
			C[i] = 0
		for j = 1 to A.length
			C[A[j]] = C[A[j]] + 1
		// C[i] now contains the number of elements equal to i
		for i = 1 to k
			C[i] = C[i] + C[i - 1]
		// C[i] now contains the number of elements less than or equal to i
		for j = A.length downto 1
			B[C[A[j]]] = A[j]
			C[A[j]] = C[A[j]] - 1
		
### C/C++
	void counting_sort(int *arr, const int length, const int max)
	{
	    if (max <= 0)
	        return;
	    int *b = new int[length];
	    for (int i = 0; i < length; ++i)
	        b[i] = arr[i];
	    int *c = new int[max + 1];
	    for (int i = 0; i <= max; ++i)
	        c[i] = 0;
	    for (int i = 0; i < length; ++i)
	        c[b[i]] += 1;
	    for (int i = 1; i <= max; ++i)
	        c[i] += c[i - 1];
	    for (int i = length - 1; i >= 0; --i)
	    {
	        arr[c[b[i]] - 1] = b[i];
	        c[b[i]] -= 1;
	    }
	    delete[] b;
	    delete[] c;
	}
	
### 测试
	#include <iostream>
	#include <stdlib.h>
	#include <time.h>
	
	int main()
	{
	    srand((unsigned)time(NULL));
	    const int length = 500000000;
	    int *arr = new int[length];
	    int *b = new int[length];
	    int max = 100;
	    for (int i = 0; i < length; ++i)
	    {
	        arr[i] = rand() % (max + 1);
	        b[i] = arr[i];
	    }
	    std::cout << "counting_sort start" << std::endl;
	    clock_t start = clock();
	    counting_sort(arr, length, max);
	    std::cout << (double)(clock() - start) / CLOCKS_PER_SEC << std::endl;
	    std::cout << "counting_sort finish" << std::endl;
	    std::cout << "std::sort start" << std::endl;
	    start = clock();
	    std::sort(b, b + length);
	    std::cout << (double)(clock() - start) / CLOCKS_PER_SEC << std::endl;
	    std::cout << "std::sort finish" << std::endl;
	}
	
这里和std::sort比较下，随机生成5亿个数，数的范围为[0..100]，分别使用counting_sort和std::sort排序。
>c++ -O2 main.cpp
>
>./a.out
>
>counting_sort start
>
>6.52047
>
>counting_sort finish
>
>std::sort start
>
>16.9916
>
>std::sort finish

以上可以看出，在输入的数组有范围的情况下计数排序是快于其他基于比较的排序方法的。
