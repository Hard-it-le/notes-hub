## 1、Dockerfile 是什么？

在学习 Dockerfile 前，首先要知道 Dockerfile 是什么，有什么作用？

Dockerfile 是构造 docker 镜像的文本文件，通过简单的语言，便可以通过 docker build 指令创建 docker 镜像。

Dockerfile 其实就是我们用来构建 Docker 镜像的源码，当然这不是所谓的编程源码，而是一些命令的集合，只要理解它的逻辑和语法格式，就可以很容易的编写 Dockerfile。简单点说，Dockerfile 可以让用户个性化定制 Docker 镜像。因为工作环境中的需求各式各样，网络上的镜像很难满足实际的需求。。

![image.png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5330ec8939b8405b9c8f98c43322d6ea~tplv-k3u1fbpfcp-watermark.image?)

## 2.Dockerfile 文件结构

Dockerfile 是一个包含用于组合映像的命令的文本文档。可以使用在命令行中调用任何命令。

Docker 通过读取 Dockerfile 中的指令自动生成映像。

docker build 命令用于从 Dockerfile 构建映像。可以在 docker build 命令中使用-f 标志指向文件系统中任何位置的 Dockerfile。

Dockerfile 由一行行命令语句组成，并且支持以#开头的注释行

Dockerfile 分为四部分：

- 基本镜像信息
- 维护者信息
- 镜像操作指令信息
- 启动时执行命令

## 3、Dockerfile 常用命令

### 1、From

FROM 指定基础镜像，最好挑一些 apline，slim 之类的基础小镜像.

### 2、LABEL

标注镜像的一些说明信息。

### 3、RUn

- RUN 指令在当前镜像层顶部的新层执行任何命令，并提交结果，生成新的镜像层。
- 生成的提交映像将用于 Dockerfile 中的下一步。分层运行 RUN 指令并生成提交符合 Docker 的核心概念，就像源代码控制一样。
- exec 形式可以避免破坏 shell 字符串，并使用不包含指定 shell 可执行文件的基本映像运行 RUN 命令。可以使用 SHELL 命令更改 shell 形式的默认 shell。在 shell 形式中，您可以使用\（反斜杠）将一条 RUN 指令继续到下一行。

> RUN<command>(shell 形式,/bin/sh-c 的方式运行，避免破坏 shell 字符串)
>
> RUN["executable","param1","param2"](exec形式)

### 4、CMD 和 ENTRYPOINT

- 都可以作为容器启动入口

  - CMD 的三种写法：

    - CMD["executable","param1","param2"](exec方式,首选方式)

    - CMD["param1","param2"](为ENTRYPOINT提供默认参数)

    - CMDcommandparam1param2(shell 形式)

  - ENTRYPOINT 的两种写法：

    - ENTRYPOINT["executable","param1","param2"](exec方式,首选方式)
    - ENTRYPOINTcommandparam1param2(shell 形式)

- CMD 命令只能有一个

  - Dockerfile 中只能有一条 CMD 指令。如果您列出多个 CMD，则只有最后一个 CMD 才会生效。
  - CMD 的主要目的是为执行中的容器提供默认值。这些默认值可以包含可执行文件，也可以省略可执行文件，在这种情况下，您还必须指定 ENTRYPOINT 指令。

- CMD 为 ENTRYPOINT 提供默认参数

  - 如果使用 CMD 为 ENTRYPOINT 指令提供默认参数，则 CMD 和 ENTRYPOINT 指令均应使用 JSON 数组格式指定。

- dockerrun 启动参数会覆盖 CMD 内容

### 5、ARG 和 ENV

#### ARG

- ARG 指令定义了一个变量，用户可以在构建时使用--build-arg=传递，dockerbuild 命令会将其传递给构建器。
- --build-arg 指定参数会覆盖 Dockerfile 中指定的同名参数
- 如果用户指定了未在 Dockerfile 中定义的构建参数，则构建会输出警告。
- ARG 只在构建期有效，运行期无效
- 不建议使用构建时变量来传递诸如 github 密钥，用户凭据等机密。因为构建时变量值使用 dockerhistory 是可见的。
- ARG 变量定义从 Dockerfile 中定义的行开始生效。
- 使用 ENV 指令定义的环境变量始终会覆盖同名的 ARG 指令。

