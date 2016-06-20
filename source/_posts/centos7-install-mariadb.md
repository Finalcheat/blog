title: CentOS7 MariaDB数据库安装与配置
create_time: 2016/06/19 21:52:09
tags:
- CentOS
- MariaDB
- MySQL
categories:
- Linux

---
## MariaDB安装
CentOS7将MySQL数据库软件从默认的程序列表中移除，用MariaDB代替。MariaDB跟MySQL在绝大多数方面是兼容的，对于开发者来说，几乎感觉不到任何不同。目前MariaDB是发展最快的MySQL分支版本，新版本发布速度已经超过了Oracle官方的MySQL版本。

执行以下命令安装MariaDB:
<pre>
[finalcheat@localhost ~]$ sudo yum install mariadb-server mariadb
</pre>
操作MariaDB的相关命令:
<pre>
systemctl start mariadb  # 启动MariaDB
systemctl stop mariadb  # 停止MariaDB
systemctl restart mariadb  # 重启MariaDB
systemctl enable mariadb  # 设置开机启动
systemctl status mariadb # 查询MariaDB运行状态
</pre>
首先启动MariaDB数据库
<pre>
[finalcheat@localhost ~]$ systemctl start mariadb
==== AUTHENTICATING FOR org.freedesktop.systemd1.manage-units ===
Authentication is required to manage system services or units.
Authenticating as: root
Password:
==== AUTHENTICATION COMPLETE ===
</pre>
然后就可以连接数据库使用了
<pre>
[finalcheat@localhost ~]$ mysql -uroot
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 10
Server version: 5.5.47-MariaDB MariaDB Server

Copyright (c) 2000, 2015, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| test               |
+--------------------+
4 rows in set (0.00 sec)

MariaDB [(none)]>
</pre>

### 设置密码
MariaDB默认root账号初始是没有密码，给它设置一个密码以保证安全。
<pre>
MariaDB [(none)]> set password for 'root'@'localhost' = password('password');
</pre>
括号中的password是密码

### 只监听内网
默认是监听地址0.0.0.0，也就是主机上的所有ip地址，我这里只希望它内网使用，不监听外网地址。
修改MariaDB配置文件(我这里是/etc/my.cnf.d/server.cnf)，加上下面这一行:
<pre>
bind-address = 192.168.1.91
</pre>
其中192.168.1.91是本机的内网地址，请自行查看自己本机的内网地址替换
然后重启MariaDB
<pre>
[finalcheat@localhost ~]$ systemctl restart mariadb
[finalcheat@localhost ~]$ sudo netstat -nlp | grep mysql
[sudo] password for finalcheat:
tcp        0      0 192.168.1.91:3306       0.0.0.0:*               LISTEN      22726/mysqld
unix  2      [ ACC ]     STREAM     LISTENING     102338   22726/mysqld         /var/lib/mysql/mysql.sock
</pre>
最终可以看到监听的地址已经变为内网地址了。

### 设置firewalld
上面的设置完成之后发现同一局域网内还是没法访问的，原因是CentOS7默认是开启firewall的，而firewall默认是禁掉端口的，所以最简单的方法就是直接禁用firewall
<pre>
[finalcheat@localhost ~]$ systemctl stop firewalld
</pre>
但是这样的做法非常不好，firewall可以一定程度的保证服务器的安全，所以最好的做法是设置firewall开启某个端口即可。
首先查看接口所属区域
<pre>
[finalcheat@localhost ~]$ firewall-cmd --get-zone-of-interface=eth0
public
</pre>
eth0是接口，public是所属区域，在所属区域内增加MariaDB的端口3306(默认)
<pre>
[finalcheat@localhost ~]$ sudo firewall-cmd --zone=public --add-port=3306/tcp --permanent
success
[finalcheat@localhost ~]$ firewall-cmd --zone=public --list-ports
3306/tcp
</pre>
--zone=public表示区域public，--add-port=3306/tcp表示允许tcp协议3306端口通过，--permanent表示永久生效
接着重启firewall即可
<pre>
[finalcheat@localhost ~]$ sudo firewall-cmd --reload
</pre>
最终同一局域网内的机器可以访问到MariaDB了。
