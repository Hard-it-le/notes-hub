## MySQL 体系架构

MySQL Server 架构自顶向下大致可以分网络连接层、服务层、存储引擎层和系统文件层。

### 网络连接层

客户端连接（Client Connectors）：提供与 MySQL 服务器建立的连接支持，目前支持所有主流服务端编程技术，比如主流语言 Java、C、Python 等，通过各自的 API 技术与 MySQL 建立连接

### 服务层（MySQL Server）

服务层是 MySQL Server 的核心，主要包含系统管理和控制工具,连接池、SQL 接口、解析器、查询优化和缓存六个部分

- 连接池（Connection Pool）：负责存储和管理客户端与数据库的连接，一个线程负责管理一个连接，
- 系统管理和控制工具（Management Services & Utilities）：例如备份恢复、安全管理、集群管理等
- SQL 接口（SQL Interface）：用于接受客户端发送的各种 SQL 命令，并且返回用户需要查询的结果。比如 DML、DDL、存储过程、视图、触发器等
- 解析器（Parser）：负责讲请求的 SQL 解析生成一个"解析树"，然后根据一些 MySQL 规则进行一步检查解析树是否合法
- 查询优化器（Optimizer）:当"解析器" 通过解析器预发检查后，交友优化器将其转化成为执行计划，然后与存储引擎交互
- 缓存（Cache & Bufer）：缓存机制是由一系列小缓存组成的。比如表缓存，记录缓存，权限缓存，引擎缓存等。如果查询缓存有命中的查询结果，查询语句就可以直接去查询缓存中取数据

### 存储引擎层（Pluggable Storage Engines）

存储引擎负责 MySQL 中数据的存储与提取，与底层系统文件进行交互。MySQL 存储引擎是插件式的，服务器中的查询执行引擎通过接口与存储引擎进行通信，接口屏蔽了不同存储引擎之间的差异。现在有很多种存储引擎，各有各的特点，最常见的是 MyISAM 和 InnoDB。

### 系统文件层（File System）

该层负责将数据库的数据和日志存储在文件系统之上，并完成与存储引擎的交互，是文件的物理存储层。主要包含日志文件，数据文件，配置文件，pid 文件，socket 文件等。

- 日志文件

  - 错误日志（Error Log）

    > 默认开启 show variables like '%log_error%'

  - 通用查询日志（General query log）

    > 记录一般查询语句，show variables like '%general%';

  - 二进制日志

    记录了对 MySQL 数据库执行的更改操作，并且记录了语句的发生时间、执行时长；但是它不记录 select、show 等不修改数据库的 SQL。主要用于数据库恢复和主从复制。

```sql
  show variables like '%log_bin%'; //是否开启
  show variables like '%binlog%'; //参数查看
  show binary logs;//查看日志文件
```

- 满查询日志
  记录所有执行时间超时的查询 SQL，默认是 10 秒。

```sql
show variables like '%slow_query%'; //是否开启
show variables like '%long_query_time%'; //时长
```

- 配置文件

  用于存放 MySQL 所有的配置信息文件，比如 my.cnf、my.ini 等。

- 数据文件

  - db.opt 文件：记录这个库的默认使用的字符集和校验规则。
  - frm 文件：存储与表相关的元数据（meta）信息，包括表结构的定义信息等，每一张表都会有一个 frm 文件。
  - MYD 文件：MyISAM 存储引擎专用，存放 MyISAM 表的数据（data)，每一张表都会有一个.MYD 文件。
  - MYI 文件：MyISAM 存储引擎专用，存放 MyISAM 表的索引相关信息，每一张 MyISAM 表对应一个.MYI 文件。
  - ibd 文件和 IBDATA 文件：存放 InnoDB 的数据文件（包括索引）。InnoDB 存储引擎有两种表空间方式：独享表空间和共享表空间。独享表空间使用.ibd 文件来存放数据，且每一张 InnoDB 表对应一个.ibd 文件。共享表空间使用.ibdata 文件，所有表共同使用一个（或多个，自行配置）.ibdata 文件。
  - ibdata1 文件：系统表空间数据文件，存储表元数据、Undo 日志等。
  - ib_logfile0、ib_logfile1 文件：Redo log 日志文件。

