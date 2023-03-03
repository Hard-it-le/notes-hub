# 安装前的环境准备

## 安装 Java

由于 Kafka 是用 Scala 语言开发的，运行在 JVM 上，因此在安装 Kafka 之前需要先安装 JDK。

```bash
yum install java-1.8.0-openjdk* -y
```

## 安装 Zookeeper

kafka 依赖 zookeeper，所以需要先安装 zookeeper

```bash
wget https://archive.apache.org/dist/zookeeper/zookeeper-3.5.8/apache-zookeeper-3.5.8-bin.tar.gz
tar -zxvf apache-zookeeper-3.5.8-bin.tar.gz
cd apache-zookeeper-3.5.8-bin
cp conf/zoo_sample.cfg conf/zoo.cfg

bin/zkServer.sh start
bin/zkCli.sh
```

# Kafka 安装

## 下载并解压压缩包

```bash
wget https://archive.apache.org/dist/kafka/2.4.1/kafka_2.11-2.4.1.tgz # 2.11是scala的版本，2.4.1是kafka的版本 tar -xzf kafka_2.11-2.4.1.tgz

tar -xzf kafka_2.11-2.4.1.tgz
cd kafka_2.11-2.4.1
```

## 修改配置文件（server.properties）

```vim
#broker.id属性在kafka集群中必须要是唯一
broker.id=0
#kafka部署的机器ip和提供服务的端口号
listeners=PLAINTEXT://127.0.0.1:9092
#kafka的消息存储文件
log.dir=/usr/local/data/kafka-logs
#kafka连接zookeeper的地址
zookeeper.connect=127.0.0.1:2181
```

## 启动服务

启动脚本语法：

```bash
kafka-server-start.sh [-daemon] server.properties
```

可以看到，server.properties 的配置路径是一个强制的参数，-daemon 表示以后台进程运行，否则 ssh 客户端退出后，就会停止服务。(注意，在启动 kafka 时会使用 linux 主机名关联的 ip 地址，所以需要把主机名和 linux 的 ip 映射配置到本地 host 里，用 vim /etc/hosts)

```bash
bin/kafka-server-start.sh -daemon config/server.properties #后台启动，不会打印日志到控制台
bin/kafka-server-start.sh config/server.properties  # 前台启动
```

## 查看 Kafka 后台进程

```bash
ps aux|grep kafka
```

## 停止 Kafka

```bash
bin/kafka-server-stop.sh
```

# 配置文件详解

| Property                   | Default                        | Description                                                                                                                                                                                           |
| -------------------------- | ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| broker.id                  | 0                              | 每个 broker 都可以用一个唯一的非负整数 id 进行标识；<br>这个 id 可以作为 broker 的“名字”，你可以选择任意你喜欢的数字作为 id，只要 id 是唯一的即可。                                                   |
| log.dirs                   | /tmp/kafka-logs                | kafka 存放数据的路径。这个路径并不是唯一的，可以是多个，路径之间只需要使用逗号分隔即可；每当创建新 partition 时，都会选择在包含最少 partitions 的路径下进行。                                         |
| listeners                  | PLAINTEXT://192.168.65.60:9092 | server 接受客户端连接的端口，ip 配置 kafka 本机 ip 即可                                                                                                                                               |
| zookeeper.connect          | localhost:2181                 | zooKeeper 连接字符串的格式为：hostname:port，此处 hostname 和 port 分别是 ZooKeeper 集群中某个节点的 host 和 port；zookeeper 如果是集群，连接方式为 hostname1:port1, hostname2:port2, hostname3:port3 |
| log.retention.hours        | 168                            | 每个日志文件删除之前保存的时间。默认数据保存时间对所有 topic 都一样。                                                                                                                                 |
| num.partitions             | 1                              | 创建 topic 的默认分区数                                                                                                                                                                               |
| default.replication.factor | 1                              | 自动创建 topic 的默认副本数量，建议设置为大于等于 2                                                                                                                                                   |
| min.insync.replicas        | 1                              | 当 producer 设置 acks 为-1 时，min.insync.replicas 指定 replicas 的最小数目（必须确认每一个 repica 的写数据都是成功的），如果这个数目没有达到，producer 发送消息会产生异常                            |
| delete.topic.enable        | false                          | 是否允许删除主题                                                                                                                                                                                      |

# Kafka 基本使用

## 创建主题

```bash
bin/kafka-topics.sh --create --zookeeper 127.0.0.1:2181 --replication-factor 1 --partitions 1 --topic test
```

## 查看已存在主题

```bash
bin/kafka-topics.sh --list --zookeeper 127.0.0.1:2181
```

除了我们通过手工的方式创建 Topic，当 producer 发布一个消息到某个指定的 Topic，这个 Topic 如果不存在，就自动创建。

## 删除主题

