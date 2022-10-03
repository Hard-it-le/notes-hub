# Docker 快速入门指南

## Docker 快速入门

### Docker 的历史

2010年，几个的年轻人，就在美国的旧金山成立了一家公司dotcloud。做一些Paas平台的创业公司！从事LXC（Linux Container容器）有关的容器技术！Linux Container容器是一种内核虚拟化技术，可以提供轻量级的虚拟化，以便隔离进程和资源。他们将自己的技术（容器化技术）命名就是Docker。Docker刚刚延生的时候，没有引起行业的注意！虽然获得了创业孵化器(Y Combinator)的支持、也获得过一些融资，但随着IT巨头们(微软、谷歌、亚马逊等厂商)也进入PaaS凭他，dotCloud举步维艰，眼看就活不下去！2013年，dotCloud的创始人，28岁的Solomon Hykes做了一个艰难的决定，将dotCloud的核心引擎开源，这项核心引擎技术能够将Linux容器中的应用程序、代码打包，轻松的在服务器之间进行迁移。这个基于LXC技术的核心管理引擎开源后，让全世界的技术人员感到惊艳。感叹这一切太方便了！！越来越多的人发现docker的优点！火了。Docker每个月都会更新一个版本！2014年6月9日，Docker1.0发布！1.0版本的发布，标志着docker平台已经足够成熟稳定，并可以被应用到生产环境。docker为什么这么火？因为docker十分的轻巧！在容器技术出来之前，我们都是使用虚拟机技术！在window中装一个VMware，通过这个软件我们可以虚拟出来一台或者多台电脑！笨重！虚拟机也属于虚拟化技术，Docker容器技术，也是一种虚拟化技术！

### Docker 的版本

docker从17.03版本之后分为CE（Community Edition:社区版）和EE（Enterprise Edition:企业版），本教程使用社区版(CE)。

<https://www.docker.com>

### 什么是docker

当人们说“Docker”时，他们通常是指Docker Engine，它是一个客户端-服务器应用程序，由Docker守护进程、一个REST API指定与守护进程交互的接口、和一个命令行接口（CLI）与守护进程通信（通过封装REST API）。Docker Engine从CLI中接受docker命令，例如docker run、docker ps来列出正在运行的容器、docker images来列出镜像，等等。所以 Docker 是什么

- docker是一个软件，可以运行在window、linux、mac等各种操作系统上。

- docker是一个开源的应用容器引擎，基于Go语言开发并遵从Apache2.0协议开源，项目代码托管在github上进行维护
- docker可以让开发者打包他们的应用以及依赖包到一个轻量级、可移植的容器中，然后发布到任何流行的Linux机器上
- 容器是完全使用沙箱机制，相互之间不会有任何接口,更重要的是容器性能开销极低

### Docker 的架构和基本组成

![image.png](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/faaaa930cf2d43608f775330644efa30~tplv-k3u1fbpfcp-watermark.image?)

- docker主机(Host)：安装了Docker程序的机器（Docker直接安装在操作系统之上）
- docker仓库(Registry)：用来保存各种打包好的软件镜像；仓库分为公有仓库和私有仓库。(很类似maven)
- docker镜像(Images)：软件打包好的镜像；放在docker仓库中
- docker容器(Container)：镜像启动后的实例称为一个容器；容器是独立运行的一个或一组应用
- Client：客户端；操作docker服务器的客户端（命令行或者界面）

> Docker用Go编程语言编写，并利用Linux内核的多种功能来交付其功能。Docker使用一种称为名称空间的技术来提供容器的隔离工作区。运行容器时，Docker会为该容器创建一组名称空间。这些名称空间提供了一层隔离。容器的每个方面都在单独的名称空间中运行，并且对其的访问仅限于该名称空间。

### Docker与操作系统的对比

| 特性     | 容器               | 虚拟机         |
| -------- | ------------------ | -------------- |
| 启动速度 | 秒级               | 分钟级         |
| 性能     | 接近原声           | 较弱           |
| 内存代价 | 很小               | 较多           |
| 硬盘使用 | 一般为 MB          | 基本在 GB 以上 |
| 运行密度 | 单机支持上千个容器 | 一般几十个     |
| 隔离性   | 安全隔离           | 完全隔离       |
| 迁移性   | 优秀               | 一般           |

