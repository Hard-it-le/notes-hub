# 什么是索引

索引是一种单独的、物理的对数据库表中一列或多列的值进行排序的一种存储结构，它是某个表中一列或若干列值的集合和相应的指向表中物理标识这些值的数据页的逻辑指针清单。

索引的作用相当于图书的目录，可以根据目录中的页码快速找到所需的内容。

索引目标是提高数据库的查询效率，没有索引的话，查询会进行全表扫描（scan every document in a collection）,数据量大时严重降低了查询效率。

默认情况下 Mongo 在一个集合（collection）创建时，自动地对集合的 `_id` 创建了唯一索引。

# 索引类型

## 单键索引 (Single Field)

MongoDB 支持所有数据类型中的单个字段索引，并且可以在文档的任何字段上定义。对于单个字段索引，索引键的排序顺序无关紧要，因为 MongoDB 可以在任一方向读取索引。

单个例上创建索引：

```sql
// 排序方式
db.collection_name.createIndex({
	"字段名": -1
})
```

特殊的单键索引过期索引 TTL（Time To Live）

TTL 索引是 MongoDB 中一种特殊的索引，可以支持文档在一定时间之后自动过期删除，目前 TTL 索引只能在单字段上建立，并且字段类型必须是日期类型。


```sql
db.collection_name.createIndex({
	"日期字段": 排序方式
	},{
		expireAfterSeconds: 描述
	}
)
```

## 复合索引 (Compound Index）

通常我们需要在多个字段的基础上搜索表/集合，这是非常频繁的。如果是这种情况，我们可能会考虑在 MongoDB 中制作复合索引。复合索引支持基于多个字段的索引，这扩展了索引的概念并将它们扩展到索引中的更大域。

制作复合索引时要注意的重要事项包括：字段顺序与索引方向。

```sql
db.collection_name.createIndex(
	{
		"字段名1":排序方式，
		"字段名2":排序方式
	},
)
```

## 多键索引（Multikey indexes）

针对属性包含数组数据的情况，MongoDB 支持针对数组中每一个 element 创建索引，Multikeyindexes 支持 strings，numbers 和 nested documents

## 地理空间索引（Geospatial Index）

针对地理空间坐标数据创建索引。

## 全文索引

MongoDB 提供了针对 string 内容的文本查询，Text Index 支持任意属性值为 string 或 string 数组元素的索引查询。注意：一个集合仅支持最多一个 Text Index，中文分词不理想推荐 ES。

db.集合.createIndex({"字段":"text"})
db.集合.find({"$text":{"$search":"coffee"}})

## 哈希索引 Hashed Index

针对属性的哈希值进行索引查询，当要使用 Hashed index 时，MongoDB 能够自动的计算 hash 值，无需程序计算 hash 值。注：hash index 仅支持等于查询，不支持范围查询。

db.集合.createIndex({"字段":"hashed"})

# 索引和 explain 分析

## 索引管理

### 创建索引并在后台运行

```bash
  db.COLLECTION_NAME.createIndex({"字段":排序方式},{background:true});
```

### 获取针对某个集合的索引

db.COLLECTION_NAME.getIndexes()

### 索引的大小

db.COLLECTION_NAME.totalIndexSize()

### 索引的重建

db.COLLECTION_NAME.reIndex()

### 索引的删除

db.COLLECTION_NAME.dropIndex("INDEX-NAME")
db.COLLECTION_NAME.dropIndexes()

注意:\_id 对应的索引是删除不了的

##  explain 分析

使用 js 循环插入 100 万条数据不使用索引字段查询查看执行计划，然后给某个字段建立索引,使用索引字段作为查询条件再查看执行计划进行分析

explain()也接收不同的参数，通过设置不同参数我们可以查看更详细的查询计划。

- queryPlanner：queryPlanner 是默认参数
- executionStats：executionStats 会返回执行计划的一些统计信息(有些版本中和 allPlansExecution 等同)。
- allPlansExecution:allPlansExecution 用来获取所有执行计划，结果参数基本与上文相同。

### queryPlanner 默认参数

### executionStats 参数

### executionStats 返回逐层分析

第一层，executionTimeMillis 最为直观 explain 返回值是 executionTimeMillis 值，指的是这条语句的执行时间，这个值当然是希望越少越好。
