# pypinyin模块学习

> 参考资料：
> [Python 中拼音库 *PyPinyin* 的用法！这个库有点意思哈！](https://zhuanlan.zhihu.com/p/76597038)
> [Python 中拼音库 *PyPinyin* 的用法](https://zhuanlan.zhihu.com/p/65151804)
> [官方使用示例](https://pypinyin.readthedocs.io/zh_CN/master/usage.html)



Python 中的汉字转拼音的库，名字叫做 PyPinyin，可以用于汉字注音、排序、检索等等场合，是基于 hotto/pinyin 这个库开发的，一些站点链接如下：

- GitHub: https://github.com/mozillazg/python-pinyin
- 文档：https://pypinyin.readthedocs.io/zh_CN/master/
- PyPi：https://pypi.org/project/pypinyin/



它有这么几个特性：

- 根据词组智能匹配最正确的拼音
- 支持多音字
- 简单的繁体支持, 注音支持
- 支持多种不同拼音/注音风格

## 基本拼音

首先我们进行一下基本的拼音转换，方法非常简单，直接调用 pinyin 方法即可：

```python
from pypinyin import pinyin
print(pinyin('中心'))
```

运行结果：

```text
[['zhōng'], ['xīn']]
```

可以看到结果会是一个二维的列表，每个元素都另外成了一个列表，其中包含了每个字的读音。

如果这个词是**多音字**咋办呢？比如 “朝阳”，它有两个读音，我们拿来试下：

```text
from pypinyin import pinyin
print(pinyin('朝阳'))
```

运行结果：

```text
[['zhāo'], ['yáng']]
```

好吧，它只给出来了一个读音，但是如果我们想要另外一种读音咋办呢？

其实很简单，只需添加 heteronym 参数并设置为 True 就好了，我们试下：

```text
from pypinyin import pinyin
print(pinyin('朝阳', heteronym=True))
```

运行结果：

```text
[['zhāo', 'cháo'], ['yáng']]
```

OK 了，这下子就显示出来了两个读音了，而且我们也明白了**结果为什么是一个二维列表**，因为里面的一维的结果可能是多个，比如多音字的情况就是这样。



**直接给我们一个一维列表呢？有！**

我们可以使用 lazy_pinyin 这个方法来生成，尝试一下：

```python
from pypinyin import lazy_pinyin
print(lazy_pinyin('聪明的小兔子'))
```

运行结果：

```text
['cong', 'ming', 'de', 'xiao', 'tu', 'zi']
```

这时候观察到得到的是一个列表，并且不再包含音调了。



使用`reduce()`函数进行运算

```python
res = lazy_pinyin('聪明的小兔子')
print(res)
from functools import reduce
a = reduce(lambda x,y: x+'_'+y ,res)
print(a)
```

运行结果：

```text
['cong', 'ming', 'de', 'xiao', 'tu', 'zi']
cong_ming_de_xiao_tu_zi
```



## 风格转换

我们可以对结果进行一些风格转换，比如不带声调风格、标准声调风格、声调在拼音之后、声调在韵母之后、注音风格等等，比如我们想要声调放在拼音后面，可以这么来实现：

我们可以对结果进行一些风格转换，比如不带声调风格、标准声调风格、声调在拼音之后、声调在韵母之后、注音风格等等，比如我们想要声调放在拼音后面，可以这么来实现：

```text
from pypinyin import lazy_pinyin, Style
style = Style.TONE3
print(lazy_pinyin('聪明的小兔子', style=style))
```

运行结果：

```text
['cong1', 'ming2', 'de', 'xiao3', 'tu4', 'zi']
```

可以看到运行结果每个拼音后面就多了一个声调，这就是其中的一个风格，叫做 TONE3，其实还有很多风格，下面是我从源码里面找出来的定义：

| Style.*             | 说明                                                         |
| ------------------- | ------------------------------------------------------------ |
| NORMAL = 0          | #:  普通风格，不带声调。如： 中国 -> ``zhong guo``           |
| TONE = 1            | #:  标准声调风格，拼音声调在韵母第一个字母上（默认风格）。如： 中国 -> ``zhōng guó`` |
| TONE2 = 2           | #:  声调风格2，即拼音声调在各个韵母之后，用数字 [1-4] 进行表示。如： 中国 ->  ``zho1ng guo2`` |
| TONE3 = 8           | #:  声调风格3，即拼音声调在各个拼音之后，用数字 [1-4] 进行表示。如： 中国 ->  ``zhong1 guo2`` |
| INITIALS = 3        | #:  声母风格，只返回各个拼音的声母部分（注：有的拼音没有声母，详见 `#27`_）。如： 中国 -> ``zh  g`` |
| FIRST_LETTER = 4    | #:  首字母风格，只返回拼音的首字母部分。如： 中国 -> ``z g`` |
| FINALS = 5          | #:  韵母风格，只返回各个拼音的韵母部分，不带声调。如： 中国 -> ``ong uo`` |
| FINALS_TONE = 6     | #:  标准韵母风格，带声调，声调在韵母第一个字母上。如：中国 -> ``ōng uó`` |
| FINALS_TONE2 = 7    | #:  韵母风格2，带声调，声调在各个韵母之后，用数字 [1-4] 进行表示。如： 中国 ->  ``o1ng uo2`` |
| FINALS_TONE3 = 9    | #:  韵母风格3，带声调，声调在各个拼音之后，用数字 [1-4] 进行表示。如： 中国 ->  ``ong1 uo2`` |
| BOPOMOFO = 10       | #:  注音风格，带声调，阴平（第一声）不标。如： 中国 -> ``ㄓㄨㄥ ㄍㄨㄛˊ`` |
| BOPOMOFO_FIRST = 11 | #:  注音风格，仅首字母。如： 中国 -> ``ㄓ ㄍ``               |
| CYRILLIC = 12       | #:  汉语拼音与俄语字母对照风格，声调在各个拼音之后，用数字 [1-4] 进行表示。如： 中国 ->  ``чжун1 го2`` |
| CYRILLIC_FIRST = 13 | #:  汉语拼音与俄语字母对照风格，仅首字母。如： 中国 -> ``ч г`` |




##　pinyin 对比 lazy_pinyin

pinyin 的方法默认带声调，而 lazy_pinyin 方法不带声调

二者使用的默认风格不同，函数定义：

pinyin 方法的定义如下：

```text
def pinyin(hans,  style=Style.TONE,  heteronym=False,  errors='default',  strict=True)
```

lazy_pinyin 方法的定义如下：

```text
def lazy_pinyin(hans,  style=Style.NORMAL,  errors='default',  strict=True)
```



## 错误处理

在这里我们先做一个测试，比如我们传入无法转拼音的字，比如：

```text
from pypinyin import lazy_pinyin
print(lazy_pinyin('你好☆☆，我是xxx'))
```

 其中包含了星号两个，还有标点一个，另外还包含了一个 xxx 英文字符，结果会是什么呢？

```text
['ni', 'hao', '☆☆，', 'wo', 'shi', 'xxx']
```

可以看到结果中星号和英文字符都作为一个整体并原模原样返回了。

那么**这种特殊字符可以单独进行处理吗？当然可以**，这里就用到刚才提到的 errors 参数了。

errors 参数是有几种模式的：

| 参数           | 说明                                                 |
| -------------- | ---------------------------------------------------- |
| Default        | 默认行为，不处理，原木原样返回                       |
| Ignore         | 忽略字符，直接抛掉                                   |
| Replace        | 直接替换为去掉  u 的 unicode 编码                    |
| callable  对象 | 当传入一个可调用的对象的时候，则可以自定义处理方式。 |



下面是 errors 这个参数的源码实现逻辑：

```text
def _handle_nopinyin_char(chars, errors='default'):
    """处理没有拼音的字符"""
    if callable_check(errors):
        return errors(chars)

    if errors == 'default':
        return chars
    elif errors == 'ignore':
        return None
    elif errors == 'replace':
        if len(chars) > 1:
            return ''.join(text_type('%x' % ord(x)) for x in chars)
        else:
            return text_type('%x' % ord(chars))
```

当处理没有拼音的字符的时候，errors 的不同参数会有不同的处理结果，更详细的逻辑可以翻看源码。

```text
from pypinyin import lazy_pinyin
print(lazy_pinyin('你好☆☆，我是xxx', errors='ignore'))
```

运行结果：

```text
['ni', 'hao', 'wo', 'shi']
```

如果我们想要自定义处理，比如把 ☆ 转化为 ※，则可以这么设置：

```text
print(lazy_pinyin('你好☆☆，我是xxx', errors=lambda item: ''.join(['※' if c == '☆' else c for c in item])))
```

运行结果：

```text
['ni', 'hao', '※※，', 'wo', 'shi', 'xxx']
```

如上便是一些相关异常处理的操作，我们可以随心所欲地处理自己想处理的字符了。



## 自定义拼音

如果对库返回的结果不满意，我们还可以自定义自己的拼音库，这里用到的方法就有 load_single_dict 和 load_phrases_dict 方法了。

比如刚才我们看到 “朝阳” 两个字的发音默认返回的是 zhao yang，我们想默认返回 chao yang，那可以这么做：

```text
from pypinyin import lazy_pinyin, load_phrases_dict
print(lazy_pinyin('朝阳'))
personalized_dict = {
    '朝阳': [['cháo'], ['yáng']]
}
load_phrases_dict(personalized_dict)
print(lazy_pinyin('朝阳'))
```

这里我们自定义了一个词典，然后使用 load_phrases_dict 方法设置了一下就可以了。

运行结果：

```text
['zhao', 'yang']
['chao', 'yang']
```

这样就可以完成自定义的设置了。

在一些项目里面我们可以自定义很多拼音库，然后加载就可以了。

另外我们还可以注册样式实现自定义，比如将某个拼音前面加上 Emoji 表情，样例：

```text
from pypinyin import lazy_pinyin
from pypinyin.style import register

@register('kiss')
def kiss(pinyin, **kwargs):
    return '😘 {0}'.format(pinyin)

lazy_pinyin('么么', style='kiss')
```



## 命令行工具

程序内置了一个命令行工具 `pypinyin` :

```
$ pypinyin 音乐
yīn yuè
$ pypinyin -h
```

命令行工具支持如下参数：

```text
$ pypinyin -h
```

输出帮助信息
```text
usage: pypinyin [-h] [-V] [-f {pinyin,slug}]
                [-s {NORMAL,zhao,TONE,zh4ao,TONE2,zha4o,TONE3,zhao4,INITIALS,zh,FIRST_LETTER,z,FINALS,ao,FINALS_TONE,4ao,FINALS_TONE2,a4o,FINALS_TONE3,ao4,BOPOMOFO,BOPOMOFO_FIRST,CYRILLIC,CYRILLIC_FIRST}]
                [-p SEPARATOR] [-e {default,ignore,replace}] [-m]
                hans

convert chinese to pinyin.

positional arguments:
  hans                  chinese string

optional arguments:
  -h, --help            show this help message and exit
  -V, --version         show program's version number and exit
  -f {pinyin,slug}, --func {pinyin,slug}
                        function name (default: "pinyin")
  -s {NORMAL,zhao,TONE,zh4ao,TONE2,zha4o,TONE3,zhao4,INITIALS,zh,FIRST_LETTER,z,FINALS,ao,FINALS_TONE,4ao,FINALS_TONE2,a4o,FINALS_TONE3,ao4,BOPOMOFO,BOPOMOFO_FIRST,CYRILLIC,CYRILLIC_FIRST}, --style {NORMAL,zhao,TONE,zh4ao,TONE2,zha4o,TONE3,zhao4,INITIALS,zh,FIRST_LETTER,z,FINALS,ao,FINALS_TONE,4ao,FINALS_TONE2,a4o,FINALS_TONE3,ao4,BOPOMOFO,BOPOMOFO_FIRST,CYRILLIC,CYRILLIC_FIRST}
                        pinyin style (default: "zh4ao")
  -p SEPARATOR, --separator SEPARATOR
                        slug separator (default: "-")
  -e {default,ignore,replace}, --errors {default,ignore,replace}
                        how to handle none-pinyin string (default: "default")
  -m, --heteronym       enable heteronym
```



`-s`, `--style` 参数可以选值的含义如下：



| -s 或 –style 的值 | 对应的拼音风格                                               |
| :---------------- | :----------------------------------------------------------- |
| zhao              | [`NORMAL`](https://pypinyin.readthedocs.io/zh_CN/master/api.html#pypinyin.Style.NORMAL) |
| zh4ao             | [`TONE`](https://pypinyin.readthedocs.io/zh_CN/master/api.html#pypinyin.Style.TONE) |
| zha4o             | [`TONE2`](https://pypinyin.readthedocs.io/zh_CN/master/api.html#pypinyin.Style.TONE2) |
| zhao4             | [`TONE3`](https://pypinyin.readthedocs.io/zh_CN/master/api.html#pypinyin.Style.TONE3) |
| zh                | [`INITIALS`](https://pypinyin.readthedocs.io/zh_CN/master/api.html#pypinyin.Style.INITIALS) |
| z                 | [`FIRST_LETTER`](https://pypinyin.readthedocs.io/zh_CN/master/api.html#pypinyin.Style.FIRST_LETTER) |
| ao                | [`FINALS`](https://pypinyin.readthedocs.io/zh_CN/master/api.html#pypinyin.Style.FINALS) |
| 4ao               | [`FINALS_TONE`](https://pypinyin.readthedocs.io/zh_CN/master/api.html#pypinyin.Style.FINALS_TONE) |
| a4o               | [`FINALS_TONE2`](https://pypinyin.readthedocs.io/zh_CN/master/api.html#pypinyin.Style.FINALS_TONE2) |
| ao4               | [`FINALS_TONE3`](https://pypinyin.readthedocs.io/zh_CN/master/api.html#pypinyin.Style.FINALS_TONE3) |
| NORMAL            | [`NORMAL`](https://pypinyin.readthedocs.io/zh_CN/master/api.html#pypinyin.Style.NORMAL) |
| TONE              | [`TONE`](https://pypinyin.readthedocs.io/zh_CN/master/api.html#pypinyin.Style.TONE) |
| TONE2             | [`TONE2`](https://pypinyin.readthedocs.io/zh_CN/master/api.html#pypinyin.Style.TONE2) |
| TONE3             | [`TONE3`](https://pypinyin.readthedocs.io/zh_CN/master/api.html#pypinyin.Style.TONE3) |
| INITIALS          | [`INITIALS`](https://pypinyin.readthedocs.io/zh_CN/master/api.html#pypinyin.Style.INITIALS) |
| FIRST_LETTER      | [`FIRST_LETTER`](https://pypinyin.readthedocs.io/zh_CN/master/api.html#pypinyin.Style.FIRST_LETTER) |
| FINALS            | [`FINALS`](https://pypinyin.readthedocs.io/zh_CN/master/api.html#pypinyin.Style.FINALS) |
| FINALS_TONE       | [`FINALS_TONE`](https://pypinyin.readthedocs.io/zh_CN/master/api.html#pypinyin.Style.FINALS_TONE) |
| FINALS_TONE2      | [`FINALS_TONE2`](https://pypinyin.readthedocs.io/zh_CN/master/api.html#pypinyin.Style.FINALS_TONE2) |
| FINALS_TONE3      | [`FINALS_TONE3`](https://pypinyin.readthedocs.io/zh_CN/master/api.html#pypinyin.Style.FINALS_TONE3) |
| BOPOMOFO          | [`BOPOMOFO`](https://pypinyin.readthedocs.io/zh_CN/master/api.html#pypinyin.Style.BOPOMOFO) |
| BOPOMOFO_FIRST    | [`BOPOMOFO_FIRST`](https://pypinyin.readthedocs.io/zh_CN/master/api.html#pypinyin.Style.BOPOMOFO_FIRST) |
| CYRILLIC          | [`CYRILLIC`](https://pypinyin.readthedocs.io/zh_CN/master/api.html#pypinyin.Style.CYRILLIC) |
| CYRILLIC_FIRST    | [`CYRILLIC_FIRST`](https://pypinyin.readthedocs.io/zh_CN/master/api.html#pypinyin.Style.CYRILLIC_FIRST) |