传统的虚拟机方式提供的是相对封闭的隔离。Docker利用Linux系统上的多种防护技术实现了严格的隔离可靠性，并且可以整合众多安全工具。从1.3.0版本开始，docker重点改善了容器的安全控制和镜像的安全机制，极大提高了使用docker的安全性。

### Docker 的安装

#### 1、删除旧的docker版本

```bash
sudo dnf remove docker \ 
                docker-client \ 
                docker-client-latest \ 
                docker-common \ 
                docker-latest \ 
                docker-latest-logrotate \ 
                docker-logrotate \ 
                docker-selinux \ 
                docker-engine-selinux \ 
                docker-engine
sudo yum remove docker*
```

#### 2、使用安装脚本自动安装

官方安装脚本

```bash
curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun
```

国内 daocloud 一键安装命令

```bash
curl -sSL https://get.daocloud.io/docker | sh
```

#### 3、使用yum安装

##### 3.1、设置docker yum源

```bash
sudo yum install -y yum-utils

sudo yum-config-manager --add-repo    https://download.docker.com/linux/centos/docker-ce.repo
```

##### 3.2、安装最新的docker engine

```bash
sudo yum install docker-ce docker-ce-cli containerd.io
```

##### 3.3、安装指定版本docker engine

```bash
#找到所有可用docker版本列表
yum list docker-ce --showduplicates | sort -r

# 安装指定版本，用上面的版本号替换<VERSION_STRING>
sudo yum install docker-ce-<VERSION_STRING>.x86_64 docker-ce-cli-
<VERSION_STRING>.x86_64 containerd.io

#例如：
#yum install docker-ce-3:20.10.5-3.el7.x86_64 docker-ce-cli-3:20.10.5-
3.el7.x86_64 containerd.io
#注意加上 .x86_64 大版本号
```

#### 4、docker 启动服务

```bash
systemctl start docker

systemctl enable docker
```

#### 5、镜像加速

- 科大镜像：**<https://docker.mirrors.ustc.edu.cn/>**
- 网易：**<https://hub-mirror.c.163.com/>**
- 阿里云：**<<https://<你的ID>.mirror.aliyuncs.com>>**
- 七牛云加速器：**<https://reg-mirror.qiniu.com>**

```bash
sudo mkdir -p /etc/docker
# /etc/docker/daemon.json 是Docker的核心配置文件
sudo tee /etc/docker/daemon.json <<-'EOF'

{
"registry-mirrors": ["https://82m9ar63.mirror.aliyuncs.com"]
}
EOF

sudo systemctl daemon-reload

sudo systemctl restart docker
```

/etc/docker/daemon.json是Docker的核心配置文件

#### 6、查看docker是否启动

```bash
docker -v
docker version
docker info
```

### Docker 常见的命令

![image.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/219db28eccdc43d18e4995fa484d0687~tplv-k3u1fbpfcp-watermark.image?)

#### docker 帮助命令

- version、info、help

| 命令           | 说明                               |
| -------------- | ---------------------------------- |
| docker version | 版本获取，可以用来验证是否安装成功 |
| docker info    | 对docker的信息描述                 |
| docker --help  | 帮助命令                           |

#### docker 镜像命令

- Images、search

| 命令                       | 说明                                                    |
| -------------------------- | ------------------------------------------------------- |
| docker images              | 列出本地主机上的镜像；                                  |
| docker images -a           | 列出本地所有的镜像（含中间映像层）；                    |
| docker images -q           | 只显示镜像ID；                                          |
| docker images -digests     | 显示镜像的摘要信息；                                    |
| docker images -no-trunc    | 显示完整的镜像信息；                                    |
| docker search tomcat       | 查询github上tomcat的镜像；（ <https://hub.docker.com>） |
| docker search --no-trunc   | 显示完整的镜像描述；                                    |
| docker search -s 30 tomcat | 列出收藏数不小于30的tomcat镜像;                         |
| docker search --automated  | 只列出 automated build(自动构建)类型的镜像；            |

- pull 、rmi

