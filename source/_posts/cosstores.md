title: Cosstores商品信息抓取
date: 2016/03/13 15:35:09
tags:
- 爬虫
- pyquery
- requests
categories:
- 爬虫
- Python

---
## [Cosstores](http://www.cosstores.com)抓取用到的技术
使用Python语言，http请求用[requests](http://docs.python-requests.org/en/master/)，html页面解析使用[pyquery](https://pythonhosted.org/pyquery/)，最终抓取的结果在[这里](http://www.finalcheat.com:7777/get/cosstores_log/)

## 列表页抓取
### 静态页面抓取
列表页就是像[http://www.cosstores.com/gb/Women/Knitwear](http://www.cosstores.com/gb/Women/Knitwear)这样的页面，目的就是从列表页面中提取出该列表中所有的商品链接。做法也很简单，用requests构造http请求获取html源码然后用pyquery解析即可，先来看下代码。
```
import requests
from pyquery import PyQuery as pyq
url = "http://www.cosstores.com/gb/Women/Knitwear"
# get请求获取列表页html源码
res = requests.get(url)
assert res.status_code == 200
# 使用pyquery解析内容
jq = pyq(res.content)
# pyquery选取元素的做法和jQuery基本一致，下面这行代码表示选取a元素，a元素的父亲是li，
# li的父亲是ul，ul的父亲拥有class为list-container
goods_list = jq('.list-container>ul>li>a')
for r in goods_list:
    # 输出每个商品的链接
    print r.get('href')
```
执行看下结果
> /gb/Women/Knitwear/Silk-cotton_v-neck_cardigan/46889-40554710.1#c-24479
> /gb/Women/Knitwear/Top_with_silk_back_panel/46889-37358830.1#c-24479
> /gb/Women/Knitwear/Top_with_folded_sleeve/46889-40650344.1#c-22755
> /gb/Women/Knitwear/Short_sleeve_knit_blazer/46889-39817700.1#c-24479
> /gb/Women/Knitwear/Basic_wide-neck_knit_jumper/46889-40589970.1#c-24479
> /gb/Women/Knitwear/Jacquard_sleeve_top/46889-40894828.1#c-22755
> /gb/Women/Knitwear/Circle_stitch_cardigan/46889-39075551.1#c-22755
> /gb/Women/Knitwear/Bonded_knit_jumper/46889-39818303.1#c-22755
> /gb/Women/Knitwear/Silk_skirt_dress/46889-38392745.1#c-24479
> /gb/Women/Knitwear/V-neck_merino_jumper/46889-40854904.1#c-24480
> /gb/Women/Knitwear/Reverse_knit_top/46889-41014057.1#c-22755

以上短短几行代码就把列表页的商品链接提取出来了？还没有(^_^)，只是把第一页的商品取出来而已，而下一页的商品信息是用ajax动态加载的。

### ajax动态请求列表页分析
继续分析html源码，找到id为infiload_nav的元素，它的html源码像下面那样(略去部分不相关的属性)
```
<div id="infiload_nav">
    <a data-maxpage="9" href="/gb/ProductListClientService/loadAdditionalProducts?&pageId=46889&page=2&DataType=html">
    </a>
</div>
```
可以看出/gb/ProductListClientService/loadAdditionalProducts/就是获取下一页商品列表的接口，参数是pageId(估计是商品类目)、page(页数)、DataType，从data-maxpage可以看出最大页数为9。分析到这里已经可以写出完整的解析列表页商品的代码了，第一页用上面的代码抓取，2到n页循环调用/gb/ProductListClientService/loadAdditionalProducts/即可，然后再使用pyquery解析。

### 完整代码
```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Finalcheat'

import requests
import re
import datetime
from pyquery import PyQuery as pyq


class CosstoresGoodsListPrase(object):
    '''
    cosstores商品列表页解析
    such as : http://www.cosstores.com/gb/Women/Denim
    '''

    COSSTORES_HOST = 'http://www.cosstores.com'

    def __init__(self):
        # 列表页商品信息保存在该变量中
        self.goods_list = []

    def parse(self, url):
        # 解析第一页商品列表
        res = requests.get(url)
        assert res.status_code == 200
        jq = pyq(res.content)

        goods_list = jq('.list-container>ul>li>a')
        for r in goods_list:
            goods_url = r.get('href')
            if not goods_url:
                continue
            goods_url = '%s%s' % (CosstoresGoodsListPrase.COSSTORES_HOST, goods_url)
            goods_name = r.get('title')
            #  print goods_url, goods_name

            goods_item = {
                'url' : goods_url,
                'name' : goods_name,
            }
            self.goods_list.append(goods_item)

        # 解析ajax动态请求的商品列表页，第2-n页
        next_page = jq('#infiload_nav>a')
        if next_page:
            next_page = next_page[0]
            max_page = int(next_page.get('data-maxpage'))
            next_url = next_page.get('href')
            np = re.findall('page=(\d+)', next_url)
            if not np:
                return
            np = int(np[0])
            while np <= max_page:
                next_url = re.sub('page=(\d+)', 'page=%s' % (np), next_url)
                np += 1
                res = requests.get('%s%s' % (CosstoresGoodsListPrase.COSSTORES_HOST, next_url))
                assert res.status_code == 200
                jq_page = pyq(res.content)
                goods_list = jq_page('li>a')
                if not goods_list:
                    # 解析完了
                    break
                for r in goods_list:
                    goods_url = r.get('href')
                    if not goods_url:
                        continue
                    goods_url = '%s%s' % (CosstoresGoodsListPrase.COSSTORES_HOST, goods_url)
                    goods_name = r.get('title')
                    goods_item = {
                        'url' : goods_url,
                        'name' : goods_name,
                    }
                    self.goods_list.append(goods_item)
```

## 商品详情
### 静态页面抓取
商品详情页也有ajax动态请求获取商品信息，这个下面再说，先抓取html源码可以获取到的信息。
商品的名称、颜色、价格、图片都可以从html中获取到，方法也很简单，用pyquery简单解析下就行了。
```
# 价格
self.price = jq('.PriceContainer').text()
# 颜色
self.color = jq('.colorLabel').text()
# 名称
self.name = jq('.productInfo>h1').text()
# 图片
images = jq('.productSlideshow>ul>li>div>img')
image_list = []
for r in images:
    image_url = r.get('src')
    if not image_url:
        continue
    image_list.append('%s%s' % (CosstoresGoodsPrase.COSSTORES_HOST, image_url))
self.image = image_list
```

### ajax动态请求商品信息分析
动态请求商品调用/gb/product/GetVariantData/接口，参数有variantId(可以从html中得到)、lookID(用户id，未登陆填null)、image(填0即可)。
该接口返回的结果有货号、原价，当前价、商品属性、商品详细描述等等，而且接口返回的json格式，不需要用pyquery解析了。

### 完整代码
```
class CosstoresGoodsPrase(object):
    '''
    cosstores商品解析
    such as : http://www.cosstores.com/gb/Women/Knitwear/Silk_skirt_dress/46889-38392745.1#c-24479
    '''

    COSSTORES_HOST = 'http://www.cosstores.com'

    def __init__(self):
        # 商品id
        self.goods_id = ''
        # 商品类目id
        self.category_id = ''
        # 商品url链接
        self.url = ''
        # 商品名称
        self.name = ''
        # 商品原价
        self.original_price = ''
        # 商品当前价
        self.price = ''
        # 商品详细描述信息
        self.details = ''
        # 商品属性
        self.attributes = []
        # 商品货号
        self.code = ''
        # 商品颜色
        self.color = []
        # 商品图片
        self.image = []
        # 操作更新时间
        self.update_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


    def parse(self, url):
        res = requests.get(url)
        assert res.status_code == 200
        jq = pyq(res.content)
        self.url = url
        self.price = jq('.PriceContainer').text()
        self.color = jq('.colorLabel').text()
        self.name = jq('.productInfo>h1').text()
        category_id = re.findall('/(\d+)-', url)
        self.category_id = category_id[0] if category_id else ''
        images = jq('.productSlideshow>ul>li>div>img')
        image_list = []
        for r in images:
            image_url = r.get('src')
            if not image_url:
                continue
            image_list.append('%s%s' % (CosstoresGoodsPrase.COSSTORES_HOST, image_url))
        self.image = image_list
        first_image = image_list[0] if image_list else ''
        goods_id = re.findall('/(\d+)/', first_image)
        self.goods_id = str(goods_id[0]) if goods_id else ''

        # ajax动态请求
        goods_detail_ids = jq('.productSizes>label>input')
        goods_detail_id = goods_detail_ids[0].get('value') if goods_detail_ids else ''
        if goods_detail_id:
            goods_detail_url = 'http://www.cosstores.com/gb/product/GetVariantData?variantId=%s&lookID=null&image=0' % (goods_detail_id)
            res = requests.get(goods_detail_url)
            assert res.status_code == 200
            result = res.json()
            self.code = result.get('HMOrderNo', '')
            self.original_price = result.get('DefaultPriceWithCurrency', '')
            self.price = result.get('PriceWithCurrency', '')
            self.attributes = result.get('Attributes', [])
            self.details = result.get('DescriptionShort', '')
```

## 总结
cosstores这样的官网爬虫难度不大，因为一般没有反爬虫策略(^_^)，只需要模拟浏览器的行为构造请求，然后解析html信息即可，对于动态加载的内容，需要分析出相应的接口和参数，然后模拟调用即可。