- pid 文件

  - pid 文件是 mysqld 应用程序在 Unix/Linux 环境下的一个进程文件，和许多其他 Unix/Linux 服务端程序一样，它存放着自己的进程 id。

- socket 文件
  - socket 文件也是在 Unix/Linux 环境下才有的，用户在 Unix/Linux 环境下客户端连接可以不通过 TCP/IP 网络而直接使用 Unix Socket 来连接 MySQL。

## MySQL 运行机制

![[1111.png]]

- 第一步：建立连接（Connectors&Connection Pool），通过客户端/服务端通信协议与 MySQL 建立连接，MySQL 客户端与服务端的通信方式是“半双工”。
  对于每一个 MySQL 的连接，时刻都有一个线程状态来标识这个连接正在做什么。

```
通讯机制：
- 全双工：能同时发送和接受数据，比如平时打电话，能听到的同时说话
- 半双工：指的某一时刻，要么发送数据，要么接收数据，不能同时发送和接受。例如早期对讲机
- 单工：只能发送数据或只能接收数据。例如单行道

  线程状态：show processlist; //查看用户正在运行的线程信息，root用户能查看所有线程，其他用户只能看自己的
```

- 第二步：查询缓存，这是 MySQL 的一个可优化查询的地方，如果开启了查询缓存且在查询缓存过程中查询到完全相同的 SQL 语句，则将查询结果直接返回给客户端；如果没有开启查询缓存或者没有查询到完全相同的 SQL 语句则会由解析器进行语法语义解析，并生成“解析树”

  - 缓存 select 查询的结果和 SQL 语句
  - 执行 Select 查询时，先查询缓存，判断是否存在可用的记录集，要求是否完全相同，这样才会匹配缓存数据命中
  - 判断哪些 SQL 不需要缓存
    - 查询语句使用 SQL_NO_CACHE
    - 查询的结果大于 query_cache_limit 设置
    - 查询中有一些不确定的参数，比如 now()
  - show variables like '%query_cache%'; //查看查询缓存是否启用，空间大小，限制等
  - show status like 'Qcache%'; //查看更详细的缓存参数，可用缓存空间，缓存块，缓存多少等

- 第三步：将客户端发送的 SQL 进行语法解析，从而生成 `解析树` 。预处理器根据一些 MySQL 规则进一步检查 `解析树` 是否合法，例如这里将检查数据表和数据列是否存在，还会解析名字和别名，看看它们是否有歧义，最后生成新的“解析树”。

- 第四步：查询优化器（Optimizer）根据“解析树”生成最优的执行计划。MySQL 使用很多优化策略生成最优的执行计划，可以分为两类：静态优化（编译时优化）、动态优化（运行时优化）。

  - 等价变换策略
    - 5=5 and a>5 改成 a > 5
    - a < b and a=5 改成 b>5 and a=5
    - 基于联合索引，调整条件位置等
  - 优化 count、min、max 等函数
    - InnoDB 引擎 min 函数只需要找索引最左边
    - InnoDB 引擎 max 函数只需要找索引最右边
    - MyISAM 引擎 count(\*)，不需要计算，直接返回
  - 提前终止查询
    - 使用了 limit 查询，获取 limit 所需的数据，就不在继续遍历后面数据
  - in 的优化
    - MySQL 对 in 查询，会先进行排序，再采用二分法查找数据。比如 where id in (2,1,3)，变成 in (1,2,3)

- 第五步：查询执行引擎负责执行 SQL 语句，此时查询执行引擎会根据 SQL 语句中表的存储引擎类型，以及对应的 API 接口与底层存储引擎缓存或者物理文件的交互，得到查询结果并返回给客户端。若开启用查询缓存，这时会将 SQL 语句和结果完整地保存到查询缓存（Cache&Bufer）中，以后若有相同的 SQL 语句执行则直接返回结果。
  - 如果开启了查询缓存，先将查询结果做缓存操作
  - 返回结果过多，采用增量模式返回

