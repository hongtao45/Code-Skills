# SUMO模块学习

## `import traci`

### 基本概念

- SUMO，全称Simulation of Urban Mobility，是开源、微观、多模态的交通仿真软件，发展始于2000年。它纯粹是微观的，可以针对每辆车进行单独控制，因此非常适合交通控制模型的开发。学习SUMO是一个趋势，但是会涉及路网文件、车辆文件等文件的编写，所以最好有些编程基础，在理解的基础上套用就足以实现一些简单的仿真。总结来说：

- SUMO有以下优点：

  1. 开源，容易获取

  2. 易提取车辆与道路信息

  3. 自带有很多跟驰模型和换道模型（如IDM、ACC、CACC跟驰模型）

  4. VISSIM无法进行模型的开发，而SUMO可以利用TraCI（(Traffic Control Interface)）接口用Python语言实现模型开发

  5. 可以导入VISUM, Vissim, Shapefiles, OSM, RoboCup, MATsim, OpenDRIVE, and XML-Descriptions（可导入地图）

-  SUMO的缺点

  1. 展示界面不美观
  2. 输入和输出都XML格式，比较麻烦

  2. 换道模型少（这点我没特殊感受）

  3. 新增或改变跟驰模型需要较难的操作

  

- 一个仿真，最少需要包含两个文件：
  map.rou.xml
  map.net.xml

  ```python
  sumo-gui -r map.rou.xml -n map.net.xml
  sumo -r map.rou.xml -n map.net.xml -C map.sumocfg
  ```

- 各个参数的含义：


### 使用示例
- 调用traci的一个完整的流程
    ```python 
    
    ```

- 如上代码，可以通过如下调用，然后得到具体的结果

  ```python
  
  ```
  
- python中，调用命令行来使用sumo 生成*.sumocfg等文件

  ```python
  
  ```