```bash
bin/kafka-topics.sh --delete --topic test --zookeeper 127.0.0.1:2181
```

## 发送消息

kafka 自带了一个 producer 命令客户端，可以从本地文件中读取内容，或者我们也可以以命令行中直接输入内容，并将这些内容以消息的形式发送到 kafka 集群中。在默认情况下，每一个行会被当做成一个独立的消息。

```bash
bin/kafka-console-producer.sh --broker-list 127.0.0.1:9092 --topic test
>this is a msg
>this is a another msg
```

## 消费消息

对于 consumer，kafka 同样也携带了一个命令行客户端，会将获取到内容在命令中进行输出，默认是消费最新的消息：

```bash
bin/kafka-console-consumer.sh --bootstrap-server 127.0.0.1:9092 --topic test
```

如果想要消费之前的消息可以通过--from-beginning 参数指定，如下命令：

```bash
bin/kafka-console-consumer.sh --bootstrap-server 127.0.0.1:9092 --from-beginning --topic test
```

## 消费多主题

```bash
bin/kafka-console-consumer.sh --bootstrap-server 127.0.0.1:9092 --whitelist "test|test-2"
```

## 单播消费

一条消息只能被某一个消费者消费的模式，类似 queue 模式，只需让所有消费者在同一个消费组里即可

分别在两个客户端执行如下消费命令，然后往主题里发送消息，结果只有一个客户端能收到消息

```bash
bin/kafka-console-consumer.sh --bootstrap-server 127.0.0.1:9092 --consumer-property group.id=testGroup --topic test
```

## 多播消费

一条消息能被多个消费者消费的模式，类似 publish-subscribe 模式费，针对 Kafka 同一条消息只能被同一个消费组下的某一个消费者消费的特性，要实现多播只要保证这些消费者属于不同的消费组即可。我们再增加一个消费者，该消费者属于 testGroup-2 消费组，结果两个客户端都能收到消息

```bash
bin/kafka-console-consumer.sh --bootstrap-server 127.0.0.1:9092 --consumer-property group.id=testGroup-2 --topic test
```

## 查看消费组名

```bash
bin/kafka-consumer-groups.sh --bootstrap-server 127.0.0.1:9092 --list
```

## 查看消费组的消费偏移量

```bash
bin/kafka-consumer-groups.sh --bootstrap-server 127.0.0.1:9092 --describe --group testGroup
```

![](https://note.youdao.com/yws/public/resource/b0357bdb4821ed2e35ecdbdacd65aa06/xmlnote/B6E3BE06B605458CA19BFB55AEA268DA/122867)

- current-offset：当前消费组的已消费偏移量
- log-end-offset：主题对应分区消息的结束偏移量(HW)
- lag：当前消费组未消费的消息数

# docker-compose 安装

```yaml
version: "3.7"
services:
  zookeeper:
    image: bitnami/zookeeper:latest
    container_name: zookeeper
    restart: always
    ports:
      - 2181:2181
    environment:
      ALLOW_ANONYMOUS_LOGIN: "yes"
      ZOOKEEPER_CLIENT_PORT: 2181
      ZOOKEEPER_TICK_TIME: 2000
      ZOOKEEPER_SYNC_LIMIT: 2
    volumes:
      - /etc/localtime:/etc/localtime ## 挂载位置（kafka镜像和宿主机器之间时间保持一直）
    networks:
      - zk-kafka

  kafka:
    image: bitnami/kafka:latest
    container_name: kafka
    ports:
      - 9092:9092
    restart: always
    environment:
      # client 要访问的 broker 地址
      KAFKA_ADVERTISED_HOST_NAME: 127.0.0.1
      # 每个容器就是一个 broker，设置其对应的 ID      KAFKA_BROKER_ID: 1
      # 通过端口连接 zookeeper      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      # kafka 监听器，告诉外部连接者要通过什么协议访问指定主机名和端口开放的 Kafka 服务。
      KAFKA_LISTENERS: PLAINTEXT://0.0.0.0:9092
      # 外部网络只能获取到容器名称，在内外网络隔离情况下
      # 通过名称是无法成功访问 kafka 的
      # 因此需要通过绑定这个监听器能够让外部获取到的是 IP      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://127.0.0.1:9092
      ALLOW_PLAINTEXT_LISTENER: yes
      KAFKA_LOG_RETENTION_HOURS: 120
      # Kafka默认使用-Xmx1G -Xms1G的JVM内存配置，
      KAFKA_HEAP_OPTS: "-Xms512M -Xmx1G"
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
    volumes:
      - ./kafka:/kafka
      ## 挂载位置（kafka镜像和宿主机器之间时间保持一直）
      - /etc/localtime:/etc/localtime
    depends_on:
      - zookeeper
    networks:
      - zk-kafka
networks:
  zk-kafka:
    name: zk-kafka
    driver: bridge
```
