![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed1bea8049f9402cb86f0d041db6a0f7~tplv-k3u1fbpfcp-zoom-crop-mark:3024:3024:3024:1702.awebp)
## 什么是 Shell

Linux 中的 shell 脚本是一个特殊的应用程序，它介于操作系统和系统内核之间，充当一个命令解释器的角色。负责接收用户输入的操作指令并进行解释，将需要执行的操作传递给内核执行，并输出执行结果。

([菜鸟教程在线编辑器 (runoob.com)](https://www.runoob.com/try/runcode.php?filename=helloworld&type=bash))

同时它又是一种程序设计语言。作为命令语言，它交互式解释和执行用户输入的命令或者自动地解释和执行预先设定好的一连串的命令；作为程序设计语言，它定义了各种变量和参数，并提供了许多在高级语言中才具有的控制结构，包括循环和分支。

Linux 提供很多提供的 Shell 解析器

```bash
cat /etc/shells

## /bin/sh
## /bin/bash
## /sbin/nologin
## /usr /bin/sh
## /usr/bin/bash
## /usr/sbin/nologin
## /bin/tcsh
## /bin/csh
```

## Shell 入门

### 脚本格式

**脚本必须以 #!/bin/bash 开头（指定解析器）**

### 脚本的常用执行方式

- 第一种：采用 bash 或 sh+脚本的相对路径或绝对路径（不用赋予脚本 +x 权限）

```bash
sh ./helloworld.sh # sh+脚本的相对路径
sh /usr/shells/helloworld.sh # sh+脚本的绝对路径
bash ./helloworld.sh # bash+脚本的相对路径
bash /usr/shells/helloworld.sh# bash+脚本的绝对路径
```

- 第二种：采用输入脚本的绝对路径或相对路径执行脚本（必须具有可执行权限 +x）

```bash
chmod +x helloworld.sh   # 首先要赋予 helloworld.sh 脚本的 +x 权限
./helloworld.sh # 然后相对路径或者绝对路径执行  helloworld.sh
```

注意：第一种执行方法，本质是 bash 解析器帮你执行脚本，所以脚本本身不需要执行权限。第二种执行方法，本质是脚本需要自己执行，所以需要执行权限。

### 变量

#### 系统预定义变量

- 系统常用变量

```bash
$HOME # 当前主目录
$PWD  # 当前所在目录路径
$SHELL 
$USER # 当前操作用户
$PATH
```

#### 自定义变量

- 基本语法
	- 定义变量：变量名=变量值，注意，**`= 号前后不能有空格`**
	- 撤销变量：unset 变量名
	- 声明静态变量：readonly 变量，注意：不能 unset
- 变量定义规则
	-  变量名称可以由字母、数字和下划线组成，但是不能以数字开头，环境变量名建议大写
      - 等号两侧不能有空格
      - 在 bash 中，变量默认类型都是字符串类型，无法直接进行数值运算。
      - 变量的值如果有空格，需要使用双引号或单引号括起来
      - 不能使用 bash 的标识符

#### 特殊变量

##### $`n`

- 基本语法
  $n（功能描述：n 为数字，$0 代表该脚本名称，
  $`1` - $ `9` 代表第一到第九个参数，十以上的参数，十以上的参数需要用大括号包含，如$ {10}）

##### $ `#`

- 基本语法
  $#（功能描述：获取所有输入参数个数，常用于循环,判断参数的个数是否正确以及加强脚本的健壮性）

##### $ `*`、$ @

- 基本语法

$ `*`（功能描述：这个变量代表命令行中所有的参数，$ \* 把所有的参数看成一个整体）
$ @（功能描述：这个变量也代表命令行中所有的参数，不过 $ @ 把每个参数区分对待）

##### $ `？`

- 基本语法

$？（功能描述：最后一次执行的命令的返回状态。如果这个变量的值为 0，证明上一个命令正确执行；如果这个变量的值为非 0（具体是哪个数，由命令自己来决定），则证明上一个命令执行不正确了）

### 运算符

Shell 和其他编程一样，支持包括：算术、关系、布尔、字符串等运算符。原生 bash 不支持简单的数学运算，但是可以通过其他命令来实现，例如 expr 。expr 是一款表达式计算工具，使用它能完成表达式的求值操作。

#### 算数运算符

| 运算符 | 说明   | 举例                                                      |
| ------ | ------ | --------------------------------------------------------- | --- |
| +      | 加法   | expr $a + $b，结果为 30。                                 |
| -      | 减法   | expr $a - $b 结果为-10。                                  |
| \*     | 乘法   | expr $a \* $b 结果为 200。                                |     |
| /      | 除法   | expr $b ＄ a 结果为 2。                                   |     |
| %      | 取余   | expr $b % ＄ a 结果为 O。                                 |     |
| =      | 赋值   | a=$b 将把变量 b 的值赋给 a.                               |     |
| ==     | 相等   | 用于比较两个数字，相同则返回 true. [$a == $b]返回 false。 |     |
| !=     | 不相等 | 用于比较两个数字，不相同则返回 true. [$a/= $b]返回 true。 |

> 条件表达式要放在方括号之间，并且要有空格，例如:`[$a==$b]`是错误的，
> 必须写成`[$a == $b]。

#### 关系运算符

关系运算符只支持数字，不支持字符串，除非字符串的值是数字

| 运算符 | 说明                                                  | 英文                     | 举例                      |
| ------ | ----------------------------------------------------- | ------------------------ | ------------------------- |
| -eq    | 检测两个数是否相等 ，相等返回 true。                  | equal                    | [ $a -eq $b]返回 false。  |
| -ne    | 检测两个数是否不相等，不相等返回 true。               | not equal                | [ $a -ne $b ] 返回 true。 |
| -gt    | 检测左边的数是否大于右边的，如果是，则返回 true。     | greater than             | [ $a -gt $b]返回 false。  |
| -It    | 检测左边的数是否小于右边的，如果是，则返回 true。     | less than                | [$a -lt $b]返回 true。    |
| -ge    | 检测左边的数是否大于等于右边的，如果是，则返回 true。 | Greater than or equal to | [$a -ge $b]返回 false。   |
| -le    | 检测左边的数是否小于等于右边的，如果是，则返回 true。 | Less than or equal to    | [$a -le $b]返回 true。    |

### 流程控制

#### if

- if

```bash
if condition
then
    command1
    command2
    ...
    commandn
fi
```

- if - else

```bash
if condition
then
    command1
    command2
    ...
    commandn
else
	command
fi
```

- if - else if- if

```bash
if condition1
then
    command1
elif condition2
then
	command2
else
	commandn
fi
```

####  for 循环

```bash
for i in (list);do
command
command
...
done
```

#### while 语句

while 循环用于不断执行一系列命令，也用于从输入文件中读取数据；命令通常为测试条件。

```bash
while condition；do
	command
done
```

#### 无限循环

```bash
for((;;))
do
	command
done

while true
do
	command
done
```

#### case

case 语句为多选择语句。可以用 case 语句匹配一个值与一个模式，如果匹配成功，执行相匹配的命令。case

```bash
case 值 in

	模式 1）
		command1
		command2
		;;
	模式 2）
		command3
		command3
		;;
esac
```

> case 工作方式如上所示。取值后面必须为单词 in，每一模式必须以右括号结束。取值可以为变量或常数。
> 匹配发现取值符合某一模式后，其间所有命令开始执行直至 ;;。
> 取值将检测匹配的每一个模式。一旦模式匹配，则执行完匹配模式相应命令后不再继续其他模式。
> 如果无一匹配模式，使用 星号 \* 捕获该值，再执行后面的命令。

### 跳出循环

在循环过程中，有时候需要在未达到循环结束条件时强制跳出循环，Shell 使用两个命令来实现该功能：break 和 continue。

#### break

break 命令允许跳出所有循环（终止执行后面的所有循环）

#### continue

continue 命令与 break 命令类似，只有一点差别，它不会跳出所有循环，仅仅跳出当前循环。

### 函数

#### 系统函数

- basename

```bash
basename [string / pathname] [suffix] # basename 命令会删掉所有的前缀包括最后一个（‘/’）字符，然后将字符串显示出来。
```

> basename 可以理解为取路径里的文件名称

- dirname

```bash

dirname 文件绝对路径 # 从给定的包含绝对路径的文件名中去除文件名（非目录的部分），然后返回剩下的路径（目录的部分））
```

> dirname 可以理解为取文件路径的绝对路径名称

#### 自定义函数

```bash
[ function ] funname()
{
	action;
	[ return int;]
}
```

> 必须在调用函数地方之前，先声明函数，shell 脚本是逐行运行。不会像其它语言一样先编译。
> 可以带 function fun() 定义，也可以直接 fu()， 不带任何参数
> （2）函数返回值，只能通过 $? 系统变量获得，可以显示加：return 返回，如果不加，将以最后一条命令运行结果，作为返回值。return 后跟数值 n(0-255)

在 Shell 中，调用函数时可以向其传递参数。在函数体内部，通过 $n 的形式来获取参数的值，例如，$1 表示第一个参数，$2 表示第二个参数...
