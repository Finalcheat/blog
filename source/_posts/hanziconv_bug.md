title: hanziconv简繁互转的坑
date: 2016/11/23 23:24:01
tags:
- Python
- hanziconv
- 简繁转换
categories:
- Python

---

[hanziconv]
---------

昨天接到一个需求是将简体转换成繁体，之前我已经使用过[OpenCC]完成过这个功能，我认为OpenCC这种使用shell调用的方式不方便python使用。
于是去网上找相应的python包，Google搜索到[hanziconv]，看到的文档调用方式是这样:

    >>> from hanziconv import HanziConv
    >>> print(HanziConv.toSimplified('繁簡轉換器'))
    繁简转换器
    >>> print(HanziConv.toTraditional('繁简转换器'))
    繁簡轉換器

简单明了的接口让我决定使用它代替OpenCC，然而今天就发现转换时候出现的bug。
bug请看下面的代码:

    >>> from hanziconv import HanziConv
    >>> print(HanziConv.toTraditional('台湾'))
    颱灣

将“台湾”这个词语转换成繁体的时候变成“颱灣”，这个转换实在是也太无语了，难道实现是单字转换？
无奈之下只好换回[OpenCC]了。

  [OpenCC]: https://github.com/BYVoid/OpenCC
  [hanziconv]: https://pypi.python.org/pypi/hanziconv/0.2.1