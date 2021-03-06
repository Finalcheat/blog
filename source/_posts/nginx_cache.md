title: Nginx缓存基本配置
date: 2016/11/22 23:27:09
tags:
- Nginx
- Cache
categories:
- Nginx

---

[Nginx缓存配置]
---------------

nginx配置缓存的两个基本指令是:proxy_cache_path和proxy_cache。

proxy_cache_path配置缓存的各种参数，proxy_cache使用proxy_cache_path配置的内容。

参数配置
--------

    proxy_cache_path /path/to/cache levels=1:2 keys_zone=my_cache:10m max_size=10g
                    inactive=60m use_temp_path=off;

    server {
    ...
        location / {
            proxy_cache my_cache;
            proxy_pass http://my_upstream;
        }
    }

参数说明

-   /path/to/cache : 缓存目录
-   levels=1:2 : 设置一个两级层次结构的目录，如果没有设置该参数，则所有文件缓存在同一目录。
-   keys_zone : 缓存键与内存空间。缓存键也就是名字，用于proxy_cache，内存空间设置，1MB可以存储大约8000个key。
-   max_size : 缓存上限(这里指磁盘空间)。
-   inactive : 缓存时间。
-   use_temppath=off : 指示NGINX将在缓存这些文件时将它们写入同一个目录下。
-   proxy_cache : 使用缓存。

更详细以及更复杂的缓存配置可以参考[官方文档](https://www.nginx.com/blog/nginx-caching-guide/)

  [Nginx缓存配置]: https://www.nginx.com/blog/nginx-caching-guide/