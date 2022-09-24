# UML 系统建模

## UML 前置了解

### 什么是 UML

- Unified Modeling Language 统一建模语言，又称标准建模语言。
- UML 是一种为面向对象开发系统的产品进行说明、可视化、和编制文档的标准语言。语言，也就是一个表达思想的符号约定。
- UML 作为一种模型语言，它使开发人员专注于建立产品的模型和结构，而不是选用什么程序语言和算法实现。
- UML 是不同于其他常见的编程语言，如C + +，Java中，COBOL等，它是一种绘画语言，用来做软件蓝图。

### UML 可以做什么

- 统一
  没有规矩不成方圆，它指定了一种标准，一种约束，使得大家的表达变得一致。它被 OMG（Object Management Group）所认可。

  >OMG 是一个国际化的、开放成员的、非盈利性的计算机行业标准协会，该协会成立于 1989 年，他是软件行业中一个标准的认可。包括客户、领域专家、分析师、设计师、程序员、测试工程师及培训人员等。uml 成为他们工作中统一的沟通工具，用于充分理解和表达自己所关注的内容。

- 建模

​  复杂业务系统建模，即建立软件系统模型。uml 的创始人之一 Booch，曾用建一座摩天大楼来比喻 uml 的必要性。简单系统下，可有可无，系统复杂或大到一定程度，建模和文档成为系统周期里非常重要的一环。

- 语言

  面向对象思想的表达。互相之间的沟通工具。一种按照特定规则和模式组成的符号系统。

### 为什么要学习 UML

- 团队或架构设计互相交流，必然需要一种沟通语言
- 是一门技能，不一定用到，但是作为架构师应该知道
- 有其他的表达办法，但是用习惯后，uml真的很方便易用

## UML 理论知识

### 关系

#### 泛化（Generalization）

![image.png](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce44153e6122449fbabc7388f57d7b58~tplv-k3u1fbpfcp-watermark.image?)

- 泛化相当于 Java 中的 extends ，用于接口与接口之间，或父类和子类之间

- 泛化是单向操作，箭头指向父类

```java
//类
public class Animal {
}
public class Cat extends Animal{
}
//接口
public interface Action{
}
public interface Jump extends Action{
}
```

#### 实现（Realization)

![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87577d24a2c04a48a28f1d5cb06194d8~tplv-k3u1fbpfcp-watermark.image?)

- 实现相当于 Java 中的 implements
- 实现是单向操作，箭头指向接口

```java
public interface Jump {
}
public class Tiger implements Jump {
}
```

#### 依赖（Dependency）

![image.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0581cb779d9049f2b4542d023e0a1559~tplv-k3u1fbpfcp-watermark.image?)

- 某个类或对象实例，依赖于另一个而存在，在其关键方法中用到对方
- 如果一方属性发送改变，使用的一方可能会受到影响
- 依赖一般是单向操作，
- 类比在表机构上，更像是外键存在

#### 关联（Associtaion）

![image.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3c7b80c0a5a4d6c9d4b0016cac53d82~tplv-k3u1fbpfcp-watermark.image?)

- 关联是一种拥有关系，双方不一定属于同一类事物
- 关联可以是单向，也可以是双向，箭头指向是被拥有者
- 类比在表结构中，更像是中间表关系

#### 聚合（Aggregation）

![image.png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9520de9ddb804322b3854a8db477ecf5~tplv-k3u1fbpfcp-watermark.image?)

- 聚合是一种很弱的拥有关系，A 可以拥有 B，但是如果 B 不存在也可以继续使用
- 聚合一般是单向操作，空心菱形起始箭头，箭头指向被拥有者
- 类比群体与个体的关系

#### 组合（Composition）

![image.png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6bd8d6f3cd9a45cdbd286d3d7a1dd9c7~tplv-k3u1fbpfcp-watermark.image?)

- 组合是一种整体与部分的关系，A 是由 B 组成，如果离开了 B，那么 A 就不完整则无法使用
- 组合是单向操作，实心菱形起始箭头，箭头指向子模块

#### 实操（一张图包含所有关系）

![image.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2460e0b2de8141bfb48e3f55190744c2~tplv-k3u1fbpfcp-watermark.image?)

#### 总结

- 继承和实现几乎不会搞混，一个上下父子关系，一个是类与接口

- 组合与聚合要注意，聚合为聚集，群体与个体。组合为组成，整体与部分

- 关联和依赖要注意，关联一般为同级别有相关性，这种相关性是长期存在的。依赖为需求关系，一方需要依赖另一方，可能会因另一方的改变而改变。

- 关系的强弱顺序：继承=实现>组合>聚合>关联>依赖

### 图

#### 什么是图

![image.png](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/960fb4986d8845b9ac937a66527605b1~tplv-k3u1fbpfcp-watermark.image?)

UML 支持的图形很多，按照类型分为结构图、行为图、交互图是那种，其中最常用的是以下 9 种类型

- 用例图：从用户角度描述系统功能。

- 类图：描述系统中类的静态结构。

- 对象图：系统中的多个对象在某一时刻的状态。

- 状态图：是描述状态到状态控制流，用于表达系统状态的变化

- 活动图：描述了业务实现用例的工作流程，强调的是动作之间的衔接

