## 概述

在实际生产环境中，一个应用往往由许多服务构成，而 docker 的最佳实践是一个容器只运行一个进程，因此运行多个微服务就要运行多个容器。多个容器协同工作需要一个有效的工具来管理他们，定义这些容器如何相互关联。compose 应运而生。compose 是用来定义和运行一个或多个容器(通常都是多个)运行和应用的工具。使用 compose 可以简化容器镜像的构建以及容器的运行。compose 使用 YAML 文件来定义多容器之间的关系。一个 docker-composeup 就可以把完整的应用跑起来。本质上，compose 把 YAML 文件解析成 docker 命令的参数，然后调用相应的 docker 命令行接口，从而将应用以容器化的方式管理起来。它通过解析容器间的依赖关系顺序地启动容器。而容器间的依赖关系由 YAML 文件中的 links 标记指定。

## 什么是 docker-compose

Docker Compose 是一个用来定义和运行复杂应用的 Docker 工具。一个使用 Docker 容器的应用，通常由多个容器组成。使用 Docker Compose 不再需要使用 shell 脚本来启动容器。

Docker Compose 能够在 Docker 节点上，以单引擎模式（Single-Engine Mode）进行多容器应用的部署和管理。多数的现代应用通过多个更小的微服务互相协同来组成一个完整可用的应用。

Docker Compose 并不是通过脚本和各种冗长的 docker 命令来将应用组件组织起来，而是通过一个声明式的配置文件描述整个应用，从而使用一条命令完成部署。应用部署成功后，还可以通过一系列简单的命令实现对其完整声明周期的管理。甚至，配置文件还可以置于版本控制系统中进行存储和管理。

在配置文件中，所有的容器通过 services 来定义，然后使用 docker-compose 脚本来启动，停止和重启应用，和应用中的服务以及所有依赖服务的容器，非常适合组合使用多个容器进行开发的场景。

## docker compose 的背景

Docker Compose 的前身是 Fig。Fig 是一个由 Orchard 公司开发的强有力的工具，在当时是进行多容器管理的最佳方案。Fig 是一个基于 Docker 的 Python 工具，允许用户基于一个 YAML 文件定义多容器应用，从而可以使用 fig 命令行工具进行应用的部署。Fig 还可以对应用的全生命周期进行管理。内部实现上，Fig 会解析 YAML 文件，并通过 Docker API 进行应用的部署和管理。在 2014 年，Docker 公司收购了 Orchard 公司，并将 Fig 更名为 Docker Compose。命令行工具也从 fig 更名为 docker-compose，并自此成为绑定在 Docker 引擎之上的外部工具。虽然它从未完全集成到 Docker 引擎中，但是仍然受到广泛关注并得到普遍使用。直至今日，Docker Compose 仍然是一个需要在 Docker 主机上进行安装的外部 Python 工具。使用它时，首先编写定义多容器（多服务）应用的 YAML 文件，然后将其交由 docker-compose 命令处理，Docker Compose 就会基于 Docker 引擎 API 完成应用的部署。

## docker compose 的安装

- 下载
	- 官网下载
	    <https://github.com/docker/compose> 通过官网直接下载即可
	    
	-  在线下载
	  ```bash
	  sudo curl -L  <https://github.com/docker/compose/releases/download/1.16.1/docker-compose>-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
```
	  

- 授权

  ```bash
  chmod +x /usr/local/bin/docker-compose
  # 开发环境可以授予最高权限
  chmod 777 /usr/local/bin/docker-compose
  ```

- 检查是否安装成功

  ```bash
  docker-compose -v
  docker-compose --version
  docker-compose version
  ```

## docker-compsoe 的配置文件详解

Docker Compose 使用 YAML 文件来定义多服务的应用。YAML 是 JSON 的一个子集，因此也可以使用 JSON。

Docker Compose 默认使用文件名 docker-compose.yml。当然，也可以使用-f 参数指定具体文件。

Docker Compose 的 YAML 文件包含 4 个一级 key：version、services、networks、volumes

- version 是必须指定的，而且总是位于文件的第一行。它定义了 Compose 文件格式（主要是 API）的版本。注意，version 并非定义 Docker Compose 或 Docker 引擎的版本号。

- services 用于定义不同的应用服务。上边的例子定义了两个服务：一个名为 mysql 数据库服务以及一个名为 eureka 的微服务。Docker Compose 会将每个服务部署在各自的容器中。

