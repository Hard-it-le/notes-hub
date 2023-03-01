# Git 各个平台安装教程

[Git](http://destyy.com/wZnV3h) 是由 **Linus Torvalds** 为 Linux 内核开发设计和开发的。Git 为非线性分布式开发提供支持，允许多个贡献者同时处理一个项目。Git 是最流行的分布式版本控制和源代码管理系统。本指南解释了如何使用各自的包管理器在 GNU/Linux、Mac Osx 和 Windows 上安装最新的、稳定的、预打包版本的 Git。[Git](http://destyy.com/wZnV3h) 也可以从[源代码编译并安装](http://destyy.com/wZn3pu)在任何操作系统上。

## Window 安装教程

### 第 1 步 — 安装 Git

打开任何终端并通过键入以下命令检查您是否已经安装了 Git：
```bash
git --version
```

如果您收到错误消息，则需要安装 Git。无论如何，我还是建议安装/更新 Git。

![image.png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2af8f1a8363741d8b53426171a90cfef~tplv-k3u1fbpfcp-watermark.image?)

系统上还没有 Git。继续打开 <https://git-scm.com/> 。我看到的最新版本是2.30.0。

现在打开您下载的安装程序并完成安装过程。除非您知道自己在做什么，否则**请将所有设置保留为默认值**。

### 许可证信息

您需要接受 GNU GPL 开源许可证才能继续。

![image.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d4ca57866724c6d9996809bdf082051~tplv-k3u1fbpfcp-watermark.image?)

### 选择目的地位置

除非系统管理员另有指示，否则请使用 Git 建议的安装路径。

![image.png](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/408e270036574f5095cb407f98a34126~tplv-k3u1fbpfcp-watermark.image?)

### 选择组件

除了预先选择的选项外，您可能还需要选择“将 Git Bash 配置文件添加到 Windows 终端”。这在以后很有用，特别是如果您计划使用 Visual Studio Code 或其他具有内置终端窗口的 IDE。

![image.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e022a4ef97b741d08c329203fbf382e5~tplv-k3u1fbpfcp-watermark.image?)

### 开始菜单文件夹

在这一步，您可以选择开始菜单文件夹的名称。默认值为 Git。在下方，您可以选择不创建此类条目。

![image.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/154dddf604764655b0abb3349d239911~tplv-k3u1fbpfcp-watermark.image?)

### Git 使用的默认编辑器

有时 Git 会要求您插入或编辑一些文本，例如在输入提交消息时。使用的默认编辑器是 Vim。但是，如果您是初学者并且以前从未使用过 Vim，**我强烈建议您**选择另一个您熟悉的文本编辑器，例如 Nodepad++、Visual Studio Code 或好用的记事本。

![image.png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f4b93b91c94542869b8288b1b0901a96~tplv-k3u1fbpfcp-watermark.image?)

### 初始分支名称

整个软件开发社区都在努力变得更具包容性。大多数 Git 存储库仍然`master`用作它们的主要分支。有一个用 main 替换 master 的动作，但 Git 仍然使用 master 作为默认值。

主要的 Git 托管公司（例如 GitHub 和 GitLab）已经将其默认分支名称从 重命名`master`为`main`.

目前，Git 仍然默认使用 master。但是，我强烈建议覆盖此设置，如下图所示。

![image.png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a9d56a503194beb8491ac87f11c9888~tplv-k3u1fbpfcp-watermark.image?)

### 路径环境

每当您希望在不指定完整位置路径的情况下从命令行使用工具时，您需要通过将该目录添加到 PATH 环境变量来告知 Windows。吉特也不例外。我建议使用默认选项。

![image.png](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9f56d7e68a34b1983cf73059a629436~tplv-k3u1fbpfcp-watermark.image?)

### SSH 可执行文件

除非你知道你已经安装了 OpenSSH，否则最好使用 Git 自带的 OpenSSH。

![image.png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/250841a3d36f4ebc9832cea95a02bf52~tplv-k3u1fbpfcp-watermark.image?)

### HTTPS 传输后端

除非您有特定说明，否则请使用 OpenSSL 库。如果您以后由于证书验证问题而遇到从组织内部克隆私有存储库的问题，您可能需要返回此部分。

![image.png](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b1771c6a87d4b3fb19db3fabe94039f~tplv-k3u1fbpfcp-watermark.image?)

### 行尾约定

Windows 和 Unix 系统对行尾使用不同的编码。除非您有其他说明，否则最好在此处使用默认值。

![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da94eee249b84de682d31f08eccf8e2d~tplv-k3u1fbpfcp-watermark.image?)

### Git Bash 的终端模拟器

MinTTY 终端仿真器更加现代，对于大多数用例来说是最佳选择。

![image.png](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb68f9c117e14c56b6482194a1a9d341~tplv-k3u1fbpfcp-watermark.image?)

### Git 拉取行为

默认情况下，从远程 Git 存储库中提取新更改不会尝试变基。由于大多数 Git 手册和教程都假定您使用默认选项，因此最好保持原样（暂时）。

![image.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b150d2592b34f9294f88d025c6bc1bf~tplv-k3u1fbpfcp-watermark.image?)

### Git 凭证助手

使用凭证助手是在 Git 中使用多因素 HTTPS 身份验证的好方法。如果您通过 HTTPS（而不是 SSH）工作，这对于使用外部 Git 存储库非常有用。

引用文档，[Git Credential Manager](https://github.com/GitCredentialManager/git-credential-manager/) “为 Azure DevOps、Azure DevOps Server（以前的 Team Foundation Server）、GitHub、Bitbucket 和 GitLab 提供多因素身份验证支持。”

![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/159beec3684444b58e83edb6eac77b4b~tplv-k3u1fbpfcp-watermark.image?)

### 额外选项

这是技术方法，所以我们将使用默认值。

![image.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb522427c0774bb2af1d534547a52fab~tplv-k3u1fbpfcp-watermark.image?)
### 实验选项

在这一点上，我不建议启用任何实验性功能。

![image.png](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cec2999e233d4de48e3461c1f56aeefa~tplv-k3u1fbpfcp-watermark.image?)

### 安装过程

这不应超过一分钟才能完成。

![image.png](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f022f78c94b49e183bbb37a77b9e094~tplv-k3u1fbpfcp-watermark.image?)

该向导还安装了一个名为 **Git Bash** 的新工具，它是 Cmd 或 Powershell 的终端替代品。我将用它来演示接下来的步骤。

![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06722aa2036647cdaa387bdb3c528e85~tplv-k3u1fbpfcp-watermark.image?)

单击复选框以启动 Git Bash，然后单击完成。

从 Git Bash 或您选择的终端，运行以下命令。

```bash
git --version
```

![image.png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c74a785d239417a9ec19c3a9c8b9216~tplv-k3u1fbpfcp-watermark.image?)

应该显示当前的 Git 版本

# Linux 安装教程
![image.png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3bee12593fa94f21b81825ef5e836bdd~tplv-k3u1fbpfcp-watermark.image?)

## 在 CentOS 8 上安装 Git

首先，更新 CentOS 本地软件包索引（可能需要一段时间）：

```bash
sudo apt update -y
```

然后，使用以下命令安装 Git：

```bash
 sudo apt install git -y
```

您可以通过检查版本来验证 Git 安装：

```bash
git --version
```

## 在 Ubuntu 20.04 上安装 Git

Git 通常包含在 Ubuntu 的默认软件包中。但是，无论出于何种原因，您都可以使用以下命令安装 Git：

首先，更新 Ubuntu 本地包索引：

```bash
sudo apt update 
```

然后，使用以下命令安装 Git：

```bash
sudo apt install git
```

您可以通过检查版本来验证 Git 安装：

```bash
git --version
```

![image.png](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee300e95f3f241a9b3552cc3837ff5db~tplv-k3u1fbpfcp-watermark.image?)