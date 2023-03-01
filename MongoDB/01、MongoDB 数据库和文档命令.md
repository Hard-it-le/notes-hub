# MongoDB 的基本操作

### 查看数据库

```sql
show dbs;
```

### 切换数据库 如果数据库不存在，则指向数据库，但不创建，直到插入数据或创建集合时数据库才被创建

```sql
use 数据库名;
```

### 删除当前数据库

```sql
db.dropDatabase();
```

## 查看当前数据库信息

```sql
db.stats();
```

![[Pasted image 20230221133635.png]]

- db：当前数据库的名字。
- collections：当前数据库的集合数。
- objects：当前数据库所有集合总所包含的对象 （即文档）的数量。
- avgObjSize：每个文档的平均大小（以字节 为单位）。
- dataSize：此数据库中保存的未压缩数据的 总大小，不是指占有磁盘大小，单位是 bytes。
- storageSize：分配给此数据库的集合用于 存储文档的空间总量，也就是当前数据库占 有磁盘大小，单位是 bytes。
- indexes：数据库中包含的所有集合的索引总数，也就是 system.indexes 表数据行数。
- indexSize：此数据库上创建的所有索引的总大小，单位是 bytes。
- numExtents：当前数据库所有集合包含的扩展数量的统计。

### 创建集合

```sql
db.createCollection(name, options)
```

- name 是要创建的集合的名称
- options 是一个文档，用于指定集合的配置 选项参数是可选的，所以只需要到指定的集合名称。以下是可以使用的选项列表：

| 字段        | 类型    | 描述                                                                                                                                                                                                                             |
| ----------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| capped      | Boolean | （可选）如果为 true，则启用封顶集合。封顶集合是固定大小的集合，当它达到其最大大小，会自动覆盖最早的条目。如果指定 true，则需要也指定 size 字段。                                                                                 |
| autoIndexID | Boolean | （可选）如果为 true，自动创建索引\_id 字段, 默认值是 false。                                                                                                                                                                     |
| size        | number  | （可选）指定集合最大可使用字节。如果封顶如果是 true，那么你还需要指定这个字段。                                                                                                                                                  |
| max         | number  | （可选） 指定封顶集合允许在文件的最大数量。Size 限制优先于此限制。如果一个封顶集合达到大小 size 限制，未达到文件的最大数量，MongoDB 删除旧的文件。如果您更喜欢使用 max，确保为上限的集合所需的大小限制，足以包含文档的最大数量。 |

### 查看集合

```sql
show tables;
show collections;
```

### 删除集合

```sql
db.集合名称.drop() // 如果成功删除选定集合，则 drop() 方法返回 true，否则返回 false
```

# MongoDB 数据类型

- String : 这是最常用的数据类型来存储数据。在 MongoDB 中的字符串必须是有效的 UTF-8。
- Integer : 这种类型是用来存储一个数值。整数可以是 32 位或 64 位，这取决于您的服务器。
- Boolean : 此类型用于存储一个布尔值 (true/ false) 。
- Double : 这种类型是用来存储浮点值。
- Min/ Max keys : 这种类型被用来对 BSON 元素的最低和最高值比较。
- Arrays : 使用此类型的数组或列表或多个值存储到一个键。
- Timestamp : 时间戳。这可以方便记录时的文件已被修改或添加。
- Object : 此数据类型用于嵌入式的文件。
- Null : 这种类型是用来存储一个 Null 值。
- Symbol : 此数据类型用于字符串相同，但它通常是保留给特定符号类型的语言使用。
- Date : 此数据类型用于存储当前日期或时间的 UNIX 时间格式。可以指定自己的日期和时间，日期和年，月，日到创建对象。
- Object ID : 此数据类型用于存储文档的 ID。
- Binary data : 此数据类型用于存储二进制数据。
- Code : 此数据类型用于存储到文档中的 JavaScript 代码。
- Regular expression : 此数据类型用于存储正则表达式

# MongoDB 文档数据操作

## 文档数据的添加(insert or save)

### insertOne(插入单个文档)

```sql
db.collectionName.insertOne(
	{
		name:"张晓峰",
		birthday:new ISODate("2000-07-01"),
		expectSalary:15000,
		gender:0,
		city:"北京"
	},
	{ writeConcern: <document> }
)
```

**writeConcern 决定一个写操作落到多少个节点上才算成功**。

writeConcern 取值

- 0：发起写操作，不关心是否成功；
- 1~集群最大数据节点数：写操作需要被复制到指定节点数才算成功；
- majority：写操作需要被复制到大多数节点上才算成功。

### insert

若插入的数据主键已经存在，则会抛  DuplicateKeyException  异常，提示主键重复，不保存当前数据。

### save

如果 \_id 主键存在则更新数据，如果不存在就插入数据。

**如果没有指定 `_id` 这个字段系统会自动生成当然我们也可以指定 `_id`**

`_id` 是 12 个字节的十六进制数。`_id` 类型是 objrctid 类型并且是一个 12 字节 BSON 类型数据，`_id` 格式如下：

