# 每个开发都必会的 Git 工作流程

Git 工作流程每个公司或者个人习惯都不是统一，因此，基于大公司都会有一套标准的 Git 工作流程

## 单人开发

- git clone （本地拉取代码）
- git checkout -b xxx  （从某个分支切换到新分支 xxx 上）
- 本地修改 xxx 分支代码
- git status （查看自己修改了那些文件）
- git diff （查看自己对文件代码的改变）
- git add （上传更新后的代码到暂存区）
- git commit -m "信息"（将暂存区的代码提交到本地 git 仓库）
- git push origin xxx （将本地的 xxx 分支上传到 github 上）

## 多人开发
-----------------------------------------------------------
- git checkout master （切换到主分支）
- git checkout xxx 回到xxx分支
- git rebase main （我在xxx分支上，先把main移过来，然后根据我的commit来修改成新的内容）
- git push -f origin xxx（把rebase后并且更新过的代码再push到远端github上）
----------------------------------------------------------------------------------------------
远端完成更新后
1.git branch -d xxx 删除本地的git分支
2.git pull origin master 再把远端的最新代码拉至本地