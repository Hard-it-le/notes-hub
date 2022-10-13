# 正则表达式入门

## 什么是正则表达式？

正则表达式是一种描述字符串数据模式的方法. 它们形成了自己的小语言，是许多编程语言的一部分，如 Javascript、Perl、Python、Php 和 Java。

正则表达式允许您检查一串字符（如电子邮件地址或密码）的模式，以查看它们是否与该正则表达式定义的模式匹配并产生可操作的信息。

创建正则表达式
有两种方法可以在 Javascript 中创建正则表达式。它可以使用 RegExp 构造函数创建，也可以使用正斜杠 ( / ) 将模式括起来。

正则表达式构造函数：
句法：new RegExp(pattern[, flags])

例子：

var regexConst = new RegExp('abc');
正则表达式文字：
句法：/pattern/flags

例子：

var regexLiteral = /abc/;
这里的标志是可选的，我将在本文后面解释这些。
在某些情况下，您可能希望动态创建正则表达式，在这种情况下，正则表达式文字不起作用，因此您必须使用正则表达式构造函数。

无论您选择哪种方法，结果都将是一个正则表达式对象。两个正则表达式对象都将具有相同的方法和属性。

由于正斜杠用于在上面的示例中包含模式，因此如果要将正斜杠用作正则表达式的一部分，则必须使用( / )反斜杠对其进行转义。( \ )

正则表达式方法
测试正则表达式的方法主要有两种。

RegExp.prototype.test()
此方法用于测试是否已找到匹配项。它接受一个字符串，我们必须针对正则表达式进行测试并返回true 或false 取决于是否找到匹配项。

例如：

var 正则表达式 = /hello/;
var str = '你好世界';
var 结果 = 正则表达式.test(str);
控制台.log（结果）；
// 返回真
RegExp.prototype.exec()
此方法返回一个包含所有匹配组的数组。它接受我们必须针对正则表达式进行测试的字符串。

例如：

var 正则表达式 = /hello/;
var str = '你好世界';
var 结果 = regex.exec(str);
控制台.log（结果）；
// 返回 ['hello', index: 0, input: 'hello world', groups: undefined ]
// 'hello' -> 是匹配的模式。
// index: -> 是正则表达式开始的地方。
// 输入：-> 是传递的实际字符串。
我们将使用test()本文中的方法。

简单的正则表达式模式
它是最基本的模式，只是简单地将文字文本与测试字符串匹配。例如：

var 正则表达式 = /hello/;
console.log(regex.test('hello world'));
// 真的
特殊字符
到目前为止，我们已经创建了简单的正则表达式模式。现在，让我们在处理更复杂的情况时充分利用正则表达式的强大功能。

例如，假设我们想要匹配多个电子邮件地址，而不是匹配特定的电子邮件地址。这就是特殊角色发挥作用的地方。为了完全理解正则表达式，您必须记住一些特殊的符号和字符。

标志：
正则表达式有五个可选的标志或修饰符。让我们讨论两个最重要的标志：

g - 全局搜索，第一次匹配后不返回
i - 不区分大小写的搜索
您还可以将标志组合在一个正则表达式中。请注意，它们的顺序对结果没有任何影响。

让我们看一些代码示例：

正则表达式文字 -语法/pattern/flags

var regexGlobal = /abc/g;
console.log(regexGlobal.test('abc abc'));
// 它将匹配所有出现的 'abc'，所以
在第一次匹配后不会返回。
var regexInsensitive = /abc/i;
console.log(regexInsensitive.test('Abc'));
// 返回 true，因为字符串字符的大小写无关紧要
// 在不区分大小写的搜索中。
正则表达式构造函数——语法new RegExp('pattern', 'flags')

var regexGlobal = new RegExp('abc','g')
console.log(regexGlobal.test('abc abc'));
// 它将匹配所有出现的 'abc'，所以在第一次匹配后不会返回。
var regexInsensitive = new RegExp('abc','i')
console.log(regexInsensitive.test('Abc'));
// 返回 true，因为字符串字符的大小写无关紧要 // 在不区分大小写的搜索中。
字符组：
字符集 [xyz] —字符集是一种在单个位置匹配不同字符的方法，它匹配字符串中括号内的字符中的任何单个字符。例如：