- 前 4 个字节表示时间戳 ObjectId("对象 Id 字符串").getTimestamp()来获取
- 接下来的 3 个字节是机器标识码紧接的两个字节由进程 id 组成（PID）
- 最后 3 个字节是随机数

### insertMany

向指定集合中插入多条文档数据

```sql
db.collection.insertMany([
	<document 1> ,
	<document 2>
	],
	{
	  writeConcern: <document>,
	   ordered: <boolean>
	}
)
```

> writeConcern：写入策略，默认为 1，即要求确认写操作，0 是不要求。
> ordered：指定是否按顺序写入，默认 true，按顺序写入。

- insert 和 save 也可以实现批量插入

```sql
db.collection_name.insert([document1,document2])
```

## 文档数据的查询(find)

```sql
db.collection.find(query, projection)
```

> query ：可选，使用查询操作符指定查询条件
> projection ：可选，使用投影操作符指定返回的键。查询时返回文档中所有键值， 只需省略该参数即可（默认省略）。投影时，\_id 为 1 的时候，其他字段必须是 1；\_id 是 0 的时候，其他字段可以是 0；如果没有\_id 字段约束，多个其他字段必须同为 0 或同为 1

### 比较条件查询

db.collection_name.find(query)

| 操作     | 条件格式           | 示例                                     | RDBMS 中的条件    |
| -------- | ------------------ | ---------------------------------------- | ----------------- |
| 等于     | {key:value}        | db.col.find({字段名:值}).pretty()        | where 字段名=值   |
| 大于     | {key:{$gt:value}}  | db.col.find({字段名:{$gt:值}}).pretty()  | where 字段名>值   |
| 小于     | {key:{$lt:value}}  | db.col.find({字段名:{$lt:值}}).pretty()  | where 字段名<值   |
| 大于等于 | {key:{$gte:value}} | db.col.find({字段名:{$gte:值}}).pretty() | where 字段名>=值  |
| 小于等于 | {key:{$lte:value}} | db.col.find({字段名:{$lte:值}}).pretty() | where 字段名<=值  |
| 不等于   | {key:{$ne:value}}  | db.col.find({字段名:{$ne:值}}).pretty()  | where 字段名 !=值 |

```sql
db.collection_name.find({key:value})
db.collection_name.find({key:{$gt:value}})
```

### 逻辑条件查询

#### and

MongoDB 的 find()方法可以传入多个键(key)，每个键(key)以逗号隔开

```sql
db.collection_name.find({key1:value1,key2:value2}).pretty()
```

#### or

```sql
db.collection_name.find({$or:[{key:value1},{key2:value2}]}).pretty()
```

#### not

```sql
db.collection_name.find({key:{$not{$操作符:value}}}).pretty()
```

### 分页查询

