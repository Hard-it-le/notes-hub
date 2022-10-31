# 每个开发人员都应该知道的 20 个 Git 命令
![image.png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65601fc01ad4485280e1215b1dde2f81~tplv-k3u1fbpfcp-watermark.image?)

在编程，特别是软件开发中，总是有新的命令要学习，旧的命令要记住。在使用特定版本控制系统（如 Git）时尤其如此。

我们将在这篇博文中介绍一些开发人员可能经常使用的最有用的 Git 命令。乍一看，它们中的每一个都可能看起来很简单，但从长远来看，了解这些可以让你的生活更轻松。继续阅读以发现更多信息。

那么让我们开始吧：

**1. git init**

使用此命令将项目设置为 git 存储库。

**2. git remote add origin**

添加或连接到远程存储库

示例：

```
git remote add origin https://github.com/xxxx/Git-demo.git
```

**3. git remote**

要查看链接的远程存储库

**4. git status**

您可以使用此命令查看本地存储库中文件的状态。可以跟踪文件吗？改变了吗？未追踪？

**5. git add**

暂存已更改或未跟踪的文件

示例：

```
git add index.html
git add index.html style.css style.scss
git add  test
```

**git add .**

使用此命令时会识别所有未暂存的文件并添加所有的文件。

**6. git reset**

使用这个命令可以取消暂存文件。

**7. git commit**

要提交暂存文件,除了实现暂存文件外，此操作还输出提交历史的提交消息。

**git commit -m “<在此处提交消息”>**

示例：

```
git commit -m "添加导航栏"
```


**git commit --amend**

使用 git commit --amend 命令对最近的提交进行更改很简单。

**8. git push -u origin**

此命令用于将所选分支中的文件从本地存储库推送到远程存储库，通常称为 GitHub。首次将文件推送到远程存储库时使用此控件。它将识别您将这些文件推送到的位置。在以下强制文件时使用 git pushs。

示例：

```
git push -u master
```


**git push**

将已提交的文件移动到远程存储库是使用此命令完成的。只有在执行上述命令传输文件之后，您才能使用此命令将文件强制到远程存储库。

**9. git fetch**

运行此命令以检索本地存储库的最新版本。它搜索新创建的分支、文件和其他更改。

**10. git pull**

你可以使用这个命令将你刚刚检索到的数据拉到你的本地存储库中。通过完成此操作，远程存储库中的最新版本将在本地仓库中更新。

**11. git rm -r --cached**

示例：

```
git rm -r — cached config.js
```

借助此命令，您可以从 GitHub 的远程存储库中删除文件，而无需从本地存储库中删除它。

**12.git branch**

要预览您当前所在的分支，请使用此命令。

- **git branch -a**
你可以使用这个mastership预览本地和远程仓库中的每一个细节。

- **git branch -r**
要预览本地存储中的每个单元，请运行此命令（也就是您已经访问过的分支）。

- **git branch**
借助此命令，您可以向本地存储库添加新内容。

**13. git checkout — origin/**

要交换分支，请使用此命令。它仅适用于您第一次访问一个单位。（在 GitHub/远程存储库中制作）。
示例：

```
git checkout --track origin/develop
```


**14. git checkout**

您可以使用此命令切换到您已经访问过的分支

示例：

```
git checkout master 
git checkout develop
```

**15. git merge**

这个命令可以保留两个部分。输入您希望从中继承修改以实现此目的的分支。将交付更改的部门是您将与此命令一起使用的部门。

例如，来自开发分支的代码将到达头分支。

```
git develop
```

**16. git merge — abort**

使用此命令停止合并。

如果没有冲突错误，则合并成功。因此，只能在合并失败后应用此中止。

你将如何利用它？

您的终端将首先显示消息“合并失败”您还可能需要解决合并问题。

这是另一个标志：

![image.png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ffc326dae6f49a3a587a41a22ba057f~tplv-k3u1fbpfcp-watermark.image?)

看看第一行的最后一句话。它在括号中说明（主）。我们在总分支，这就是原因。如果你是，它会注明“你在开发分支” `(develop)`。

`(master|merging)`如果您的合并不成功，它将提及或类似的内容。它可能会说合并可能是一个正斜杠，它可能在不同的分支上，等等。无论如何，这个想法是明确的。

这意味着您的合并不成功。

`git merge --abort`将不得不解散合并。

**17. git merge -X theirs**

例子：

```
git merge -X theirs develop
```

使用此命令可以保留两个部分。如果存在合并冲突（而不是当前冲突），此命令只会假定您更喜欢在给定分支中所做的修改。

**18. git reset — hard HEAD**

使用此命令，您可以将本地存储库更新为上传到 GitHub 的最新版本，同时删除您之前所做的任何修改。

**19. git clean -f**

此命令用于从本地存储库中拖动不应该的文件。

**20. git clean -d**

要从本地存储库中删除未跟踪的文件夹，请使用此命令。此外，您可以通过将其与 git clean-fd 结合来实现这两者。