- networks 用于指引 Docker 创建新的网络。默认情况下，Docker Compose 会创建 bridge 网络。这是一种单主机网络，只能够实现同一主机上容器的连接。当然，也可以使用 driver 属性来指定不同的网络类型。

- volumes 用于指引 Docker 来创建新的卷。

### 1、image

指定为镜像名称或镜像 ID。如果镜像不存在，Compose 将尝试从互联网拉取这个镜像，例如： image: ubuntu image: orchardup/postgresql image: a4bc65fd

### 2、build

指定 Dockerfile 所在文件夹的路径。Compose 将会利用他自动构建这个镜像，然后使用这个镜像。 build: ./dir

### 3、command

覆盖容器启动后默认执行的命令。 command: bundle exec thin -p 3000

### 4、links

链接到其他服务容器，使用服务名称(同时作为别名)或服务别名（SERVICE:ALIAS）都可以

```
links:
 - db
 - db:database
 - redis
```

注意：使用别名会自动在服务器中的/etc/hosts 里创建，如：172.17.2.186 db，相应的环境变量也会被创建。

### 5、external_links

链接到 docker-compose.yml 外部的容器，甚至并非是 Compose 管理的容器。参数格式和 links 类似。 external_links:

```
- redis_1
 - project_db_1:mysql
 - project_db_2:sqlserver
```

### 6、ports

暴露端口信息。 宿主机器端口：容器端口（HOST:CONTAINER）格式或者仅仅指定容器的端口（宿主机器将会随机分配端口）都可以。

```
ports:
 - "3306"
 - "8080:80"
 - "127.0.0.1:8090:8001"
```

注意：当使用 HOST:CONTAINER 格式来映射端口时，如果你使用的容器端口小于 60 你可能会得到错误得结果，因为 YAML 将会解析 xx:yy 这种数字格式为 60 进制。所以建议采用字符串格式。

### 7、expose

暴露端口，与 posts 不同的是 expose 只可以暴露端口而不能映射到主机，只供外部服务连接使用；仅可以指定内部端口为参数。

```
expose:
 - "3000"
 - "8000"
```

### 8、volumes

设置卷挂载的路径。可以设置宿主机路径:容器路径（host:container）或加上访问模式（host:container:ro）ro 就是 readonly 的意思，只读模式。

```
volumes:
 - /var/lib/mysql:/var/lib/mysql
 - /configs/mysql:/etc/configs/:ro
```

### 9、volunes_from

挂载另一个服务或容器的所有数据卷。

```
volumes_from:
 - service_name
 - container_name
```

### 10、environment

设置环境变量。可以属于数组或字典两种格式。 如果只给定变量的名称则会自动加载它在 Compose 主机上的值，可以用来防止泄露不必要的数据。

```
environment:
 - RACK_ENV=development
 - SESSION_SECRET
```

### 11、env_file

从文件中获取环境变量，可以为单独的文件路径或列表。 如果通过 docker-compose -f FILE 指定了模板文件，则 env_file 中路径会基于模板文件路径。 如果有变量名称与 environment 指令冲突，则以后者为准。

```
env_file: .env
env_file:
 - ./common.env
 - ./apps/web.env
 - /opt/secrets.env
```

环境变量文件中每一行都必须有注释，支持#开头的注释行。

```
# common.env: Set Rails/Rack environment
RACK_ENV=development
```

### 12、extends

基于已有的服务进行服务扩展。例如我们已经有了一个 webapp 服务，模板文件为 common.yml.

```
# common.yml
webapp:
build: ./webapp
environment:
\ - DEBUG=false
\ - SEND_EMAILS=false
```

编写一个新的 development.yml 文件，使用 common.yml 中的 webapp 服务进行扩展。 development.yml

```
web:
extends:
file: common.yml
service:
  webapp:
    ports:
      \ - "8080:80"
    links:
      \ - db
    envelopment:
      - DEBUG=true
   db:
    image: mysql:5.7
```

后者会自动继承 common.yml 中的 webapp 服务及相关的环境变量。

### 13、net

设置网络模式。使用和 docker client 的 --net 参数一样的值。

```
# 容器默认连接的网络，是所有Docker安装时都默认安装的docker0网络.
net: "bridge"
# 容器定制的网络栈.
net: "none"
# 使用另一个容器的网络配置
net: "container:[name or id]"
# 在宿主网络栈上添加一个容器，容器中的网络配置会与宿主的一样
net: "host"
```

