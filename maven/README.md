# 关于 Maven，一定要会的几个知识点，你知道吗？

![image.png](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/054a45350e9a48388e35127213a47a9f~tplv-k3u1fbpfcp-watermark.image?)

## 一、什么是 Maven

Maven 是一个项目管理和整合工具，可以帮助程序员构建工程、管理 Jar 包、编译代码、完成测试、项目打包等功能。

Maven 拥有一套完整的构建生命周期框架。使得开发者和开发团队几乎不需要花费多少时间就能完成工程的基础构建配置。Maven 可以让开发更加的简单快速。

## 二、Maven 的安装

你可以从 [Maven](https://maven.apache.org/download.cgi) 官网进行版本下载。

![image.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1945030b3ec54f54bf8029d5e427b887~tplv-k3u1fbpfcp-watermark.image?)

注意事项： 下载完成后解压即可，**解压目录不要有空格和中文**。

![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8cb13f1b51cc4739be4ae3b7de2e5b3b~tplv-k3u1fbpfcp-watermark.image?)

### 目录结构说明

-   bin

    > bin 目录包含了 MVN 运行的脚本，这些脚本主要是配置 Java 命令，准备好 ClassPath 和相关 Java 属性后，然后就可以执行 Java 命令。

-   boot

    > boot 目录 下文件是一个类加载器，相对于默认的 Java 类加载器，提供了更丰富的语法以方便配置，Maven 用该框架，加载自己的类库。

-   conf

    > conf 目录包含着 Maven 的配置文件，里面有一个 setting.xml 文件，是 Maven 的核心配置文件，后续 Maven 配置操作都在此文件操作。

### 配置环境变量

-   lib

    > lib 目录包含了所有 Maven 运行时需要的 Java 类库，Maven 是分模块开发，另外该目录还存在一些 Maven 用到的第三方依赖。

    win系统在 PATH 中设置 MAVEN_HOME（MAVEN 安装目录的 Bin 目录）

    LInux 系统在 /etc/profile 文件设置 MAVEN_HOME以便在控制台使用 MVN 命令

    打开终端使用 mvn -v 命令验证 Maven 是否安装成功

    ```
    mvn -v
    ```

![image.png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e6ba785909094caaa2bf63efb7ef30f4~tplv-k3u1fbpfcp-watermark.image?)

  至此，Maven 的安装就完成了。

## 三、Maven 的仓库类型


![image.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59758da9671e446a8c8fa348e065bac5~tplv-k3u1fbpfcp-watermark.image?)

-   本地仓库

    > 本地仓库是指用户的计算机的文件夹，用来存储从远程仓库或者中央仓库下载的 Jar 包，只有下载到本地仓库的 Jar 包才能提供给项目使用。项目使用 Jar 包优先从本地仓库中查找。

-   远程仓库

    > 远程仓库一般指私服，它是架设在局域网的仓库服务，可以从中央仓库下载资源，提供给局域网内的程序员使用，从而减少每个程序员都从中央仓库下载造成带宽的巨大浪费。

-   中央仓库

    > 中央仓库是 Apache 等其他互联网公司提供的公网服务器，是 Maven 提供的最大仓库，里面拥有最全的 Jar 包资源。如果项目中需要的 Jar 包，本地仓库和远程仓库都没有，则直接会去中央仓库下载到本地仓库提供给项目使用。

## 四、Maven 初体验

### 创建 Maven 项目


![image.png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da4fd63e6b524f53aa62ee12855627d3~tplv-k3u1fbpfcp-watermark.image?)

### Maven 工程结构

![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c66cc78935054d66a9d03cc50a684e86~tplv-k3u1fbpfcp-watermark.image?)

#### 目录说明

-   src

    src 目录存放着程序员开发的源代码。

    -   src/main/java> 该目录存放项目的 Java 文件
    -   src/main/resources> 存放项目资源文件，比如配置文件、xml 文件、temple 等文件
    -   src/test/java> 存放项目中国呢的测试文件，常用来编写测试用例
    -   src/test/resources> 存放测试时需要的资源文件

-   **target**

    -   target 存放时编译生成的文件，一般情况是项目的 Jar 包。

-   **pom.xml**

    -   pom.xml 是 Maven 项目的配置文件，里面存放着项目的基础信息、Jar 的坐标信息、需要安装的插件

#### Maven 工程类型

-   POM 工程 POM 工程是逻辑工程，Maven 并不会对该类型工程做打包处理，这些工程往往不包含具体的业务，而是用来整合其他工程的。

-   JAR 工程

    普通 Java 工程，在打包时会将项目打成 jar 包。

-   WAR工程 JAVA Web 工程，在打包时会将项目打成 war包。

## 五、 Maven 的生命周期

使用maven完成项目的构建的过程中，包括：验证、编译、测试、 打包、部署等过程，maven将这些过程规范为项目构建的生命周期。


![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/186a2d31b5fd4054922965836f071d7c~tplv-k3u1fbpfcp-watermark.image?)

| 生命周期     | 作用说明                         |
| -------- | ---------------------------- |
| validate | 验证项目是否正确                     |
| compile  | 源代码编译                        |
| Test     | 使用适当的单元测试框架（例如junit）运行测试     |
| package  | 创建JAR/WAR包                   |
| verify   | 对集成测试的结果进行检查，以保证质量达标         |
| install  | 安装打包的项目到本地仓库，以供其他项目使用        |
| deploy   | 拷贝最终的工程包到远程仓库中，以共享给其他开发人员和工程 |

> maven有三套相互独立的生命周期。分为是构建生命周期， clean生命周期（清理构建后的文件）、site生命周期（生成项目报告）。

## 六、Maven 常用命令

![image.png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/401473c181894894ae3b92e458d0dbf2~tplv-k3u1fbpfcp-watermark.image?)

| 命令              | 作用                           |
| --------------- | ---------------------------- |
| myn clean       | 清除编译的class文件，即删除target目录     |
| mvn validate    | 验证项目是否正确                     |
| myn compile     | 编译maven项目                    |
| myn test        | 编译maven项目及运行测试文件             |
| myn package     | 编译maven项目及运行测试文件，并打包         |
| mvn install     | 编译maven项目及运行测试文件并打包，并发布到本地仓库 |
| mvn deploy      | 部署项目到远程仓库                    |
| myn tomcat7：run | 使用tomcat运行项目                 |

> Maven依赖插件来执行命令，比如clean、 validate等命令是 maven自带的，tomcat7命令是引入的第三方插件

## 七、Maven pom.xml 结构模型

![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b5eb52a74d6045199f5be41859121235~tplv-k3u1fbpfcp-watermark.image?)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd"> 
    <!-- groupId 一般定义项目组名，命名规则使用反向域名 -->
    <groupId>cn.demo</groupId> 
    <!--artifactId 一般定义项目名，命名使用小写字母。项目发布后，它的坐标是 groupId+artifactId -->
    <artifactId>cn.demo</artifactId> 
    <!-- version 定义版本号。版本号一般有三段，第一段：革命性的产品升级。 第二段：新功能版本。第三段：修正一些 bug -->
    <version>0.0.1-SNAPSHOT</version> 
    <!--项目名称 -->
    <name>demmo</name> 
    <!--项目描述 -->
    <description>demo</description>
    <modelVersion>4.0.0</modelVersion> 
    <!-- packaging 定义打包方式 -->
    <packaging>pom</packaging> 
    <!-- 定义一些配置信息 -->
    <properties>
        <java.version>1.8</java.version>
        <drools.version>7.3.0.Final</drools.version>
        <maven.compiler.source>8</maven.compiler.source>
        <maven.compiler.target>8</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties> 
    <!-- 定义依赖的 jar 包坐标-->
    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.drools</groupId>
                <artifactId>drools-core</artifactId>
                <version>${drools.version}</version> 
                <!-- 排除依赖包 -->
                <exclusions>
                    <exclusion>
                        <groupId>org.slf4j</groupId>
                        <artifactId>slf4j-api</artifactId>
                    </exclusion>
                </exclusions>
            </dependency>
        </dependencies>
    </dependencyManagement>
    <build> 
        <!-- 加载插件 -->
        <plugins>
            <plugin>
                <groupId>org.jacoco</groupId>
                <artifactId>jacoco-maven-plugin</artifactId>
                <version>0.7.9</version>
                <executions>
                    <execution>
                        <goals>
                            <goal>prepare-agent</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>
```

## 八、Maven 的依赖范围


![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f36034f0e01a4ac8891cbed73ecc2d38~tplv-k3u1fbpfcp-watermark.image?)
通常情况下为了解决编译遇到的依赖问题，通过在`<dependency>`中添加`<scope>`，设置依赖的作用范围来解决
通过依赖有以下几个范围

- compile

>默认范围。表示该依赖在编译和运行时生效，项目打包时也会将该依赖打包进去。

- provided

>使用此依赖范围的Maven依赖，编译和测试时有效，但在运行时无效。典型的例子是 servlet-api，在运行时Web容器已经提供依赖，就不需要Maven重复地引入一遍。

- runtime

>runtime范围表明编译时不需要生效，而只在运行时生效。典型的例子是 JDBc驱动包，编译时只需要DK的 JDBC 接口即可，只有运行项目时才需要具体的 JDBC 驱动。

- test

>test范围表明使用此依赖范围的依赖，只在编译和运行测试代码的时生效，程序的正常运行不需要此类依赖。典型的例子就是JUnit，它只有在编译测试代码及运行测试的时候才需要。

- system

>如果有些你依赖的jar包没有Maven坐标的，它完全不在 Maven体系中，这时候你可以把它下载到本地硬盘，然后通过system来引用。（不推荐使用）

## 九、Maven 依赖冲突




### 依赖冲突产生的原因-依赖传递

假设你的项目依赖jar包A，jar包A又依赖jar包B。当添加jar包A时，Maven会把jar包B也自动加入到项目中。
这时就可能会产生依赖冲突问题，比如依赖A会引入依赖C，依赖B也会引入依赖C。


![image.png](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9fd4435afc8e4866b0293691f3eb7593~tplv-k3u1fbpfcp-watermark.image?)

### Maven 解决依赖的原则

![image.png](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b66b51c476164b89b224bc8370e144eb~tplv-k3u1fbpfcp-watermark.image?)


#### 第一原则：最短路径优先原则

最短路径优先原则就是说项目依赖关系树中路径最短的版本会被使用。例如，假设有几个jar包之间的依赖关系是：A->B->C->D(2.0)和E->F->D(1.0)，如果同时引入A和E，那么D(1.0)会被使用，因为E到D的路径更短。

#### 第二原则：最先声明原则

在依赖路径长度相等的前提下，在POM中依赖声明的顺序靠前的会被解析使用。

### Maven 解决依赖的方案

![image.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c87b66f7a11492bbcd686d1b6de6951~tplv-k3u1fbpfcp-watermark.image?)

#### 排除依赖

通过使用 `<exclusions>` 标签下的 `<exclusion>` 将有冲突依赖的 JAR 写进入。

#### 锁定版本

在 Maven 中为某个 jar 包配置锁定版本后，不考虑依赖的声明顺序和依赖路径，以锁定的版本的为准添加到工程中，此方法在企业开发中常用。

通常情况下在 `<dependencyManagement>` 标签使用 `<dependencies>` 标签进行依赖的版本固定


## 十、Maven 聚合

![image.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0c9326e2c0f463bad109c1b8ff4008c~tplv-k3u1fbpfcp-watermark.image?)

### 聚合关系

Maven 将一个大项目分成一个个小项目开发，最后打包时会将这些小的项目打成一个完整的 war 包独立运行。

### 继承关系

Maven 中的继承是针对于父工程和子工程。父工程定义的依赖和插件子工程可以直接使用。注意父工程类型一定为 POM 类型工程。

Maven 中对于继承采用的也是单继承，也就是说一个子项目只能有一个父项目。但我们可以在 配置多继承。

### 聚合与继承的关系

聚合：聚合模块知道哪些被聚合的模块，但被聚合的模块不知道聚合模块的存在

继承：父POM不知道子模块，但子模块都知道父POM的存在

### 依赖传递失效及解决方案

直接在本工程再次添加一遍依赖

![image.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c942ef2c98f7431196676c0d9609dff2~tplv-k3u1fbpfcp-watermark.image?)