| 命令                               | 说明                                   |
| ---------------------------------- | -------------------------------------- |
| docker pull tomcat                 | 下载tomcat镜像；                       |
| docker pull centos                 | 下载一个CentOS镜像；                   |
| docker pull tomcat:latest          | 下载最新版tomcat镜像；                 |
| docker rmi + 名字                  | 删除镜像；                             |
| docker rmi -f + 名字（或ID）       | 删除单个（强制删除）；                 |
| docker rmi -f hello-world nginx    | 删除多个，删除hello-world和nginx镜像； |
| docker rmi -f $(docker images -qa) | 删除全部                               |

#### docker 容器命令

- pul、run

| 命令                              | 说明                                                         |
| --------------------------------- | ------------------------------------------------------------ |
| docker pull centos                | 下载CentOS镜像；                                             |
| docker run centos                 | 【重要】新建并启动centos容器；                               |
| docker run -it centos             | 【常用】-i：以交互模式运行容器；-t：为容器重新分配一个伪输入终端。-i与-t经常一起使用；（进入容器的终端） |
| docker run --name mycentos centos | 新建并启动centos容器，并取别名mycentos；                     |
| docker run -d centos              | 后台运行centos容器，并返回容器ID，也即启动守护式容器；（不进入容器终端） |
| docker run -P centos              | 随机端口映射；                                               |
| docker run -p centos              | 指定端口映射，有以下四种格式；（ip:hostPort:containerPort 、ip::containerPort 、hostPort:containerPort 、containerPort） |

- ps、exit 、ctrl+P+Q

| 命令                 | 说明                                        |
| -------------------- | ------------------------------------------- |
| docker ps            | 列出当前所有正在运行的容器；                |
| docker ps -l         | 显示最近创建的容器；                        |
| docker ps -a         | 列出当前所有正在运行的容器+历史上运行过的； |
| docker ps -n         | 显示最近n个创建的容器；                     |
| docker ps -q         | 静默模式，只显示容器编号；                  |
| docker ps --no-trunc | 不截断输出；                                |
| exit                 | 容器停止退出；                              |
| ctrl+P+Q             | 容器不停止退出；（退出容器终端到主机）      |

- start、restart、stop、kill

| 命令                            | 说明                               |
| ------------------------------- | ---------------------------------- |
| docker start + 容器ID或容器名   | 启动容器；                         |
| docker restart + 容器ID或容器名 | 重启容器，成功则返回对应容器编号； |
| docker stop + 容器ID或容器名    | 停止容器；（缓慢停止，正常关闭）   |
| docker kill + 容器ID或容器名    | 强制停止容器；                     |

- rm、logs、top、inspect

| 命令                              | 说明                                                         |
| --------------------------------- | ------------------------------------------------------------ |
| docker rm + 容器ID                | 删除已停止的容器                                             |
| docker rmi + 容器ID               | 删除已停止的容器镜像；                                       |
| docker rm -f $(docker ps -a -q)   | 一次性删除多个容器；                                         |
| docker ps -a -q                   | xargs docker rm                                              |
| docker logs -f -t --tail + 容器ID | 查看容器日志；（-t 是加入时间戳；-f 跟随最新的日志打印；–tail 数字 显示最后多少条） |
| docker logs --tail 3 + 容器ID     | 查看容器最后三行日志；                                       |
| docker top + 容器ID               | 查看容器内运行的进程；（可以把容器看成简易Linux，大部分命令可以使用） |
| docker inspect + 容器ID           | 查看容器内部细节；                                           |

- exec、attach、cp

| 命令                                     | 说明                                                         |
| ---------------------------------------- | ------------------------------------------------------------ |
| docker exec -it 容器ID bashShell         | 对正在执行的容器进行bashShell操作，不进入容器终端            |
| docker exec -it 123abc ls -l /tmp        | 对ID为123abc的容器进行ls -l /tmp操作，不进入容器终端；       |
| docker exec -it 123abc /bin/bash         | 进入容器终端；（启动新进程）                                 |
| docker attach 容器ID                     | 重新进入行的容器并以命令行交互，进入容器终端；（不启动新进程） |
| docker cp 容器ID:容器内路径 目的主机路径 | 从容器内拷贝文件到主机上（数据永久化）；                     |
| docker cp 123abc: /tmp/yum.log /root     | 将ID为123abc容器里的/tmp/yum.log文件拷贝到/root目录下；      |

### Docker 常见软件部署

#### nginx

