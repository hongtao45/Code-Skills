# optparse模块学习

## `import optparse`

### 基本概念

-  `optparse`模块主要用来为脚本传递命令参数，采用预先定义好的选项来解析命令行参数。

-  首先需要引入optparser模块，然后执行初始化，

-  实例化一个OptionParser对象(可以带参，也可以不带参数)

- 再为命令行添加选项，[示例](https://blog.csdn.net/dcrmg/article/details/78045570)：

  ```python
  from optparse import OptionParser
  usage= " show something usefull -- for example: how to use this program"
  parser = OptionParser(usage) #带参的话会把参数变量的内容作为帮助信息输出
  # parser = OptionParser()
  parser.add_option("-f","--file",dest="filename",help="read picture from File",metavar="FILE",action="store",type="string")
  parser.add_option("-s","--save",dest="save_mold",help="save image to file or not", default = True)
  parser.add_option("-c","--cave",help="save image to file or not", default = True)
  
  fakeArgs =  ['-s','good luck to you', '-f', 'arg22', 'arge'] %函数中，运行脚本时，可以不用加，此处用作模拟
  options, args =parser.parse_args(fakeArgs)
  
  print (options.filename)
  print (options.save_mold)
  print(options.cave)
  print(options)
  print(args)
  ```

  

- 各个参数的含义：

| dest：   | 用于保存输入的临时变量，其值通过options的属性进行访问（options.filename），存储的内容是-f或 --file之后输入的参数<br>没有指定时，通过命令本省来访问：options.cave |
| -------- | ------------------------------------------------------------ |
| help：   | 用于生成帮助信息                                             |
| default: | 给dest的默认值，如果用户没有在命令行参数给dest分配值，则使用默认值 |
| type:    | 用于检查命令行参数传入的参数的数据类型是否符合要求，有string，int，float等类型 |
| action:  | 用于指导程序在遇到命令行参数时候该如何处理，有三种值可选： store,store_false和store_true,默认值是store |
| store：  | 读取参数，如果参数类型符合type的要求，则将参数值传递给dest变量，作为options的一个属性供使用。 <br/> `store_true/store_false`: 一般作为一个标记使用，分别设置dest变量的值为True和False |
|          |                                                              |
| metavar: | 占位字符串，用于在输出帮助信息时，代替当前命令选项的附加参数的值进行输出，只在帮助信息里有用，注意其和default的区别 |

  

- - **parse_args()说明:**

    - 如果没有传入参加，parse_args会默认将sys.argv[1:]的值作为默认参数。

    - 这里我们将  fakeArgs模拟输入的值

  

### 使用方法

