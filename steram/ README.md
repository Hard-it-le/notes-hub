# 15 个练习帮助你掌握 Java Stream API
使用强大的 Java Stream API 简化您的代码逻辑

自 Java 8 以来 Java 流 API 的首次亮相创造了一种新的编码方式，它极大地简化了代码逻辑并减少了许多编程任务的代码行数。Stream API 不是循环遍历列表或数组中的每个项目，而是使用数据流流，因此您可以通过向流中添加一系列操作来实现业务需求。

让我通过一个示例向您展示流 API 的强大功能。比如说，任务是将一组员工记录分组到一个按职位组织的数据图中。这是遍历列表并构造数据映射的传统方式。


```java
public Map<String, List<Employee>> groupByJobTitle(List<Employee> employeeList) {

Map<String, List<Employee>> resultMap = new HashMap<>();

for (int i = 0; i < employeeList.size(); i++) {

Employee employee = employeeList.get(i);

List<Employee> employeeSubList = resultMap.getOrDefault(employee.getTitle(), new ArrayList<Employee>());

employeeSubList.add(employee);

resultMap.put(employee.getTitle(), employeeSubList);

}

return resultMap;

}
```

Java Stream API 隐含应用收集器生成按员工职称分组的数据映射。您可以看到使用 Stream API 的编码风格更简单，您可以编写更少的代码来实现相同的结果。

```java
public Map<String, List<Employee>> groupByJobTitle(List<Employee> employeeList) {

return employeeList.stream()

.collect(Collectors.groupingBy(Employee::getTitle));

}
```

Java Stream API 不仅对数据操作有用，而且使数据合并和计算更加容易。让我们看另一个计算列表中所有员工平均工资的例子

传统的方法是创建一个for循环来总结每个员工的工资，然后通过将总和除以记录数来计算平均值。

```java
public double calculateAverage(List<Employee> employeeList) {

int sum = 0;

int count = 0;

for (int i = 0; i < employeeList.size(); i++) {

Employee employee = employeeList.get(i);

sum += employee.getSalary();

count++;

}

return (double) sum / count;

}
```

如何使用 Java Stream API 实现它？它将员工记录转换为数据流中的工资金额，然后计算平均值。我会说使用 Stream API 的代码更具表现力且更易于阅读。

```java
public double calculateAverage(List<Employee> employeeList) {

return employeeList.stream()

.mapToInt(employee -> employee.getSalary())

.average()

.getAsDouble();

}
```

## Stream API 的关键概念

Java流API的设计符合函数式编程，它是一种通过组合函数并在数据流中执行它们来实现程序逻辑的编码风格。

Java Stream API 的一般概念如下图所示，流发出数据元素并通过一系列操作，如数据转换、过滤和排序。整个过程由终端操作结束，终端操作生成计算平均值和数据收集等输出。

