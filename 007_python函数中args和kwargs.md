# 【Python】函数中的*args和**kwargs



> 参考资料：
>
> [【Python】函数中的*args和**kwargs是个什么东西？](https://zhuanlan.zhihu.com/p/479358658)



## 1. 概述

在Python代码中，经常见到函数中有*args和\*\*kwargs写法

它们都起到了**可选参数（optional arguments）**的作用。

那么具体怎么使用呢？且看下文细细分解

## 2. *和**

在了解\*args和\*\*kwargs的作用之前，首先要理解\*和\*\*在Python中的使用。\*和\*\*主要有三方面的用途:（一）是对可迭代对象进行拆分

（二）可变变量的赋值

（三）函数的可选参数标志。[[1\]](https://zhuanlan.zhihu.com/p/479358658#ref_1)

### 2.1 用于对可迭代对象进行拆分

在Python中，一切内置了\_\_iter\__方法的对象都是可迭代对象，

典型的可迭代对象包括元组（tuple）、列表（list）、集合（set）、字典（dict）等等。

这种拆解主要运用在函数的参数语境中，以print函数为例，以下5个表达式是完全等价的：

```python3
print("a", "b", "c")                
print(*("a", "b", "c"))             # 元组 
print(*["a", "b", "c"])             # 列表
print(*{"a": 1, "b": 2, "c": 3})    # 注意：对字典拆解时只拆解key
print(*"abc")                       # 注意：字符串也是可迭代对象
```

输出结果完全一样（如下）但是要注意的是，集合不太一样，因为集合是无序的，所以print(*{"a", "b", "c"})的时候"a", "b", "c"可能是乱序的。

```text
a b c
a b c
a b c
a b c
a b c
```

除了函数参数语境，赋值语境下也可以对可迭代对象进行拆分，如

```python3
a = *range(3),
b = *range(3), 3
c = [*range(3)]
d = {*range(3)}
e = {*{'y': 1}}     # 只对key进行拆解
f = {**{'y': 1}}    # 对key和value都进行了拆解


print(a)  # output: (0,1,2)
print(b)  # output: (0,1,2,3)
print(c)  # output: [0,1,2]
print(d)  # output: {0,1,2}
print(e)  # output: {'y'}
print(f)  # output: {'y':1}
```

**但是这种用法只能在元组、列表、集合和字典内部使用，其他地方就会报错**，比如

```python3
a = *range(3),   # 这么写默认是在元组内部，即等效于a = (*range(3), )
a = *range(3)    # 这么写就会报错
```

### 2.2 可变变量的赋值

如果对于一个可迭代对象l = [1, 2, 3, 4, 5, 6]，如果我想把第一个元素赋值给变量a，而把剩下的元素通通赋值给变量b，该怎么写呢？你可能会想这么写

```python3
l = [1, 2, 3, 4, 5, 6]
a = l[0]
b = l[1:]
```

这么写有两个问题：

- （一）设想一个更复杂的情况，如果我想把第一个元素赋值给变量a，最后一个元素赋值给c，而把剩下的元素统统赋值给变量b，那么代码将变得又臭又长；

- （二）这么写对于unsubscriptable的对象是不适用的，比如集合。

用*可以非常优雅地解决这个问题，如

```python3
a, *b, c = {1, 2, 3, 4, 5, 6}
```

### 2.3 函数的可选参数标志

理解了前面两点，这一点其实就是上面两点的综合运用。

如果是单星号\*标记的就是可选的位置参数（positional arguments）

如果是双星号\*\*标记的就是可选的关键词参数（keyword arguments），如

```python3
def function(a, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)

function(1, 2, 3, c=4)
```

输出结果如下

```text
$ python demo.py 
1
(2, 3)
{'c': 4}
```

## 3. args: positional arguments

args指的是可选的位置参数，这个东西有什么用呢？举个简单的例子我想自定义一个函数求两个元素的和，可以这么写

```python3
def my_sum_function(a, b):
    print(a + b)

my_sum_function(1, 2)
```

可是如果我想求三个元素的和呢，那是不是要这样写？

```python3
def my_sum_function(a, b, c):
    print(a + b + c)

my_sum_function(1, 2, 3)
```

你可能已经意识到了，就是这种写函数的思路扩展性非常差，对传入参数的个数有着严格的要求。\*args可以解决这一问题，如

```python3
def my_sum_function(*args):
    print(sum(args))

# 对于这个函数，不管传入多少个参数都是可以的
my_sum_function(1)
my_sum_function(1, 2)
my_sum_function(1, 2, 3)
```

## 4. kwargs: keyword arguments

- 既然已经有了可选的位置参数（args），还要可选的关键词参数（kwargs）干嘛呢？

- 关键词参数相当于给参数一个关键词，有着特定的用途，关键词对这个特殊用途进行标识。

- 由于需要关键词，因此kwargs的传入函数的类型是字典。

- 比如我想定义一个函数：这个函数计算传入参数的和，但是如果我传入的参数中包含分母（denominator），就会在这个和的基础上再除以分母。在这种情形下，这个分母（denominator）不一定需要，因此是可选参数。同时，有区别于其他的位置参数，因此需要加一个关键词。这个函数可以这么写

```python3
def self_defined_function(*args, **kwargs):
    if "denominator" not in kwargs:
        print(sum(args))
    else:
        # 注意：kwargs的类型是字典
        denominator = kwargs["denominator"]          
        print(sum(args) / denominator)

# 没有denominator时，打印几个数的和
self_defined_function(1, 2, 3)         
# 有denominator时，先求几个数的和，再除以denominator              
self_defined_function(1, 2, 3, denominator=3)        
```

当然，这个函数有更优雅的写法，就是用kwargs.get()或者kwargs.pop()，如

```python3
def self_defined_function(*args, **kwargs):
    denominator = kwargs.get("denominator", 1)
    print(sum(args) / denominator)

self_defined_function(1, 2, 3)
self_defined_function(1, 2, 3, denominator=3)
```

- kwargs.get("denominator", 1)会从kwargs这个字典中读取"denominator"这个key对应的值，如果没有这个key，就会返回1。这样写可以避免不断地写if else语句。

- kwargs.pop()与kwargs.get()不同的地方在于，kwargs.pop()读取某个key对应的值后，kwargs这个字典中的这个键值对就会被删除。

## 5. 注意

在Python中默认的函数参数顺序是：必选参数、默认参数、*args和**kwargs。如

```python3
def self_defined_function(name, purpose="Demo", *args, **kwargs):
    # name是必选参数
    # purpose是默认参数

    print("Name: ", name)
    print("Purpose: ", purpose)
    denominator = kwargs.pop("denominator", 1)
    print(sum(args) / denominator)

# 这里"Demo"不能少
self_defined_function("A self-defined function", "Demo", 1, 2, 3, denominator=3)   

```

在这种写法中，你会发现"Demo"不能少，如果少了"Demo"，purpose就变成了1。同时你又不能下面这样写，因为这样不符合传参的规范

```python3
# 不能这样写，这不符合传参的规范
self_defined_function("A self-defined function", purpose="Demo", 1, 2, 3, denominator=3)    
```

这样程序会报错。既然无论如何都必须要把"Demo"参数写出来，那么默认参数就失去了意义。

因此在Python3中放松了对顺序的限制[[2\]](https://zhuanlan.zhihu.com/p/479358658#ref_2)，**只要\**kwargs放在最后就行，剩下三个（必选参数、默认参数、\*args）的顺序不做严格规定**，因此上述问题就可以得到解决

```python3
def self_defined_function(name, *args, purpose="Demo", **kwargs):
    # name是必选参数
    # purpose是默认参数

    print("Name: ", name)
    print("Purpose: ", purpose)
    denominator = kwargs.pop("denominator", 1)
    print(sum(args) / denominator)

# 默认参数purpose终于不需要专门定义了
self_defined_function("A self-defined function", 1, 2, 3, denominator=3)  
```

