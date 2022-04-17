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

### `git branch`