实际上，该机制类似于for循环，它迭代数据列表中的每个数据元素并执行程序逻辑。但是，程序代码更简单，更易读。
![](http://qiniu.it-pang.com/img/20220818092124.png)
									Java Stream API — 一个典型的数据流

## Java Stream API 练习

练习动手练习是掌握新技能的快速方法。在本文中，您将完成 15 个练习并涵盖广泛的场景，以提高您的 Java Stream API 技能。

这些练习基于数据模型——客户、订单和产品。参考下图的实体关系图，客户可以下多个订单，所以是一对多的关系，而产品和订单的关系是多对多的




在练习这 15 个练习时，您将学习以下 Java Steam API 操作，因此您将有足够的知识来进一步探索其他操作。

**Non-Terminal Operations***

-   filter（）
-   map（）
-   distinct（）
-   sorted（）
-   peek（）

***Terminal Operations***

-   anyMatch（）
-   collect（）
-   count（）
-   findFirst（）
-   min（）
-   max（）
-   sum（）
-   average（）

### 练习 1 — 获取属于“书籍”类别且价格 > 100 的产品列表

这显然是一个过滤逻辑，输出要满足两个过滤要求。因此，您可以应用 2 个**filter()**操作来获得结果。

## 练习 2 — 获取产品属于“宝贝”类别的订单列表

您需要从订单实体的数据流开始，然后检查订单的产品是否属于“宝贝”类别。因此，过滤器逻辑查看每个订单记录的产品流，并使用**anyMatch()**来确定是否有任何产品满足条件。

## 练习 3 — 获取类别 =“玩具”的产品列表，然后应用 10% 的折扣

在本练习中，您将了解如何使用流 API 转换数据。**使用filter()**获得属于“玩具”类别的产品列表后，您可以使用**map()**对产品价格应用 10% 的折扣。

# 练习 4 - 获取 2021 年 2 月 1 日至 2021 年 4 月 1 日第 2 层客户订购的产品列表

这个练习说明了**flatMap()**的用法。您可以先从订单列表开始，然后按客户等级和订单日期过滤列表。接下来，从每个订单记录中获取产品列表，并使用**flatMap()**将产品记录发送到流中。例如，如果我们有 3 个订单记录并且每个订单包含 10 个产品，那么**flatMap()**将为每个订单记录发出 10 个数据元素，从而在流中输出 30 (3 x 10) 个产品记录。

因为如果多个订单包含相同的产品，产品列表将包含重复的产品记录。为了生成唯一的产品列表，应用**distinct()**操作可以帮助生成唯一列表。

# 练习 5 — 获取“书籍”类别中最便宜的产品

获取价格最低的产品的有效方法之一是按价格升序对产品列表进行排序并获取第一个元素。Java Stream API 提供**sorted()**操作，用于根据特定字段属性对流数据进行排序。为了获取流中的第一个元素，可以使用终端操作**findFirst()**。该操作返回由 Optional 包装的第一个数据元素，因为输出流可能为空。

此解决方案只能返回最低价格的单个产品记录。如果有多个最低价格相同的产品记录，则应修改解决方案，首先查找最低价格金额，然后按价格金额过滤产品记录，以获得最低价格相同的产品列表。


根据您的建议，使用 min() 是一个更好的解决方案，因为代码更简洁，并且可以使用 2 个操作符 (filter →min) 而不是 3 个 (filter → sorted →findFirst) 来完成。

## 练习 6 — 获取最近的 3 个订单

与之前的练习类似，显而易见的解决方案是按订单日期字段对订单记录进行排序。棘手的地方在于，这次的排序应该是降序排列，这样才能获取到最近下单日期的下单记录。只需调用**Comparator.reversed()**即可实现。

## 练习 7 — 获取 2021 年 3 月 15 日订购的订单列表，将订单记录记录到控制台，然后返回其产品列表

您可以看到此练习涉及两个操作 - (1) 将订单记录写入控制台和 (2) 生成产品列表。从流中生成不同的输出是不可能的，我们如何满足这个要求？除了运行两次流之外，操作**peek()**允许将系统逻辑作为流的一部分执行。示例解决方案在数据过滤后立即运行**_peek()_**将订单记录写入控制台，然后执行**flatMap()**等后续操作输出产品记录。

## 练习 8 - 计算 2021 年 2 月下达的所有订单的总金额

之前的所有练习都是通过终端操作输出一个记录列表，这次我们来做一些计算。本练习是对 2021 年 2 月订购的所有产品进行总结。通过之前的练习，您可以使用**filter()**和**flatMap()**操作轻松获取产品列表。接下来，您可以使用**mapToDouble()**操作，通过将 price 字段指定为映射值，将流转换为数据类型 Double 的流。最后，终端操作**sum()**将帮助您将所有值相加并返回总值。

## 练习 9 - 计算 2021 年 3 月 14 日的订单平均付款

除了总和之外，流 API 还提供平均值计算操作。您可能会发现返回数据类型与**sum()**不同，因为它是 Optional 数据类型。原因是数据流为空，因此计算不会输出空数据流的平均值。

## 练习 10 — 获取类别“书籍”的所有产品的统计数据集合（即总和、平均值、最大值、最小值、计数）

如果你需要同时得到 sum、average、max、min 和 count 怎么办？我们是否应该将数据流运行 5 次以逐一获取这些数字？这种方法不是很有效。**幸运的是，流 API 提供了一种方便的方法，可以使用终端操作summaryStatistics()**一次获取所有这些值。它返回包含所有必需数字的数据类型**DoubleSummaryStatistics 。**

## 练习 11 - 获取包含订单 ID 和订单产品数量的数据映射

除了数值计算，之前的所有练习都只是输出一个记录列表。帮助器类 Collectors 为数据整合和数据收集输出提供了许多有用的操作。让我们看看这个练习，以创建一个以订单 ID 为键的数据映射，而关联的值为产品计数。终端操作**Collectors.toMap()**接受两个参数，分别用于指定键和值。

## 练习 12 - 生成按客户分组的订单记录的数据映射

此练习是按客户合并订单列表。**Collectors.groupingBy()**是一个方便的函数，您可以简单地指定什么是关键数据元素，然后它将为您聚合数据。

## 练习 13 - 生成包含订单记录和产品总和的数据映射

这次输出的数据图并不是简单的从流中提取数据字段，需要为每个订单创建一个子流，以便计算产品总和。因为，关键元素是订单记录本身而不是订单id，所以**Function.identity()**用于告诉**Collectors.toMap()**使用数据元素作为关键。

## 练习 14 - 获取按类别列出产品名称的数据图

本练习可帮助您熟悉转换数据映射条目的数据输出的方式。如果您只使用**Collectors.groupingBy(Product::getCategory)**，则输出将为 Map<Category, List of Products> 但预期输出应为 Map<Category, List of Product Name>。您可以使用**Collectors.mapping()**将产品对象转换为产品名称以进行数据映射构建。

## 练习 15 - 按类别获取最昂贵的产品

与使用**Collectors.mapping()**进行数据转换类似，**Collectors.maxBy()**有助于获取具有最大值的记录，作为数据映射构建的一部分。通过提供产品价格的比较器，**maxBy()**能够得到每个类别中价值最大的产品。

# 最后的想法

希望这些练习有助于您熟悉 Java Stream API 的使用以及以更简单的方式编写逻辑的方式。毫无疑问，采用 Java Stream API 是一种思维转变，因为您的思维过程将从传统的命令式编程转变为函数式编程。因此，练习练习对于帮助您思考流数据流中的逻辑很重要。借助 Java Stream API 的技能，您可以轻松掌握 Spring WebFlux 开发等技术，因为它的编码风格与 Java Stream API 具有相似的概念。