## MySQL 存储引擎

存储引擎在 MySQL 的体系架构中位于第三层，负责 MySQL 中的数据的存储和提取，是与文件打交道的子系统，它是根据 MySQL 提供的文件访问层抽象接口定制的一种文件访问机制，这种机制就叫作存储引擎。

```sql
show engines # 查看当前数据库支持的引擎信息
```

存储引擎基本用法

- InnoDB：支持事务，具有提交，回滚和崩溃恢复能力，事务安全
- MyISAM：不支持事务和外键，访问速度快
- Memory：利用内存创建表，访问速度非常快，因为数据在内存，而且默认使用 Hash 索引，但是一旦关闭，数据就会丢失
- Archive：归档类型引擎，仅能支持 insert 和 select 语句
- Csv：以 CSV 文件进行数据存储，由于文件限制，所有列必须强制指定 not null，另外 CSV 引擎也不支持索引和分区，适合做数据交换的中间表
- BlackHole:黑洞，只进不出，进来消失，所有插入数据都不会保存
- Federated：可以访问远端 MySQL 数据库中的表。一个本地表，不保存数据，访问远程表内容。
- MRG_MyISAM：一组 MyISAM 表的组合，这些 MyISAM 表必须结构相同，Merge 表本身没有数据，对 Merge 操作可以对一组 MyISAM 表进行操作。

#### InnoDB 和 MyISAM 对比

InnoDB 和 MyISAM 是使用 MySQL 时最常用的两种引擎类型，我们重点来看下两者区别。

- 事务和外键
  InnoDB 支持事务和外键，具有安全性和完整性，适合大量 insert 或 update 操作
  MyISAM 不支持事务和外键，它提供高速存储和检索，适合大量的 select 查询操作

- 锁机制
  InnoDB 支持行级锁，锁定指定记录。基于索引来加锁实现。
  MyISAM 支持表级锁，锁定整张表

- 索引结构
  InnoDB 使用聚集索引（聚簇索引），索引和记录在一起存储，既缓存索引，也缓存记录。
  MyISAM 使用非聚集索引（非聚簇索引），索引和记录分开。

- 并发处理能力
  MyISAM 使用表锁，会导致写操作并发率低，读之间并不阻塞，读写阻塞。
  InnoDB 读写阻塞可以与隔离级别有关，可以采用多版本并发控制（MVCC）来支持高并发

- 存储文件
  InnoDB 表对应两个文件，一个.frm 表结构文件，一个.ibd 数据文件。InnoDB 表最大支持 64TB；
  MyISAM 表对应三个文件，一个.frm 表结构文件，一个 MYD 表数据文件，一个.MYI 索引文件。从 MySQL5.0 开始默认限制是 256TB。

  - 使用场景
    - MyISAM
      - 不需要事务支持（不支持）
      - 并发相对较低（锁定机制问题）
      - 数据修改相对较少，以读为主
      - 数据一致性要求不高
    - InnoDB
      - 需要事务支持（具有较好的事务特性）
      - 行级锁定对高并发有很好的适应能力
      - 数据更新较为频繁的场景
      - 数据一致性要求较高
      - 硬件设备内存较大，可以利用 InnoDB 较好的缓存能力来提高内存利用率，减少磁盘 IO

- 总结
  - 是否需要事务？有，InnoDB
  - 是否存在并发修改？有，InnoDB
  - 是否追求快速查询，且数据修改少？是，MyISAM
  - 在绝大多数情况下，推荐使用 InnoDB

#### InnoDB 线程模型

![[Pasted image 20230214111235.png]]

