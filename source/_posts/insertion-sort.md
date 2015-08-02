title: 插入排序
---

算法导论伪代码

	INSERTION_SORT(A)
		for j = 2 to A.length
			key = A[j]
			// Insert A[j] into the sorted sequence A[1..j-1]
			i = j - 1
			while i > 0 and A[i] > key
				A[i + 1] = A[i]
				i = i - 1
			A[i + 1] = key
			
C/C++代码

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
	
Python代码

	def insertionSort(arr):
		length = len(arr)
    	for i in range(1, length):
        	key = arr[i]
        	j = i - 1
        	while j >= 0 and arr[j] > key:
            	arr[j + 1] = arr[j]
            	j = j - 1
        	arr[j + 1] = key
      



