## 日志分级

| 级别  | 名称  | 作用                                                                                                   |
| ----- |:-----:| ------------------------------------------------------------------------------------------------------ |
| debug | 调 试 | 开发调试信息                                                                                           |
| trace | 追 踪 | 最详细的信息，一般这些信息只记录到日志文件中。                                                         |
| info  | 信 息 | 用于记录系统运行过程或重要信息点，主要为故障定位、过程溯源、数据分析等提供辅助能力                     |
| warn  | 警 告 | 系统出现不符合预期的现象，但服务并未受损，可根据实际情况选择性预警，解决时效性要求不高，但需要额外关注 |
| error | 错 误 | 应用系统出现异常或故障，需要预警并及时解决，否则该功能无法正常运行并提供服务能力                       |

注意事项：

- debug 日志仅限调试和本地开发开启，线上环境一定要关闭
- 默认上报级别
  - trace：每次请求生成的日志
  - info：一些需要关注的重要信息
  - warn：`unhandledRejection` 和 `uncaughtException` 未处理的异常，加入错误堆栈
  - error：全局异常拦截中拦截到的异常，此级别下需要打印错误堆栈

### 打印规范

- 【强制】**在日志输出时，字符串变量之间的拼接使用占位符的方式**

  说明：因为 String 字符串的拼接会使用 StringBuilder 的 append() 方式，有一定的性能损耗。使用占位符仅是替换动作，可以有效提升性能。

  正例：

```java
logger.debug("Processing trade with id : {} and symbol : {}", id, symbol);
```

- 【强制】生产环境禁止使用 System.out 或 System.err 输出或使用 e.printStackTrace() 打印异常堆栈。

  说明：标准日志输出与标准错误输出文件每次 Jboss 重启时才滚动，如果大量输出送往这两个文件，容易造成文件大小超过操作系统大小限制。

- 异常信息应该包括两类信息：案发现场信息和异常堆栈信息。如果不处理，那么通过关键字 throws 往上抛出。

  正例：

```java
logger.error("inputParams: {} and errorMessage: {}", 各类参数或者对象 toString(), e.getMessage(), e);
```

- 避免重复打印日志，浪费磁盘空间，务必在日志配置文件中设置 additivity=false
- 日志打印时禁止直接用 JSON 工具将对象转换成 String。

  说明：如果对象里某些 get 方法被覆写，存在抛出异常的情况，则可能会因为打印日志而影响正常业务流程的执行。

  正例：打印日志时仅打印出业务相关属性值或者调用其对象的 toString() 方法

- 服务启动日志必须详尽，每一个关键步骤的详细信息都要打印
- 在接口/方法的出入口打印请求和响应参数日志
- 禁止在代码循环体中直接打印非 DEBUG 级别的日志
- 禁止日志打印内容中仅有特殊字符或数字的情况
- 日志内容中应该包含关键特征类信息，例如：用户标识或订单流水号
- 每条日志在语义上可独立被理解，减少上下文关联理解
- 日志时间戳要求至少毫秒级别
- 不同类型的日志文件放在不同文件夹
- **建议使用异步的方式来输出日志**

## 日志框架

### **不能建议直接使用日志系统（Log4j、Logback）中的** API，而是使用日志框架 SLF4J 中的 API

- 常用的 Java 日志框架可选择 `Log4j/Logback/Log4j2` 等，但为了避免后续更换日志框架所带来的额外改造成本，建议将接口层和实现层进行分离
- 将 SLF4J 作为接口层，将 `Log4j/Logback/Log4j2` 作为实现层，两者通过桥接的方式进行集成，可以使用 Lombok 实现

本篇以 **Logback 为例。**

## 日志存储

### 写本地文件配置（logback）

```yml
logging.info_log_file_path: log/info/security-platform.info
logging.info_log_max_history_in_hours: 168
logging.error_log_file_path: log/error/security-platform.error
logging.error_log_max_history_in_days: 30
logging.warn_log_file_path: log/warn/security-platform.warn
logging.warn_log_max_history_in_days: 30
logging.debug_log_file_path: log/debug/security-platform.debug
logging.debug_log_max_history_in_days: 7
logging.access_log_file_path: log/access/security-platform.access
logging.access_log_max_history_in_hours: 168
logging.access_debug_log_file_path: log/access_debug/security-platform.access_debug
logging.access_debug_log_max_history_in_days: 3
logging:
  config: "classpath:logback.xml"
logback.access:
  enabled: true
  config: "classpath:logback-access.xml"
  log_full_content: true
  useServerPortInsteadOfLocalPort: true
  tomcat:
    enableRequestAttributes: true
```