- 序列图：对象之间的动态合作关系，强调对象发送消息的顺序

- 协作图：描述对象之间的协助关系，强调对象之间的合作关系

- 组件图：描述系统各个组件及其相关关系的静态视图

- 部署图：定义系统中软硬件的物理体系结构

#### 类图

##### 基本说明

- 类图在面向对象系统建模中最常用的图，也是最重要的图，是定义其他图的基础

- 类图主要是用来显示系统中的类、接口以及他们之间的静态结构和关系的一种静态模型
- 类图主要是描述细化相关的属性和操作，是一个对业务模型面向对象化的过程，也是对系统的约束
- 类图可以注解构建可执行代码，但使用场景较少

> `类图是唯一可以直接映射到面向对象的语言UML图。因此，它被广泛应用于开发者社区。`

##### 基本使用

![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36eabeb281484ad084e1c47d06313818~tplv-k3u1fbpfcp-watermark.image?)

#### 对象图

##### 基本说明

- 对象图和类图一样反映系统的静态过程，但它表达的是一个实际场景。
- 对象图显示某时刻对象和对象之间的关系。可看成一个类图的快照。
- 对象图是类图的实例，所以几乎使用与类图完全相同的标识。

对象图因为是运行在某个时间节点的对象镜像，所以关系比较单一，描述的是类与类的实例之间。不涉及接口

##### 基本使用

![image.png](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96871c481aaa44b6a64c40430e3f8ca4~tplv-k3u1fbpfcp-watermark.image?)

**对象图是类图的一个实例**。类图的基本要素是类似的。对象图是由对象和链接。在一个特定的时刻，它捕获该系统的实例。 对象图用于原型设计，逆向工程和实际场景建模。

#### 用例图

##### 基本说明

- 用例图是从用户角度描述系统功能的技术，并指出各功能的操作者，表示一个系统中用例与参与者及其关系的图

- 主要用于需求分析阶段，和产品文档比较贴近
- 用例图相当于从用户的视角来描述和建模整个系统，分析系统的功能与行为。
- 用例图，通过它可以使得系统分析员和客户之间能够更好地沟通系统的需求。

##### 基本使用

![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d29dae3c9bb4845b587f6235ac459ac~tplv-k3u1fbpfcp-watermark.image?)

#### 交互图

##### 基本说明

交互图，用于捕获系统的动态性质。 交互图包括`序列图`和协作图，

- 时序图显示对象之间的动态合作关系，它强调对象之间消息发送的顺序，同时显示对象之间的交互`；
- 协作图描述对象间的协作关系，协作图跟时序图相似，显示对象间的动态合作关系。

##### 时序图

###### 基本说明

时序图 (Sequence Diagram)，又名序列图、循序图，是一种 UML 交互图。它通过描述对象之间发送消息的时间顺序显示多个对象之间的动态协作。

###### 基本使用

![image.png](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7600a92233474033a5d8a1de938dfc3e~tplv-k3u1fbpfcp-watermark.image?)

#### 状态图（拓展）

##### 基本说明

状态图（Statechart Diagram）是一个用于模拟系统的动态性质的五个图。这些图用来模拟一个对象的整个生命周期。 一个对象的状态被定义为对象所在的条件下，特定的时间和对象移动对其他状态，在某些事件发生时。状态图还用于正向和反向工程。 状态图着重描述从一个状态到另一个状态的流程，主要有外部事件的参与。

##### 基本使用

![image.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44487640be234112b6bf2272a8296c5e~tplv-k3u1fbpfcp-watermark.image?)

#### 组件图（拓展）

##### 基本说明

组件图适用于基于组件的开发模式（Component-Based Development, CBD），它通过组件，及组件的接口、端口来表达组件的构成及其关系。当我们使用 CBD 进行开发时，其实是对行为进行了抽象，一个组件提供了若干的行为，组件图通过接口、端口的方式来表达组件间的连接，很形象的表达出组件是可被替换的概念，一个组件可以被另一个提供了相同接口的组件替换。因此，当我们通过组件进行建模时，能够设计出一个扩展性良好的系统。

##### 使用场景

组件图是用于描述系统的物理、逻辑结构的，他关注组件间的关联（使用什么接口，通过什么端口通讯），强调通过接口来描述组件行为，因此， **对于后端来说**，组件图比较适用于 SOA 架构、微服务架构的表达，描述整个系统的结构以及子系统间的通讯方式，或者表达一些基础设施，比如脚手架，消息中间件等等。 **对于前端来说**，组件图适合在使用类似 react、vue 这样组件化的前端技术框架时，表达对组件的设计，比如一个页面会有个骨架组件，骨架组件包含了导航组件，列表组件等等。

##### 基本使用

![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd515e2cc859467d801965fde7644a32~tplv-k3u1fbpfcp-watermark.image?)

#### 部署图（拓展）

##### 基本说明

部署图一种展示运行时进行处理的节点和在节点上存在的组件配置的图。阐述了在实际应用中软件和它的运行环境的关系，并且描述了软件部署在硬件上的具体方式。    一个系统模型只有一个部署图，部署图通常用来帮助理解分布式系统。

##### 基本使用

![image.png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d40d5c374cf0433282b5b4ead0b57111~tplv-k3u1fbpfcp-watermark.image?)