```bash
docker run --name gourdnginx -p 80:80 \
 --restart=always -e TZ="Asia/Shanghai" -d \
 -v $PWD/conf/nginx.conf:/etc/nginx/nginx.conf \
 -v $PWD/logs:/var/log/nginx nginx
```

#### mysql

- 5.7 版本

```bash
docker run -p 3306:3306 --name mysql57-app \
-v /app/mysql/log:/var/log/mysql \
-v /app/mysql/data:/var/lib/mysql \
-v /app/mysql/conf:/etc/mysql/conf.d \
-e MYSQL_ROOT_PASSWORD=123456  -d mysql:5.7
```

- 8.0 版本

```bash
docker run -p 3306:3306 --name mysql8-app \
-v /app/mysql/log:/var/log/mysql \
-v /app/mysql/data:/var/lib/mysql \
-v /app/mysql/conf:/etc/mysql/conf.d \
-e MYSQL_ROOT_PASSWORD=123456  --privileged -d mysql:8.0
```

#### redis

```bash
docker run -p 6379:6379 --name redis \
-v /app/redis/redis.conf:/etc/redis/redis.conf \
-v /app/redis/data:/data \
-d redis:6.2.1-alpine3.13 \
redis-server /etc/redis/redis.conf --appendonly yes
```

#### tomcat

```bash
docker run --name tomcat-app -p 8080:8080 \
-v tomcatconf:/usr/local/tomcat/conf \
-v tomcatwebapp:/usr/local/tomcat/webapps \
-d tomcat:jdk8-openjdk-slim-buster
```

#### mongo

```bash
docker run -d --name mongo --restart=always \
-v /usr/local/gourd/docker/mongodb/datadb:/data/db -p 27017:27017 \
-e MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=root \
-e TZ="Asia/Shanghai" --privileged=true mongo
```

#### Zookeeper

```bash
docker  run --privileged=true --name zookeeper \
-p 2181:2181 --restart=always -e TZ="Asia/Shanghai" \
-d zookeeper:latest
```

#### Kafka

```bash
ocker run -d --name kafka -p 9092:9092 --restart=always \
-e TZ="Asia/Shanghai" \
-e KAFKA_BROKER_ID=0 -e KAFKA_ZOOKEEPER_CONNECT=172.19.175.13:2181 \
-e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://172.19.175.13:9092 \
-e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092 \
-t wurstmeister/kafka
```

### Docker 容器重启策略

- no，默认策略，在容器退出时不重启容器
- on-failure，在容器非正常退出时（退出状态非0），才会重启容器
- on-failure:3，在容器非正常退出时重启容器，最多重启3次
- always，在容器退出时总是重启容器
- unless-stopped，在容器退出时总是重启容器，但是不考虑在Docker守护进程启动时就已经停止了的容器

## Docker 网络

### 基础理论

docker使用Linux桥接网卡，在宿主机虚拟一个docker容器网桥（docker0），docker启动一个容器时会根据docker网桥的网段分配给容器一个IP地址，称为Container-IP，同时Docker网桥是每个容器的默认网络网关。因为在同一宿主机内的容器都接入同一个网桥，这样容器之间就能够通过容器的Container-IP直接通信。

docker网桥是宿主机虚拟出来的，并不是真实存在的网络设备，外部网络是无法寻址到的，这也意味着外部网络无法通过直接Container-IP访问到容器。

如果容器希望外部访问能够访问到，可以通过映射容器端口到宿主主机(端口映射)，即docker run创建容器时候通过-p或-P参数来启用，访问容器的时候就通过`宿主机IP:容器端口`访问容器。

### 网络模式

| Docker 网络   模式 | 配置                      | 说明                                                         |
| ------------------ | ------------------------- | ------------------------------------------------------------ |
| host 模式          | –net=host                 | 容器和宿主机共享`Network namespace`。 <br>容器将不会虚拟出自己的网卡，配置自己的IP 等，而是使用宿主机的IP和端口。 |
| container 模式     | -net=container:NAME_or_ID | 容器和另外一个容器共享`Network namespace`。<br> kubernetes中的pod就是多个容器共享一个Network namespace。<br> 创建的容器不会创建自己的网卡，配置自己的 IP， 而是和`一个指定的容器共享IP、端口范围`。 |
| none 模式          | –net=none                 | 容器有独立的Network namespace，并没有对其进行任何网络设置，如分配veth pair和网桥连接，配置IP等。<br> `该模式关闭了容器的网络功能。` |
| bridge 模式        | –net=bridge               | (默认模式)。此模式会为每一个容器分配、设置IP等，并将容器连接到一个`docker0虚拟网桥`，通过`docker0网桥`以及`Iptable nat`表配置与宿主机通信 |
| 用户自定义         | --net=mynet               | 用户自己使用network相关命令定义网络，创建容器的时候可以指定为自己定义的网络 |

