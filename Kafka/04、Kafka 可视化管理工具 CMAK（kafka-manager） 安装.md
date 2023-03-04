# 一、CMAK 简介

为了简化开发者和服务工程师维护 Kafka 集群的工作，yahoo 构建了一个叫做 Kafka 管理器的基于 Web 工具，叫做 CMAK。这个管理工具可以很容易地发现分布在集群中的哪些 topic 分布不均匀，或者是分区在整个集群分布不均匀的的情况。它支持管理多个集群、选择副本、副本重新分配以及创建 Topic。同时，这个管理工具也是一个非常好的可以快速浏览这个集群的工具，有如下功能：

- 管理多个集群
- 轻松检查集群状态（主题、消费者、偏移量、代理、副本分布、分区分布）
- 运行首选副本选举
- 使用选项生成分区分配以选择要使用的代理
- 运行分区的重新分配（基于生成的分配）
- 使用可选主题配置创建主题（0.8.1.1 的配置与 0.8.2+ 不同）
- 删除主题（仅在 0.8.2+ 上支持并记住在代理配 ​​ 置中设置 delete.topic.enable=true）
- 主题列表现在指示标记为删除的主题（仅支持 0.8.2+）
- 为多个主题批量生成分区分配，并可选择要使用的代理
- 批量运行多个主题的分区重新分配
- 将分区添加到现有主题
- 更新现有主题的配置
- 可选择为代理级别和主题级别指标启用 JMX 轮询。
- 可选地过滤掉 zookeeper 中没有 ids/owners/ & offsets/ 目录的消费者。

CMAK（kafka-manager ） 项目地址：[https://github.com/yahoo/CMAK](https://github.com/yahoo/CMAK)

集群管理

[![簇](https://github.com/yahoo/CMAK/raw/master/img/cluster.png)](https://github.com/yahoo/CMAK/blob/master/img/cluster.png)

---

主题列表

[![话题](https://github.com/yahoo/CMAK/raw/master/img/topic-list.png)](https://github.com/yahoo/CMAK/blob/master/img/topic-list.png)

---

主题视图

[![话题](https://github.com/yahoo/CMAK/raw/master/img/topic.png)](https://github.com/yahoo/CMAK/blob/master/img/topic.png)

---

消费者列表视图

[![消费者](https://github.com/yahoo/CMAK/raw/master/img/consumer-list.png)](https://github.com/yahoo/CMAK/blob/master/img/consumer-list.png)

---

消费主题视图

[![消费者](https://github.com/yahoo/CMAK/raw/master/img/consumed-topic.png)](https://github.com/yahoo/CMAK/blob/master/img/consumed-topic.png)

---

经纪人名单

[![经纪人](https://github.com/yahoo/CMAK/raw/master/img/broker-list.png)](https://github.com/yahoo/CMAK/blob/master/img/broker-list.png)

---

经纪人观点

[![经纪人](https://github.com/yahoo/CMAK/raw/master/img/broker.png)](https://github.com/yahoo/CMAK/blob/master/img/broker.png)

# 二、下载

[https://github.com/yahoo/Kafka-manager/releases](https://github.com/yahoo/Kafka-manager/releases)

上传到服务器中

```bash
unzip cmak-3.0.0.6.zip

cd /cmak-3.0.0.6
```


# 三、配置

查看在 conf 目录中的 application.conf 文件中找到 `cmak.zkhosts` 配置属性

- 单机配置

```vim
cmak.zkhosts="my.zookeeper.host.com:2181"
```

- 集群配置

```vim
cmak.zkhosts="my.zookeeper.host.com:2181,other.zookeeper.host.com:2181"
```

# 四、启动

```bash
# 默认启动
bin/cmak
# 配置文件启动
bin/cmak -Dconfig.file=/path/to/application.conf
# 指定 Java 版本启动
$ bin/cmak -java-home /usr/lib/jvm/zulu-11-amd64
```

