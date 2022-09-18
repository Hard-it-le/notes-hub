目前大多数的公司和开发者都选择 Git 作为版本控制工具，这意味着每个开发者每天都在使用 Git，都会使用 Git Commit Mesasge ，虽然 Git Commit Message 看起来很简单，但实际上却异常重要。

每个接触项目的开发者通过 Git Commit Message 快速了解当次提交的信息，比如新增了那些功能、解决了那些 Bug、优化了那些问题等。所以一套有效 Git Commit Message 管理规范是很有必要的。也对项目有着更好的维护性。

规范化 Git Commit Message 不仅仅有以上的好处，还有更多的好处，比如：

-   自动化生成 changeLog

-   基于提交的类型，自动决定语义化的版本变更

-   触发构建和部署流程

-   使参与者更容易的探索结构化的提交历史，降低贡献项目的难度

## Conventional Commits

[Conventional Commits](https://conventionalcommits.org/spec/v1.0.0-beta.2.html) 的书写规范 就是在 Angular 规范的基础上进一步总结而成。

标准格式

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Type

type 用于表示此次改动的类型，目前常用的主要有以下几种：

-   feat：新功能（feature）表示在代码库中新增了一个功能

-   fix：表示在代码库中修复了一个 bug

-   docs： 文档（documentation）的新增、修改、删除等操作

-   style： 格式化, 缺失分号等; 不包括生产代码变动

-   refactor： 重构代码（即不是新增功能，也不是修改 bug 的代码变动）

-   perf： 性能优化

-   test： 添加缺失的测试, 重构测试, 不包括生产代码变动

-   chore： 更新 grunt 任务（构建过程或辅助工具的变动）等; 不包括生产代码变动

如果 type 为 feat 和 fix，则该 commit 将肯定出现在 Change log 之中。其他情况（docs、chore、style、refactor、test）由提交者自己决定，要不要放入 Change log，通常情况建议是不要。

### scope

optional 表示 scope 可以选择填写也可以不选择填写。

scope 用于说明 commit 影响的范围，比如数据层、控制层、视图层等等，视项目不同而不同。

### description

简明扼要描述本次提交的内容，首字母无需大写，结尾不加句号，尽量不超过 50 个字符

### body

详细描述本次提交，比如此次变更的动机，如需换行，则使用 `|`。

### footer

描述与之关联的 issue 或 break change。一般使用于不兼容变动或者关闭 issue 或者 break change。

### 注意事项

1.  提交必须以类型为前缀，该类型由名词、、`feat`等组成`fix`，后跟可选范围、可选`!`，以及必需的终端冒号和空格。

2.  `feat`当提交向您的应用程序或库添加新功能时，必须使用该类型。

3.  `fix`当提交代表您的应用程序的错误修复时，必须使用该类型。

4.  可以在类型之后提供范围。范围必须由一个名词组成，描述代码库的一部分，用括号括起来，例如，`fix(parser):`

5.  描述必须紧跟在类型/范围前缀之后的冒号和空格之后。描述是代码更改的简短摘要，例如，*修复：字符串中包含多个空格时的数组解析* *问题*。

6.  可以在简短描述之后提供更长的提交主体，提供有关代码更改的附加上下文信息。正文必须在描述之后开始一个空行。

7.  提交主体是自由格式的，可以由任意数量的换行符分隔的段落组成。

8.  一个或多个页脚可以在正文之后提供一个空行。每个页脚必须由一个单词标记组成，后跟一个`:<space>`或`<space>#`分隔符，后跟一个字符串值（这受到 **[git 预告片约定](https://git-scm.com/docs/git-interpret-trailers)**的启发）。

9.  页脚的标记必须用来`-`代替空白字符，例如，`Acked-by`（这有助于将页脚部分与多段正文区分开来）。例外`BREAKING CHANGE`，它也可以用作标记。

10. 页脚的值可以包含空格和换行符，并且当观察到下一个有效的页脚标记/分隔符对时，解析必须终止。

11. 必须在提交的类型/范围前缀中或作为页脚中的条目指示重大更改。

12. 如果包含在页脚中，则重大更改必须由大写文本 BREAKING CHANGE 后跟冒号、空格和描述组成，例如 *BREAKING CHANGE：环境变量现在优先于配置文件*。

13. 如果包含在类型/范围前缀中，则中断更改必须由 `!`紧接在`:`. 如果`!`使用，`BREAKING CHANGE:`可以从页脚部分省略，提交描述应用于描述重大更改。

14. 您的提交消息中可以使用`feat`和以外的类型，例如*docs: updated ref docs。* `fix`

15. 构成常规提交的信息单元不得被实施者视为区分大小写，但必须为大写的 BREAKING CHANGE 除外。

16. 当用作页脚中的标记时，BREAKING-CHANGE 必须与 BREAKING CHANGE 同义。


## 示例

### **提交带有描述和重大更改页脚的消息**

```
feat: allow provided config object to extend other configs

BREAKING CHANGE: `extends` key in config file is now used for extending other config files
```

### **提交消息** **`!`** **以引起对重大变化的关注**

```
feat!: send an email to the customer when a product is shipped
```

### **提交有范围的信息并** **`!`** **引起对重大变化的关注**

```
feat(api)!: send an email to the customer when a product is shipped
```

### **同时提交消息** **`!`** **和 BREAKING CHANGE 页脚**

```
chore!: drop support for Node 6

BREAKING CHANGE: use JavaScript features not available in Node 6.
```

### **提交没有正文的消息**

```
docs: correct spelling of CHANGELOG
```

### **提交具有范围的消息**

```
feat(lang): add Polish language
```

### **提交带有多段正文和多个页脚的消息**

```
fix: prevent racing of requests

Introduce a request id and a reference to latest request. Dismiss
incoming responses other than from latest request.

Remove timeouts which were used to mitigate the racing issue but are
obsolete now.

Reviewed-by: Z
Refs: #123
```