### bridge 模式

默认的网络模式。bridge 模式下容器没有一个公有 ip,只有宿主机可以直接访问,外部主机是不可见的,但容器通过宿主机的 NAT 规则后可以访问外网。

#### Bridge 桥接模式的实现步骤

- Docker Daemon 利用 veth pair 技术，在宿主机上创建两个虚拟网络接口设备，假设为 veth0 和veth1。而 veth pair技术的特性可以保证无论哪一个veth接收到网络报文，都会将报文传输给另一方。

- Docker Daemon 将 veth0 附加到 Docker Daemon 创建的 docker0 网桥上。保证宿主机的网络报文可以发往 veth0;

- Docker Daemon 将 veth1 添加到 Docker Container 所属的 namespace 下，并被改名为 eth0。 如此一来，保证宿主机的网络报文若发往 veth0 则立即会被 eth0 接收，实现宿主机到Docker Container网络的联通性;同时也保证Docker Container单独使用eth0，实现容器网络环境的隔离性。

#### Bridge桥接模式的缺陷

Docker Container 不具有一个公有IP，即和宿主机eth0不处于同一个网段。导致的结果是宿主机以外的世界不能直接和容器进行通信。

#### 注意事项

eth 设备是成双成对出现的，一端是容器内部命名为 eth0，一端是加入到网桥并命名的 veth (通常命名为 veth)，它们组成了一个数据传输通道，一端进一端出，veth 设备连接了两个网络设备并实现了数据通信。

### Host 网络模式

host 模式相当于 Vmware 中的 NAT 模式，与宿主机在同一个网络中，但`没有独立IP地址`。

启动容器使用 host 模式，容器将不会获得一个独立的Network Namespace，而是和宿主机共用一个Network Namespace。

容器将不会虚拟出自己的网卡，配置自己的IP等，而是使用宿主机的IP和端口。除此之外容器的其他方面，比如文件系统、进程列表等还是和宿主机隔离

使用host模式的容器可以直接使用宿主机的IP地址与外界通信，容器内部的服务端口也可以使用宿主机的端口，不需要进行NAT，`host最大的优势就是网络性能比较好`，docker host上已经使用的端口就不能再用了，网络的隔离性不好。

host网络模式需要在容器创建时指定–network=host

host模式是bridge桥接模式很好的补充。采用host模式的Docker Container，可以直接使用宿主机的IP地址与外界进行通信，若宿主机的eth0是一个公有IP，那么容器也拥有这个公有IP。同时容器内服务的端口也可以使用宿主机的端口，无需额外进行NAT转换。

host模式可以让容器共享宿主机网络栈,这样的好处是外部主机与容器直接通信,但是容器的网络缺少隔离性。

#### Host网络模式的缺陷

使用Host模式的容器不再拥有隔离、独立的网络环境。虽然可以让容器内部的服务和传统情况无差别、无改造的使用，但是由于网络隔离性的弱化，该容器会与宿主机共享竞争网络栈的使用; 另外，容器内部将不再拥有所有的端口资源，原因是部分端口资源已经被宿主机本身的服务占用，还有部分端口已经用以bridge网络模式容器的端口映射。

### Container 网络模式

一种特殊host网络模式，
ontainer网络模式是Docker中一种较为特别的网络的模式。在容器创建时使用– network=container:vm1指定。(vm1指定的是运行的容器名)处于这个模式下的 Docker 容器会共享一个网络环境,这样两个容器之间可以使用localhost高效快速通信。

#### Container 网络模式的缺陷

Container 网络模式没有改善容器与宿主机以外世界通信的情况(和桥接模式一样，不能连接宿主机以外的其他设备)。

