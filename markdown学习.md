# Markdown学习笔记

## 常用快捷键

- 加粗： `Ctrl + B`

- 标题： `Ctrl + H`

- 插入链接： `Ctrl + K`

- 插入代码： `Ctrl + Shift + C` -- 无法执行

- 行内代码： `Ctrl + Shift + K`

- 插入图片： `Ctrl + Shift + I`

- 无序列表：`Ctrl + Shift + L` -- 无法执行

- 撤销： `Ctrl + Z`

- 一级标题： `Ctrl + 1` -- 以此类推

- Typora快捷键整合
  ```
  Ctrl+1  一阶标题    Ctrl+B  字体加粗
  Ctrl+2  二阶标题    Ctrl+I  字体倾斜
  Ctrl+3  三阶标题    Ctrl+U  下划线
  Ctrl+4  四阶标题    Ctrl+Home   返回Typora顶部
  Ctrl+5  五阶标题    Ctrl+End    返回Typora底部
  Ctrl+6  六阶标题    Ctrl+T  创建表格
  Ctrl+L  选中某句话   Ctrl+K  创建超链接
  Ctrl+D  选中某个单词  Ctrl+F  搜索
  Ctrl+E  选中相同格式的文字   Ctrl+H  搜索并替换
  Alt+Shift+5 删除线 Ctrl+Shift+I    插入图片
  Ctrl+Shift+M    公式块 Ctrl+Shift+Q    引用
  
  注：一些实体符号需要在实体符号之前加”\”才能够显示
  ```

## 引用

- 通过 $ > $ 符号来插入引用

> 这是一Markdown 学习入门笔记
>
> 我这边是引用部分



## 代码

- 通过`esc正下方的按键`，设置代码
- 英文输入法状态下的反引号
  - 行内代码，用一个反引号即可 ` （~ 键）`，快捷键：无
  -  代码块，用三个反引号，快捷键：`Ctrl + Shift + K`

```python
import os,sys,time
import xml.etree.ElementTree as ET

# set SUMO environment
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")
from cfgGenerate import cfgGenerate
from osmGenerate import osmGenerate
from netGenerate import netGenerate
from detGenerate import detGenerate
from tazGenerate import tazGenerate
from rouGenerate import rouGenerate
from sumoLaunch import sumoLaunch

# from netCutLine import *
# from runAccident import *
# 
# 
# 
def read_xml(ifn):
    tree = ET.parse(ifn)
    return tree

```



## 插入图片

- 插入图片、`![标题](url)` 组合使用（不留空格
- 快捷点：`Ctrl+Shift+I` 

![images](./figure/images.jpg)

![images2](./figure/images2.jpg)

## 列表

### 无序列表

* 使用` * + - `都可以创建一个无序列表
* 需求 part1
* 需求part2
  * p 2 -1
  * p2 -2
    + 测试缩进显示列表
    + $java$  吸收了 $c++$的有点
    + $\sin{\theta}$和其他的三角函数都理解都可以

### 有序列表

- 使用` 1. 2. 3. `创建有序列表
  1. AAA
  2. BBB
  3. CCC

## 表格

- 输入 `| 表头1 | 表头2 |`并回车。即可创建一个包含2列表
- 快捷键 `Ctrl + T`弹出对话框。

| 序号 |      |   
| ---- | ---- | 
|      |      |     
|      |      |      
|      |      |      

## 任务列表

- \- [ ] 不勾选
- \- [x] 勾选
- `-`和`[]`之间需要又空格
- [ ] 任务1
- [x] 勾选
- [ ] 

---

## 数学公式

- 公式块：
  - 按下 `$$`，然后按下回车键，即可进行数学公式的编辑
  - 快捷键： `Ctrl+Shift+M`
- 内联公式：
  - 行内的的$ $之间就可以输入公式 
  - 快捷键  `Ctrl+M`

$$
\mathbf{v}_1\times\mathbf{v}_2 = \mathbf{v}_3
$$

## 插入链接

- 使用`[ ]( )` 显示内容+ 链接（和插入图片的格式是一样的
- 快捷键： ` Ctrl + K`
- [Git Bash 命令行 配置](https://achuan-2.github.io/posts/be43.html)



## 对齐方式

居中：

```text
<center>诶嘿</center>
```

左对齐：

```text
<p align="left">诶嘿</p>
```

右对齐：

```text
<p align="right">诶嘿</p>
```

绝对正确，诶嘿~~



## 插入小图标

![npm bundle size](https://img.shields.io/bundlephobia/min/Git-MarkDown-Skills?style=plastic)

![npm bundle size](https://img.shields.io/bundlephobia/minzip/Git-MarkDown-Skills?style=plastic)