var 正则表达式 = /[bt]ear/;
console.log(regex.test('tear')); 
// 返回 true 
console.log(regex.test('bear')); 
// 返回 true 
console.log(regex.test('fear')); 
// 返回假
注意——除了插入符号（在字符集中具有完全不同的含义）之外的所有特殊字符(^)在字符集中都失去了它们的特殊含义。

否定字符集 [^xyz] —它匹配任何未包含在方括号中的内容。例如：

var 正则表达式 = /[^bt]ear/;
console.log(regex.test('tear')); 
// 返回 false 
console.log(regex.test('bear')); 
// return false 
console.log(regex.test('fear')); 
// 返回真
Ranges [az]——假设我们想匹配一个字母表中的所有字母，我们可以将所有字母写在括号内，但有一种更简单的方法，那就是range。例如：[ah]将匹配从 a 到 h 的所有字母。范围也可以是[0-9]之类的数字或[AZ]之类的大写字母。

var 正则表达式 = /[az]ear/;
console.log(regex.test('fear')); 
// 返回真
console.log(regex.test('tear')); 
// 返回真
元字符——元字符是具有特殊含义的字符。有许多元字符，但我将在这里介绍最重要的元字符。

\d — 匹配任何数字字符（与 相同[0-9]）。
\w — 匹配任何单词字符。单词字符是任何字母、数字和下划线。（与 相同[a-zA-Z0–9_]）即字母数字字符。
\s — 匹配空白字符（空格、制表符等）。
\t — 仅匹配制表符。
\b — 在单词的开头或结尾查找匹配项。也称为字边界。
. —（句点）匹配除换行符以外的任何字符。
\D — 匹配任何非数字字符（与 相同[^0–9]）。
\W — 匹配任何非单词字符（与 相同[^a-zA-Z0–9_]）。
\S — 匹配非空白字符。
量词：——量词是在正则表达式中具有特殊含义的符号。

+ — 匹配前面的表达式 1 次或多次。
var 正则表达式 = /\d+/; 
console.log(regex.test('8')); 
// 真的
console.log(regex.test('88899')); 
// 真的
console.log(regex.test('8888845')); 
// 真的
* - 匹配前面的表达式 0 次或更多次。
var 正则表达式 = /go*d/;
console.log(regex.test('gd')); 
// 真的
console.log(regex.test('god')); 
// 真的
console.log(regex.test('good')); 
// 真的
console.log(regex.test('good')); 
// 真的
? — 匹配前面的表达式 0 次或 1 次，即前面的模式是可选的。
var 正则表达式 = /goo?d/;
console.log(regex.test('god')); 
// 真的
console.log(regex.test('good')); 
// 真的
console.log(regex.test('good')); 
// 错误的
^ - 匹配字符串的开头，它后面的正则表达式应该在测试字符串的开头。即插入符号(^) 匹配字符串的开头。
var 正则表达式 = /^g/;
console.log(regex.test('good')); 
// 真的
console.log(regex.test('bad')); 
// 错误的
console.log(regex.test('tag')); 
// 错误的
$ - 匹配字符串的结尾，即它前面的正则表达式应该在测试字符串的结尾。美元 ($) 符号匹配字符串的结尾。
var 正则表达式 = /.com$/;
console.log(regex.test('test@testmail.com')); 
// 真的
console.log(regex.test('test@testmail')); 
// 错误的
{N} — 恰好匹配前面正则表达式的 N 次出现。
var 正则表达式 = /go{2}d/;
console.log(regex.test('good')); 
// 真的
console.log(regex.test('god')); 
// 错误的
{N,} - 匹配至少 N 次出现的前面的正则表达式。
var 正则表达式 = /go{2,}d/;
console.log(regex.test('good')); 
// 真的
console.log(regex.test('good')); 
// 真的
console.log(regex.test('gooood')); 
// 真的
{N,M} - 匹配至少 N 次出现且最多 M 次出现的前面正则表达式（其中 M > N）。
var 正则表达式 = /go{1,2}d/;
console.log(regex.test('god')); 
// 真的
console.log(regex.test('good')); 
// 真的
console.log(regex.test('good')); 
// 错误的
交替 X|Y — 匹配 X 或 Y。例如：

