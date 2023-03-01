# NoSQL 和 MongoDB

NoSQL=Not Only SQL，支持类似 SQL 的功能，与 Relational Database 相辅相成。其性能较高，不使用 SQL 意味着没有结构化的存储要求(SQL 为结构化的查询语句)，没有约束之后架构更加灵活。

NoSQL 数据库四大家族

- 列存储 Hbase
- 键值 (Key-Value) 存储 Redis
- 图像存储 Neo4j
- 文档存储 MongoDB

MongoDB 是一个基于分布式文件存储的数据库，由 C++ 编写，可以为 WEB 应用提供可扩展、高性能、易部署的数据存储解决方案。

MongoDB 是一个介于关系数据库和非关系数据库之间的产品，是非关系数据库当中功能最丰富，最像关系数据库的。它支持的数据结构非常松散，数据格式是 BSON，一种类似 JSON 的二进制形式的存储格式，简称 Binary JSON ，和 JSON 一样支持内嵌的文档对象和数组对象，因此可以存储比较复杂的数据类型。Mongo 最大的特点是它支持的查询语言非常强大，其语法有点类似于面向对象的查询语言，几乎可以实现类似关系数据库单表查询的绝大部分功能，而且还支持对数据建立索引。原则上 Oracle 和 MySQL 能做的事情，MongoDB 都能做（包括 ACID 事务）。

MongoDB 是一个开源 OLTP 数据库，它灵活的文档模型（JSON）非常适合敏捷式开发、高可用和水平扩展的大数据应用。

# MongoDB 体系结构

![[Pasted image 20230220191235.png]]

# MongoDB 和 RDBMS (关系型数据库) 对比

| RDBMS                                | MongoDB                                       |
| ------------------------------------ | --------------------------------------------- |
| database (数据库)                    | database（数据库）                            |
| table（表）                          | collection（集合）                            |
| row（行）                            | document（BSON 文档）                         |
| column（列）                         | field（字段）                                 |
| index（唯一索引、主键索引）          | index（支持地理位置索引、全文索引、哈希索引） |
| join（主外键关联）                   | embedded Document (嵌套文档)                  |
| primary key (指定 1 至 N 个列做主键) | primary key (指定\_id field 做为主键)         |
| view (视图)                          | 视图（view)                                   |

# MongoDB 技术优势

- JSON 结构和对象模型接近，开发代码量低
- JSON 的动态模型意味着更容易响应新的业务需求
- 复制集提供 99.999%高可用
- 分片架构支持海量数据和无缝扩容

## 简单直观：从错综复杂的关系模型到一目了然的对象模型

