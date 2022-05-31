# Pandas中loc和iloc和isin函数用法



> 参考资料：
> [Pandas中loc和iloc函数用法](https://blog.csdn.net/W_weiying/article/details/81411257)



## Pandas中loc和iloc函数用法

- loc函数：通过行索引 "Index" 中的具体值来取行数据（如取"Index"为"A"的行）

- iloc函数：通过行号来取行数据（如取第二行的数据）



- loc、iloc常见的五种用法

  

1. 利用loc、iloc提取**行**数据 【只有一个参数的时候，是提取**行数据**

  ```python
  import numpy as np
  import pandas as pd
  
  # 创建一个Dataframe
  data=pd.DataFrame(np.arange(16).reshape(4,4),index=list('abcd'),columns=list('ABCD'))
  
  #
  In[1]: data
  Out[1]: 
      A   B   C   D
  a   0   1   2   3
  b   4   5   6   7
  c   8   9  10  11
  d  12  13  14  15
  #
  
  #取索引为'a'的行
  data.loc['a']
  #Out[2]:
  A    0
  B    1
  C    2
  D    3
  
  #取第一行数据，索引为'a'的行就是第一行，所以结果相同
  
  data.iloc[0]
  Out[3]:
  A    0
  B    1
  C    2
  D    3
  
  
  ```

  

2. 利用loc、iloc提取**列**数据 【第一个参数用 英文冒号 : 占领

  ```pytho
  data.loc[:,['A']] #取'A'列所有行，多取多列格式为 data.loc[:,['A','B']]
  Out[4]: 
  A
  a   0
  b   4
  c   8
  d  12
  
  data.iloc[:,[0]] #取第0列所有行，多取几列格式为 data.iloc[:,[0,1]]
  Out[5]: 
      A
  a   0
  b   4
  c   8
  d  12
  ```

  

3. 利用loc、iloc提取指定行、指定列数据

   ```python
   In[6]:data.loc[['a','b'],['A','B']] #提取index为'a','b',列名为'A','B'中的数据
      Out[6]: 
         A  B
      a  0  1
      b  4  5
   
   In[7]:data.iloc[[0,1],[0,1]] #提取第0、1行，第0、1列中的数据
   Out[7]: 
      A  B
   a  0  1
   b  4  5
   ```

   

4. 利用loc、iloc提取所有数据

   ```python
   #取A,B,C,D列的所有行
   data.loc[:,:] 
   Out[8]: 
       A   B   C   D
       a   0   1   2   3
       b   4   5   6   7
       c   8   9  10  11
       d  12  13  14  15
   
   #取第0,1,2,3列的所有行
   data.iloc[:,:] 
   Out[9]: 
       A   B   C   D
   a   0   1   2   3
   b   4   5   6   7
   c   8   9  10  11
   d  12  13  14  15
   
   ```

5. 利用loc函数，根据某个数据来提取数据所在的行

   ```python
   #提取data数据(筛选条件: A列中数字为0所在的行数据)
   data.loc[data['A']==0]
   Out[10]: 
       A  B  C  D
       a  0  1  2  3
   
   #提取data数据(多个筛选条件)
   data.loc[(data['A']==0)&(data['B']==2)] 
   Out[11]: 
       A  B  C  D
       a  0  1  2  3
   
   #同时，以下几种写法也可提取数据所在的行，与第五种用法类似，仅作补充。
   
   data[data['A']==0] #dataframe用法
   data[data['A'].isin([0])] #isin函数
   data[(data['A']==0)&(data['B']==2)] #dataframe用法
   data[(data['A'].isin([0]))&(data['B'].isin([2]))] #isin函数
   
   Out[15]: 
       A  B  C  D
       a  0  1  2  3
   ```

   

## Pandas中isin函数用法

```python

df=pd.DataFrame(np.random.randn(4,4),columns=['A','B','C','D'])
df['E']=['a','a','c','b']


df.E.isin(['a','c'])
df.isin(['b','c'])#整个df也同样适用


df.D=[0,1,0,2]
df[df.E.isin(['a','d'])&df.D.isin([0,])]
```