这个模式指定新创建的容器和已经存在的一个容器共享一个Network Namespace，而不是和宿主机共享。新创建的容器不会创建自己的网卡，配置自己的IP，而是和一个指定的容器共享IP、端口范围等。 同样，两个容器除了网络方面，其他的如文件系统、进程列表等还是隔离的。两个容器的进程可以通过lo网卡设备通信

### none 模式

使用none模式，Docker容器拥有自己的Network Namespace，但是，并不为Docker容器进行任何网络配置。`Docker容器没有网卡、IP、路由等信息。需要我们自己为Docker容器添加网卡、配置IP等。`

这种网络模式下容器只有lo回环网络，没有其他网卡。none模式可以在容器创建时通过-- network=none来指定。`这种类型的网络没有办法联网，封闭的网络能很好的保证容器的安全性。`

#### docker 容器创建流程

- 创建一对虚拟接口/网卡，也就是veth pair，分别放到本地主机和新容器中;

- 本地主机一端桥接到默认的 docker0 或指定网桥上，并具有一个唯一的名字，如 vetha596da4;

- 容器一端放到新容器中，并修改名字作为 eth0，这个网卡/接口只在容器的名字空间可见;

- 从网桥可用地址段中(也就是与该bridge对应的network)获取一个空闲地址分配给容器的 eth0，并配置默认路由到桥接网卡 vetha596da4。

- 容器就可以使用 eth0 虚拟网卡来连接其他容器和其他网络。 如果不指定--network，创建的容器默认都会挂到 docker0 上，使用本地主机上 docker0 接口的 IP 作为 所有容器的默认网关。

- 进入容器查看网络地址

#### 容器网络连接图

![image.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c0b21832beb4879855567d2efcc5ae6~tplv-k3u1fbpfcp-watermark.image?)

### docker 网络常用命令

| 命令 | 说明 |
| ---- | ---- |
|      |      |

| docker network ls  [--no-trunc]     | 查看已经建立的网络对象       |
| ----------------------------------- | ---------------------------- |
| docker network create  NETWORK_name | 创建新的网络对象             |
| docker network rm NETWORK           | 删除一个或多个网络           |
| docker network inspect network_id   | 查看一个或多个网络的详细信息 |
| docker run –-network container_id   | 为启动的容器指定网络模式     |
| docker network connect              | 容器网络连接                 |
| docker network  disconnect          | 容器网络断开连接             |

- 常用参数

  -

#### 容器镜像设定固定ip

```
# --driver string 指定网络的驱动(默认 "bridge")
#  --subnet strings 指定子网网段(如192.168.0.0/16、172.88.0.0/24)
# --ip-range strings  执行容器的IP范围，格式同subnet参数
# --gateway strings 子网的IPv4 or IPv6网关，如(192.168.0.1)
docker network create -d bridge --subnet=172.172.0.0/24  --gateway 172.172.0.1 network

# 172.172.0.0/24: 24 代表子码掩码是255.255.255.0 172.172.0.0/16: 16 代表子码掩码

docker network ls

docker run -itd --name nginx3 -p 80:80 --net network --ip 172.172.0.10
```

## docker 数据挂载

### 什么是数据卷

使用 docker 容器的时候，会产生一系列的数据文件，这些数据文件在删除 docker 容器时是会消失的，但是其中产生的部分内容是希望能够把它给保存起来另作用途的，Docker将应用与运行环境打包成容器发布，程序员希望在运行过程钟产生的部分数据是可以持久化的的，而且容器之间我们希望能够实现数据共享。

一般地来说，docker容器数据卷可以看成常用的u盘，它存在于一个或多个的容器中，由docker挂载到容器，但不属于联合文件系统，Docker不会在容器删除时删除其挂载的数据卷。

#### 数据卷的特点

- 1. 数据卷可以在容器之间共享或重用数据

- 2. 数据卷中的更改可以立即生效

- 3. 数据卷中的更改不会包含在镜像的更新中

- 4. 数据卷默认会一直存在，即使容器被删除

- 5. 数据卷的生命周期一直持续到没有容器使用它为止

#### 容器中的管理数据

- 数据卷:Data Volumes 容器内数据直接映射到本地主机环境

- 数据卷容器:Data Volume Containers 使用特定容器维护数据卷

### docker数据卷

