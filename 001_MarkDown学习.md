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
- `-`和`[]`之间需要有**空格** [] 之间也要有**空格** 
- [ ] 任务1
- [x] 勾选 



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

- 使用`[ ]( )` 显示内容+ 链接（和插入图片的格式l类似，少了一个感叹号
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



## GitHub徽标

> GitHub徽标，GitHub Badge，也可以叫它徽章
>
> 在项目README中经常看到的那些表明构建状态或者版本等信息的小图标
>
> 使用的网站[Shields.io](https://shields.io/), 例如如下


没学明白，下面是从别人代码库里面复制来的。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


[![Last Commit](https://img.shields.io/github/last-commit/hongtao45/Git-MarkDown-Skills/main?label=&style=plastic)](https://github.com/hongtao45/Git-MarkDown-Skills/commits/main "Commit History")

[![Last Commit](https://img.shields.io/github/last-commit/hongtao45/Git-MarkDown-Skills/main?label=&style=plastic)](https://github.com/hongtao45/Git-MarkDown-Skills/commits/main)



## 表情符号

Emoji 支持表情符号，你可以用系统默认的 Emoji 符号。

输入方式

1. 输入 `:` 将会出现智能提示`:smile:`![img](https://github.githubassets.com/images/icons/emoji/unicode/1f604.png?v8)
2. 直接输入法选入
3. 快捷键后点选：
   - Mac: control+command+space点选
   - Window:使用 Win键+. 或者Win键+. 点选

不同方式输入的emoji可能最后渲染的会不一样😄，影响不大

```markdown
:smile: :laughing: :dizzy_face: :sob: :cold_sweat: :sweat_smile:  :cry: :triumph: :heart_eyes: :relaxed: :sunglasses: :weary: :100: :clap: :bell: :gift: :question: :bomb: :heart: :coffee: :cyclone: :bow: :kiss: :pray: :sweat_drops: :hankey: :exclamation: :anger:
```

![img](https://github.githubassets.com/images/icons/emoji/unicode/1f604.png?v8) ![img](https://github.githubassets.com/images/icons/emoji/unicode/1f606.png?v8) ![img](https://github.githubassets.com/images/icons/emoji/unicode/1f635.png?v8) ![img](https://github.githubassets.com/images/icons/emoji/unicode/1f62d.png?v8) ![img](https://github.githubassets.com/images/icons/emoji/unicode/1f630.png?v8)![img](https://github.githubassets.com/images/icons/emoji/unicode/1f605.png?v8) ![img](https://github.githubassets.com/images/icons/emoji/unicode/1f622.png?v8) ![img](https://github.githubassets.com/images/icons/emoji/unicode/1f624.png?v8) ![img](https://github.githubassets.com/images/icons/emoji/unicode/1f60d.png?v8) ![img](https://github.githubassets.com/images/icons/emoji/unicode/263a.png?v8) ![img](https://github.githubassets.com/images/icons/emoji/unicode/1f60e.png?v8) ![img](https://github.githubassets.com/images/icons/emoji/unicode/1f629.png?v8) ![img](https://github.githubassets.com/images/icons/emoji/unicode/1f4af.png?v8) ![img](https://github.githubassets.com/images/icons/emoji/unicode/1f44f.png?v8) ![img](https://github.githubassets.com/images/icons/emoji/unicode/1f514.png?v8) ![img](https://github.githubassets.com/images/icons/emoji/unicode/1f381.png?v8) ![img](https://github.githubassets.com/images/icons/emoji/unicode/2753.png?v8) ![img](https://github.githubassets.com/images/icons/emoji/unicode/1f4a3.png?v8) ![img](https://github.githubassets.com/images/icons/emoji/unicode/2764.png?v8) ![img](https://github.githubassets.com/images/icons/emoji/unicode/2615.png?v8) ![img](https://github.githubassets.com/images/icons/emoji/unicode/1f300.png?v8) ![img](https://github.githubassets.com/images/icons/emoji/unicode/1f647.png?v8) ![img](https://github.githubassets.com/images/icons/emoji/unicode/1f48b.png?v8) ![img](https://github.githubassets.com/images/icons/emoji/unicode/1f64f.png?v8) ![img](https://github.githubassets.com/images/icons/emoji/unicode/1f4a6.png?v8) ![img](https://github.githubassets.com/images/icons/emoji/unicode/1f4a9.png?v8) ![img](https://github.githubassets.com/images/icons/emoji/unicode/2757.png?v8) ![img](https://github.githubassets.com/images/icons/emoji/unicode/1f4a2.png?v8)