Docker 会为每个节点自动创建三个网络： 网络名称 作用 bridge 容器默认连接的网络，是所有 Docker 安装时都默认安装的 docker0 网络 none 容器定制的网络栈 host 在宿主网络栈上添加一个容器，容器中的网络配置会与宿主的一样 附录： 操作名称 命令 创建网络 docker network create -d bridge mynet 查看网络列表 docker network ls

### 14、pid

和宿主机系统共享进程命名空间，打开该选项的容器可以相互通过进程 id 来访问和操作。

```
pid: "host"
```

### 15、dns

```
配置DNS服务器。可以是一个值，也可以是一个列表。
dns: 8.8.8.8
dns:
 - 8.8.8.8
 - 9.9.9.9
```

### 16、cap_add，cap_drop

添加或放弃容器的 Linux 能力（Capability）。

```
cap_add:
 - ALL
cap_drop:
 - NET_ADMIN
 - SYS_ADMIN
```

### 17、dns_search

配置 DNS 搜索域。可以是一个值也可以是一个列表。

```
dns_search: example.com
dns_search:
 - domain1.example.com
 \ - domain2.example.com
working_dir, entrypoint, user, hostname, domainname, mem_limit, privileged, restart, stdin_open, tty, cpu_shares
```

这些都是和 docker run 支持的选项类似。

```
cpu_shares: 73
working_dir: /code
entrypoint: /code/entrypoint.sh
user: postgresql
hostname: foo
domainname: foo.com
mem_limit: 1000000000
privileged: true
restart: always
stdin_open: true
tty: true
```

## docker-compose 常用命令

| 命令                   | 说明                 |
| ---------------------- | -------------------- |
| docker-compose up -d   | 创建并启动服务             |
| docker-compose down    | 停止服务             |
| docker-compose ps      | 列出所有运行容器     |
| docker-compose logs    | 查看服务日志         |
| docker-compose build   | 构建或者重新构建服务 |
| Docker-compose start   | 启动服务             |
| docker-compose stop    | 停止已运行的服务     |
| docker-compose restart | 重启服务             |

## docker-compose 示例

### Mysql 多节点安装

```yaml
version: '3'
services:
  mysql-master:
    image: mysql/mysql-server:8.0.27
    restart: always
    container_name: mysql-master
    volumes:
      - ./master/data:/var/lib/mysql
      - ./master/my.cnf:/etc/mysql/my.cnf
      - ./master/init/:/docker-entrypoint-initdb.d/
      - /etc/localtime:/etc/localtime
    ports:
      - '13306:3306' #“宿主机端口号：容器内端口号”
    environment:
      MYSQL_ROOT_PASSWORD: "rootroot"
      MASTER_SYNC_USER: "sync_admin" #设置脚本中定义的用于同步的账号
      MASTER_SYNC_PASSWORD: "rootroot" #设置脚本中定义的用于同步的密码
      ADMIN_USER: "root" #当前容器用于拥有创建账号功能的数据库账号
      ADMIN_PASSWORD: "rootroot"
      ALLOW_HOST: "0.0.0.0" #允许同步账号的host地址
      TZ: "Asia/Shanghai" #解决时区问题
    command:
      -  "--server-id=1"
      -  "--default-authentication-plugin=mysql_native_password"
      -  "--character-set-server=utf8mb4"
      -  "--collation-server=utf8mb4_unicode_ci"
      -  "--log-bin=mysql-bin"
      -  "--sync_binlog=1"
    networks:
      - mysql-cluster
  mysql-slave1:
    image: mysql/mysql-server:8.0.27
    restart: always
    container_name: mysql-slave1
    ports:
      - '13307:3306'
    environment:
      MYSQL_ROOT_PASSWORD: "123456"
      SLAVE_SYNC_USER: "sync_admin" #用于同步的账号，由master创建
      SLAVE_SYNC_PASSWORD: "123456"
      ADMIN_USER: "root"
      ADMIN_PASSWORD: "123456"
      MASTER_HOST: "10.10.10.10" #master地址，开启主从同步需要连接master
      TZ: "Asia/Shanghai" #设置时区
    command:
      -  "--server-id=2"
      -  "--default-authentication-plugin=mysql_native_password"
      -  "--character-set-server=utf8mb4"
      -  "--collation-server=utf8mb4_unicode_ci"
      -  "--log-bin=mysql-bin"
      -  "--sync_binlog=1"
    networks:
      - mysql-cluster
    depends_on:
      - mysql-master
    volumes:
      - ./slave1/data:/var/lib/mysql
      - ./slave1/my.cnf:/etc/mysql/my.cnf
      - ./slave1/init/:/docker-entrypoint-initdb.d/
      - /etc/localtime:/etc/localtime
  mysql-slave2:
    image: mysql/mysql-server:8.0.27
    restart: always
    container_name: mysql-slave2
    ports:
      - '13308:3306'
    environment:
      MYSQL_ROOT_PASSWORD: "123456"
      SLAVE_SYNC_USER: "sync_admin" #用于同步的账号，由master创建
      SLAVE_SYNC_PASSWORD: "123456"
      ADMIN_USER: "root"
      ADMIN_PASSWORD: "123456"
      MASTER_HOST: "10.10.10.10" #master地址，开启主从同步需要连接master
      TZ: "Asia/Shanghai" #设置时区
    command:
      -  "--server-id=3"
      -  "--default-authentication-plugin=mysql_native_password"
      -  "--character-set-server=utf8mb4"
      -  "--collation-server=utf8mb4_unicode_ci"
      -  "--log-bin=mysql-bin"
      -  "--sync_binlog=1"
    networks:
      - mysql-cluster
    depends_on:
      - mysql-master
    volumes:
      - ./slave2/data:/var/lib/mysql
      - ./slave2/my.cnf:/etc/mysql/my.cnf
      - ./slave2/init/:/docker-entrypoint-initdb.d/
      - /etc/localtime:/etc/localtime
networks:
  mysql-cluster:
    name: mysql-cluster
    driver: bridge


```