数据卷(Data Volumes)是一个可供一个或多个容器使用的特殊目录，它将主机操作系统目录直接映射进容器。

#### 数据卷注意事项

- 挂载数据卷，最好是通过run而非create/start创建启动容器，create/start命令创建启动容器 后，再挂载数据卷相当麻烦，要修改很多配置文件，但并非不可以。

- docker官网推荐尽量进行目录挂载，不要进行文件挂载

#### 数据卷类型

- 1. 宿主机数据卷:直接在宿主机的文件系统中但是容器可以访问(bind mount)

- 2. 命名的数据卷:磁盘上Docker管理的数据卷，但是这个卷有个名字。

- 3. 匿名数据卷:磁盘上Docker管理的数据卷，因为没有名字想要找到不容易，Docker来管理这些文件。

#### 宿主机数据卷

bind mounts:容器内的数据被存放到宿主机文件系统的任意位置，甚至存放到一些重要的系统目录或 文件中。除了docker之外的进程也可以任意对他们进行修改。

当使用bind mounts时，宿主机的目录或文件被挂载到容器中。容器将按照挂载目录或文件的绝对路径 来使用或修改宿主机的数据。宿主机中的目录或文件不需要预先存在，在需要的使用会自动创建。

使用bind mounts在性能上是非常好的，但这依赖于宿主机有一个目录妥善结构化的文件系统。

使用bind mounts的容器可以在通过容器内部的进程对主机文件系统进行修改，包括创建，修改和删除 重要的系统文件和目录，这个功能虽然很强大，但显然也会造成安全方面的影响，包括影响到宿主机上 Docker以外的进程

##### 注意事项

- 如果挂载一个空的数据卷到容器中的一个非空目录中，那么这个目录下的文件会被复制到数据卷中

- 如果挂载一个非空的数据卷到容器中的一个目录中，那么容器中的目录会显示数据卷中的数据。如果原来容器中的目录有数据，那么原始数据会被隐藏掉

##### 基本使用

- 语法

```
docker run -v /宿主机绝对路径目录:/容器内目录 镜像名
```

- 基本使用

```
docker run -itd --name mysql --restart always --privileged=true -p 3306:3306 -e MYSQL_ROOT_PASSWORD=admin
-v /data/mysql:/var/lib/mysql mysql:5.7.31 --character-set-server=utf8 --collation-server=utf8_general_ci
```

##### 容器目录权限

```
通过 -v 容器内路径: ro rw 改变读写权限 ro:readonly 只读

rw:readwrite 可读可写

docker run -it -v /宿主机绝对路径目录:/容器内目录:ro 镜像名

docker run -it -v /宿主机绝对路径目录:/容器内目录:rw 镜像名

例如:

docker run -d -P --name nginx05 -v nginx1:/etc/nginx:ro nginx

docker run -d -P --name nginx05 -v nginx2:/etc/nginx:rw nginx

ro 只要看到ro就说明这个路径只能通过宿主机来操作，容器内部是无法操作!
```

#### 命名的数据卷

- 基本使用

```
docker run -itd --name nginx -p 80:80 -v lagouedu-nginx:/etc/nginx nginx:1.19.3-

alpine

查看docker数据卷 docker volume ls

查看lagouedu-nginx宿主机目录

docker volume inspect lagouedu-nginx

进入docker数据卷默认目录

cd /var/lib/docker/volumes/lagouedu-nginx

查看文件

ls

所有的文件docker默认保存在_data目录中 cd _data

删除容器

docker rm $(docker stop $(docker ps -aq))

查看挂载数据是否还存在，通过查看数据，发现删除容器后，宿主机中的数据还存在

ls
```

#### 匿名数据卷

- 基本使用

```
docker run -itd --name nginx -p 80:80 -v /etc/nginx nginx:1.19.3-alpine 查看docker数据卷

docker volume ls 
查看宿主机目录

docker volume inspect dbd07daa4e40148b11.... 

进入docker数据卷默认目录

cd /var/lib/docker/volumes/dbd07daa4e40148b11.... 

查看文件

ls

所有的文件docker默认保存在_data目录中 cd _data

删除容器

docker rm $(docker stop $(docker ps -aq))

查看挂载数据是否还存在，通过查看数据，发现删除容器后，宿主机中的数据还存在

ls
```
