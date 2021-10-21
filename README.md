# 环境要求

```python
python=3.7
Django=2.2
```



## 1.数据库创建

```python
# 进入数据库
mysql -uroot -proot

# 创建 oasystem 数据库
create database oasystem charset=utf8;
```



## 2.遇到的问题及解决办法

### 1.fatal: unable to access 'https://github.com/kangpeilun/OA_system.git/': OpenSSL SSL_read: Connection was reset, errno 10054

```python
在开启shadowsock的前提下，手动配置git的代理。git客户端输入如下两个命令就可以了。

git config --global http.proxy http://127.0.0.1:1080

git config --global https.proxy http://127.0.0.1:1080
```