### Redis 多节点安装

```yaml
version: '3.2'

services:
  redis-master:
    image: redis:6.2.7
    container_name: redis-master
    restart: always
    ports:
      - 6379:6379
    environment:
      TZ: "Asia/Shanghai"
    volumes:
      # 映射配置文件和数据目录
      - ./master/conf/redis.conf:/etc/redis/redis.conf
      - ./master/data:/data
      - ./master/logs:/logs
    command: [ "redis-server", "/etc/redis/redis.conf" ]
    privileged: true
    networks:
      - redis-cluster
  redis-slave1:
    image: redis:6.2.7
    container_name: redis-slave1
    restart: always
    ports:
      - 6380:6379
    environment:
      TZ: "Asia/Shanghai"
    volumes:
      # 映射配置文件和数据目录
      - ./slave1/conf/redis.conf:/etc/redis/redis.conf
      - ./slave1/data:/data
      - ./slave1/logs:/logs
    command: [ "redis-server", "/etc/redis/redis.conf" ]
    depends_on:
      - redis-master
    privileged: true
    networks:
      - redis-cluster
  redis-slave2:
    image: redis:6.2.7
    container_name: redis-slave2
    restart: always
    ports:
      - 6381:6379
    environment:
      TZ: "Asia/Shanghai"
    volumes:
      # 映射配置文件和数据目录
      - ./slave2/conf/redis.conf:/etc/redis/redis.conf
      - ./slave2/data:/data
      - ./slave2/logs:/logs
    command: [ "redis-server", "/etc/redis/redis.conf" ]
    depends_on:
      - redis-master
    privileged: true
    networks:
      - redis-cluster

networks:
  redis-cluster:
    name: redis-cluster
    driver: bridge

```

### Zookeeper 和 kafka 单节点安装

```yaml
version: '3.2'

services:
  zookeeper:
    image: zookeeper
    restart: always
    ports:
      - "2181:2181"
    volumes:
      - ./zookeeper/data:/data
      - ./zookeeper/logs:/logs
      - ./zookeeper/config:/conf
      - ./zookeeper/datalog:/datalog
    container_name: zookeeper
    networks:
      - zk-kafka

  kafka:
    image: wurstmeister/kafka
    restart: always
    ports:
      - "9092:9092"
    environment:
      KAFKA_BROKER_ID: 0
      KAFKA_LISTENERS: PLAINTEXT://0.0.0.0:9092
      KAFKA_ADVERTISED_HOST_NAME: "127.0.0.1"
      KAFKA_ZOOKEEPER_CONNECT: "zookeeper:2181"
    volumes:
      - ./kafka:/kafka
    depends_on:
      - zookeeper
    container_name: kafka
    networks:
      - zk-kafka

networks:
  zk-kafka:
    name: zk-kafka
    driver: bridge

```

### Postgressql 单节点安装