![0](https://note.youdao.com/yws/public/resource/c1fdfae65ce29ffac56d7315bbfc7079/xmlnote/097CE93B50374A1BB085BBFD1C3B9FD5/35864)

## 快速：最简单快速的开发方式

![0](https://note.youdao.com/yws/public/resource/c1fdfae65ce29ffac56d7315bbfc7079/xmlnote/224E8BC628E8433297FAC199155419A1/35863)

## 灵活：快速响应业务变化

![0](https://note.youdao.com/yws/public/resource/c1fdfae65ce29ffac56d7315bbfc7079/xmlnote/8089520781CB4F56A27AD2509E3E1FFD/35861)

## MongoDB 优势：原生的高可用

![0](https://note.youdao.com/yws/public/resource/c1fdfae65ce29ffac56d7315bbfc7079/xmlnote/DF09D17CFF554FA4A67A6846EE8FCF50/35866)

## MongoDB 优势：横向扩展能力

![0](https://note.youdao.com/yws/public/resource/c1fdfae65ce29ffac56d7315bbfc7079/xmlnote/624091A7005C47AEBF317382848007F5/35869)

# MongoDB 应用场景

- 游戏场景，使用 MongoDB 存储游戏用户信息，用户的装备、积分等直接以内嵌文档的形式存储，方便查询、更新；
- 物流场景，使用 MongoDB 存储订单信息，订单状态在运送过程中会不断更新，以 MongoDB 内嵌数组的形式来存储，一次查询就能将订单所有的变更读取出来；
- 社交场景，使用 MongoDB 存储存储用户信息，以及用户发表的朋友圈信息，通过地理位置索引实现附近的人、地点等功能；
- 物联网场景，使用 MongoDB 存储所有接入的智能设备信息，以及设备汇报的日志信息，并对这些信息进行多维度的分析；
- 视频直播，使用 MongoDB 存储用户信息、礼物信息等；
- 大数据应用，使用云数据库 MongoDB 作为大数据的云存储系统，随时进行数据提取分析，掌握行业动态。

# 如何考虑是否选择 MongoDB?

没有某个业务场景必须要使用 MongoDB 才能解决，但使用 MongoDB 通常能让你以更低的成本解决问题。如果你不清楚当前业务是否适合使用 MongoDB,可以通过做几道选择题来辅助决策。

![0](https://note.youdao.com/yws/public/resource/c1fdfae65ce29ffac56d7315bbfc7079/xmlnote/4566444BFD1F4A73897D12FF69CFA7E4/35862)

只要有一项需求满足就可以考虑使用 MongoDB，匹配越多，选择 MongoDB 越合适。

# 什么是 BSON

BSON 是一种类 Json 的一种二进制形式的存储格式，简称 Binary JSON，它和 JSON 一样，支持内嵌的文档对象和数组对象，但是 BSON 有 JSON 没有优点。

- **访问速度更快**。BSON 会存储 Value 的类型，相比于明文存储，不需要进行字符串类型到其他类型的转换操作。以整型 12345678 为例，JSON 需要将字符串转成整型，而 BSON 中存储了整型类型标志，并用 4 个字节直接存储了整型值
- **存储空间更低**。还是以整型 12345678 为例，JSON 采用明文存储的方式需要 8 个字节，但是 BSON 对于 Int32 的值统一采用 4 字节存储，Long 和 Double 采用 8 字节存储。 当然这里说存储空间更低也分具体情况，比如对于小整型，BSON 消耗的空间反而更高
- **数据类型更丰富**。BSON 相比 JSON，增加了 BinData，TimeStamp，ObjectID，Decimal128 等类型。

BSON 示例

```bson
{
	key: value,
	key2: value2
}
```

这是一个 BSON 的例子，其中 key 是字符串类型,后面的 value 值，value 的类型一般是字符串,double,Array,ISODate 等类型。

**BSON 有三个特点：轻量性、可遍历性、高效性**

# BSON 在 MongoDB 中的使用

MongoDB 使用了 BSON 这种结构来存储数据和网络数据交换。把这种格式转化成一文档这个概念 (Document)，这里的一个 Document 也可以理解成关系数据库中的一条记录(Record)，只是这里的 Document 的变化更丰富一些，如 Document 可以嵌套。

# MongoDB 安装

## Linux 在线安装

### 下载安装 `Mongodb` 所需依赖

```bash
  sudo yum install libcurl openssl
```

### Mongodb wget 下载

```bash
wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-rhel70-6.0.0.tgz
```

### 源码包解压

```bash
tar -zxvf mongodb-linux-x86_64-rhel70-6.0.0.tgz
```

### 启动

#### 默认启动

```bash
./bin/mongod
```

#### 指定配置文件方式的启动

```bash
./bin/mongod -f mongo.conf
```

## Linux 压缩包安装

### 官网下载 mongodb

下载 MongoDB Community Server

> 下载地址：[https://www.mongodb.com/try/download/community](https://www.mongodb.com/try/download/community)

### 上传压缩包到服务器

```bash
scp  [本地上传文件地址] [用户名]@[ip]:[远程地址]
```

### 解压压缩包

```bash
tar -zxvf MongoDB-linux-x86_64-4.1.3.tgz
```

### 启动

#### 默认启动

```bash
./bin/mongod
```

#### 指定配置文件方式的启动

```bash
./bin/mongod -f mongo.conf
```

## Docker-compose 安装单机版 MongoDB

### 安装 yaml 文件

```yml
version: "3.7"
services:
  mongodb:
    image: mongo:6.0  # mongo 镜像
    container_name: mongodb  # 容器名称
    ports:
      - "27017:27017"  # 开放端口
    restart: always    # 断连策略
    volumes:
     - ./db:/data/db    # 数据文件外挂
     - ./log:/var/log/mongodb  # 日志文件外挂
     - ./config:/etc/mongo  # 配置文件挂在
    environment:
      - MONGO_INITDB_ROOT_USERNAME=admin   # 设置用户名
      - MONGO_INITDB_ROOT_PASSWORD=admin   # 设置密码
      - TZ=Asia/Shanghai                   # 设置时区
      - wiredTigerCacheSizeGB=1             # 设置缓存
networks:
  mongodb:
    name: mongodb
    driver: bridge
```

### 下载容器并启动

```bash
docker-compose up -d
```

# MongoDB 启动参数说明

| 参数      | 说明                           |
| --------- | ------------------------------ |
| dbpath    | 数据库目录，默认 /data/db      |
| port      | 监听的端口，默认 27017         |
| bind_ip   | 监听 IP 地址，默认全部可以访问 |
| fork      | 是否以后台启动的方式登陆       |
| logpath   | 日志路径                       |
| logappend | 是否追加日志                   |
| auth      | 是开启用户密码登陆             |
| config    | 指定配置文件                   |

## 添加环境变量

修改 /etc/profile，添加环境变量,方便执行 MongoDB 命令

```vim
export MONGODB_HOME=/usr/local/soft/mongodb
PATH=$PATH:$MONGODB_HOME/bin
```

然后执行 source /etc/profile 重新加载环境变量

### 配置文件示例

#### 单机配置文件

```vim
dbpath=/var/lib/mongodb
logpath=/var/log/mongodb/mongodb.log pidfilepath=/var/log/mongodb/master.pid
directoryperdb=true
logappend=true
bind_ip=127.0.0.1
port=27017
fork=true
```

#### 集群配置文件

```vim
dbpath=/var/lib/mongodb
logpath=/var/log/mongodb/mongodb.log pidfilepath=/var/log/mongodb/master.pid
directoryperdb=true
logappend=true
replSet=name
bind_ip=127.0.0.1
port=27017
fork=true
noprealloc=true
```

# 安全认证

创建管理员账号

```sql
# 设置管理员用户名密码需要切换到admin库
use admin
# 创建管理员
db.createUser({user:"fox",pwd:"fox",roles:["root"]})
# 查看当前数据库所有用户信息
show users
# 显示可设置权限
show roles
# 显示所有用户
db.system.users.find() 
```

![0](https://note.youdao.com/yws/public/resource/c1fdfae65ce29ffac56d7315bbfc7079/xmlnote/019875295F7B4791BD9CF27383E7CE8C/35935)

## 常用权限

| 权限名               | 描述                                                                                |     |
| -------------------- | ----------------------------------------------------------------------------------- | --- | --- |
| read                 | 允许用户读取指定数据库                                                              |     |
| readWrite            | 允许用户读写指定数据库                                                              |
| dbAdmin              | 允许用户在指定数据库中执行管理函数，如索引创建、删除，查看统计或访问 system.profile |
| dbOwner              | 允许用户在指定数据库中执行任意操作，增、删、改、查等                                |
| userAdmin            | 允许用户向 system.users 集合写入，可以在指定数据库里创建、删除和管理用户            |     |     |
| clusterAdmin         | 只在 admin 数据库中可用，赋予用户所有分片和复制集相关函数的管理权限                 |     |     |
| readAnyDatabase      | 只在 admin 数据库中可用，赋予用户所有数据库的读权限                                 |
| readWriteAnyDatabase | 只在 admin 数据库中可用，赋予用户所有数据库的读写权限                               |     |     |
| userAdminAnyDatabase | 只在 admin 数据库中可用，赋予用户所有数据库的 userAdmin 权限                        |
| dbAdminAnyDatabase   | 只在 admin 数据库中可用，赋予用户所有数据库的 dbAdmin 权限                          |
| root                 | 只在 admin 数据库中可用。超级账号，超级权限                                         |

## 重新赋予用户操作权限

```sql
db.grantRolesToUser( "fox" , [ { role: "clusterAdmin", db: "admin" } , { role: "userAdminAnyDatabase", db: "admin"}, { role: "userAdminAnyDatabase", db: "admin"}, { role: "readWriteAnyDatabase", db: "admin"} ])
```

## 删除用户

```sql
# 删除指定用户
db.dropUser("fox")
#删除当前数据库所有用户  
db.dropAllUser()
```

用户认证，返回 1 表示认证成功

![0](https://note.youdao.com/yws/public/resource/c1fdfae65ce29ffac56d7315bbfc7079/xmlnote/C251340C204C4283A6EC458108F7DCD2/35937)

## 创建应用数据库用户

```sql
use appdb db.createUser({user:"appdb",pwd:"fox",roles:["dbOwner"]})
```

默认情况下，MongoDB 不会启用鉴权，以鉴权模式启动 MongoDB

```bash
mongod -f /mongodb/conf/mongo.conf --auth
```

启用鉴权之后，连接 MongoDB 的相关操作都需要提供身份认证。

```bash
mongo 127.0.0.1:27017 -u fox -p fox --authenticationDatabase=admin
```

# MongoDB Database Tools

下载地址：[https://www.mongodb.com/try/download/database-tools](https://www.mongodb.com/try/download/database-tools)

| 文件名称     | 作用               |
| ------------ | ------------------ |
| mongostat    | 数据库性能监控工具 |
| mongotop     | 热点表监控工具     |
| mongodump    | 数据库逻辑备份工具 |
| mongorestore | 数据库逻辑恢复工具 |
| mongoexport  | 数据导出工具       |
| mongoimport  | 数据导入工具       |
| bsondump     | BSON 格式转换工具  |
| mongofiles   | GridFS 文件工具    |
