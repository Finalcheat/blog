title: 向量旋转
date: 2015/08/05 21:56:00
tags:
- 编程珠玑
- 算法
- 旋转
- C/C++
categories:
- C/C++
- 编程珠玑

---
## 编程珠玑
> 1. 问题描述

>	将一个n元一维向量向左旋转i个位置。例如，当n=8且i=3时，向量abcdefgh旋转为defghabc。简单的代码使用一个n元的中间向量在n步就能够完成该工作，你能否仅使用数十个额外字节的存储空间，正比于n的时间内完成向量旋转？

> 2. 解决思路

>	旋转向量x其实就是交换向量ab的两段，得到向量ba。这里a代表x中的前i个元素。假设a比b短，将b分为bl和br，使得br具有与a相同的长度。交换a和br，也就是将ablbr 。序列a此时已处于其最终的位置，因此现在就集中到交换b的两部分。由于新问题与原来的问题具有相同的形式，我们可以递归地解决之。
	
>	编程珠玑提供了更简单使用的方法，我们将问题看做是把数组ab转换成ba，同时假定我们拥有一个函数可以将数组中特定部分的元素求逆。从ab开始，首先对a求逆，得到arb，然后对b求逆，得到arbr。最后整体求逆，得到(arbr)r。此时恰好是ba。

## C/C++
	void reverse(char *arr, unsigned int start, unsigned int end)
	{
	    while (start < end)
	    {
	        int tmp = arr[start];
	        arr[start] = arr[end];
	        arr[end] = tmp;
	        ++start;
	        --end;
	    }
	}

	void rotate(char *arr, const unsigned int length, const unsigned int i)
	{
		 /* arr = abcdefgh length = 8 i = 3 */
	    reverse(arr, 0, i -1);            /* cbadefgh */
	    reverse(arr, i, length - 1);      /* cbahgfed */
	    reverse(arr, 0, length - 1);      /* defghabc */
	}