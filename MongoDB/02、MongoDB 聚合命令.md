# MongoDB 聚合操作

聚合是 MongoDB 的高级查询语言，它允许我们通过转化合并由多个文档的数据来生成新的在单个文档里不存在的文档信息。一般都是将记录按条件分组之后进行一系列求最大值，最小值，平均值的简单操作，也可以对记录进行复杂数据统计，数据挖掘的操作。

聚合操作处理数据记录并返回计算结果。聚合操作组值来自多个文档，可以对分组数据执行各种操作以返回单个结果。

聚合操作包含三类：单一作用聚合、聚合管道、MapReduce。

- 单一作用聚合：提供了对常见聚合过程的简单访问，操作都从单个集合聚合文档。
- 聚合管道是一个数据聚合的框架，模型基于数据处理流水线的概念。文档进入多级管道，将 文档转换为聚合结果。
- MapReduce 操作具有两个阶段：处理每个文档并向每个输入文档发射一个或多个对象的 map 阶段，以及 reduce 组合 map 操作的输出阶段。

## 单一作用聚合操作

MongoDB 提供 estimatedDocumentCount(), count(), distinct() 这类单一作用的聚合函数。 所有这些操作都聚合来自单个集合的文档。虽然这些操作提供了对公共聚合过程的简单访问，但它们缺乏聚合管道和 map-Reduce 的灵活性和功能

### count 方法

返回与 find()集合或视图的查询匹配的文档计数 。等同于 db.collection.find(query).count()构造

```sql
db.collection_name.count();
db.collection_name.find({}).count();
```

### distinct 方法

在单个集合或视图中查找指定字段的不同值，并在数组中返回结果。

```sql
db.collection_name.find({}).distinct("key");
```

