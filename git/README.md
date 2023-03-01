## 1、Git 是什么

Git 是一种分布式开源[版本控制](https://aws.amazon.com/cn/devops/source-control/)系统 (VCS)，您可以用它存储代码、跟踪修订历史记录、合并代码更改，并在需要时恢复为较早的代码版本。

## 2、什么是版本控制

[[01、SVN、Git、Mercurial 如何选择你的版本控制系统]]

## Git 的安装

[[02、Git 各个平台安装教程]]

## 3、仓库

![](https://www.pdai.tech/images/git-four-areas.png)

- 仓库初始化

```bash
git init
```

- 工作区添加到暂存区

```bash
git add . # 当前项目所有的更改
git add xx/xx.java xx/xx1.java # 添加特定的文件
```

- 本地仓库状态

```bash
git status
```

- 暂存区提交到本地仓库

```bash
git commit -m "commit 的描述"
```

- 本地仓库绑定远程仓库

```bash
git remote add <name> <git-repo-url>
# 例如 git remote add origin https://github.com/xxxxxx
```

- 本地仓库推送到远程仓库

```bash
git push -u origin master # 第一次需要关联上
git push # 之后再推送就不用指明应该推送的远程分支了
```

- 本地仓库关联远程仓库地址

```bash
git remote -v
```

- 修改远程仓库地址

```bash
git remote set-url origin <your-git-url>
```

- 克隆远程仓库到本地

```bash
git clone <git-repo-url>
```

## 4、 分支

- 创建新分支不切换

```bash
git branch <new-branch-name>
```

- 创建新分支并切换

```bash
git checkout -b <new-branch-name>
```

- 查看当前 Git 仓库的分支列表

```bash
git branch
```

- 切换到现有分支

```bash
git checkout master
```

- 分支合并

```bash
git merge <branch-name>
```

- 删除分支

```bash
git branch -d <branch-name>
```

- 拉取分支

```bash
git pull origin <branch-name>
```

## 5、标签

- 查看当前仓库的标签

```bash
git tag
```

- 创建标签

```bash
git tag v0.0.1
```

- 创建带说明的标签

```bash
git tag -a <标签名> -m "<说明>"
```

- 查看标签信息

```bash
git show <tagname>
```

- 删除本地标签

```bash
git tag -d <tagname>
```

- 删除远程标签

```bash
git push origin :refs/tags/<tagname>
```

- 本地单个标签推送远程

```bash
git push origin <tagname>
```

- 本地全部标签推送到远程

```bash
git push origin --tags
```

> **git reflog** 显示命令历史

## 6、Git 配置

- 查看 Git 配置

```bash
git config --list
```

- 本地仓库绑定用户名

```bash
git config --global user.name "<name>"
```

- 本地仓库绑定邮箱

```bash
git config --global user.email "你的邮箱"
```

## 7、版本回退

- 查看历史版本

```bash
git log # 显示从最近到最远的提交历史
git log --graph --decorate --abbrev-commit --all
git log --graph  # 查看分支合并图
git log --oneline  # 标记把每一个提交压缩到了一行中
git log -n n   # 只展示最后 n 次提交日志
```

- 查看文件修改的具体内容

```bash
git diff # 查看文件修改的具体内容
```

- 合并多个 commit 为 1 个（仅限最新的 commit）

```bash
git rebase -i HEAD~n # n 表示几个 commit
```

- 回退到某一个版本

```bash
git reset --hard <hash>
```

- 回退到上一个版本

```bash
git reset --hard HEAD^^
```

- 删除版本库的文件

```bash
git rm
```

## 8、文件撤销操纵

- 恢复暂存区文件到工作区

```bash
git checkout <file-name>
```

- 恢复暂存区所有文件到工作区

```bash
git checkout .
```

- 重置暂存区某个文件，与上一个 commit 保持一致，但工作区不变

```bash
git reset <file-name>
```

- 重置暂存区与工作区，与上一次 commit 保持一致

```bash
git reset --hard <file-name>
# 如果是回退版本(commit)，那么file，变成commit的hash码就好了。
```

## 9、Git 忽略文件

[[05、Git 忽略提交 .gitignore]]

- 检查 Git 会忽略该文件信息

```bash
git check-ignore -v <file>
```

## Git 常用操作 - 代码提交和同步代码

- 查看当前仓库文件的增删改

```bash
git status
```

- 将文件添加到暂存区

```bash
git add .
```

- 暂存区提交到本地仓库

```bash
git commit -m "<这里写 commit 的描述>"
```

- 本地仓库推送到远程仓库

```bash
git push -u origin master # 第一次需要关联上
git push # 之后再推送就不用指明应该推送的远程分支了
```

## Git 常用操作 - 代码操作和撤销同步

![](https://www.pdai.tech/images/git-five-states.png)

### 已修改未同步

```bash
git diff --cached # 显示暂存区和本地仓库的差异

git reset # 暂存区的修改恢复到工作区

git reset --soft # 与 git reset 等价，回到已修改状态，修改的内容仍然在工作区中

git reset --hard  # 回到未修改的状态，清空暂存区和工作区
```

> git reset --hard 操作相当于 git reset 和 git checkout 两个操作

### 已提交未推送

> 执行完 git commit 后，本地仓库会生成一个版本号（hash 值），表示这次提交的唯一值，之后任何操作都可以用这个版本号回退到这次提交

```bash
git diff <branch-name1> <branch-name2> # 比较2个分支之间的差异
git diff master origin/master # 查看本地仓库与本地远程仓库的差异
git reset --hard origin/master # 回退与本地远程仓库一致
git reset --hard HEAD^ # 回退到本地仓库上一个版本
git reset --hard <hash code> # 回退到任意版本
git reset --soft/git reset # 回退且回到已修改状态，修改仍保留在工作区中。
```

### 已推送远程

```bash
git push -f orgin master  # 强制覆盖远程分支
git push -f # 如果关联过远程分支，则分支名忽略不计
```

> 慎用，一般情况下，本地分支比远程要新，所以可以直接推送到远程，但有时推送到远程后发现有问题，进行了版本回退，旧版本或者分叉版本推送到远程，需要添加 -f 参数，表示强制覆盖。

## 储藏变更

- 当有其他任务插进来时，把当前工作现场“存储”起来,以后恢复后继续工作

```bash
git stash
```

- 查看储藏区列表

```bash
git stash list
```

- 恢复却不删除`stash`内容

```bash
git stash apply
```

- 删除`stash`内容

```bash
git stash drop
```