#### ENV

- 在构建阶段中所有后续指令的环境中使用，并且在许多情况下也可以内联替换。
- 引号和反斜杠可用于在值中包含空格。
- ENV 可以使用 keyvalue 的写法，但是这种不建议使用了，后续版本可能会删除
- dockerrun--env 可以修改这些值
- 容器运行时 ENV 值可以生效 ENV
- 在 image 阶段就会被解析并持久化（docker inspect image 查看）

### 6、ADD 和 COPY

#### COPY

- -chown 功能仅在用于构建 Linux 容器的 Dockerfiles 上受支持，而在 Windows 容器上不起作用
- COPY 指令从 src 复制新文件或目录，并将它们添加到容器的文件系统中，路径为 dest。
- 可以指定多个 src 资源，但是文件和目录的路径将被解释为相对于构建上下文的源。
- 每个 src 都可以包含通配符，并且匹配将使用 Go 的 filepath.Match 规则进行。

> COPY[--chown=<user>:<group>]<src>...<dest>
>
> COPY[--chown=<user>:<group>]["",...""]

#### ADD

ADD 除了拥有 COPY 的作用之外，同时 ADD 拥有自动下载远程文件和解压的功能。

注意事项：

- src 路径必须在构建的上下文中；不能使用../something/something 这种方式，因为 docker 构建的第一步是将上下文目录（和子目录）发送到 docker 守护程序。
- 如果 src 是 URL，并且 dest 不以斜杠结尾，则从 URL 下载文件并将其复制到 dest。
  - 如果 dest 以斜杠结尾，将自动推断出 url 的名字（保留最后一部分），保存到 dest
- 如果 src 是目录，则将复制目录的整个内容，包括文件系统元数据。

### 7、WORKDIR 和 VOLUME

#### WORKDIR

- WORKDIR 指令为 Dockerfile 中跟随它的所有 RUN，CMD，ENTRYPOINT，COPY，ADD 指令设置工作目录。如果 WORKDIR 不存在，即使以后的 Dockerfile 指令中未使用它也将被创建。
- WORKDIR 指令可在 Dockerfile 中多次使用。如果提供了相对路径，则它将相对于上一个 WORKDIR 指令的路径。也可以用到环境变量

#### VOLUME

把容器的某些文件夹映射到主机外部

> VOLUME["/var/log/"]#可以是 JSON 数组
>
> VOLUME/var/log#可以直接写
>
> VOLUME/var/log/var/db#可以空格分割多个

### 8、USER

USER 指令设置运行映像时要使用的用户名（或 UID）以及可选的用户组（或 GID），以及 Dockerfile 中 USER 后面所有 RUN，CMD 和 ENTRYPOINT 指令。

### 9、EXPOSE

- EXPOSE 指令通知 Docker 容器在运行时在指定的网络端口上进行侦听。可以指定端口是侦听 TCP 还是 UDP，如果未指定协议，则默认值为 TCP。
- EXPOSE 指令实际上不会发布端口。它充当构建映像的人员和运行容器的人员之间的一种文档，即有关打算发布哪些端口的信息。要在运行容器时实际发布端口，请在 dockerrun 上使用-p 标志发布并映射一个或多个端口，或使用-P 标志发布所有公开的端口并将其映射到高阶端口。

### 10、multi-stage builds

多阶段构建

## 4、构建一个自己的 tomcat 镜像

通过自己创建一个简单的镜像来熟悉指令：

准备：

首先要有 tomcat 以及其依赖 jdk 的压缩包，我们在工作目录下准备

apache-tomcat-8.5.55.tar.gz

jdk-8u251-linux-x64.tar.gz

复制代码

其次创建 dockerfile 文件

vim myTomcat

复制代码

接下来在 myTomcat 中正式编写 Dockerfile

首先我们要有 tomcat 运行的操作系统

FROM centos # 这里的 tomcat 在 centos 系统下运行，添加此语句 docker 会自动从仓库中导入 centos 镜像

复制代码

其次添加作者信息

MAINTAINER kloein<kloein@126.com> #尖括号前代表作者名，尖括号中间代表邮箱