var regex = /（绿色|红色）苹果/；
console.log(regex.test('青苹果')); 
// true 
console.log(regex.test('red apple')); 
// true 
console.log(regex.test('blue apple')); 
// 错误的
注意——如果你想使用任何特殊字符作为表达式的一部分，比如你想匹配文字+或.，那么你必须用反斜杠转义它们( \ )。

例如：

var 正则表达式 = /a+b/; // 这行不通
var 正则表达式 = /a\+b/; // 这将起作用
console.log(regex.test('a+b')); // 真的
先进的
(x) — 匹配 x 并记住匹配。这些称为捕获组。这也用于在正则表达式中创建子表达式。例如 ：-

var 正则表达式 = /(foo)bar\1/; 
console.log(regex.test('foobarfoo')); 
// 真的
console.log(regex.test('foobar')); 
// 错误的
\1记住并使用括号内第一个子表达式的匹配项。

(?:x) — 匹配 x 并且不记得匹配。这些被称为非捕获组。这里\1行不通，它会匹配文字\1。

var 正则表达式 = /(?:foo)bar\1/; 
console.log(regex.test('foobarfoo')); 
// 错误的
console.log(regex.test('foobar')); 
// 错误的
console.log(regex.test('foobar\1')); 
// 真的
x(?=y) - 仅当 x 后跟 y 时才匹配 x。也称为积极展望。例如：

var 正则表达式 = /Red(?=Apple)/;
console.log(regex.test('RedApple')); 
// 真的
在上面的例子中，匹配只会在Red后面跟着Apple.

练习正则表达式：
让我们练习一下我们在上面学到的一些概念。

匹配任何 10 位数字：
var 正则表达式 = /^\d{10}$/;
console.log(regex.test('9995484545')); 
// 真的
让我们分解一下，看看上面发生了什么。

如果我们想强制匹配必须跨越整个字符串，我们可以添加量词^和$。插入符号^ 匹配输入字符串的开头，而美元符号$匹配结尾。因此，如果字符串包含超过 10 个数字，它将不匹配。
\d匹配任何数字字符。
{10}匹配前面的表达式，在这种情况下\d正好 10 次。因此，如果测试字符串包含少于或多于 10 位数字，则结果将为 false。
匹配具有以下格式的日期 DD-MM-YYYY 或DD-MM-YY
var 正则表达式 = /^(\d{1,2}-){2}\d{2}(\d{2})?$/; 
console.log(regex.test('01-01-1990')); 
// true 
console.log(regex.test('01-01-90')); 
// true 
console.log(regex.test('01-01-190')); 
// 错误的
让我们分解一下，看看上面发生了什么。

同样，我们将整个正则表达式包装在^ and$中，以便匹配跨越整个字符串。
(第一个子表达式的开始。
\d{1,2}匹配至少 1 个数字和最多 2 个数字。
-匹配文字连字符。
)第一个子表达式的结尾。
{2}精确匹配第一个子表达式两次。
\d{2}完全匹配两位数。
(\d{2})?完全匹配两位数。但它是可选的，因此任一年份包含 2 位或 4 位。
匹配除换行符以外的任何内容
该表达式应匹配任何格式的字符串，例如abc.def.ghi.jkl每个变量a, b, c, d, e, f, g, h, i, j, k, l 可以是除换行符以外的任何字符。

var 正则表达式 = /^(.{3}\.){3}.{3}$/;
console.log(regex.test('123.456.abc.def')); 
// 真的
console.log(regex.test('1243.446.abc.def')); 
// 错误的
console.log(regex.test('abc.def.ghi.jkl')); 
// 真的
让我们分解一下，看看上面发生了什么。

我们将整个正则表达式包装在^ and$中，这样匹配就跨越了整个字符串。
(第一个子表达式的开始
.{3}匹配除换行符以外的任何字符恰好 3 次。
\.匹配文字.句点
)第一个子表达式的结尾
{3}精确匹配第一个子表达式 3 次。
.{3}匹配除换行符以外的任何字符恰好 3 次。
结论
正则表达式有时可能相当复杂，但正确理解上述概念将有助于您轻松理解更复杂的正则表达式模式。您可以在此处了解更多关于正则表达式的信息并在此处练习。