- IO Thread
  在 InnoDB 中使用了大量的 AIO（Async IO）来做读写处理，这样可以极大提高数据库的性能。在 InnoDB1.0 版本之前共有 4 个 IO Thread，分别是 write，read，insert bufer 和 log thread，后来版本将 read thread 和 write thread 分别增大到了 4 个，一共有 10 个了
  - read thread：负责读取操作，将数据从磁盘加载到缓存 page 页。4 个
- write thread：负责写操作，将缓存脏页刷新到磁盘。4 个
  - log thread：负责将日志缓冲区内容刷新到磁盘。1 个
  - insert bufer thread：负责将写缓冲内容刷新到磁盘。1 个
- Purge Thread
  事务提交之后，其使用的 undo 日志将不再需要，因此需要 Purge Thread 回收已经分配的 undo 页。

  ```sql
  show variables like '%innodb_purge_threads%';
  ```

  - Page Cleaner Thread
    作用是将脏数据刷新到磁盘，脏数据刷盘后相应的 redo log 也就可以覆盖，即可以同步数据，又能达到 redo log 循环使用的目的。会调用 write thread 线程处理。

    ```sql
    show variables like '%innodb_page_cleaners%';
    ```

  - Master Thread
    Master thread 是 InnoDB 的主线程，负责调度其他各线程，优先级最高。作用是将缓冲池中的数据异步刷新到磁盘，保证数据的一致性。包含：脏页的刷新（page cleaner thread）、undo 页回收（purge thread）、redo 日志刷新（log thread）、合并写缓冲等。内部有两个主处理，分别是每隔 1 秒和 10 秒处理。

  每 1 秒的操作：

  - 刷新日志缓冲区，刷到磁盘
  - 合并写缓冲区数据，根据 IO 读写压力来决定是否操作
  - 刷新脏页数据到磁盘，根据脏页比例达到 75%才操作（innodb_max_dirty_pages_pct，innodb_io_capacity）

  每 10 秒的操作：

  - 刷新脏页数据到磁盘
  - 合并写缓冲区数据
  - 刷新日志缓冲区
  - 删除无用的 undo 页

## Undo Log

### Undo Log 介绍

Undo：意为撤销或取消，以撤销操作为目的，返回指定某个状态的操作。

Undo Log：数据库事务开始之前，会将要修改的记录存放到 Undo 日志里，当事务回滚时或者数据库崩溃时，可以利用 Undo 日志，撤销未提交事务对数据库产生的影响。

Undo Log 产生和销毁：Undo Log 在事务开始前产生；事务在提交时，并不会立刻删除 undolog，innodb 会将该事务对应的 undo log 放入到删除列表中，后面会通过后台线程 purge thread 进行回收处理。Undo Log 属于逻辑日志，记录一个变化过程。例如执行一个 delete，undolog 会记录一个 insert；执行一个 update，undolog 会记录一个相反的 update。

Undo Log 存储：undo log 采用段的方式管理和记录。在 innodb 数据文件中包含一种 rollbacksegment 回滚段，内部包含 1024 个 undo log segment。可以通过下面一组参数来控制 Undo log 存储。

```sql
showvariableslike'%innodb_undo%';
```

### Undo Log 作用

- 实现事务的原子性
  Undo Log 是为了实现事务的原子性而出现的产物。事务处理过程中，如果出现了错误或者用户执行了 ROLLBACK 语句，MySQL 可以利用 Undo Log 中的备份将数据恢复到事务开始之前的状态。
- 实现多版本并发控制（MVCC）
  Undo Log 在 MySQL InnoDB 存储引擎中用来实现多版本并发控制。事务未提交之前，Undo Log 保存了未提交之前的版本数据，Undo Log 中的数据可作为数据旧版本快照供其他并发事务进行快照读。
  ![[Pasted image 20230214112812.png]]
  事务 A 手动开启事务，执行更新操作，首先会把更新命中的数据备份到 Undo Bufer 中。
  事务 B 手动开启事务，执行查询操作，会读取 Undo 日志数据返回，进行快照读

## Redo Log

### Redo Log 介绍

Redo：顾名思义就是重做。以恢复操作为目的，在数据库发生意外时重现操作。