## 日志文件格式

日志分类关系如下：

**所有的日志都存在于一个 `log` 文件夹下，按不同的级别进行分类，如下：**

![](https://steamory.feishu.cn/space/api/box/stream/download/asynccode/?code=ZGYyMjlmMWJlNjZhN2VmMzI1NzgyMGI4YTg4Y2NjOTNfTWdGVHh2NDdmWlg4NkZrVkJzYWowUDhjVDdTVlpMdjJfVG9rZW46Ym94Y25VNmZDYzZUSlVpcjZqMzJOV0I1YnlmXzE2NzMyNjM1Mzg6MTY3MzI2NzEzOF9WNA)

### Access

此日志是与服务进行交互的日志，最小拆分单位为**小时，如图**

![](https://steamory.feishu.cn/space/api/box/stream/download/asynccode/?code=ZmM2OWQyMzAxZTU0NGVjNzczZWUyZDBjMTZlZDQ0OWJfcVBRUmZmazYxeFlDRWtLV3hTV2pSazJOdGZCU0c3ZHFfVG9rZW46Ym94Y25VenQ2M1J0aDhjN1Bxb1VQcGhJczNJXzE2NzMyNjM1Mzg6MTY3MzI2NzEzOF9WNA)

每个日志文件中**按行**进行打印格式为：

![](https://steamory.feishu.cn/space/api/box/stream/download/asynccode/?code=NTE3NTgzNGIwYzYwOWYxNmI4NzI1Y2RjOWY1MTE2NWRfR3Y5TlB0NTRBb05pZFpINjh5SXcwMVBvOUw2V1ZSNVdfVG9rZW46Ym94Y25EZEFHakZ5T2JHbjFUNVNwbE90R01jXzE2NzMyNjM1Mzg6MTY3MzI2NzEzOF9WNA)

### Access Debug

目录结构与 access 一致

每次请求的日志按如下格式进行打印：

![](https://steamory.feishu.cn/space/api/box/stream/download/asynccode/?code=YjZmYjgyOGQ4MzljMzdiNTVkMGNlNDY0MThlYzUyZTdfOTVyZ0E0MVhrSU5UUEkxMkZTQlQyYTFGSUFyRURGZk9fVG9rZW46Ym94Y252VjN6SDl4N0t3dkhmWmk2eHc2VWxiXzE2NzMyNjM1Mzg6MTY3MzI2NzEzOF9WNA)

### Debug、Info、Warn、Error

#### 按小时拆分打平（对收集比较友好）

如下

![](https://steamory.feishu.cn/space/api/box/stream/download/asynccode/?code=YzJhOGIwYmY0NjU4MGQ5NjBkMmI0ZDQ3N2ZjNTk5MGNfR0RpQklrTGNBNFJ0TFhkQ21MaFBNeGlESlFYVjk5SlVfVG9rZW46Ym94Y243QVRNRWxPbmFTc3VEdFZJMXFsdkRlXzE2NzMyNjM1Mzg6MTY3MzI2NzEzOF9WNA)

#### 按天文件夹聚合（对用户自己检索比较友好）

如下服务运行的 debug 级别日志

![](https://steamory.feishu.cn/space/api/box/stream/download/asynccode/?code=ZDBlY2NlYmE5Zjc0YWI1Y2RmOGY5YjUzY2VlNTY3MzFfMU5aVGdFMmFmcEVsdG16MTZKODJXVkRmQlhXSzJMZDNfVG9rZW46Ym94Y25NeEx4VFBUUEpYZm5tb2R5dG9Ic1hlXzE2NzMyNjM1Mzg6MTY3MzI2NzEzOF9WNA)

历史日志会按指定大小进行拆分

![](https://steamory.feishu.cn/space/api/box/stream/download/asynccode/?code=ZDgzOGI4NDQ3ZjAwOTkwOTA3NWI1NDVlNGZmYWRlM2RfcEdhT3d2TGdpRDZhVHZKaG1qSkN6SlZsbno4Y3ZEODJfVG9rZW46Ym94Y25BRWNBMDI2N3NNVWZTajFndUlRMmR0XzE2NzMyNjM1Mzg6MTY3MzI2NzEzOF9WNA)

示例

![](https://steamory.feishu.cn/space/api/box/stream/download/asynccode/?code=NWM3ZDdlYTAwZWE0Y2NjMDFmNWZiY2U4MGE4ZGJiOTJfckJEVVJXVHUydHJFZ1dtV1FMZTdxbkFNZEtsY1pENFpfVG9rZW46Ym94Y251QkhlTlJ2TVRHWXJkUGxRcU14cEVlXzE2NzMyNjM1Mzg6MTY3MzI2NzEzOF9WNA)

## 日志字段切分

理想的**日志格式**，应当包括这些最基本的信息：如当**前时间戳**（一般毫秒精确度）、**日志级别**，**线程名字**等等。在 logback 日志里可以这么配置：

```JSON
<property name="logging.log_pattern"
		  value="${logging.log_pattern:-%d{yyyy-MM-dd HH:mm:ss.SSS} | %p | ${PID:--} | %t | %logger | %X{x-authing-request-id:--} | %X{currentUser:--} | %F:%M:%L | %m%n}"/>
```

### Info、debug、error、warn

**以 “ | ” 来切分日志**（注意前后有空格，共三个字符）

示例：

```txt
2022-06-18 22:36:35.703 | INFO | 7432 | main | cn.authing.security.PasswordServerApplication | - | - | StartupInfoLogger.java:logStarted:61 | Started PasswordServerApplication in 14.07 seconds (JVM running for 18.854)

2022-09-08 14:16:28.056 | INFO | 1 | http-nio-8790-exec-3 | cn.authing.security.common.logging.AuthingRequestIdFilter | e596ff56-4983-4655-9780-6c571517c687 | - | AuthingRequestIdFilter.java:afterCompletion:76 | [status:200,time:8ms] GET /api/v3/sec/password-policy/89/strength/6219de6ce6bfeabc92071991
```

| **切分后数组** | **字段描述** | **示例**                                                                    |
| -------------- | ------------ | --------------------------------------------------------------------------- |
| 第一位         | 时间         | 2022-06-18 21:21:08.567                                                     |
| 第二位         | 类型         | INFO                                                                        |
| 第三位         | PID          | 7432                                                                        |
| 第四位         | 线程名       | main                                                                        |
| 第五位         | 日志名       | cn.authing.security.PasswordServerApplication                               |
| 第六位         | 请求 ID      | -                                                                           |
| 第七位         | 当前用户     | -                                                                           |
| 第八位         | 位置详情     | StartupInfoLogger.java:logStarted:61                                        |
| 第九位         | 内容         | Started PasswordServerApplication in 14.07 seconds (JVM running for 18.854) |

### Access

**以 “ | ” 来切分日志**（注意前后有空格，共三个字符）

格式：

```txt
%i{ClientIp} | %h | %l | %u | [%t] | "%r" | %s | %b | "%i{Referer}" | "%i{User-Agent}" | %i{x-ssl-header} | %D
```

示例：

- | 127.0.0.1 | - | - | [18/六月/2022:21:23:30 +0800] | "DELETE /api/v3/sec/password/updated-remind-token HTTP/1.1" | 200 | 108 | "-" | "PostmanRuntime/7.26.8" | - | 8

| **切分后数组** | **字段描述** | **示例**                                                    |
| -------------- | ------------ | ----------------------------------------------------------- |
| 第一位         | 客户端 IP    | -                                                           |
| 第二位         | 主机         | 127.0.0.1                                                   |
| 第三位         | 日志名       | -                                                           |
| 第四位         | 用户         | -                                                           |
| 第五位         | 日期         | [18/六月/2022:21:23:30 +0800]                               |
| 第六位         | 请求         | "DELETE /api/v3/sec/password/updated-remind-token HTTP/1.1" |
| 第七位         | 状态码       | 200                                                         |
| 第八位         | 内容长度     | 108                                                         |
| 第九位         | Referer      | "-"                                                         |
| 第十位         | User-Agent   | "PostmanRuntime/7.26.8"                                     |
| 第十一位       | header       | -                                                           |
| 第十二位       | 耗时毫秒     | 8                                                           |

## 示例

- logback.xml

```xml
      <?xml version="1.0" encoding="UTF-8"?><configuration debug="true">    <jmxConfigurator/>    <!-- configure logger level -->    <logger name="cn.authing.security" level="DEBUG"/>    <contextListener class="ch.qos.logback.classic.jul.LevelChangePropagator"/>    <if condition='isDefined("spring.config.location")'>        <then>            <property file="${spring.config.location}"/>        </then>    </if>    <if condition='!isDefined("spring.config.location")'>        <then>            <property resource="application.yml"/>        </then>    </if>    <property name="logging.log_pattern" value="${logging.log_pattern:-%d{yyyy-MM-dd HH:mm:ss.SSS} | %p | ${PID:--} | %t | %logger | %X{x-authing-request-id:--} | %X{currentUser:--} | %F:%M:%L | %m%n}"/><!--    <property name="logging.log_pattern" value="${logging.log_pattern:-%d{yyyy-MM-dd HH:mm:ss.SSS} %-5.5p %-6(${PID:- }) [%-10.10t] -&#45;&#45; %-40.40logger : [%X{x-authing-request-id}][%X{currentUser}][%F:%M:%L] %m%n}"/>-->    <property name="logging.max_log_file_size" value="${logging.max_log_file_size:-50MB}"/>    <!-- for dev environment, add console appender -->    <if condition='isDefined("logging.has_console_appender")'>        <then>            <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">                <encoder>                    <pattern>${logging.log_pattern}</pattern>                </encoder>            </appender>            <appender name="ASYNC-STDOUT" class="ch.qos.logback.classic.AsyncAppender">                <!-- 不丢失日志.默认的,如果队列的80%已满,则会丢弃TRACT、DEBUG、INFO级别的日志 -->                <discardingThreshold>256</discardingThreshold>                <!-- 更改默认的队列的深度,该值会影响性能.默认值为256 -->                <queueSize>1024</queueSize>                <!-- 如果设置为true，队列满了会直接丢弃信息，而不是阻塞（其实就是使用的offer而不是put方法）-->                <neverBlock>true</neverBlock>                <!-- 添加附加的appender,最多只能添加一个 -->                <appender-ref ref="STDOUT"/>            </appender>        </then>    </if>    <if condition='isDefined("logging.info_log_file_path")'>        <then>            <appender name="INFO_LOG_FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">                <filter class="ch.qos.logback.classic.filter.ThresholdFilter">                    <level>INFO</level>                </filter>                <encoder>                    <charset>UTF-8</charset>                    <pattern>${logging.log_pattern}</pattern>                </encoder>                <file>${logging.info_log_file_path}.log</file>                <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">                    <fileNamePattern>${logging.info_log_file_path}.%d{yyyyMMddHH}.log</fileNamePattern>                    <if condition='isDefined("logging.info_log_max_history_in_hours")'>                        <then>                            <maxHistory>${logging.info_log_max_history_in_hours}</maxHistory>                        </then>                    </if>                </rollingPolicy>            </appender>            <appender name="ASYNC-INFO_LOG_FILE" class="ch.qos.logback.classic.AsyncAppender">                <!-- 不丢失日志.默认的,如果队列的80%已满,则会丢弃TRACT、DEBUG、INFO级别的日志 -->                <discardingThreshold>256</discardingThreshold>                <!-- 更改默认的队列的深度,该值会影响性能.默认值为256 -->                <queueSize>1024</queueSize>                <!-- 如果设置为true，队列满了会直接丢弃信息，而不是阻塞（其实就是使用的offer而不是put方法）-->                <neverBlock>true</neverBlock>                <!-- 添加附加的appender,最多只能添加一个 -->                <appender-ref ref="INFO_LOG_FILE"/>            </appender>        </then>    </if>    <if condition='isDefined("logging.error_log_file_path")'>        <then>            <appender name="ERROR_LOG_FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">                <filter class="ch.qos.logback.classic.filter.ThresholdFilter">                    <level>ERROR</level>                </filter>                <encoder>                    <charset>UTF-8</charset>                    <pattern>${logging.log_pattern}</pattern>                </encoder>                <file>${logging.error_log_file_path}.log</file>                <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">                    <fileNamePattern>${logging.error_log_file_path}.%d{yyyyMMddHH}.log</fileNamePattern>                    <if condition='isDefined("logging.error_log_max_history_in_hours")'>                        <then>                            <maxHistory>${logging.error_log_max_history_in_hours}</maxHistory>                        </then>                    </if>                </rollingPolicy>            </appender>            <appender name="ASYNC-ERROR_LOG_FILE" class="ch.qos.logback.classic.AsyncAppender">                <!-- 不丢失日志.默认的,如果队列的80%已满,则会丢弃TRACT、DEBUG、INFO级别的日志 -->                <discardingThreshold>0</discardingThreshold>                <!-- 更改默认的队列的深度,该值会影响性能.默认值为256 -->                <queueSize>1024</queueSize>                <!-- 如果设置为true，队列满了会直接丢弃信息，而不是阻塞（其实就是使用的offer而不是put方法）-->                <neverBlock>false</neverBlock>                <!-- 添加附加的appender,最多只能添加一个 -->                <appender-ref ref="ERROR_LOG_FILE"/>            </appender>        </then>    </if>    <if condition='isDefined("logging.warn_log_file_path")'>        <then>            <appender name="WARN_LOG_FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">                <filter class="ch.qos.logback.classic.filter.ThresholdFilter">                    <level>WARN</level>                </filter>                <encoder>                    <charset>UTF-8</charset>                    <pattern>${logging.log_pattern}</pattern>                </encoder>                <file>${logging.warn_log_file_path}.log</file>                <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">                    <fileNamePattern>${logging.warn_log_file_path}.%d{yyyyMMddHH}.log</fileNamePattern>                    <if condition='isDefined("logging.warn_log_max_history_in_hours")'>                        <then>                            <maxHistory>${logging.warn_log_max_history_in_hours}</maxHistory>                        </then>                    </if>                </rollingPolicy>            </appender>            <appender name="ASYNC-WARN_LOG_FILE" class="ch.qos.logback.classic.AsyncAppender">                <!-- 不丢失日志.默认的,如果队列的80%已满,则会丢弃TRACT、DEBUG、INFO级别的日志 -->                <discardingThreshold>256</discardingThreshold>                <!-- 更改默认的队列的深度,该值会影响性能.默认值为256 -->                <queueSize>1024</queueSize>                <!-- 如果设置为true，队列满了会直接丢弃信息，而不是阻塞（其实就是使用的offer而不是put方法）-->                <neverBlock>true</neverBlock>                <!-- 添加附加的appender,最多只能添加一个 -->                <appender-ref ref="WARN_LOG_FILE"/>            </appender>        </then>    </if>    <if condition='isDefined("logging.debug_log_file_path")'>        <then>            <appender name="DEBUG_LOG_FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">                <filter class="ch.qos.logback.classic.filter.ThresholdFilter">                    <level>DEBUG</level>                </filter>                <encoder>                    <charset>UTF-8</charset>                    <pattern>${logging.log_pattern}</pattern>                </encoder>                <file>${logging.debug_log_file_path}.log</file>                <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">                    <fileNamePattern>${logging.debug_log_file_path}.%d{yyyyMMddHH}.log</fileNamePattern>                    <if condition='isDefined("logging.debug_log_max_history_in_hours")'>                        <then>                            <maxHistory>${logging.debug_log_max_history_in_hours}</maxHistory>                        </then>                    </if>                </rollingPolicy>            </appender>            <appender name="ASYNC-DEBUG_LOG_FILE" class="ch.qos.logback.classic.AsyncAppender">                <!-- 不丢失日志.默认的,如果队列的80%已满,则会丢弃TRACT、DEBUG、INFO级别的日志 -->                <discardingThreshold>256</discardingThreshold>                <!-- 更改默认的队列的深度,该值会影响性能.默认值为256 -->                <queueSize>1024</queueSize>                <!-- 如果设置为true，队列满了会直接丢弃信息，而不是阻塞（其实就是使用的offer而不是put方法）-->                <neverBlock>true</neverBlock>                <!-- 添加附加的appender,最多只能添加一个 -->                <appender-ref ref="DEBUG_LOG_FILE"/>            </appender>        </then>    </if>    <!-- configure root -->    <root level="INFO">        <if condition='isDefined("logging.debug_log_file_path")'>            <then>                <appender-ref ref="ASYNC-DEBUG_LOG_FILE" />            </then>        </if>        <if condition='isDefined("logging.info_log_file_path")'>            <then>                <appender-ref ref="ASYNC-INFO_LOG_FILE" />            </then>        </if>        <if condition='isDefined("logging.error_log_file_path")'>            <then>                <appender-ref ref="ASYNC-ERROR_LOG_FILE" />            </then>        </if>        <if condition='isDefined("logging.warn_log_file_path")'>            <then>                <appender-ref ref="ASYNC-WARN_LOG_FILE" />            </then>        </if>        <if condition='isDefined("logging.has_console_appender")'>            <then>                <appender-ref ref="ASYNC-STDOUT" />            </then>        </if>    </root></configuration>
```

- logback-access.xml

```xml
      <?xml version="1.0" encoding="UTF-8"?><configuration debug="true">    <!-- access_debug filter, /api prefix only, css/html/js file content will not be logged  -->    <!--<property name="logging.access_debug_uri_prefix" value="/"/>-->    <statusListener class="ch.qos.logback.core.status.OnConsoleStatusListener"/>    <if condition='isDefined("spring.config.location")'>        <then>            <property file="${spring.config.location}"/>        </then>    </if>    <if condition='!isDefined("spring.config.location")'>        <then>            <property resource="application.yml"/>        </then>    </if>    <property name="logging.max_log_file_size" value="${logging.max_log_file_size:-50MB}"/>    <property name="logging.access_debug_uri_prefix" value="${logging.access_debug_uri_prefix:-/}"/>    <if condition='isDefined("logging.access_log_file_path")'>        <then>            <appender name="ACCESS_LOG_FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">                <encoder>                    <charset>UTF-8</charset>                    <pattern>%i{ClientIp} | %h | %l | %u | [%t] | "%r" | %s | %b | "%i{Referer}" | "%i{User-Agent}" | %i{x-ssl-header} | %D                    </pattern>                </encoder>                <file>${logging.access_log_file_path}.log</file>                <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">                    <fileNamePattern>${logging.access_log_file_path}.%d{yyyyMMddHH}.log</fileNamePattern>                    <if condition='isDefined("logging.access_log_max_history_in_hours")'>                        <then>                            <maxHistory>${logging.access_log_max_history_in_hours}</maxHistory>                        </then>                    </if>                </rollingPolicy>            </appender>        </then>    </if>    <if condition='isDefined("logging.access_debug_log_file_path")'>        <then>            <appender name="ACCESS_DEBUG_LOG_FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">                <filter class="ch.qos.logback.core.filter.EvaluatorFilter">                    <evaluator name="ApiOnly">                        <expression>                            event.getRequestURI().startsWith("${logging.access_debug_uri_prefix}")                        </expression>                    </evaluator>                    <onMismatch>DENY</onMismatch>                </filter>                <encoder>                    <charset>UTF-8</charset>                    <pattern>%i{ClientIp} | %h | %l | %u | [%t] | "%r" | %s | %b | "%i{Referer}" | "%i{User-Agent}" | %i{x-ssl-header} | %n======&gt;%n%fullRequest | %n&lt;======%n%fullResponse                    </pattern>                </encoder>                <file>${logging.access_debug_log_file_path}.log</file>                <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">                    <fileNamePattern>${logging.access_debug_log_file_path}.%d{yyyyMMddHH}.log</fileNamePattern>                    <if condition='isDefined("logging.access_debug_log_max_history_in_hours")'>                        <then>                            <maxHistory>${logging.access_debug_log_max_history_in_hours}</maxHistory>                        </then>                    </if>                </rollingPolicy>            </appender>        </then>    </if>    <!-- add appender -->    <if condition='isDefined("logging.access_log_file_path")'>        <then>            <appender-ref ref="ACCESS_LOG_FILE"/>        </then>    </if>    <if condition='isDefined("logging.access_debug_log_file_path")'>        <then>            <appender-ref ref="ACCESS_DEBUG_LOG_FILE"/>        </then>    </if></configuration>

```

参考资料

[LogBack 学习笔记](https://werty.cn/2020/07/JAVA/LogBack%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0/)