```yaml
version: '3.5'

services:
  postgres:
    container_name: postgres
    image: postgres:14.5
    environment:
      POSTGRES_USER: ${POSTGRES_USER:-postgres}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:-postgres}
      PGDATA: data/postgres
    volumes:
      - ./postgres:/data/postgres
    ports:
      - "5432:5432"
    networks:
      - postgres
    restart: always
    privileged: true

networks:
  postgres:
    name: postgres
    driver: bridge

```

### MongoDB 单节点安装

```yaml
version: "3.7"
services:
  mongodb:
    image: mongo:6.0
    container_name: mongodb
    ports:
      - 27017:27017
    restart: always
    volumes:
     - ./db:/data/db    # 挂载数据文件，
     - ./log:/var/log/mongodb  # 挂载日志文件，
     - ./config:/etc/mongo  # 挂载配置文件
     - /etc/localtime:/etc/localtime
    environment:
      - MONGO_INITDB_ROOT_USERNAME=admin
      - MONGO_INITDB_ROOT_PASSWORD=admin
      - TZ=Asia/Shanghai
      - wiredTigerCacheSizeGB=1.5
networks:
  mongodb:
    name: mongodb
    driver: bridge
```

### ELK 单节点安装

```yaml
version: '3.2'

services:
  elasticsearch:
    image: elasticsearch:7.17.4
    volumes:
      - /etc/localtime:/etc/localtime
      - ./es/plugins:/usr/share/elasticsearch/plugins #插件文件挂载
      - ./es/data:/usr/share/elasticsearch/data #数据文件挂载
    ports:
      - "9200:9200"
      - "9300:9300"
    container_name: elasticsearch
    restart: always
    environment:
      - "cluster.name=elasticsearch" #设置集群名称为elasticsearch
      - "discovery.type=single-node" #以单一节点模式启动
      - "ES_JAVA_OPTS=-Xms1024m -Xmx1024m" #设置使用jvm内存大小
    networks:
      - elk

  logstash:
    image: logstash:7.17.4
    container_name: logstash
    restart: always
    volumes:
      - /etc/localtime:/etc/localtime
      - "./logstash/pipelines.yml:/usr/share/logstash/config/pipelines.yml"
      - "./logstash/logstash-audit.conf:/usr/share/logstash/pipeline/logstash-audit.conf"
      - "./logstash/logstash-user-action.conf:/usr/share/logstash/pipeline/logstash-user-action.conf"
    ports:
      - "5044:5044"
      - "50000:50000/tcp"
      - "50000:50000/udp"
      - "9600:9600"
    environment:
      LS_JAVA_OPTS: -Xms1024m -Xmx1024m
      TZ: Asia/Shanghai
      MONITORING_ENABLED: false
    links:
      - elasticsearch:es #可以用es这个域名访问elasticsearch服务
    networks:
      - elk
    depends_on:
      - elasticsearch

  kibana:
    image: kibana:7.17.4
    container_name: kibana
    restart: always
    volumes:
      - /etc/localtime:/etc/localtime
      - ./kibana/config/kibana.yml:/usr/share/kibana/config/kibana.yml
    ports:
      - "5601:5601"
    links:
      - elasticsearch:es #可以用es这个域名访问elasticsearch服务
    environment:
      - ELASTICSEARCH_URL=http://elasticsearch:9200 #设置访问elasticsearch的地址
      - "elasticsearch.hosts=http://es:9200" #设置访问elasticsearch的地址
      - I18N_LOCALE=zh-CN
    networks:
      - elk
    depends_on:
      - elasticsearch

networks:
  elk:
    name: elk
    driver: bridge
      #  ik 分词器的安装

      # 集群 docker-compose exec elasticsearch elasticsearch-plugin install https://github.com/medcl/elasticsearch-analysis-ik/releases/download/v7.17.4/elasticsearch-analysis-ik-7.17.4.zip

      # 单点 bin/elasticsearch-plugin install https://github.com/medcl/elasticsearch-analysis-ik/releases/download/v7.17.4/elasticsearch-analysis-ik-7.17.4.zip

```

## 总结

docker-compsoe 是一个非常有必要学习的东西，挺不错的

使用 compose 对 Docker 容器进行编排管理时，需要编写 docker-compose.yml 文件，初次编写时，容易遇到一些比较低级的问题，导致执行 docker-compose up 时先解析 yml 文件的错误。比较常见的是 yml 对缩进的严格要求。
