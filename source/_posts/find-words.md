title: 变位词集
create_time: 2015/08/06 22:33:00
tags:
- 编程珠玑
- C++
- 算法
categories:
- C++
- 编程珠玑

---
## 编程珠玑
> 给定一个英语单词词典，请找出所有的变位词集。例如，因为"pots","stop","tops"相互之间都是由另一个词的各个字母改变序列而构成的，因此这些词相互之间就是变位词集。

<!-- more -->

## 实现思路
对每一个单词进行字母排序得到新的单词，使用新的单词作为key构造字典，变位词集的key是相同的，值则是变位词集。

## C++
	typedef std::map< std::string, std::vector<std::string> > strMap;
	strMap findWords(const std::vector<std::string> &words)
	{
	    strMap wordsMap;
	    typedef std::pair< std::string, std::vector<std::string> > strPair;
	    for (const auto& word: words)
	    {
	        std::string _word = word;
	        std::sort(_word.begin(), _word.end());
	        auto iter = wordsMap.find(_word);
	        if (iter != wordsMap.end())
	        {
	            std::vector<std::string> &_value = iter->second;
	            _value.push_back(word);
	        }
	        else
	        {
	            strPair item(_word, std::vector<std::string>{word});
	            wordsMap.insert(item);
	        }
	    }
	    return wordsMap;
	}
	
## 测试
	#include <iostream>
	#include <map>
	#include <algorithm>
	#include <vector>
	
	int main()
	{
	    std::vector<std::string> words{ "pans", "pots", "opt", "snap", "stop", "tops" };
	    auto t = findWords(words);
	    for (const auto& item : t)
	    {
	        std::vector<std::string> w = item.second;
	        for (const auto& i : w)
	        {
	            std::cout << i << " ";
	        }
	        std::cout << std::endl;
	    }
	    /*  输出结果
	    	pans snap
	    	pots stop tops
	    	opt
	    */

	    return 0;
	}