db.集合名.find({条件}).sort({排序字段:排序方式})).skip(跳过的行数).limit(一页显示多少数据

skip 用于指定跳过记录数，limit 则用于限定返回结果数量。可以在执行 find 命令的同时指定 skip、limit 参数，以此实现分页的功能。

db.books.find().skip(8).limit(4)

```sql
db.collection_name.find({key:value}).limit(10) // 根据查询条件 10 条分页

db.collection_name.find({key:value}).sort({age:desc}).limit(10) // 根据查询条件并以 age 倒序排列一页十条，1 表示升序，-1 表示降序

db.collection_name.find({key:value}).sort({age:-1}).skip(2).limit(10)

db.collection_name.find({ey:value}).sort({排序字段:排序方式})).skip(跳过的行数).limit(一页显示多少数据)
```

#### 如何处理分页问题 – 巧分页

数据量大的时候，应该避免使用 skip/limit 形式的分页。

`使用查询条件+唯一排序条件`

第一页

```sql
db.collection_name.find({}).sort({_id: 1}).limit(20);
```

第二页

```sql
db.collection_name.find({_id: {$gt: <第一页最后一个_id>}}).sort({_id: 1}).limit(20);
```

第三页

```sql
db.collection_name.find({_id: {$gt: <第二页最后一个_id>}}).sort({_id: 1}).limit(20);
```

#### 处理分页问题 – 避免使用 count

尽可能不要计算总页数，特别是数据量大和查询条件不能完整命中索引时。
考虑以下场景：假设集合总共有 1000w 条数据，在没有索引的情况下考虑以下查询：

```sql
db.collection_name.find({x: 100}).limit(50);
db.collection_name.count({x: 100});
```

- 前者只需要遍历前 n 条，直到找到 50 条 x=100 的文档即可结束；
- 后者需要遍历完 1000w 条找到所有符合要求的文档才能得到结果。 为了计算总页数而进行的 count() 往往是拖慢页面整体加载速度的原因

## 文档数据的更新(update)

```sql
//$set ：设置字段值
//$unset: 删除指定字段
//$inc: 对修改的值进行自增
db.collection_name.update(
	<query>,
	<update>,
	{
		update:<boolean>,
		multi:<boolean>,
		writeConcern:<document>
	}
)
```

参数说明：

- query：update 的查询条件，类似 sql update 查询内 where 后面的。
- update：update 的对象和一些更新的操作符（如`$set`,`$inc`...）等，也可以理解为 sql update 中 set 后面的
- option：描述更新的选项
  - upsert：可选，这个参数的意思是，如果不存在 update 的记录，是否插入 objNew,true 为插入，默认是 false，不插入。
  - multi：可选，MongoDB 默认是 false,只更新找到的第一条记录，如果这个参数为 true,就把按条件查出来多条记录全部更新。
  - writeConcern：可选，用来指定 mongod 对写操作的回执行为比如写的行为是否需要确认。

### 更新操作符

| 操作符      | 格式                                            | 描述                                           |
| ----------- | ----------------------------------------------- | ---------------------------------------------- |
| `$set`      | {$set:{field:value}}                            | 指定一个键并更新值，若键不存在则创建           |
| `$unset`    | {$unset : {field : 1 }}                         | 删除一个键                                     |
| `$inc`      | {$inc : {field : value } }                      | 对数值类型进行增减                             |
| `$rename`   | {$rename : {old_field_name : new_field_name } } | 修改字段名称                                   |
| `$push`     | { $push : {field : value } }                    | 将数值追加到数组中，若数组不存在则会进行初始化 |
| `$pushAll`  | {$pushAll : {field : value_array }}             | 追加多个值到一个数组字段内                     |
| `$pull`     | {$pull : {field : \_value } }                   | 从数组中删除指定的元素                         |
| `$addToSet` | {$addToSet : {field : value } }                 | 添加元素到数组中，具有排重功能                 |
| `$pop`      | {$pop : {field : 1 }}                           | 删除数组的第一个或最后一个元素                 |

示例

```sql
// 数据存在时，只更新不插入
db.conllection_name.update(
	{key:oldValue},
	{$set:{key:newValue}},
	{
		multi:false,
		upsert:false
	}
)
// 数据不存在时，进行插入
db.conllection_name.update(
	{key:oldValue},
	{$set:{key:newValue}},
	{
		multi:false,
		upsert:true
	}
)
// 数据存在时，删除字段
db.conllection_name.update(
	{key:oldValue},
	{$unset:{key:""}},
	{
		multi:false,
		upsert:true
	}
)

// 数据存在时，对现有字段的值进行自增
db.conllection_name.update(
	{key:oldValue},
	{$inc:{key:""}},
	{
		multi:false,
		upsert:true
	}
)
```

### 更新单个文档

某个 book 文档被收藏了，则需要将该文档的 favCount 字段自增

```sql
db.books.update(
	{
		_id:ObjectId("61caa09ee0782536660494d9")
	},
	{
		$inc:{favCount:1}
	}
)
```

### 更新多个文档

默认情况下，update 命令只在更新第一个文档之后返回，如果需要更新多个文档，则可以使用 multi 选项。

将分类为“novel”的文档的增加发布时间（publishedDate）

```sql
db.books.update({type:"novel"},{$set:{publishedDate:new Date()}},{"multi":true})
```

### update 简化命令

- updateOne：更新单个文档。
- updateMany：更新多个文档。
- replaceOne：替换单个文档

## 文档数据的删除(remove or delete)

### 使用 remove 删除文档

```sql
db.collection_name.remove(
	<query>,
	{
		justOne:<boolean>,
		writeConcern:<document>
	}
)
```

参数说明

- query:（可选）删除的文档的条件。
- jjustOne:（可选）如果设为 true 或 1，则只删除一个文档，如果不设置该参数，或使用默认值 false，则删除所有匹配条件的文档。
- writeConcern:（可选）用来指定 mongod 对写操作的回执行为。

注意事项:

> remove 命令需要配合查询条件使用
> 匹配查询条件的文档会被删除
> 指定一个空文档条件会删除所有文档

示例

```sql
// 删除存在 age >18 的文档
db.collection_name.remove(
	{age:{$gt:18}},
	{
		justOne: true
	}
)
```

### 使用 delete 删除文档

- deleteOne()
- deleteMany()

```sql
db.collection_name.deleteMany ({}) //删除集合下全部文档
db.collection_name.deleteMany ({ type:"novel" }) //删除 type等于 novel 的全部文档
db.collection_name.deleteOne ({ type:"novel" }) //删除 type等于novel 的一个文档
```

### 返回被删除文档

remove、deleteOne 等命令在删除文档后只会返回确认性的信息，如果希望获得被删除的文档，则可以使用 findOneAndDelete 命令

```sql
db.collection_name.findOneAndDelete ({ type:"novel" }) //删除 type等于novel 的一个文档
```

## 文档操作最佳实践

关于文档结构

- 防止使用太长的字段名（浪费空间）
- 防止使用太深的数组嵌套（超过 2 层操作比较复杂）
- 不使用中文，标点符号等非拉丁字母作为字段名

关于写操作

- update 语句里只包括需要更新的字段
- 尽可能使用批量插入来提升写入性能
- 使用 TTL 自动过期日志类型的数据
