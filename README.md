# Git Skills

本文记录过程中遇到的与MarkDown有关的所有问题：都记录见 [markdown学习](./markdown学习.md)

## 完整的流程

>流程1：
>
>​	先初始化本地git，再把git提交成远程分支

- 初始化一个`git`，初始完`git`后，如果你是`Windows`用户，你会在目录里看到一个`.git`文件夹，这就说明本地初始化`git`成功了，然后输入

```bash
git init
```

- 给`git`添加文件`README.md`

```bash
git add README.md
```

- 添加完以后，需要进行托付，并写明托付原因：
- 其中`-m`后面的`first commit`就是你要写的托付原因，当然也是支持汉语的。接下来就是，添加远程仓库：(注意后面的链接是你创建`GitHub`项目时，自动生成的)

```bash
git commit -m "first commit"
```

- 添加完远程仓库分支后，接下来就是提交这个分支了：
```bash
git remote add origin https://github.com/nongshuqiner/-git-.git
git push -u origin master
```

> 流程2：
>
> ​	网页端，直接先把远程库创建好

```bash
git clone https://github.com/nongshuqiner/playgit.git
git add .
git commit -m ' '
git push
```

## 流程中会遇到的问题记录

### `branch`基本操作

- 增 (新建分支)

```bash
# 创建一个分支
git branch testing

# 切换到新分支
git checkout testing

# 上面两步操作合并简写,新建分支,并将本地HEAD切换到新分支上
git checkout -b testing

# 它是下面两条命令的简写：
git branch testing
git checkout testing

# 推送到远端,origin没有什么特殊含义,指定远程仓库,通常默认为origin
git push origin testing

# 如果远端上的分支名字不一样,我们可以进行本地到远端的映射
$ git push origin testing:awesomebranch
```

- 删 (删除分支)

```bash
git branch -d hotfix

# 分支没有合并,但可以使用大写的D强制删除
git branch -D hotfix
```

- 查 (分支状态)

```bash
# 查看电脑B本地仓库的分支
git branch

# 查看本地和远程仓库的所有分支
git branch -a

# 查看远程仓库的分支
git branch -r
```

### 删除远程分支

- 查看远程分支

```bash
git branch -a
```

- 删除远程分支

```bash
git push origin --delete <branchName>

# 推送一个空分支到远程分支，其实就相当于删除远程分支
git push origin :dbg_lichen_star
```

### 退到指定状态，再新建分支

1. 找到需要分支的节点，然后git checkout `<commit id>`，将HEAD指过去。
2. 此时`HEAD`为游离状态`（’detached HEAD‘）`。
3. 创建分支，并切换，`git checkout -b <branch name>`。在分支上修改，操作。
4. `push`到远程仓库，`git push origin <branch name>`完成
5. `git push origin dev`，这条命令表示把本地`dev`分支提交到远程仓库，**即创建了远程分支`dev`**
