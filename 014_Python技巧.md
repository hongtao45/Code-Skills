# Python使用技巧

> 参考资料：
> 



## 高级循环

- 一般的遍历集合

  ```python
  data = ['John', 'Doe', 'was', 'here']
  
  # 不推荐
  idx = 0
  while idx < len(data):
      print(data[idx])
      idx += 1
  
      # 不推荐
  for idx in range(len(data)):
      print(data[idx])
  
  # 强烈推荐
  for item in data:
      print(item)
  
  for idx, val in enumerate(data):
      print('{}: {}'.format(idx, val))
  ```

- 反向遍历集合

  ```python
  # 不推荐
  i = len(data) - 1
  while i >= 0:
      print(data[i])
      i -= 1
  
  # 推荐
  for item in reversed(data):
      print(item)
  
  # 推荐
  for item in data[::-1]:
      print(item)
  ```

- 同时遍历n个集合

  ```python
  collection1 = ['a', 'b', 'c']
  collection2 = (10, 20, 30, 40, 50)
  collection3 = ['John', 'Doe', True]
  
  # 不推荐
  shortest = len(collection1)
  if len(collection2) < shortest:
      shortest = len(collection2)
  if len(collection3) < shortest:
      shortest = len(collection3)
      
  i = 0
  while i < shortest:
      print(collection1[i], collection2[i], collection3[i])
      i += 1
  
  shortest = min(len(collection1), len(collection2), len(collection3))
  for i in range(shortest):
      print(collection1[i], collection2[i], collection3[i])
      
  # 推荐
  for first, second, third in zip(collection1, collection2, collection3):
      print(first, second, third)
  
      
  # 使用zip 创建字典
  my_dict = dict(zip(collection1, collection2))
  print(my_dict)
  ```

  * `for - else` 

    检查集合中的匹配项

    假设我们要验证集合中的至少一个元素是否满足某个条件。 让我们考虑以下相对幼稚的示例，其中我们要验证 `data` 中至少一项是“python”（不区分大小写）。 如果没有，我们将引发 ValueError。

    ```python 
    # 不推荐
    found = False
    for val in data:
        if str(val).lower() == 'python':
            found = True
            break
    if not found:
        raise ValueError("Nope, couldn't find.")
    
    # 推荐
    for val in data:
        if str(val).lower() == 'python':
            break
    else:
        raise ValueError("Nope, couldn't find.")
    ```

## 高级字典

- 获取不存在的值

  ```python	
  my_dict = {'a': 1, 'b': 2, 'c': 3}
  
  # 不推荐
  if 'g' in my_dict:
      value = my_dict['g']
  else:
      value = 'some default value'
  print(value)
  # 推荐
  value = my_dict.get('g', 'some default value')
  print(value)
  
  value = my_dict.get('g')
  print(value is None) # 会返回None
  
  # 或者这样
  my_dict = {'a': 1, 'b': 2, 'c': 3}
  
  key = 'g'
  value = my_dict.setdefault(key, 'some default value')
  
  print(value)
  print(my_dict)
  ```

- 新建字典

  ```python
  # 推荐
  my_dict = {k: v for k, v in zip(keys, values)}
  print(my_dict)
  
  # 推荐:
  my_dict2 = dict(zip(keys, values))
  
  assert my_dict2 == my_dict
  
  # 推荐
  for key, val in my_dict.items():
      print('key: {:15s} value: {}'.format(key, val))
  ```

  