Redo Log：指事务中修改的任何数据，将最新的数据备份存储的位置（Redo Log），被称为重做日志。

Redo Log 的生成和释放：随着事务操作的执行，就会生成 Redo Log，在事务提交时会将产生 Redo Log 写入 Log Bufer，并不是随着事务的提交就立刻写入磁盘文件。等事务操作的脏页写入到磁盘之后，Redo Log 的使命也就完成了，Redo Log 占用的空间就可以重用（被覆盖写入）。

### Redo Log 工作原理

Redo Log 是为了实现事务的持久性而出现的产物。防止在发生故障的时间点，尚有脏页未写入表的 IBD 文件中，在重启 MySQL 服务的时候，根据 Redo Log 进行重做，从而达到事务的未入磁盘数据进行持久化这一特性。

![[Pasted image 20230214114300.png]]

### Redo Log 写入机制

Redo Log 文件内容是以顺序循环的方式写入文件，写满时则回溯到第一个文件，进行覆盖写。

![[Pasted image 20230214114333.png]]

- write pos 是当前记录的位置，一边写一边后移，写到最后一个文件末尾后就回到 0 号文件开头；
- checkpoint 是当前要擦除的位置，也是往后推移并且循环的，擦除记录前要把记录更新到数据文件；

write pos 和 checkpoint 之间还空着的部分，可以用来记录新的操作。如果 write pos 追上 checkpoint，表示写满，这时候不能再执行新的更新，得停下来先擦掉一些记录，把 checkpoint 推进一下。

### Redo Log 相关配置参数

每个 InnoDB 存储引擎至少有 1 个重做日志文件组（group），每个文件组至少有 2 个重做日志文件，默认为 ib_logfile0 和 ib_logfile1。可以通过下面一组参数控制 Redo Log 存储：

Redo Bufer 持久化到 Redo Log 的策略，可通过 Innodb_flush_log_at_trx_commit 设置：

- 0：每秒提交 Redo bufer ->OS cache -> flush cache to disk，可能丢失一秒内的事务数据。由后台 Master 线程每隔 1 秒执行一次操作。
- 1（默认值）：每次事务提交执行 Redo Bufer -> OS cache -> flush cache to disk，最安全，性能最差的方式。
- 2：每次事务提交执行 Redo Buffer -> OS cache，然后由后台 Master 线程再每隔 1 秒执行 OSCache -> flush cache to disk 的操作。
  一般建议选择取值 2，因为 MySQL 挂了数据没有损失，整个服务器挂了才会损失 1 秒的事务提交数据。

## BinLog 日志

### BinLog 记录模式

Redo Log 是属于 InnoDB 引擎所特有的日志，而 MySQL Server 也有自己的日志，即 Binarylog（二进制日志），简称 Binlog。Binlog 是记录所有数据库表结构变更以及表数据修改的二进制日志，不会记录 SELECT 和 SHOW 这类操作。Binlog 日志是以事件形式记录，还包含语句所执行的消耗时间。开启 Binlog 日志有以下两个最重要的使用场景。

- 主从复制：在主库中开启 Binlog 功能，这样主库就可以把 Binlog 传递给从库，从库拿到 Binlog 后实现数据恢复达到主从数据一致性。
- 数据恢复：通过 mysqlbinlog 工具来恢复数据

Binlog 文件名默认为“主机名\_binlog-序列号”格式，例如 oak_binlog-000001，也可以在配置文件中指定名称。文件记录模式有 STATEMENT、ROW 和 MIXED 三种，具体含义如下。

- ROW（row-based replication, RBR）：日志中会记录每一行数据被修改的情况，然后在 slave 端对相同的数据进行修改。

  优点：能清楚记录每一个行数据的修改细节，能完全实现主从数据同步和数据的恢复。
  缺点：批量操作，会产生大量的日志，尤其是 alter table 会让日志暴涨。