复制代码

将 tomcat 与 jdk 文件添加到 docker 镜像中

\# 通过 ADD 指令将本文件夹的两个文件添加到镜像系统中的 /usr/local/文件夹下

ADD jdk-8u251-linux-x64.tar.gz /usr/local/

ADD apache-tomcat-8.5.55.tar.gz /usr/local/

复制代码

如果有要求，可以让镜像中的系统通过 RUN 指令执行某些语句

RUN yum -y install vim

复制代码

可以指定用户运行镜像时默认进入的文件夹

ENV MYPATH /usr/local # ENV 指令可以设置环境变量 MYPATH 为变量名，/usr/local 为其路径

WORKDIR $MYPATH # 将 MYPATH 指定为默认目录

复制代码

配置系统的环境变量，以便运行镜像后可以直接使用 java 以及 tomcat

ENV JAVA_HOME /usr/local/jdk1.8.0_251

ENV CLASSPATH $JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar

ENV CATALINA_HOME /usr/local/apache-tomcat-8.5.55

ENV CATALINA_BASH /usr/local/apache-tomcat-8.5.55

ENV PATH $PATH:$JAVA_HOME/bin:$CATALINA_HOME/lib:$CATALINA_HOME/bin

复制代码

对外暴露端口

EXPOSE 8080 # 对外暴露 8080 端口

复制代码

了解此指令需要先了解 docker run 指令

docker run 镜像名 #此语句可以运行镜像，而在其后可以加上参数 -p 主机端口:容器端口

​ \#这样就可以通过真正系统中的端口访问到容器系统中的端口，实例如下

docker run tomcat -p 8001:8080 #这样便可以通过真正系统中的 8001 端口访问到容器中的 8080 端口

复制代码

而 EXPOSE 8080 语句可以在你不指定 -p 主机端口:容器端口 的情况下默认为你分配一个真实系统随机中的随机端口给容器系统中的 8080 端口

自动运行指令

\# 将 tomcat 服务启动 && 监视 tomcat 日志

CMD /usr/local/apache-tomcat-8.5.55/bin/startup.sh &&

tail -F /usr/local/apache-tomcat-8.5.55/bin/logs/catalina.out

复制代码

CMD 命令看起来和 RUN 功能好像一样，它们俩的区别 RUN 在创建镜像时就会执行，而 CMD 会在创建容器时才执行

综述，整个 Dockerfile 文件如下

FROM centos # 这里的 tomcat 在 centos 系统下运行，添加此语句 docker 会自动从仓库中导入 centos 镜像

MAINTAINER kloein<kloein@126.com> #尖括号前代表作者名，尖括号中间代表邮箱

\# 通过 ADD 指令将本文件夹的两个文件添加到镜像系统中的 /usr/local/文件夹下

ADD jdk-8u251-linux-x64.tar.gz /usr/local/

ADD apache-tomcat-8.5.55.tar.gz /usr/local/

RUN yum -y install vim

ENV MYPATH /usr/local # ENV 指令可以设置环境变量 MYPATH 为变量名，/usr/local 为其路径 WORKDIR $MYPATH # 将 MYPATH 指定为默认目录

ENV JAVA_HOME /usr/local/jdk1.8.0_251

ENV CLASSPATH $JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar

ENV CATALINA_HOME /usr/local/apache-tomcat-8.5.55

ENV CATALINA_BASH /usr/local/apache-tomcat-8.5.55

ENV PATH $PATH:$JAVA_HOME/bin:$CATALINA_HOME/lib:$CATALINA_HOME/bin

EXPOSE 8080 # 对外暴露 8080 端口

\# 将 tomcat 服务启动 && 监视 tomcat 日志 CMD /usr/local/apache-tomcat-8.5.55/bin/startup.sh && tail -F /usr/local/apache-tomcat-8.5.55/bin/logs/catalina.out

复制代码

最后，在此文件夹下运行 docker build 指令

docker build -t myTomcat:1.0 # -t 用来指定 Dockerfile 文件名，这里是 myTomcat :后可以添加版本号

复制代码

这样一个简单的 tomcat 镜像文件就制作完成了，任何人只要在 linux 上下载了此镜像，都可以直接运行
