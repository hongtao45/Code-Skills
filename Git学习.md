# Git Skills

## 完整的流程

>流程1：
>
>先初始化本地git，再把git提交成远程分支

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
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY-NAME.git
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



## git 放弃修改/增加文件操作

> [git 放弃修改，放弃增加文件操作](https://blog.csdn.net/ustccw/article/details/79068547)

1. 本地**修改了**一些文件 (并没有使用 `git add` 到暂存区)，想放弃修改

   - 单个文件/文件夹：

     ```bash
      git checkout filename
     ```

   - 所有文件/文件夹：

     ```bash
      git checkout .
     ```

2. 本地**新增了**一些文件 (并没有 `git add` 到暂存区)，想放弃修改

   - 单个文件/文件夹：

     ```bash
     rm  -rf filename
     ```

   - 所有文件：

     ```bash
     git clean -xdf
     ```

     > 删除新增的文件，如果文件已经已经 git add 到暂存区，并不会删除！

   - 所有文件和文件夹：
   
     ```bash
     git clean -xdff
     ```
   
     >  [谨慎操作] 本命令删除新增的文件和文件夹，如果文件已经已经 git a dd 到暂存区，并不会删除！



3. 本地**修改/新增了**一些文件，**已经** `git add` 到暂存区，想放弃修改

   - 单个文件/文件夹：

     ```bash
      git reset HEAD filename
     ```
   
   - 所有文件/文件夹：
   
       ```bash
       git reset HEAD .
       ```
   
4. 本地通过 `git add` 和 `git commit` 后，想要撤销此次 commit

   - 撤销 commit, 同时保留该 commit 修改：

     ```bash
     git reset last_commit_id
     ```

     >
     > 这个 commit_id 是你想要回到的那个节点，可以通过 git log 查看，可以只选前 6 位。
     >
     > 撤销之后，你所做的已经 commit 的修改还在工作区！

   - 撤销 `commit`, 同时本地删除该 `commit` 修改：

     ```bash
     git reset --hard last_commit_id
     ```

     > 这个 commit_id 是你想要回到的那个节点，可以通过 git log 查看，可以只选前6位
     >
     > [谨慎操作] 撤销之后，你所做的已经 commit 的修改将会清除，仍在工作区/暂存区的代码也将会清除！

---



# Git Bash常用基本指令

- [常用的基本指令](https://www.jianshu.com/p/2ccdfd59e215)

```bash
pwd #查看当前目录（pwd）
cd  #切换目录（cd 想要切换到的目录名称
ls  #查看当前目录下的内容（ls     ls -al          ls -l）

mkdir #创建目录（mkdir 目录名称）
touch #创建文件（touch 文件名称.html/txt（注意：文件需要带后缀名））

clear #清空（clear）

cat：查看文件全部内容（cat index.html）

rm #删除文件（rm index.html）
rm -rf #把选择的文件夹下所有的文件删除（rm -rf 文件夹名称）
mv # 移动文件或重命名（mv 想要移动的文件 想要移动到的路径）
 （mv 想要重命名的文件 想要重命名的文件的名称）

cp #复制文件（cp 想要复制的文件 想要复制到的路径）

wc #字数信息统计（wc 文件名称）
wc -l #报告行数（wc -l 文件名称）
wc -c #报告字节数（wc -c 文件名称）
wc -m # 报告字符数（wc -m 文件名称）
wc -w #报告单词数（wc -w 文件名称）
```



- 获取帮助信息

```bash
# 指令 --help
ls --help
```

