本文介绍了在使用阿里云 Redis 的开发规范，从键值设计、命令使用、客户端使用、相关工具等方面进行说明，通过本文的介绍可以减少使用 Redis 过程带来的问题。

## 一、键值设计

### **1. key 名设计**

- 可读性和可管理性

以业务名(或数据库名)为前缀(防止 key 冲突)，用冒号分隔，比如平台服务:基础模块:配置文件（Hash 结构的 key）或者 业务名:表名:id

```bash
ugc:video:1
hpfm:fnd:profile
```

- 简洁性

保证语义的前提下，控制 key 的长度，当 key 较多时，内存占用也不容忽视

```bash
user:{uid}:friends:messages:{mid} 简化为 u:{uid}:fr:m:{mid}
```

- 不要包含特殊字符

反例：包含空格、换行、单双引号以及其他转义字符

[Key 详细解析](https://mp.weixin.qq.com/s?__biz=Mzg2NTEyNzE0OA==&mid=2247483663&idx=1&sn=7c4ad441eaec6f0ff38d1c6a097b1fa4&chksm=ce5f9e8cf928179a2c74227da95bec575bdebc682e8630b5b1bb2071c0a1b4be6f98d67c37ca&scene=21#wechat_redirect)

### **2. value 设计**

- 拒绝 bigkey (防止网卡流量、慢查询)

建议 String 类型的 Value 控制在 10KB 范围以内，hash、list、set、zset 元素个数不要超过 5000。这是因为 Redis 随着 Value 不断增长，在超过 10KB 后，有一个非常奇妙的性能拐点，如下图所示

反例：一个包含 200 万个元素的 list。
非字符串的 bigkey，不要使用 del 删除，使用 hscan、sscan、zscan 方式渐进式删除，同时要注意防止 bigkey 过期时间自动删除问题(例如一个 200 万的 zset 设置 1 小时过期，会触发 del 操作，造成阻塞，而且该操作不会不出现在慢查询中(latency 可查))，[查找方法](https://developer.aliyun.com/article/531067#cc1)和[删除方法](https://developer.aliyun.com/article/531067#cc2)

[ value 设计详细解析](https://mp.weixin.qq.com/s?__biz=Mzg2NTEyNzE0OA==&mid=2247483677&idx=1&sn=5c320b46f0e06ce9369a29909d62b401&chksm=ce5f9e9ef928178834021b6f9b939550ac400abae5c31e1933bafca2f16b23d028cc51813aec&scene=21#wechat_redirect)

- 选择适合的数据类型。

例如：实体类型(要合理控制和使用数据结构内存编码优化配置,例如 ziplist，但也要注意节省内存和性能之间的平衡)

反例：

```bash
set user:1:name tom
set user:1:age 19
set user:1:favor football
```

正例:

```bash
hmset user:1 name tom age 19 favor football
```

### **3.控制 key 的生命周期，Redis 不是垃圾桶**

建议使用 expire 设置过期时间(条件允许可以打散过期时间，防止集中过期)，不过期的数据重点关注 idletime。

尽可能对每一个 Key 都设置过期时间，这个是非常有益处的。否则，你想象一下，半年以后，一年以后，你的 Redis 集群中有上百 G 甚至更多的数据，谁都不知道这些数据哪些是有价值的，哪些已经成为垃圾。如果你的每个 Key 都设置了过期时间，那么就不会出现这个问题了。集群在运行过程中，或自动淘汰那些已经不再使用的垃圾缓存数

## 二、命令使用

### **1.时间复杂度为 O(n) 的命令需要注意 N 的数量**

例如 hgetall、lrange、smembers、zrange、sinter 等并非不能使用，但是需要明确 N 的值。有遍历的需求可以使用 hscan、sscan、zscan 代替。

以 List 类型为例，LINDEX、LREM 等命令的时间复杂度就是 O(n)。也就是说，随着 List 中元素数量越来越多，这些命令的性能越来越差。而 Redis 又是单线程的，如果出现一个慢命令，会导致在这个命令之后执行的命令耗时也会增长，这是使用 Redis 的大忌。

### **2.禁用命令：KEYS、FLUSHDB、FLUSHALL 等**

禁止线上使用 keys、flushall、flushdb 等，通过 Redis 的 rename 机制禁掉命令，或者使用 scan 的方式渐进式处理。
FLUSHDB 和 FLUSHALL 这两个命令会清空数据，后果可想而知。
至于 KEYS 命令，这个命令的不当使用导致的损失，会随着你的业务并发越大价值越大而导致损失越大。

### **3.合理使用 select**

select 的作用是选择 Redis 的 db，这是只有在非 cluster 模式下才能起作用的。默认 db 数量为 16，可以通过 redis.conf 中的 databases 进行配置。

Redis 规范建议谨慎多个业务运行在同一个 Redis 实例的多个 db 上。这是因为 Redis 整个实例是单线程处理命令的，这就意味着，如果某个 db 上有慢命令，那么会影响其他 db 上的实例。当然，Redis6.0 准备支持多线程，但是还是不建议这样做！

### **4.使用批量操作提高效率**

批量命令主要分为两类，原生命令和非原生命令

- 原生命令包括：例如 mget、mset、hmget、hmset、LPUSH key value 集合等
- 非原生命令包括：Pipeline

合理使用这些命令对操作性能提升是**极其巨大**的，尤其在单机 Redis 或者 Sentinel 模式下。因为这两种架构不涉及跨 Slot，Redis 集群性能也有提升，但是使用会受到一些限制，例如不支持跨 Slot 的操作等，官方并不太建议在 Rdis 集群环境下使用 Pileline 和 multi key 操作。

但要注意控制一次批量操作的**元素个数**(例如 500 以内，实际也和元素字节数有关)。

注意原生命令和非原生命令的不同：

- 1. 原生是原子操作，pipeline 是非原子操作。
- 2. pipeline 可以打包不同的命令，原生做不到
- 3. pipeline 需要客户端和服务端同时支持。

### **5.Redis 事务功能较弱，不建议过多使用**

Redis 的事务功能较弱(不支持回滚)，而且集群版本(自研和官方)要求一次事务操作的 key 必须在一个 slot 上(可以使用 hashtag 功能解决)

官方给出的 Redis 不支持 “Redis 在事务失败时不进行回滚，而是继续执行余下的命令” 做法的优点：

- Redis 命令只会因为错误的语法而失败，或是命令用在了错误类型的键上面：这也就是说，从实用性的角度来说，失败的命令是由编程错误造成的，而这些错误应该在开发的过程中被发现，而不应该出现在生产环境中。
- 因为不需要对回滚进行支持，所以 Redis 的内部可以保持简单且快速。

### **6.Redis 集群版本在使用 Lua 上有特殊要求**

- 1.所有 key 都应该由 KEYS 数组来传递，redis.call/pcall 里面调用的 redis 命令，key 的位置，必须是 KEYS array, 否则直接返回 error，"-ERR bad lua script for redis cluster, all the keys that the script uses should be passed using the KEYS array"
- 2.所有 key，必须在 1 个 slot 上，否则直接返回 error, "-ERR eval/evalsha command keys must in same slot"

### **7.必要情况下使用 monitor 命令时，要注意不要长时间使用**

monitor 命令一般是用来观察 redis 服务端都在执行哪些命令并实时输出。之所以规范建议控制 monitor 命令的使用时间，是因为随着 monitor 命令执行时间越来越长，会导致越来越多的数据积压在输出缓冲区，从而导致输出缓冲区占用内存越来越大。而且，这种影响会由于 Redis 并发越高，而更加放大。

## 三、客户端使用

### **1.避免多个应用使用一个 Redis 实例**

正例：不相干的业务拆分，公共数据做服务化。

### **2.使用带有连接池的数据库，可以有效控制连接，同时提高效率**

标准使用方式：

```java
Jedis jedis = null;
try {
    jedis = jedisPool.getResource();
    //具体的命令
    jedis.executeCommand()
} catch (Exception e) {
    logger.error("op key {} error: " + e.getMessage(), key, e);
} finally {
    //注意这里不是关闭连接，在JedisPool模式下，Jedis会被归还给资源池。
    if (jedis != null)
        jedis.close();
}
```

下面是 JedisPool 优化方法的文章:

- [Jedis 常见异常汇总](https://yq.aliyun.com/articles/236384)
- [JedisPool 资源池优化](https://yq.aliyun.com/articles/236383)

### **3.高并发下建议客户端添加熔断功能(例如 netflix hystrix)**

### **4.设置合理的密码，如有必要可以使用 SSL 加密访问**

### **5.根据自身业务类型，选好 maxmemory-policy (最大内存淘汰策略)，设置好过期时间**

默认策略是 volatile-lru，即超过最大内存后，在过期键中使用 lru 算法进行 key 的剔除，保证不过期数据不被删除，但是可能会出现 OOM 问题。

#### 其他策略如下：

- allkeys-lru：根据 LRU 算法删除键，不管数据有没有设置超时属性，直到腾出足够空间为止。
- allkeys-random：随机删除所有键，直到腾出足够空间为止。
- volatile-random:随机删除过期键，直到腾出足够空间为止。
- volatile-ttl：根据键值对象的 ttl 属性，删除最近将要过期数据。如果没有，回退到 noeviction 策略。
- noeviction：不会剔除任何数据，拒绝所有写入操作并返回客户端错误信息"(error) OOM command not allowed when used memory"，此时 Redis 只响应读操作。

## 四、相关工具

### **1.数据同步**

redis 间数据同步可以使用：redis-port

### **2.big key 搜索**

[redis 大 key 搜索工具](https://yq.aliyun.com/articles/117042)

### **3.热点 key 寻找(内部实现使用 monitor，所以建议短时间使用)**

[facebook 的 redis-faina](https://github.com/facebookarchive/redis-faina)

> 注意事项：
> 阿里云 Redis 已经在内核层面解决热点 key 问题

## 五 附录：删除 bigkey

下面操作可以使用 pipeline 加速。

##### **1. Hash 删除: hscan + hdel**

```java
public void delBigHash(String host, int port, String password, String bigHashKey) {
    Jedis jedis = new Jedis(host, port);
    if (password != null && !"".equals(password)) {
        jedis.auth(password);
    }
    ScanParams scanParams = new ScanParams().count(100);
    String cursor = "0";
    do {
        ScanResult<Entry<String, String>> scanResult = jedis.hscan(bigHashKey, cursor, scanParams);
        List<Entry<String, String>> entryList = scanResult.getResult();
        if (entryList != null && !entryList.isEmpty()) {
            for (Entry<String, String> entry : entryList) {
                jedis.hdel(bigHashKey, entry.getKey());
            }
        }
        cursor = scanResult.getStringCursor();
    } while (!"0".equals(cursor));

    //删除bigkey
    jedis.del(bigHashKey);
}
```

##### 2. List 删除: ltrim

```java
public void delBigList(String host, int port, String password, String bigListKey) {
    Jedis jedis = new Jedis(host, port);
    if (password != null && !"".equals(password)) {
        jedis.auth(password);
    }
    long llen = jedis.llen(bigListKey);
    int counter = 0;
    int left = 100;
    while (counter < llen) {
        //每次从左侧截掉100个
        jedis.ltrim(bigListKey, left, llen);
        counter += left;
    }
    //最终删除key
    jedis.del(bigListKey);
}
```

##### 3. Set 删除: sscan + srem

```java
public void delBigSet(String host, int port, String password, String bigSetKey) {
    Jedis jedis = new Jedis(host, port);
    if (password != null && !"".equals(password)) {
        jedis.auth(password);
    }
    ScanParams scanParams = new ScanParams().count(100);
    String cursor = "0";
    do {
        ScanResult<String> scanResult = jedis.sscan(bigSetKey, cursor, scanParams);
        List<String> memberList = scanResult.getResult();
        if (memberList != null && !memberList.isEmpty()) {
            for (String member : memberList) {
                jedis.srem(bigSetKey, member);
            }
        }
        cursor = scanResult.getStringCursor();
    } while (!"0".equals(cursor));

    //删除bigkey
    jedis.del(bigSetKey);
}
```

##### 4. SortedSet 删除: zscan + zrem

```java
public void delBigZset(String host, int port, String password, String bigZsetKey) {
    Jedis jedis = new Jedis(host, port);
    if (password != null && !"".equals(password)) {
        jedis.auth(password);
    }
    ScanParams scanParams = new ScanParams().count(100);
    String cursor = "0";
    do {
        ScanResult<Tuple> scanResult = jedis.zscan(bigZsetKey, cursor, scanParams);
        List<Tuple> tupleList = scanResult.getResult();
        if (tupleList != null && !tupleList.isEmpty()) {
            for (Tuple tuple : tupleList) {
                jedis.zrem(bigZsetKey, tuple.getElement());
            }
        }
        cursor = scanResult.getStringCursor();
    } while (!"0".equals(cursor));

    //删除bigkey
    jedis.del(bigZsetKey);
}
```

## 总结

总而言之，任何一门技术都有利有弊，技术的世界里不存在没有弱点的技术。所以，我们对使用到生产环境的任何一个技术，都要非常熟悉：知道它所擅长的和它的弱点，这样才能结合自己的项目特点，设计出更合理的架构，编写出最合理的代码。