![](https://note.youdao.com/yws/public/resource/dad1b8090503bafd9cc48019bda7570f/xmlnote/8FE5C77DF25949E9859FB70A27338EC0/39657)

### estimatedDocumentCount

返回集合或视图中所有文档的计数

```sql
db.collection_name.estimatedDocumentCount();
```

## 聚合管道(Aggregation Pipeline)

### 什么是管道

MongoDB 聚合框架（Aggregation Framework）是一个计算框架，可以对每个阶段的管道进行分组、过滤等功能，然后经过一系列的处理，输出相应的聚合结果。
它可以：

- 作用在一个或几个集合上；
- 对集合中的数据进行的一系列运算；
- 将这些数据转化为期望的形式；

从效果而言，聚合框架相当于 SQL 查询中的 GROUP BY、 LEFT OUTER JOIN 、 AS 等。
如图所示：

![](https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2019/7/30/16c4326217ad1740~tplv-t2oaga2asx-zoom-in-crop-mark:4536:0:0:0.awebp)

**聚合管道操作：**

```sql
db.collection_name.aggregate(AGGREGATE_OPERATION);
```

### 管道（Pipeline）和阶段（Stage）

管道在 Unix 和 Linux 中一般用于将当前命令的输出结果作为下一个命令的参数，MongoDB 的聚合管道将 MongoDB 文档在一个管道处理完毕后将结果传递给下一个管道处理。**整个聚合运算过程称为管道（Pipeline），它是由多个阶段（Stage）组成的**
管道可以支持

> 接受一系列文档（原始数据）；
> 每个阶段对这些文档进行一系列运算；
> 结果文档输出给下一个阶段

![](https://note.youdao.com/yws/public/resource/dad1b8090503bafd9cc48019bda7570f/xmlnote/731EA7E78D384C938C9221C99BDB5FB4/39636)

### 管道基本语法

```sql
pipeline = [$stage1, $stage2, ...$stageN]; db.collection.aggregate(pipeline, {options})
```

- pipelines 一组数据聚合阶段。除 `$out`、`$Merge` 和 `$geonear` 阶段之外，每个阶段都可以在管道中出现多次
- options 可选，聚合操作的其他参数。包含：查询计划、是否使用临时文件、 游标、最大操作时间、读写策略、强制索引等等

![](https://note.youdao.com/yws/public/resource/dad1b8090503bafd9cc48019bda7570f/xmlnote/F64F9F488D494D7BAA2983FEB6A68C37/39613)

### 常用的管道聚合阶段

聚合管道包含非常丰富的聚合阶段，下面是最常用的聚合阶段

| MongoDB 聚合操作 | MySql 操作/函数 |
| ---------------- | --------------- |
| $match           | where           |
| $group           | group by        |
| $match           | having          |
| $project         | select          |
| $sort            | order by        |
| $limit           | limit           |
| $sum             | sum()           |
| $lookup          | join            |


文档：[Aggregation Pipeline Stages — MongoDB Manual](https://docs.mongodb.com/manual/reference/operator/aggregation-pipeline/)



**管道操作符**

| 常用管道 | 解析                                                           |
| -------- | -------------------------------------------------------------- | --- |
| $group   | 将 collection 中的 document 分组，可用于统计结果               |     |
| $match   | 过滤数据，只输出符合结果的文档                                 |     |
| $project | 修改输入文档的结构(例如重命名，增加、删除字段，创建结算结果等) |     |
| $sort    | 将结果进行排序后输出                                           |
| $limit   | 限制管道输出的结果个数                                         |
| $skip    | 跳过制定数量的结果，并且返回剩下的结果                         |
| $unwind  | 将数组类型的字段进行拆分                                       |

**表达式操作符**

| 常用表达式 | 含义                                                                                                          |
| ---------- | ------------------------------------------------------------------------------------------------------------- |
| `$sum`     | 计算总和，`{$sum: 1}`表示返回总和 ×1 的值(即总和的数量),使用{$sum: '$制定字段'}也能直接获取制定字段的值的总和 |
| $avg       | 求平均值                                                                                                      |
| $min       | 求 min 值                                                                                                     |
| $max       | 求 max 值                                                                                                     |
| $push      | 将结果文档中插入值到一个数组中                                                                                |
| $first     | 根据文档的排序获取第一个文档数据                                                                              |
| $last      | 同理，获取最后一个数据                                                                                        |

### 总结

**为了便于理解，将常见的 mongo 的聚合操作和 MySql 的查询做类比：**



##  MapReduce 编程模型

MongoDB 还提供 map-reduce 操作来执行聚合。 通常，**map-reduce 操作有两个阶段**：**一个 map 阶段**，它处理每个文档并为每个输入文档发出一个或多个对象，以及**reduce 阶段**组合 map 操作的输出。 可选地，map-reduce 可以具有最终化阶段以对结果进行最终修改。 与其他聚合操作一样，map-reduce 可以指定查询条件以选择输入文档以及排序和限制结果。

Pipeline 查询速度快于 MapReduce，但是 MapReduce 的强大之处在于能够在多台 Server 上并行执行复杂的聚合逻辑。MongoDB 不允许 Pipeline 的单个聚合操作占用过多的系统内存，如果一个聚合操作消耗 20%以上的内存，那么 MongoDB 直接停止操作，并向客户端输出错误消息。

MapReduce 是一种计算模型，简单的说就是将大批量的工作（数据）分解（MAP）执行，然后再将结果合并成最终结果（REDUCE）。

Map-reduce 使用自定义 JavaScript 函数来执行映射和减少操作，以及可选的 finalize 操作。 虽然自定义 JavaScript 与聚合管道相比提供了极大的灵活性，但通常，map-reduce 比聚合管道效率更低，更复杂。模式如下：

![](https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2019/7/30/16c434f6a684bd16~tplv-t2oaga2asx-zoom-in-crop-mark:4536:0:0:0.awebp)

使用 MapReduce 要实现两个函数 Map 函数和 Reduce 函数,Map 函数调用 emit(key, value),遍历 collection 中所有的记录,将 key 与 value 传递给 Reduce 函数进行处理。

```sql
db.collection_name.mapReduce(
	 <map>,
	 <reduce>,
	 <query>,
	 <output>
)
```

参数说明

- map：是 JavaScript 函数，负责将每一个输入文档转换为零或多个文档，生成键值对序列,作为 reduce 函数参数
- reduce：是 JavaScript 函数，对 map 操作的输出做合并的化简的操作（将 key-value 变成 keyvalues，也就是把 values 数组变成一个单一的值 value）
- out：统计结果存放集合
- query：一个筛选条件，只有满足条件的文档才会调用 map 函数。
- sort：和 limit 结合的 sort 排序参数（也是在发往 map 函数前给文档排序），可以优化分组机制
- limit：发往 map 函数的文档数量的上限（要是没有 limit，单独使用 sort 的用处不大）
- finalize：可以对 reduce 输出结果再一次修改
- verbose：是否包括结果信息中的时间信息，默认为 fasle