- STATMENT（statement-based replication, SBR）：每一条被修改数据的 SQL 都会记录到 master 的 BinLog 中，slave 在复制的时候 SQL 进程会解析成和原来 master 端执行过的相同的 SQL 再次执行。简称 SQL 语句复制。

  优点：日志量小，减少磁盘 IO，提升存储和恢复速度

  缺点：在某些情况下会导致主从数据不一致，比如 last_insert_id()、now()等函数。

- MIXED（mixed-based replication, MBR）：以上两种模式的混合使用，一般会使用 STATEMENT 模式保存 binlog，对于 STATEMENT 模式无法复制的操作使用 ROW 模式保存 binlog，MySQL 会根据执行的 SQL 语句选择写入模式。

### BinLog 文件结构

MySQL 的 binLog 文件中记录的是对数据库的各种修改操作，用来表示修改操作的数据结构是 LogEvent。不同的修改操作对应的不同的 log event。比较常用的 log event 有：Query event、RowEvent、Xid event 等。binLog 文件的内容就是各种 Log event 的集合。

### Binlog 写入机制

- 根据记录模式和操作触发 event 事件生成 log event（事件触发执行机制）

- 将事务执行过程中产生 log event 写入缓冲区，每个事务线程都有一个缓冲区

  Log Event 保存在一个 binlog_cache_mngr 数据结构中，在该结构中有两个缓冲区，一个是 stmt_cache，用于存放不支持事务的信息；另一个是 trx_cache，用于存放支持事务的信息。

- 事务在提交阶段会将产生的 log event 写入到外部 binlog 文件中。
  不同事务以串行方式将 log event 写入 binlog 文件中，所以一个事务包含的 log event 信息在 binlog 文件中是连续的，中间不会插入其他事务的 log event。

### Binlog 文件操作

- binLog 状态查看

  ```sql
  showvariableslike'log_bin'
  ```

````

- 开启Binlog功能

  第一种方式

  ```sql
  setgloballog_bin=mysqllogbin;
````

第二种方式

需要修改 my.cnf 或 my.ini 配置文件，在[mysqld]下面增加 log_bin=mysql_bin_log，重启 MySQL 服务。

```
#log-bin=ON
#log-bin-basename=mysqlbinlogbin
log-format=ROW
log-bin=mysqlbinlog
```

- 使用 show binlog events 命令

  ```sql
  show binary logs;//等价于show master logs;
  show master status;
  show binlog events;
  ```

````

- 使用binlog恢复数据

  ```sql
  ## 按指定时间恢复
  mysqlbinlog --start-datetime="2020-04-2518:00:00" --stopdatetime="2020-04-2600:00:00" mysqlbinlog.000002 | mysql -uroot -p1234
##   按事件位置号恢复
mysqlbinlog --start-position=154 --stop-position=957 mysqlbinlog.000002
| mysql -uroot -p1234
````

mysqldump：定期全部备份数据库数据。mysqlbinlog 可以做增量备份和恢复操作。

- 删除 Binlog 文件

  ```sql
  purge binary logs to'mysqlbinlog.000001';//删除指定文件
  purge binary logs before'2020-04-2800:00:00';//删除指定时间之前的文件
  reset master;//清除所有文件
  ```

> 可以通过设置 expire_logs_days 参数来启动自动清理功能。默认值为 0 表示没启用。设置为 1 表示超出 1 天 binlog 文件会自动删除掉。

## Redo Log 和 Bin Log 区别

- Redo Log 是属于 InnoDB 引擎功能，Binlog 是属于 MySQL Server 自带功能，并且是以二进制文件记录。
- Redo Log 属于物理日志，记录该数据页更新状态内容，Binlog 是逻辑日志，记录更新过程。
- Redo Log 日志是循环写，日志空间大小是固定，Binlog 是追加写入，写完一个写下一个，不会覆盖使用。
- Redo Log 作为服务器异常宕机后事务数据自动恢复使用，Binlog 可以作为主从复制和数据恢复使用。Binlog 没有自动 crash-safe 能力。
