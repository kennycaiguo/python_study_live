# 21. collections

Python的集合（collections）模块，为很多用其他方法很难实现的场景提供了解决方案。本文我们将会学习该模块的抽象概念是如何产生的，日后处理不同问题的过程中迟早会用得到这些知识。

*免责声明：这篇文章是关于Python的一个相当高级的特性，如果你刚入门，建议先收藏，请等一等再学！*

*没想到这篇文章这么受欢迎， 修改优化下。*

## **一、模块概述**

## 1、模块作用

**官方说法：**collections模块实现了特定目标的容器，以提供Python标准内建容器dict ,list , set , 和tuple的替代选择。

**通俗说法：**Python内置的数据类型和方法，collections模块在这些内置类型的基础提供了额外的高性能数据类型，比如基础的字典是不支持顺序的，collections模块的OrderedDict类构建的字典可以支持顺序，collections模块的这些扩展的类用处非常大，熟练掌握该模块，可以大大简化Python代码，提高Python代码逼格和效率，**高手入门必备。**

## 2、模块资料

关于该模块，官方的参考资料写的非常详细，也很有价值，大家可以参考

中文文档：[https://docs.python.org/zh-cn/3/library/collections.html#module-collections](https://link.zhihu.com/?target=https%3A//docs.python.org/zh-cn/3/library/collections.html%23module-collections)

英文文档：[https://docs.python.org/3/library/collections.html#module-collections](https://link.zhihu.com/?target=https%3A//docs.python.org/3/library/collections.html%23module-collections)

## 3、模块子类

用collections.__all__查看所有的子类，一共包含9个

```python
import collections
print(collections.__all__)
['deque', 'defaultdict', 'namedtuple', 'UserDict', 'UserList', 
'UserString', 'Counter', 'OrderedDict', 'ChainMap']
```

这个模块实现了特定目标的容器，以提供Python标准内建容器dict , list , set , 和tuple 的替代选择。

| namedtuple() | 创建命名元组子类的工厂函数，生成可以使用名字来访问元素内容的tuple子类 |
| ------------ | ------------------------------------------------------------ |
| deque        | 类似列表(list)的容器，实现了在两端快速添加(append)和弹出(pop) |
| ChainMap     | 类似字典(dict)的容器类，将多个映射集合到一个视图里面         |
| Counter      | 字典的子类，提供了可哈希对象的计数功能                       |
| OrderedDict  | 字典的子类，保存了他们被添加的顺序，有序字典                 |
| defaultdict  | 字典的子类，提供了一个工厂函数，为字典查询提供一个默认值     |
| UserDict     | 封装了字典对象，简化了字典子类化                             |
| UserList     | 封装了列表对象，简化了列表子类化                             |
| UserString   | 封装了字符串对象，简化了字符串子类化（中文版翻译有误）       |

## **二、**计数器-**Counter**

## 1、基础介绍

一个计数器工具提供快速和方便的计数，Counter是一个dict的子类，用于**计数可哈希对象**。它是一个集合，元素像字典键(key)一样存储，它们的计数存储为值。计数可以是任何整数值，包括0和负数，Counter类有点像其他语言中的bags或multisets。简单说，就是可以统计计数，来几个例子看看就清楚了，比如

```python
#计算top10的单词
from collections import Counter
import re
text = 'remove an existing key one level down remove an existing key one level down'
words = re.findall(r'\w+', text)
Counter(words).most_common(10)
[('remove', 2),('an', 2),('existing', 2),('key', 2),('one', 2)('level', 2),('down', 2)] 


#计算列表中单词的个数
cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1
cnt
Counter({'red': 2, 'blue': 3, 'green': 1})


#上述这样计算有点嘛，下面的方法更简单，直接计算就行
L = ['red', 'blue', 'red', 'green', 'blue', 'blue'] 
Counter(L)
Counter({'red': 2, 'blue': 3, 'green': 1}
```

元素从一个iterable 被计数或从其他的mapping (or counter)初始化：

```python
from collections import Counter

#字符串计数
Counter('gallahad') 
Counter({'g': 1, 'a': 3, 'l': 2, 'h': 1, 'd': 1})

#字典计数
Counter({'red': 4, 'blue': 2})  
Counter({'red': 4, 'blue': 2})

#是个啥玩意计数
Counter(cats=4, dogs=8)
Counter({'cats': 4, 'dogs': 8})

Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
Counter({'red': 2, 'blue': 3, 'green': 1})
```

计数器对象除了字典方法以外，还提供了三个其他的方法：

## **1、elements()**

**描述：**返回一个迭代器，其中每个元素将重复出现计数值所指定次。 元素会按首次出现的顺序返回。 如果一个元素的计数值小于1，elements() 将会忽略它。

**语法：**elements( )

**参数：**无

```python
c = Counter(a=4, b=2, c=0, d=-2)
list(c.elements())
['a', 'a', 'a', 'a', 'b', 'b']

sorted(c.elements())
['a', 'a', 'a', 'a', 'b', 'b']

c = Counter(a=4, b=2, c=0, d=5)
list(c.elements())
['a', 'a', 'a', 'a', 'b', 'b', 'd', 'd', 'd', 'd', 'd']
```

## **2、most_common()**

返回一个列表，其中包含n个最常见的元素及出现次数，按常见程度由高到低排序。 如果 n 被省略或为None，most_common() 将返回计数器中的所有元素，计数值相等的元素按首次出现的顺序排序，经常用来计算top词频的词语。

```python
Counter('abracadabra').most_common(3)
[('a', 5), ('b', 2), ('r', 2)]

Counter('abracadabra').most_common(5)
[('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]
```

## **3、subtract()**

从迭代对象或映射对象减去元素。像dict.update() 但是是减去，而不是替换。输入和输出都可以是0或者负数。

```python
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
c
Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})

#减去一个abcd
str0 = Counter('aabbccdde')
str0
Counter({'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 1})

str0.subtract('abcd')
str0
Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1}
```

## **4、字典方法**

通常字典方法都可用于Counter对象，除了有两个方法工作方式与字典并不相同。

**fromkeys(iterable)**

这个类方法没有在Counter中实现。

**update([iterable-or-mapping])**

从迭代对象计数元素或者从另一个映射对象 (或计数器) 添加。 像 dict.update() 但是是加上，而不是替换。另外，迭代对象应该是序列元素，而不是一个 (key, value) 对。

```python
sum(c.values())                 # total of all counts
c.clear()                       # reset all counts
list(c)                         # list unique elements
set(c)                          # convert to a set
dict(c)                         # convert to a regular dictionary
c.items()                       # convert to a list of (elem, cnt) pairs
Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
c.most_common()[:-n-1:-1]       # n least common elements
+c                              # remove zero and negative counts
```

## **5、数学操作**

这个功能非常强大，提供了几个数学操作，可以结合 Counter 对象，以生产 multisets (计数器中大于0的元素）。 加和减，结合计数器，通过加上或者减去元素的相应计数。交集和并集返回相应计数的最小或最大值。每种操作都可以接受带符号的计数，但是输出会忽略掉结果为零或者小于零的计数。

```python
c = Counter(a=3, b=1)
d = Counter(a=1, b=2)
c + d                       # add two counters together:  c[x] + d[x]
Counter({'a': 4, 'b': 3})
c - d                       # subtract (keeping only positive counts)
Counter({'a': 2})
c & d                       # intersection:  min(c[x], d[x]) 
Counter({'a': 1, 'b': 1})
c | d                       # union:  max(c[x], d[x])
Counter({'a': 3, 'b': 2})
```

单目加和减（一元操作符）意思是从空计数器加或者减去。

```python
c = Counter(a=2, b=-4)
+c
Counter({'a': 2})
-c
Counter({'b': 4})
```

写一个计算文本相似的算法，加权相似

```python
def str_sim(str_0,str_1,topn):
    topn = int(topn)
    collect0 = Counter(dict(Counter(str_0).most_common(topn)))
    collect1 = Counter(dict(Counter(str_1).most_common(topn)))       
    jiao = collect0 & collect1
    bing = collect0 | collect1       
    sim = float(sum(jiao.values()))/float(sum(bing.values()))        
    return(sim)         

str_0 = '定位手机定位汽车定位GPS定位人定位位置查询'         
str_1 = '导航定位手机定位汽车定位GPS定位人定位位置查询'         

str_sim(str_0,str_1,5)    
0.75       
```

## **二、**双向队列-deque

双端队列，可以快速的从另外一侧追加和推出对象,deque是一个双向链表，针对list连续的数据结构插入和删除进行优化。它提供了两端都可以操作的序列，这表示在序列的前后你都可以执行添加或删除操作。双向队列(deque)对象支持以下方法：

## 1、append()

添加 x 到右端。

```python
d = deque('ghi')  
d.append('j') 
d
deque(['g', 'h', 'i', 'j'])
```

## 2、appendleft()

添加 x 到左端。

```python
d.appendleft('f')
d
deque(['f', 'g', 'h', 'i', 'j'])
```

## 3、clear()

移除所有元素，使其长度为0.

```python
d = deque('ghi')
d.clear()
d
deque([])
```

## 4、copy()

创建一份浅拷贝。

```python
d = deque('xiaoweuge')
y = d.copy()
print(y)
deque(['x', 'i', 'a', 'o', 'w', 'e', 'u', 'g', 'e'])
```

## 5、count()

计算 deque 中元素等于 *x* 的个数。

```python
d = deque('xiaoweuge-shuai')
d.count('a')
2
```

## 6、extend()

扩展deque的右侧，通过添加iterable参数中的元素。

```python
a = deque('abc')
b = deque('cd')
a.extend(b)
a
deque(['a', 'b', 'c', 'c', 'd'])

#与append 的区别
a = deque('abc')
b = deque('cd')
a.append(b)
deque(['a', 'b', 'c', deque(['c', 'd'])])
```

## 7、extendleft()

扩展deque的左侧，通过添加iterable参数中的元素。注意，左添加时，在结果中iterable参数中的顺序将被反过来添加。

```python
a = deque('abc')
b = deque('cd')
a.extendleft(b)
a
deque(['d', 'c', 'a', 'b', 'c'])
```

## 8、index()

返回 x 在 deque 中的位置（在索引 start 之后，索引 stop 之前）。 返回第一个匹配项，如果未找到则引发 ValueError。

```python
d = deque('xiaoweuge')
d.index('w')
4
```

## 9、insert()

在位置 i 插入 x 。

如果插入会导致一个限长 deque 超出长度 maxlen 的话，就引发一个 IndexError。

```python
a = deque('abc')
a.insert(1,'X')
deque(['a', 'X', 'b', 'c'])
```

## 10、pop()

移去并且返回一个元素，deque 最右侧的那一个。 如果没有元素的话，就引发一个 IndexError。

```python3
d.pop()      
'j'
```

## 11、popleft()

移去并且返回一个元素，deque 最左侧的那一个。 如果没有元素的话，就引发 IndexError。

```python
d.popleft()
'f'
```

## 12、remove(value)

移除找到的第一个 value。 如果没有的话就引发 ValueError。

```python
a = deque('abca')
a.remove('a')
a
deque(['b', 'c', 'a'])
```

## 13、reverse()

将deque逆序排列。返回 None 。

```python
#逆序排列
d = deque('ghi') # 创建一个deque
list(reversed(d))
['i', 'h', 'g']

deque(reversed(d))
deque(['i', 'h', 'g'])
```

## 14、rotate(n=1)

向右循环移动 n 步。 如果 n 是负数，就向左循环。

如果deque不是空的，向右循环移动一步就等价于 d.appendleft(d.pop()) ， 向左循环一步就等价于 d.append(d.popleft()) 。

```python
# 向右边挤一挤
d = deque('ghijkl')
d.rotate(1)                      
d
deque(['l', 'g', 'h', 'i', 'j', 'k'])

# 向左边挤一挤
d.rotate(-1)                     
d
deque(['g', 'h', 'i', 'j', 'k', 'l'])

#看一个更明显的
x = deque('12345')
x
deque(['1', '2', '3', '4', '5'])
x.rotate()
x
deque(['5', '1', '2', '3', '4'])

d = deque(['12','av','cd'])
d.rotate(1)
deque(['cd', '12', 'av'
```

## 15、maxlen

Deque的最大尺寸，如果没有限定的话就是 None 。

```python
from collections import deque
d=deque(maxlen=10)
for i in range(20):
   d.append(i)
d  
deque([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
```

除了以上操作，deque还支持迭代、封存、len(d)、reversed(d)、copy.deepcopy(d)、copy.copy(d)、成员检测运算符 in 以及下标引用例如通过 d[0] 访问首个元素等。 索引访问在两端的复杂度均为 O(1) 但在中间则会低至 O(n)。 如需快速随机访问，请改用列表。

Deque从版本3.5开始支持 __add__(), __mul__(), 和 __imul__() 。

```python
from collections import deque
d = deque('ghi')                 # 创建一个deque

for elem in d:
    print(elem.upper())
G
H
I

#从右边添加一个元素
d.append('j')
d   
deque(['g', 'h', 'i', 'j'])

#从左边添加一个元素
d.appendleft('f')
d 
deque(['f', 'g', 'h', 'i', 'j'])


#右边删除
d.pop()                          
'j'
#左边边删除
d.popleft()
'f'
#看看还剩下啥
list(d)                          # 
['g', 'h', 'i']
#成员检测
'h' in d                         
True
#添加多个元素
d.extend('jkl')              
d
deque(['g', 'h', 'i', 'j', 'k', 'l'])


d.clear()                        # empty the deque
d.pop()                          # cannot pop from an empty deque
Traceback (most recent call last):
    File "<pyshell#6>", line 1, in -toplevel-
        d.pop()
IndexError: pop from an empty deque


d.extendleft('abc')              # extendleft() reverses the input order
d
deque(['c', 'b', 
```

## **三、**有序字典-OrderedDict

有序词典就像常规词典一样，但有一些与排序操作相关的额外功能,popitem() 方法有不同的签名。它接受一个可选参数来指定弹出哪个元素。move_to_end() 方法，可以有效地将元素移动到任一端。

有序词典就像常规词典一样，但有一些与排序操作相关的额外功能。由于内置的 dict 类获得了记住插入顺序的能力（在 Python 3.7 中保证了这种新行为），它们变得不那么重要了。

一些与 dict 的不同仍然存在：

- 常规的 dict 被设计为非常擅长映射操作。 跟踪插入顺序是次要的。
- OrderedDict 旨在擅长重新排序操作。 空间效率、迭代速度和更新操作的性能是次要的。
- 算法上， OrderedDict 可以比 dict 更好地处理频繁的重新排序操作。 这使其适用于跟踪最近的访问（例如在 [LRU cache](https://link.zhihu.com/?target=https%3A//medium.com/@krishankantsinghal/my-first-blog-on-medium-583159139237) 中）。
- 对于 OrderedDict ，相等操作检查匹配顺序。
- OrderedDict 类的 popitem() 方法有不同的签名。它接受一个可选参数来指定弹出哪个元素。
- OrderedDict 类有一个 move_to_end() 方法，可以有效地将元素移动到任一端。
- Python 3.8之前， dict 缺少 __reversed__() 方法。

| 传统字典方法 | OrderedDict方法 | 差异                                                         |
| ------------ | --------------- | ------------------------------------------------------------ |
| clear        | clear           |                                                              |
| copy         | copy            |                                                              |
| fromkeys     | fromkeys        |                                                              |
| get          | get             |                                                              |
| items        | items           |                                                              |
| keys         | keys            |                                                              |
| pop          | pop             |                                                              |
| popitem      | popitem         | OrderedDict 类的 popitem() 方法有不同的签名。它接受一个可选参数来指定弹出哪个元素。 |
| setdefault   | setdefault      |                                                              |
| update       | update          |                                                              |
| values       | values          |                                                              |
|              | move_to_end     | 可以有效地将元素移动到任一端。                               |

## 1、popitem

语法：popitem(last=True)

功能：有序字典的 popitem() 方法移除并返回一个 (key, value) 键值对。 如果 last 值为真，则按 LIFO 后进先出的顺序返回键值对，否则就按 FIFO 先进先出的顺序返回键值对。

```python
from collections import OrderedDict
d = OrderedDict.fromkeys('abcde')
d.popitem()
 ('e', None)
d
OrderedDict([('a', None), ('b', None), ('c', None), ('d', None)])
#last=False时，弹出第一个
d = OrderedDict.fromkeys('abcde')
''.join(d.keys())
'abcde'
d.popitem(last=False)
''.join(d.keys())
'bcde'
```

## 2、move_to_end

```python
from collections import OrderedDict
d = OrderedDict.fromkeys('abcde')
d.move_to_end('b')
''.join(d.keys())
'acdeb'
d
OrderedDict([('a', None), ('c', None), ('d', None), ('e', None), ('b', None)])


d.move_to_end('b', last=False)
''.join(d.keys())
'bacde'
```

## 3、reversed()

相对于通常的映射方法，有序字典还另外提供了逆序迭代的支持，通过reversed() 。

```python
d = OrderedDict.fromkeys('abcde')
list(reversed(d))
['e', 'd', 'c', 'b', 'a']
```

## **四、**可命名元组-namedtuple

生成可以使用名字来访问元素内容的tuple子类，命名元组赋予每个位置一个含义，提供可读性和自文档性。它们可以用于任何普通元组，并添加了通过名字获取值的能力，通过索引值也是可以的。

## 1、参数介绍

**namedtuple(typename,field_names,\*,verbose=False, rename=False, module=None)**

1）typename：该参数指定所创建的tuple子类的类名，相当于用户定义了一个新类。

2）field_names：该参数是一个字符串序列，如 ['x'，'y']。此外，field_names 也可直接使用单个字符串代表所有字段名，多个字段名用空格、逗号隔开，如 'x y' 或 'x,y'。任何有效的 Python 标识符都可作为字段名（不能以下画线开头）。有效的标识符可由字母、数字、下画线组成，但不能以数字、下面线开头，也不能是关键字（如 return、global、pass、raise 等）。

3）rename：如果将该参数设为 True，那么无效的字段名将会被自动替换为位置名。例如指定 ['abc','def','ghi','abc']，它将会被替换为 ['abc', '_1','ghi','_3']，这是因为 def 字段名是关键字，而 abc 字段名重复了。

4）verbose：如果该参数被设为 True，那么当该子类被创建后，该类定义就被立即打印出来。

5）module：如果设置了该参数，那么该类将位于该模块下，因此该自定义类的 __module__ 属性将被设为该参数值。

## 2、应用案例

1）水族箱案例

Python元组是一个不可变的，或不可改变的，有序的元素序列。元组经常用来表示纵列数据;例如，一个CSV文件中的行数或一个SQL数据库中的行数。一个水族箱可以用一系列元组来记录它的鱼类的库存。

一个单独的鱼类元组:

![img](https://picx.zhimg.com/v2-efa2efb16a4e3a24b191bf866281836b_1440w.jpg)

这个元组由三个字符串元素组成。

虽然在某些方面很有用，但是这个元组并没有清楚地指明它的每个字段代表什么。实际上，元素0是一个名称，元素1是一个物种，元素2是一个饲养箱。

鱼类元组字段说明:

![img](https://pica.zhimg.com/v2-de3e2a13b4a1524a0b3cb42d18346ad4_1440w.jpg)

这个表清楚地表明，该元组的三个元素都有明确的含义。

来自collections模块的namedtuple允许你向一个元组的每个元素添加显式名称，以便在你的Python程序中明确这些元素的含义。

让我们使用namedtuple来生成一个类，从而明确地命名鱼类元组的每个元素:

![img](https://pic3.zhimg.com/v2-6feda1c80a14993793c335c93d667262_1440w.jpg)

```text
from collections import namedtuple 
```

可以让你的Python程序访问namedtuple工厂函数。namedtuple()函数调用会返回一个绑定到名称Fish的类。namedtuple()函数有两个参数:我们的新类“Fish”的期望名称和命名元素["name"、"species”、“tank"]的一个列表。

我们可以使用Fish类来表示前面的鱼类元组:

![img](https://pic4.zhimg.com/v2-e8975db7e7c2f9d0de2e1faa7427ba83_1440w.jpg)

如果我们运行这段代码，我们将看到以下输出:

![img](https://pic4.zhimg.com/v2-168252851c2344011745913d8b8330b7_1440w.jpg)

sammy是使用Fish类进行实例化的。sammy是一个具有三个明确命名元素的元组。

sammy的字段可以通过它们的名称或者一个传统的元组索引来访问:

![img](https://pic4.zhimg.com/v2-ba1c11aa62529004b8b20b5507c8b371_1440w.jpg)

如果我们运行这两个print调用，我们将看到以下输出:

![img](https://picx.zhimg.com/v2-0c90981e53acc01aac99f161467407cf_1440w.jpg)

访问.species会返回与使用[1]访问sammy的第二个元素相同的值。

使用collections模块中的namedtuple可以在维护元组(即它们是不可变的、有序的)的重要属性的同时使你的程序更具可读性。

此外，namedtuple工厂函数还会向Fish实例添加几个额外的方法。

使用._asdict()将一个实例转换为字典:

![img](https://pic3.zhimg.com/v2-6d8e3cd1dbf4186e0e24620b884bcf3c_1440w.jpg)

如果我们运行print，你会看到如下输出:

![img](https://picx.zhimg.com/v2-8f982aebadbbea91fffd8b63922813e3_1440w.jpg)

在sammy上调用.asdict()将返回一个字典，该字典会将三个字段名称分别映射到它们对应的值。

大于3.8的Python版本输出这一行的方式可能略有不同。例如，你可能会看到一个OrderedDict，而不是这里显示的普通字典。

**2）加法器案例**

```python
from collections import namedtuple
# 定义命名元组类：Point
Point = namedtuple('Point', ['x', 'y'])
# 初始化Point对象，即可用位置参数，也可用命名参数
p = Point(11, y=22)
# 像普通元组一样用根据索引访问元素
print(p[0] + p[1]) 
33
#执行元组解包，按元素的位置解包
a, b = p
print(a, b) 
11, 22
#根据字段名访问各元素
print(p.x + p.y) 
33
print(p) 
Point(x=11, y=22)
```

## 3、三个方法

备注: 在Python中，带有前导下划线的方法通常被认为是“私有的”。但是，namedtuple提供的其他方法(如._asdict()、._make()、._replace()等)是公开的。

除了继承元组的方法，命名元组还支持三个额外的方法和两个属性。为了防止字段名冲突，方法和属性以下划线开始。

### **_make(iterable)**

类方法从存在的序列或迭代实例创建一个新实例。

```python
t = [14, 55]
Point._make(t)
```

### **_asdict()**

返回一个新的 dict ，它将字段名称映射到它们对应的值：

```python
p = Point(x=11, y=22)
p._asdict()
OrderedDict([('x', 11), ('y', 22)])
```

### **_replace(\**kwargs)**

返回一个新的命名元组实例，并将指定域替换为新的值

```text
p = Point(x=11, y=22)
p._replace(x=33)

Point(x=33, y=22)
```

## 4、两个属性

**_fields**

字符串元组列出了字段名。用于提醒和从现有元组创建一个新的命名元组类型。

```python
p._fields            # view the field names
('x', 'y')
Color = namedtuple('Color', 'red green blue')
Pixel = namedtuple('Pixel', Point._fields + Color._fields)
Pixel(11, 22, 128, 255, 0)
Pixel(x=11, y=22, red=128, green=255, blue=0)
```

**_field_defaults**

字典将字段名称映射到默认值。

```python
Account = namedtuple('Account', ['type', 'balance'], defaults=[0])
Account._field_defaults
{'balance': 0}
Account('premium')
Account(type='premium', balance=0)
```

## 5、其他函数

**getattr()**

要获取这个名字域的值，使用 getattr() 函数 :

```python
getattr(p, 'x')
11
```

转换一个字典到命名元组，使用 ** 两星操作符

```python3
d = {'x': 11, 'y': 22}
Point(**d)
Point(x=11, y=22)
```

因为一个命名元组是一个正常的Python类，它可以很容易的通过子类更改功能。这里是如何添加一个计算域和定宽输出打印格式:

```python
class Point(namedtuple('Point', ['x', 'y'])):
    __slots__ = ()
    @property
    def hypot(self):        
        return (self.x ** 2 + self.y ** 2) ** 0.5
    def __str__(self):
        return 'Point: x=%6.3f  y=%6.3f  hypot=%6.3f' % (self.x, self.y, self.hypot)
for p in Point(3, 4), Point(14, 5/7):
     print(p)
Point: x= 3.000  y= 4.000  hypot= 5.000
Point: x=14.000  y= 0.714  hypot=14.018
```

## **五、**默认字典-defaultdict

在Python字典中收集数据通常是很有用的。

在字典中获取一个 key 有两种方法, 第一种 get , 第二种 通过 [] 获取.

**使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict。**

当我使用普通的字典时，用法一般是dict={},添加元素的只需要dict[element] =value即，调用的时候也是如此，dict[element] = xxx,但前提是element字典里，如果不在字典里就会报错

这时defaultdict就能排上用场了，defaultdict的作用是在于，当字典里的key不存在但被查找时，返回的不是keyError而是一个默认值，这个默认值是什么呢，下面会说

## 1、基础介绍

**defaultdict([default_factory[, ...]])**

返回一个新的类似字典的对象。 defaultdict是内置dict类的子类。它重载了一个方法并添加了一个可写的实例变量。其余的功能与dict类相同，此处不再重复说明。

本对象包含一个名为default_factory的属性，构造时，第一个参数用于为该属性提供初始值，默认为 None。所有其他参数（包括关键字参数）都相当于传递给 dict 的构造函数。

defaultdict 对象除了支持标准 dict 的操作，还支持以下方法作为扩展：

**__missing__(key)**

如果 default_factory 属性为 None，则调用本方法会抛出 KeyError 异常，附带参数 key。

如果 default_factory 不为 None，则它会被（不带参数地）调用来为 key 提供一个默认值，这个值和 key 作为一对键值对被插入到字典中，并作为本方法的返回值返回。

如果调用 default_factory 时抛出了异常，这个异常会原封不动地向外层传递。

在无法找到所需键值时，本方法会被 dict 中的 __getitem__() 方法调用。无论本方法返回了值还是抛出了异常，都会被 __getitem__() 传递。

注意，__missing__() 不会 被 __getitem__() 以外的其他方法调用。意味着 get() 会像正常的 dict 那样返回 None，而不是使用 default_factory。

## 2、示例介绍

使用 list 作为 default_factory，很轻松地将（键-值对组成的）序列转换为（键-列表组成的）字典

```python
s  = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)


sorted(d.items())
[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
```

当每个键第一次遇见时，它还没有在字典里面，所以自动创建该条目，即调用default_factory方法，返回一个空的 list。 list.append() 操作添加值到这个新的列表里。当再次存取该键时，就正常操作，list.append() 添加另一个值到列表中。这个计数比它的等价方法dict.setdefault()要快速和简单：

```python
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = {}
for k, v in s:
    d.setdefault(k, []).append(v)


sorted(d.items())
[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
```

设置 default_factory为int，使defaultdict用于计数（类似其他语言中的 bag或multiset）：

```python
s = 'mississippi'
d = defaultdict(int)
for k in s:
    d[k] += 1
sorted(d.items())
 [('i', 4), ('m', 1), ('p', 2), ('s', 4)]
```

设置 default_factory 为 set 使 defaultdict 用于构建 set 集合：

```python
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = defaultdict(set)
for k, v in s:
    d[k].add(v)


sorted(d.items())
[('blue', {2, 4}), ('red', {1, 3})]
```

defaultdict绝不会引发一个KeyError。如果一个键不存在，defaultdict会插入并返回一个占位符值来代替:

![img](https://pic3.zhimg.com/v2-e9411272b33c99cdfe9b78c9d03f9b90_1440w.jpg)

如果我们运行这段代码，我们将看到如下输出:

![img](https://pic3.zhimg.com/v2-520a3b53ca349a4c1e821d044d850dce_1440w.jpg)

defaultdict会插入并返回一个占位符值，而不是引发一个KeyError。在本例中，我们将占位符值指定为一个列表。

相比之下，常规字典会在缺失的键上引发一个KeyError:

![img](https://picx.zhimg.com/v2-76d68d5bc235feea862299e4159a0ce5_1440w.jpg)

如果我们运行这段代码，我们将看到如下输出:

![img](https://pic3.zhimg.com/v2-520a3b53ca349a4c1e821d044d850dce_1440w.jpg)

当我们试图访问一个不存在的键时，常规字典my_regular_dict会引发一个KeyError。

defaultdict的行为与常规字典不同。defaultdict会不带任何参数调用占位符值来创建一个新对象，而不是在缺失的键上引发一个KeyError。在本例中，是调用list()创建一个空列表。

继续我们虚构的水族箱示例，假设我们有一个表示水族箱清单的鱼类元组列表:

![img](https://pica.zhimg.com/v2-3c82b2b94a06a00daee8ee56f0a3b722_1440w.jpg)

水族箱中有三种鱼——它们的名字、种类和饲养箱在这三个元组中都有指出。

我们的目标是按饲养箱组织我们的清单—我们想知道每个饲养箱中存在的鱼的列表。换句话说，我们需要一个能将“tank-a”映射到["Jamie", "Mary"] ，并且将“tank-b”映射到["Jamie"]的字典。

我们可以使用defaultdict来按饲养箱对鱼进行分组:

![img](https://pic4.zhimg.com/v2-dfc8d0750c881756d3bd6c6335c5e08f_1440w.jpg)

运行这段代码，我们将看到以下输出:

![img](https://pic2.zhimg.com/v2-ef4f16054ebda651b702ca60191c880f_1440w.jpg)

fish_names_by_tank被声明为一个defaultdict，它默认会插入list()而不是引发一个KeyError。由于这保证了fish_names_by_tank中的每个键都将指向一个list，所以我们可以自由地调用.append()来将名称添加到每个饲养箱的列表中。

这里，defaultdict帮助你减少了出现未预期的KeyErrors的机会。减少未预期的KeyErrors意味着你可以用更少的行更清晰地编写你的程序。更具体地说，defaultdict习惯用法让你避免了手动地为每个饲养箱实例化一个空列表。

如果没有 defaultdict, for循环体可能看起来更像这样:

![img](https://pic2.zhimg.com/v2-61edd6a75a4588ea47ffb8bce558f4cd_1440w.jpg)

使用常规字典(而不是defaultdict)意味着for循环体总是必须检查fish_names_by_tank中给定的tank是否存在。只有在验证了fish_names_by_tank中已经存在tank，或者已经使用一个[]初始化了tank之后，我们才可以添加鱼类名称。

在填充字典时，defaultdict可以帮助我们减少样板代码，因为它从不引发KeyError。

## 六、映射链-ChainMap

## 1、ChainMap是什么

ChainMap最基本的使用，可以用来合并两个或者更多个字典，当查询的时候，从前往后依次查询。

**ChainMap：将多个字典视为一个，解锁Python超能力。**

ChainMap是由Python标准库提供的一种数据结构，允许你将多个字典视为一个。换句话说:**ChainMap是一个基于多dict的可更新的视图，它的行为就像一个普通的dict。**

ChainMap类用于快速链接多个映射，以便将它们视为一个单元。它通常比创建新字典和多次调用update()快得多。

你以前可能从来没有听说过ChainMap，你可能会认为ChainMap的使用情况是非常特定的。坦率地说，你是对的。

我知道的用例包括：

- 通过多个字典搜索
- 提供链缺省值
- 经常计算字典子集的性能关键的应用程序

## 2、特性

1）找到一个就不找了：这个列表是按照第一次搜索到最后一次搜索的顺序组织的，搜索查询底层映射，直到一个键被找到。

2）更新原始映射：不同的是，写，更新和删除只操作第一个映射。

3）支持所有常用字典方法。

简而言之ChainMap：将多个字典视为一个，解锁Python超能力。

Python标准库中的集合模块包含许多为性能而设计的实用的数据结构。著名的包括命名元组或计数器。

今天，通过实例，我们来看看鲜为人知的**ChainMap**。通过浏览具体的示例，我希望给你一个提示，关于在更高级的Python工作中使用ChainMap将如何从中受益。

## 3、应用案例-基础案例

```python
from collections import ChainMap 
baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
ChainMap(adjustments, baseline)
ChainMap({'art': 'van gogh', 'opera': 'carmen'}, {'music': 'bach', 'art': 'rembrandt'})
list(ChainMap(adjustments, baseline))
['music', 'art', 'opera']
#存在重复元素时，也不会去重
dcic1 = {'label1': '11', 'label2': '22'}
dcic2 = {'label2': '22', 'label3': '33'}
dcic3 = {'label4': '44', 'label5': '55'}
last  = ChainMap(dcic1, dcic2,dcic3)
last  
ChainMap({'label1': '11', 'label2': '22'}, {'label2': '22', 'label3': '33'}, {'label4': '44', 'label5': '55'})
```

### **new_child()方法**

用法：new_child(m=None)

返回一个新的ChainMap类，包含了一个新映射(map)，后面跟随当前实例的全部映射map。如果m被指定，它就成为不同新的实例，就是在所有映射前加上 m，如果没有指定，就加上一个空字典，这样的话一个 d.new_child() 调用等价于ChainMap({}, *d.maps) 。这个方法用于创建子上下文，不改变任何父映射的值。

```python
last.new_child(m={'key_new':888})
ChainMap({'key_new': 888}, {'label1': '11', 'label2': '22'}, {'label2': '22', 'label3': '33'},
 {'label4': '44', 'label5': '55'})
```

### **parents属性**

属性返回一个新的ChainMap包含所有的当前实例的映射，除了第一个。这样可以在搜索的时候跳过第一个映射。使用的场景类似在 [nested scopes](https://link.zhihu.com/?target=https%3A//docs.python.org/zh-cn/3/glossary.html%23term-nested-scope) 嵌套作用域中使用nonlocal关键词。用例也可以类比内建函数super() 。一个d.parents 的引用等价于ChainMap(*d.maps[1:]) 。

```python
last.parents
ChainMap({'label2': '22', 'label3': '33'}, {'label4': '44', 'label5': '55'})
```

## 4、应用案例-购物清单

作为使用ChainMap的第一个例子，让我们考虑一张购物清单。我们的清单可能包含玩具，电脑，甚至衣服。所有这些条目都有价格，所以我们将把我们的条目存储在名称价格映射中。

```adl
toys = {'Blocks':30,'Monopoly':20}
computers = {'iMac':1000,'Chromebook':1000,'PC':400}
clothing = {'Jeans':40,'T-shirt':10}
```

现在我们可以使用ChainMap在这些不同的集合上建立一个单一的视图：

```text
from collections import ChainMap
inventory = ChainMap(toys,computers,clothing)
```

这使得我们可以查询清单，就像它是一个单一的字典：

```text
inventory['Monopoly']
20
inventory['Jeans']40
```

正如官方文档所述，ChainMap支持所有常用的字典方法。我们可以使用.get()来搜索可能不存在的条目，或者使用 .pop()删除条目。

```text
inventory.get('Blocks-1')
None
inventory.get('Chromebook')
1000
inventory.pop('Blocks')
inventory
ChainMap({'Monopoly': 20}, {'iMac': 1000, 'Chromebook': 1000, 'PC': 400}, {'Jeans': 40, 'T-shirt': 10})
```

如果我们现在把玩具添加到toys字典里，它也将在清单中可用。这是ChainMap的可更新的方面。

```text
toys['Nintendo'] = 20
inventory['Nintendo']
20
```

Oh和ChainMap有一个恰当的字符串表示形式：

```text
str(inventory)
"ChainMap({'Monopoly': 20, 'Nintendo': 20}, {'iMac': 1000, 'Chromebook': 1000, 'PC': 400}, {'Jeans': 40, 'T-shirt': 10})"
```

一个很好的特点是，在我们的例子中，toys, computers和clothing都是在相同的上下文中（解释器），它们可以来自完全不同的模块或包。这是因为ChainMap通过引用存储底层字典。

第一个例子是使用ChainMap一次搜索多个字典。

事实上，当构建ChainMap时，我们所做的就是有效地构建一系列字典。当查找清单中的一个项时，toys首先被查找，然后是computers，最后是clothing。



![img](https://pic3.zhimg.com/v2-d679e081f5420e6fb13b2daef2feaee4_1440w.jpg)



*ChainMap真的只是一个映射链！*

**实际上，ChainMap的另一个任务是维护链的默认值。**

我们将以一个命令行应用程序的例子来说明这是什么意思。

## 5、应用案例-CLI配置

让我们面对现实，管理命令行应用程序的配置可能是困难的。配置来自多个源：命令行参数、环境变量、本地文件等。

我们通常实施**优先级**的概念：如果A和B都定义参数P，A的P值将被使用，因为它的优先级高于B。

例如，如果传递了命令行参数，我们可能希望在环境变量上使用命令行参数。如何轻松地管理配置源的优先级？

一个答案是将所有配置源存储在ChainMap中。

**因为ChainMap中的查找是按顺序连续地对每个底层映射执行的**（按照他们传给构造函数的顺序），所以我们可以很容易地实现我们寻找的优先级。

下面是一个简单的命令行应用程序。调试参数从命令行参数、环境变量或硬编码默认值中提取：

![img](https://pic4.zhimg.com/v2-c69ecbd6433f66bb29a25079a89ad8fb_1440w.jpg)

在执行脚本时，我们可以检查是否首先在命令行参数中查找debug，然后是环境变量，最后是默认值：

![img](https://pic4.zhimg.com/v2-0f9bcf49cd958ec597af013c8b5bc7bd_1440w.jpg)



这样看上去就非常整洁，对吧？

## 6、我为什么关心？

坦率地说，ChainMap是那些你可以忽略的Python特性之一。

还有其他ChainMap的替代方案。例如，使用更新循环—例如创建一个dict并用字典update()它—可能奏效。但是，这只有在您不需要跟踪项目的起源时才有效，就像我们的多源CLI配置示例中的情况一样。**但是，当你知道ChainMap存在的时候，ChainMap可以让你更轻松，你的代码更优雅。**

## 7、总结

总而言之，我们一起看了ChainMap是什么，一些具体的使用示例，以及如何在现实生活中，性能关键的应用程序中使用ChainMap。如果您想了解更多关于Python的高性能数据容器的信息，请务必从Python的标准库中collections模块中查看其他出色类和函数。

## 七、UserDict

UserDict类是用作字典对象的外包装。对这个类的需求已部分由直接创建dict的子类的功能所替代；不过这个类处理起来更容易，因为底层的字典可以作为属性来访问。

模拟一个字典类。这个实例的内容保存为一个正常字典，可以通过UserDict实例的data属性存取。如果提供了initialdata 值， data 就被初始化为它的内容，注意一个 initialdata 的引用不会被保留作为其他用途。

UserDict 实例提供了以下属性作为扩展方法和操作的支持:data一个真实的字典，用于保存 UserDict 类的内容。

## 八、UserList

这个类封装了列表对象。它是一个有用的基础类，对于你想自定义的类似列表的类，可以继承和覆盖现有的方法，也可以添加新的方法。这样我们可以对列表添加新的行为。

对这个类的需求已部分由直接创建 list 的子类的功能所替代；不过，这个类处理起来更容易，因为底层的列表可以作为属性来访问。

模拟一个列表。这个实例的内容被保存为一个正常列表，通过 UserList 的 data 属性存取。实例内容被初始化为一个 list 的copy，默认为 [] 空列表。 list可以是迭代对象，比如一个Python列表，或者一个UserList 对象。

UserList 提供了以下属性作为可变序列的方法和操作的扩展:data

一个 list 对象用于存储 UserList 的内容。

子类化的要求: UserList 的子类需要提供一个构造器，可以无参数调用，或者一个参数调用。返回一个新序列的列表操作需要创建一个实现类的实例。它假定了构造器可以以一个参数进行调用，这个参数是一个序列对象，作为数据源。

如果一个分离的类不希望依照这个需求，所有的特殊方法就必须重写；请参照源代码进行修改。

## 九、UserString

UserString类是用作字符串对象的外包装。对这个类的需求已部分由直接创建str的子类的功能所替代，不过这个类处理起来更容易，因为底层的字符串可以作为属性来访问。

模拟一个字符串对象。这个实例对象的内容保存为一个正常字符串，通过UserString的data属性存取。实例内容初始化设置为seq的copy。seq 参数可以是任何可通过内建str()函数转换为字符串的对象。

UserString 提供了以下属性作为字符串方法和操作的额外支持：data一个真正的str对象用来存放 UserString 类的内容。





# 22. functools

### 参考链接： https://zhuanlan.zhihu.com/p/696908076

Python的`functools`模块提供了一系列用于高阶函数（操作或返回其他函数的函数）的工具，能显著简化代码并优化性能。它是函数式编程范式的核心组件，尤其适用于装饰器、缓存和函数组合等场景。

![image-20260502073216810](./built-in-modules2.assets/image-20260502073216810.png)

------

### 1. 使用functools.lru_cache实现智能缓存

`lru_cache`是最常用的缓存装饰器，通过LRU（最近最少使用）算法存储函数结果，避免重复计算。适用于I/O密集型或递归函数。

```python
from functools import lru_cache

@lru_cache(maxsize=128)  # 缓存最近128次调用结果
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(50))  # 秒级计算，无缓存时需指数级时间
```

**关键词**：缓存装饰器、性能优化、递归函数加速

------

### 2. 用functools.partial简化函数参数

`partial`（偏函数）允许固定函数的部分参数，生成新函数。适用于接口适配或参数预设场景。

```python
from functools import partial

def power(base, exponent):
    return base ** exponent

# 固定exponent=2，创建平方函数
square = partial(power, exponent=2)  
print(square(5))  # 输出25
```

**优势**：减少重复参数传递，提升代码可读性。

------

### 3. functools.reduce处理累积计算

`reduce`对可迭代对象逐元素应用函数并累积结果，是MapReduce模型的简化实现。

```python
from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)  # 1*2*3*4=24
```

**适用场景**：聚合统计、链式计算（替代多层循环）。

------

### 4. 用@total_ordering自动生成比较方法

只需定义`__eq__`和`__lt__`，此装饰器会自动补全其他比较方法（如`__gt__`），减少样板代码。

```python
from functools import total_ordering

@total_ordering
class Student:
    def __init__(self, grade):
        self.grade = grade

    def __eq__(self, other):
        return self.grade == other.grade

    def __lt__(self, other):
        return self.grade < other.grade

# 自动支持 >, <=, >= 等操作
print(Student(85) > Student(80))  # True
```

------

### 5. functools.wraps保留函数元信息

修复装饰器的副作用：确保被装饰函数保留原始名称(`__name__`)和文档字符串(`__doc__`)。

```python
from functools import wraps

def logger(func):
    @wraps(func)  # 保留func的元信息
    def wrapper(*args, **kwargs):
        print(f"调用函数: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
def calculate(x):
    """返回平方值"""
    return x * x

print(calculate.__name__)  # 输出"calculate"而非"wrapper"
```

# 23. threading

### 参考网址1： https://zhuanlan.zhihu.com/p/824873590

### 参考网址2：https://www.cnblogs.com/zoubilin/p/18215670

### 参考网址3： https://www.runoob.com/python3/python-treading.html

### 参考网址4： https://medium.com/@me.mdhamim/a-comprehensive-guide-to-python-threading-advanced-concepts-and-best-practices-9f3aea6f0a63

# 24. multiprocessing

## 一篇文章搞定Python多进程(全)

前面写了三篇关于python多线程的文章，大概概况了多线程使用中的方法，文章链接如下：

一篇文章搞懂Python多线程简单实现和[GIL](https://zhida.zhihu.com/search?content_id=102507664&content_type=Article&match_order=1&q=GIL&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzgwMDUzODYsInEiOiJHSUwiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoxMDI1MDc2NjQsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.NTStW_L5MOq149XdFD3gD5QXDLDdCX70UPb-ZRDbNsM&zhida_source=entity) - [https://mp.weixin.qq.com/s/Hgp-x-T3ss4IiVk2_4VUrA](https://link.zhihu.com/?target=https%3A//mp.weixin.qq.com/s/Hgp-x-T3ss4IiVk2_4VUrA)
一篇文章理清Python多线程同步锁，死锁和递归锁 - [https://mp.weixin.qq.com/s/RZSBe2MG9tsbUVZLHxK9NA](https://link.zhihu.com/?target=https%3A//mp.weixin.qq.com/s/RZSBe2MG9tsbUVZLHxK9NA)
一篇文章理清Python多线程之同步条件，信号量和队列 - [https://mp.weixin.qq.com/s/vKsNbDZnvg6LHWVA-AOIMA](https://link.zhihu.com/?target=https%3A//mp.weixin.qq.com/s/vKsNbDZnvg6LHWVA-AOIMA)

今天开始会开启python多进程的内容，大家看过前面文章的应该都知道python中的GIL的存在，也就是多线程的时候，同一时间只能有一个线程在CPU上运行，而且是单个CPU上运行，不管你的CPU有多少核数。如果想要充分地使用多核CPU的资源，在python中大部分情况需要使用多进程。

### **1.Python多进程模块**

Python中的多进程是通过[multiprocessing](https://zhida.zhihu.com/search?content_id=102507664&content_type=Article&match_order=1&q=multiprocessing&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzgwMDUzODYsInEiOiJtdWx0aXByb2Nlc3NpbmciLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoxMDI1MDc2NjQsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.YHJ115IIsyvscM9JF9sNJHEE6W5YRAnfBnBzaJ9lrmc&zhida_source=entity)包来实现的，和多线程的threading.Thread差不多，它可以利用multiprocessing.[Process](https://zhida.zhihu.com/search?content_id=102507664&content_type=Article&match_order=1&q=Process&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzgwMDUzODYsInEiOiJQcm9jZXNzIiwiemhpZGFfc291cmNlIjoiZW50aXR5IiwiY29udGVudF9pZCI6MTAyNTA3NjY0LCJjb250ZW50X3R5cGUiOiJBcnRpY2xlIiwibWF0Y2hfb3JkZXIiOjEsInpkX3Rva2VuIjpudWxsfQ.CKr0p4m7CZ1_jHa7_XkR7YucYUP5ZRYtGnOrpwCSShM&zhida_source=entity)对象来创建一个进程对象。这个进程对象的方法和线程对象的方法差不多也有start(), run(), join()等方法，其中有一个方法不同Thread线程对象中的守护线程方法是setDeamon，而Process进程对象的守护进程是通过设置daemon属性来完成的。

下面说说Python多进程的实现方法，和多线程类似

### **2.Python多进程实现方法一**

```text
from multiprocessing import  Process

def fun1(name):
    print('测试%s多进程' %name)

if __name__ == '__main__':
    process_list = []
    for i in range(5):  #开启5个子进程执行fun1函数
        p = Process(target=fun1,args=('Python',)) #实例化进程对象
        p.start()
        process_list.append(p)

    for i in process_list:
        p.join()

    print('结束测试')
```

结果

```text
测试Python多进程
测试Python多进程
测试Python多进程
测试Python多进程
测试Python多进程
结束测试

Process finished with exit code 0
```

上面的代码开启了5个子进程去执行函数，我们可以观察结果，是同时打印的，这里实现了真正的并行操作，就是多个CPU同时执行任务。我们知道进程是python中最小的资源分配单元，也就是进程中间的数据，内存是不共享的，每启动一个进程，都要独立分配资源和拷贝访问的数据，所以进程的启动和销毁的代价是比较大了，所以在实际中使用多进程，要根据服务器的配置来设定。

### **3.Python多进程实现方法二**

还记得python多线程的第二种实现方法吗?是通过类继承的方法来实现的，python多进程的第二种实现方式也是一样的

```text
from multiprocessing import  Process

class MyProcess(Process): #继承Process类
    def __init__(self,name):
        super(MyProcess,self).__init__()
        self.name = name

    def run(self):
        print('测试%s多进程' % self.name)


if __name__ == '__main__':
    process_list = []
    for i in range(5):  #开启5个子进程执行fun1函数
        p = MyProcess('Python') #实例化进程对象
        p.start()
        process_list.append(p)

    for i in process_list:
        p.join()

    print('结束测试')
```

结果

```text
测试Python多进程
测试Python多进程
测试Python多进程
测试Python多进程
测试Python多进程
结束测试

Process finished with exit code 0
```

效果和第一种方式一样。

我们可以看到Python多进程的实现方式和多线程的实现方式几乎一样。

### **Process类的其他方法**

```text
构造方法：

Process([group [, target [, name [, args [, kwargs]]]]])
　　group: 线程组 
　　target: 要执行的方法
　　name: 进程名
　　args/kwargs: 要传入方法的参数

实例方法：
　　is_alive()：返回进程是否在运行,bool类型。
　　join([timeout])：阻塞当前上下文环境的进程程，直到调用此方法的进程终止或到达指定的timeout（可选参数）。
　　start()：进程准备就绪，等待CPU调度
　　run()：strat()调用run方法，如果实例进程时未制定传入target，这star执行t默认run()方法。
　　terminate()：不管任务是否完成，立即停止工作进程

属性：
　　daemon：和线程的setDeamon功能一样
　　name：进程名字
　　pid：进程号
```

关于join，daemon的使用和python多线程一样，这里就不在复述了，大家可以看看以前的python多线程系列文章。

### **4.Python多线程的通信**

进程是系统独立调度核分配系统资源（CPU、内存）的基本单位，进程之间是相互独立的，每启动一个新的进程相当于把数据进行了一次克隆，子进程里的数据修改无法影响到主进程中的数据，不同子进程之间的数据也不能共享，这是多进程在使用中与多线程最明显的区别。但是难道Python多进程中间难道就是孤立的吗？当然不是，python也提供了多种方法实现了多进程中间的通信和数据共享（可以修改一份数据）

### **进程对列[Queue](https://zhida.zhihu.com/search?content_id=102507664&content_type=Article&match_order=1&q=Queue&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzgwMDUzODYsInEiOiJRdWV1ZSIsInpoaWRhX3NvdXJjZSI6ImVudGl0eSIsImNvbnRlbnRfaWQiOjEwMjUwNzY2NCwiY29udGVudF90eXBlIjoiQXJ0aWNsZSIsIm1hdGNoX29yZGVyIjoxLCJ6ZF90b2tlbiI6bnVsbH0.ZyVPR3pyXwdOZtj9Dvfd0yciDZ_yZj_m9PyhF3K5nzY&zhida_source=entity)**

Queue在多线程中也说到过，在生成者消费者模式中使用，是线程安全的，是生产者和消费者中间的数据管道，那在python多进程中，它其实就是进程之间的数据管道，实现进程通信。

```text
from multiprocessing import Process,Queue


def fun1(q,i):
    print('子进程%s 开始put数据' %i)
    q.put('我是%s 通过Queue通信' %i)

if __name__ == '__main__':
    q = Queue()

    process_list = []
    for i in range(3):
        p = Process(target=fun1,args=(q,i,))  #注意args里面要把q对象传给我们要执行的方法，这样子进程才能和主进程用Queue来通信
        p.start()
        process_list.append(p)

    for i in process_list:
        p.join()

    print('主进程获取Queue数据')
    print(q.get())
    print(q.get())
    print(q.get())
    print('结束测试')
```

结果

```text
子进程0 开始put数据
子进程1 开始put数据
子进程2 开始put数据
主进程获取Queue数据
我是0 通过Queue通信
我是1 通过Queue通信
我是2 通过Queue通信
结束测试

Process finished with exit code 0
```

上面的代码结果可以看到我们主进程中可以通过Queue获取子进程中put的数据，实现进程间的通信。

### **管道[Pipe](https://zhida.zhihu.com/search?content_id=102507664&content_type=Article&match_order=1&q=Pipe&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzgwMDUzODYsInEiOiJQaXBlIiwiemhpZGFfc291cmNlIjoiZW50aXR5IiwiY29udGVudF9pZCI6MTAyNTA3NjY0LCJjb250ZW50X3R5cGUiOiJBcnRpY2xlIiwibWF0Y2hfb3JkZXIiOjEsInpkX3Rva2VuIjpudWxsfQ.LXN0TakbOgFqaAA1c927rMhNdirL2McN5_MVTd315Ig&zhida_source=entity)**

管道Pipe和Queue的作用大致差不多，也是实现进程间的通信，下面之间看怎么使用吧

```text
from multiprocessing import Process, Pipe
def fun1(conn):
    print('子进程发送消息：')
    conn.send('你好主进程')
    print('子进程接受消息：')
    print(conn.recv())
    conn.close()

if __name__ == '__main__':
    conn1, conn2 = Pipe() #关键点，pipe实例化生成一个双向管
    p = Process(target=fun1, args=(conn2,)) #conn2传给子进程
    p.start()
    print('主进程接受消息：')
    print(conn1.recv())
    print('主进程发送消息：')
    conn1.send("你好子进程")
    p.join()
    print('结束测试')
```

结果

```text
主进程接受消息：
子进程发送消息：
子进程接受消息：
你好主进程
主进程发送消息：
你好子进程
结束测试

Process finished with exit code 0
```

上面可以看到主进程和子进程可以相互发送消息

### **Managers**

Queue和Pipe只是实现了数据交互，并没实现数据共享，即一个进程去更改另一个进程的数据。那么久要用到Managers

```text
from multiprocessing import Process, Manager

def fun1(dic,lis,index):

    dic[index] = 'a'
    dic['2'] = 'b'    
    lis.append(index)    #[0,1,2,3,4,0,1,2,3,4,5,6,7,8,9]
    #print(l)

if __name__ == '__main__':
    with Manager() as manager:
        dic = manager.dict()#注意字典的声明方式，不能直接通过{}来定义
        l = manager.list(range(5))#[0,1,2,3,4]

        process_list = []
        for i in range(10):
            p = Process(target=fun1, args=(dic,l,i))
            p.start()
            process_list.append(p)

        for res in process_list:
            res.join()
        print(dic)
        print(l)
```

结果：

```text
{0: 'a', '2': 'b', 3: 'a', 1: 'a', 2: 'a', 4: 'a', 5: 'a', 7: 'a', 6: 'a', 8: 'a', 9: 'a'}
[0, 1, 2, 3, 4, 0, 3, 1, 2, 4, 5, 7, 6, 8, 9]
```

可以看到主进程定义了一个字典和一个列表，在子进程中，可以添加和修改字典的内容，在列表中插入新的数据，实现进程间的数据共享，即可以共同修改同一份数据

### **5.进程池**

进程池内部维护一个进程序列，当使用时，则去进程池中获取一个进程，如果进程池序列中没有可供使用的进进程，那么程序就会等待，直到进程池中有可用进程为止。就是固定有几个进程可以使用。

进程池中有两个方法：

apply：同步，一般不使用

apply_async：异步

```text
from  multiprocessing import Process,Pool
import os, time, random

def fun1(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    pool = Pool(5) #创建一个5个进程的进程池

    for i in range(10):
        pool.apply_async(func=fun1, args=(i,))

    pool.close()
    pool.join()
    print('结束测试')
```

结果

```text
Run task 0 (37476)...
Run task 1 (4044)...
Task 0 runs 0.03 seconds.
Run task 2 (37476)...
Run task 3 (17252)...
Run task 4 (16448)...
Run task 5 (24804)...
Task 2 runs 0.27 seconds.
Run task 6 (37476)...
Task 1 runs 0.58 seconds.
Run task 7 (4044)...
Task 3 runs 0.98 seconds.
Run task 8 (17252)...
Task 5 runs 1.13 seconds.
Run task 9 (24804)...
Task 6 runs 1.46 seconds.
Task 4 runs 2.73 seconds.
Task 8 runs 2.18 seconds.
Task 7 runs 2.93 seconds.
Task 9 runs 2.93 seconds.
结束测试
```

对`Pool`对象调用`join()`方法会等待所有子进程执行完毕，调用`join()`之前必须先调用`close()`，调用`close()`之后就不能继续添加新的`Process`了。

### **进程池map方法**

案例来源于网络，侵权请告知，谢谢

因为网上看到这个例子觉得不错，所以这里就不自己写案例，这个案例比较有说服力

```text
import os 
import PIL 

from multiprocessing import Pool 
from PIL import Image

SIZE = (75,75)
SAVE_DIRECTORY = 'thumbs'

def get_img_paths(folder):
    return (
        os.path.join(folder,f) for f in os.listdir(folder) if "jpg" in f
    )

def create_thumbnail(filePath): # 这个filePath必须是一个包含文件名的绝对路径
    image = Image.open(filePath)
    image.thumbnail(SIZE,Image.Resampling.LANCZOS)
    base,filename = os.path.split(filePath)
    savePath = os.path.join(base,SAVE_DIRECTORY,filename)
    print(savePath)
    image.save(savePath) # 注意：Iamge保存文件的时候，目标文件夹必须存在

if __name__ == '__main__':
    folder = os.path.dirname(os.path.abspath(__file__))
    src_folder = os.path.join(folder,"mypic")
    thum_dir = os.path.join(src_folder, SAVE_DIRECTORY)
    if not os.path.exists:
        print("not exist")
        os.mkdir(thum_dir)
    else:
        print("dir exists...")    

    images = get_img_paths(src_folder)
    # print(list(images))
    pool = Pool()
    pool.map(create_thumbnail, images) #关键点，images是一个可迭代对象
    pool.close()
    pool.join()
```

上边这段代码的主要工作就是将遍历传入的文件夹中的图片文件，一一生成缩略图，并将这些缩略图保存到特定文件夹中。这我的机器上，用这一程序处理 6000 张图片需要花费 27.9 秒。 map 函数并不支持手动线程管理，反而使得相关的 debug 工作也变得异常简单。

map在爬虫的领域里也可以使用，比如多个URL的内容爬取，可以把URL放入元祖里，然后传给执行函数。



# 25. socket

# Python Socket Programming: Client, Server, Peer Libraries

![PubNub](https://miro.medium.com/v2/resize:fill:64:64/0*4Li-_S-zjwJO3FGf.png)

[PubNub](https://medium.com/@PubNub?source=post_page---byline--a61023e98e1f---------------------------------------)

Follow

7 min read

·

Nov 24, 2023

13











Press enter or click to view image in full size

![img](https://miro.medium.com/v2/resize:fit:875/0*Ywn0AiZ6TUScP1uj.jpg)

In this tutorial, you’ll learn how to exchange data between a client and a server using Python socket programming and the Socket API. Later, this tutorial will discuss exchanging data directly between two or more Python clients using a hosted provider. The source code used in this tutorial can be found within the [GitHub repository](https://github.com/PubNubDevelopers/python-socket-demo).

Socket programming connects two sockets (a client socket and a server socket) and allows them to communicate bi-directionally in real time. Direct socket connections can benefit all real-time applications since data can be sent or received anytime.

### Is Python good for socket programming?

Yes! Python is a great choice for socket programming as it has many of the required modules built-in such as socket, select, and asyncio to create client-server applications.

### What are Python sockets used for?

Python sockets are used for applications that need to communicate over a network: such as web servers, chat applications, or email clients. The server program listens and handles incoming connections, whilst the client connects to the server to send and receive data. Python sockets support both [TCP](https://www.pubnub.com/guides/tcp-ip/) — a reliable protocol that ensures in-order packet delivery, and [UDP](https://www.pubnub.com/guides/udp/) — a connectionless and lightweight protocol for applications where packet loss is acceptable.

### How do I run a socket program in Python?

The following guide will walk you through creating a Python client and server which can communicate with each other. You need to run both programs separately, i.e.:

```
python myServer.py
python myClient.py
```

### **Python Programming** Environment Set up

You will need a stable version of [Python version 3.x](https://www.python.org/downloads/) installed on your machine. If you are a Windows user, you have the option of adding Python to your PATH.

You will also need a code editor to follow along with this tutorial. [Visual Studio Code](https://code.visualstudio.com/) is a popular open-source and free code editor that supports many languages and frameworks, including Python. VSCode also supports extensions for Python to help with code completion and debugging.

### Build and run a Python socket application

Let’s build a straightforward socket application using Python. Python provides a native [socket class](https://docs.python.org/3/library/socket.html) (socket module), so developers don’t need to depend on external libraries. Begin by setting up the Python socket programming client and server:

Press enter or click to view image in full size

![img](https://miro.medium.com/v2/resize:fit:875/0*jm-KeLmSZF0Z8xHn.png)

### Import your Python socket library

Create the fileclient.py in the project directory. To use sockets, import the Python socket library and create a new socket object that connects to a specified IP address (in this case, localhost on port number 8080, but you can select any ipv4 address). Create a new connection to the socket server, send data to the TCP server, and close the socket connection.

Your client.py file should look like this:

```
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('0.0.0.0', 8080))
client.send("I am CLIENT\n".encode())
from_server = client.recv(4096)
client.close()
print (from_server.decode())
```

You will need a socket server to listen for incoming connections and messages from your client. Create the file server.py and add the following contents:

```
import socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('0.0.0.0', 8080))
serv.listen(5)
while True:
  conn, addr = serv.accept()
  from_client = ''
  while True:
    data = conn.recv(4096)
    if not data: break
    from_client += data.decode('utf8')
    print (from_client)
    conn.send("I am SERVER\n".encode())
  conn.close()
print ('client disconnected and shutdown')
```

Server.py binds the socket object to the hostname (localhost) on port 8080 and continually listens for new client connections. When a client connects to this address, the server accepts the connection and reads any data. Once the data is successfully read from the client, the server provides a data response, at which point the client terminates the connection.

### Testing your Python socket programming

To test this out yourself, open two terminal windows simultaneously. In one window, run:

```
python3 server.py
```

In the second window, run:

```
python3 client.py
```

Notice that the server continues running and will establish a new connection every time you run the client and append any new output.

[![Download the Medium App]()](https://medium.com/download-app?source=promotion_paragraph---post_body_banner_better_screentime--a61023e98e1f---------------------------------------)

The client will send the “I am CLIENT” string to the server and wait for a reply. The server will read the client’s message, output it to the terminal, and send back a response to the client.

Press enter or click to view image in full size

![img](https://miro.medium.com/v2/resize:fit:875/0*oz5_6fGpQkcZ_DPX.png)

### Socket Programming in Python using PubNub

So far, this tutorial has covered exchanging messages between a server and a client, but what if you need to communicate directly between Python clients?

Sending data directly between two or more client devices is tricky because you run into many scaling and security considerations as your number of devices increases. A client-server architecture is used to moderate and manage your client-to-client communication. If you don’t have a web server or you worry about your server scaling to meet your application’s demands, you should opt for a hosted, real-time communication solution such as [PubNub](https://www.pubnub.com/). PubNub is a globally distributed and scalable cloud platform, so you don’t have to worry about deploying and maintaining servers. PubNub’s cross-platform SDKs, including [Python](https://www.pubnub.com/docs/sdks/python), can identify users and send messages to specific channels, which only subscribed clients will receive.

### Client-to-Client Python socket programming

So, how would the simple app presented previously be written with PubNub to exchange messages directly between two clients? It’s essential to understand that although PubNub uses the ‘publish’ and ‘subscribe’ architecture (pub/sub) to send and receive bidirectional messages between endpoints, it still uses sockets behind the scenes. PubNub gives you the benefits of socket communication without worrying about the details of Python network programming and maintaining an always-on connection between your clients regardless of the operating system.

To integrate PubNub into the project, install the PubNub package with pip in the terminal; this will allow you to use the [PubNub Python SDK](https://www.pubnub.com/docs/sdks/python) and communicate with the PubNub infrastructure.

```
pip3 install 'pubnub>=7.1.0'
```

You will need to create two clients to connect to and communicate over the PubNub network. Create a file pn_client_1.py and add the following code:

```
from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
import time
import os
pnconfig = PNConfiguration()
userId = os.path.basename(__file__)
pnconfig.publish_key = 'demo'
pnconfig.subscribe_key = 'demo'
pnconfig.user_id = userId
pnconfig.ssl = True
pubnub = PubNub(pnconfig)
def my_publish_callback(envelope, status):
  # Check whether request successfully completed or not
  if not status.is_error():
    pass
class MySubscribeCallback(SubscribeCallback):
  def presence(self, pubnub, presence):
    pass
  def status(self, pubnub, status):
    pass
  def message(self, pubnub, message):
    if message.publisher == userId : return
    print ("from device " + message.publisher + ": " + message.message)
pubnub.add_listener(MySubscribeCallback())
pubnub.subscribe().channels("chan-1").execute()
## publish a message
while True:
  msg = input("")
  if msg == 'exit': os._exit(1)
  pubnub.publish().channel("chan-1").message(str(msg)).pn_async(my_publish_callback)
```

Create the file pn_client_2.py and add the same code as you used for pn_client_1.py

The code above uses ‘demo’ keys, but you can obtain your custom [PubNub keys](https://admin.pubnub.com/#/register) for free.

Run both pn_client_1.py and pn_client_2.py simultaneously in two different terminal windows

```
python3 pn_client_1.pypython3 pn_client_2.py
```

Each client initializes its connection to the PubNub network and subscribes to receive new messages whenever they are published to the ‘chan-1’ channel. You can think of this as sending data over a TCP socket in Python; behind the scenes, PubNub is creating and managing the socket for you and routing your message to all clients who are listening for it. Once the remote client receives the message, the received message is displayed on the command line.

Press enter or click to view image in full size

![img](https://miro.medium.com/v2/resize:fit:875/0*XrBEg9d4SB-PM9sz.png)

And that’s all there is to it!

### What is the alternative to sockets in Python?

For more information on developing with PubNub, check out their range of [tutorials](https://www.pubnub.com/tutorials/) and [demos](https://www.pubnub.com/demos/). Alternatively, check out the [PubNub interactive tour](https://www.pubnub.com/tour/introduction/) to understand how the platform provides real-time interactivity to applications. PubNub supports TCP and UDP datagram communication, as well as Linux, Unix, and Windows.

We have an extensive collection of resources on realtime messaging, including expert-written articles and guides on Websockets. Here are some valuable links for you to explore.

- [What are Websockets](https://www.pubnub.com/guides/what-are-websockets-and-when-should-you-use-them/)
- [PubNub resources](https://www.pubnub.com/resources)
- [PubNub blog](https://www.pubnub.com/blog/)

## How can PubNub help you?

This article was originally published on [PubNub.com](https://pubnub.com/blog/socket-programming-in-python-client-server-p2p/)

Our platform helps developers build, deliver, and manage real-time interactivity for web apps, mobile apps, and IoT devices.

The foundation of our platform is the industry’s largest and most scalable real-time edge messaging network. With over 15 points-of-presence worldwide supporting 800 million monthly active users, and 99.999% reliability, you’ll never have to worry about outages, concurrency limits, or any latency issues caused by traffic spikes.

### Experience PubNub

Check out [Live Tour](https://www.pubnub.com/tour/introduction/) to understand the essential concepts behind every PubNub-powered app in less than 5 minutes

### Get Setup

Sign up for a [PubNub account](https://admin.pubnub.com/signup/) for immediate access to PubNub keys for free

### Get Started

The [PubNub docs](https://www.pubnub.com/docs) will get you up and running, regardless of your use case or [SDK](https://www.pubnub.com/docs)

#### 参考网址： https://www.datacamp.com/tutorial/a-complete-guide-to-socket-programming-in-python



# 26. sqlite3

### 参考网址1：https://www.cnblogs.com/nxhujiee/p/18976947

SQLite 是 Python 内置的轻量级数据库，无需单独的服务器进程，使用文件存储数据。它适合小型应用、原型开发或嵌入式系统，支持标准 SQL 语法。下面详细介绍 `sqlite3` 模块的用法和示例。

### **1. 连接数据库**

使用 `sqlite3.connect()` 创建数据库连接。如果数据库不存在，会自动创建。

```python
import sqlite3

# 连接到数据库（如果不存在则创建）
conn = sqlite3.connect('example.db')  # 或使用内存数据库: sqlite3.connect(':memory:')

# 创建游标对象执行 SQL 命令
cursor = conn.cursor()
```

### **2. 创建表**

使用 `CREATE TABLE` 语句创建表，需调用 `conn.commit()` 提交事务。

```python
# 创建 users 表
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE
)
''')
conn.commit()  # 提交事务
```

### **3. 插入数据**

使用 `INSERT INTO` 插入单条或多条记录。

```python
# 插入单条记录
cursor.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)", 
               ("Alice", 30, "alice@example.com"))

# 插入多条记录（使用 executemany）
users_data = [
    ("Bob", 25, "bob@example.com"),
    ("Charlie", 35, "charlie@example.com")
]
cursor.executemany("INSERT INTO users (name, age, email) VALUES (?, ?, ?)", users_data)

conn.commit()  # 提交事务
```

### **4. 查询数据**

使用 `SELECT` 语句查询数据，通过 `fetchone()`、`fetchall()` 或 `fetchmany()` 获取结果。

```python
# 查询所有记录
cursor.execute("SELECT * FROM users")
all_users = cursor.fetchall()
print("所有用户:", all_users)

# 查询单条记录
cursor.execute("SELECT * FROM users WHERE name = ?", ("Alice",))
user = cursor.fetchone()
print("Alice:", user)

# 使用 fetchmany 获取部分结果
cursor.execute("SELECT * FROM users")
some_users = cursor.fetchmany(2)
print("前两条记录:", some_users)
```

### **5. 更新和删除数据**

使用 `UPDATE` 和 `DELETE` 语句修改数据，需提交事务。

```python
# 更新记录
cursor.execute("UPDATE users SET age = ? WHERE name = ?", (31, "Alice"))

# 删除记录
cursor.execute("DELETE FROM users WHERE age < ?", (30,))

conn.commit()  # 提交事务
```

### **6. 参数化查询**

使用参数化查询（`?` 占位符）防止 SQL 注入。

```python
# 安全示例：使用参数化查询
name = "Charlie"
cursor.execute("SELECT * FROM users WHERE name = ?", (name,))

# 不安全示例（避免这样写）
# cursor.execute(f"SELECT * FROM users WHERE name = '{name}'")
```

### **7. 事务处理**

SQLite 默认使用自动提交模式，可通过 `conn.commit()` 和 `conn.rollback()` 管理事务。

```python
try:
    # 开始事务
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("David", "david@example.com"))
    # 模拟错误
    # 1 / 0  # 取消注释此行触发异常
    conn.commit()  # 提交事务
except Exception as e:
    print(f"Error: {e}")
    conn.rollback()  # 回滚事务
```

### **8. 高级特性**

#### **8.1 自定义函数**

```python
def multiply(a, b):
    return a * b

conn.create_function("multiply", 2, multiply)
cursor.execute("SELECT multiply(3, 4)")
print(cursor.fetchone())  # 输出: (12,)
```

#### **8.2 行对象（Row Objects）**

```python
conn.row_factory = sqlite3.Row
cursor.execute("SELECT * FROM users")
row = cursor.fetchone()
print(row["name"], row["age"])  # 通过列名访问数据
```

### **9. 关闭连接**

操作完成后关闭游标和连接。

```python
cursor.close()
conn.close()
```

### **完整示例：用户管理系统**

下面是一个完整的用户管理系统示例，包含增删改查功能：

```python
import sqlite3

def create_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = create_connection()
    with conn:
        conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE,
            age INTEGER
        )
        ''')

def add_user(name, email, age):
    conn = create_connection()
    with conn:
        try:
            conn.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", 
                        (name, email, age))
            return True
        except sqlite3.IntegrityError:
            print(f"Error: Email {email} already exists.")
            return False

def get_all_users():
    conn = create_connection()
    with conn:
        return conn.execute("SELECT * FROM users").fetchall()

def update_user_age(user_id, new_age):
    conn = create_connection()
    with conn:
        conn.execute("UPDATE users SET age = ? WHERE id = ?", (new_age, user_id))

def delete_user(user_id):
    conn = create_connection()
    with conn:
        conn.execute("DELETE FROM users WHERE id = ?", (user_id,))

# 使用示例
if __name__ == "__main__":
    create_table()
    add_user("Eve", "eve@example.com", 28)
    users = get_all_users()
    for user in users:
        print(dict(user))  # 打印为字典格式
```

### **注意事项**

1. **线程安全**：SQLite 支持多线程读，但写入时需加锁（默认模式）。
2. **事务管理**：批量操作时使用事务可显著提高性能。
3. **大数据处理**：SQLite 适合中小型数据集，大数据量建议使用 PostgreSQL 或 MySQL。

通过上述示例，你可以掌握 `sqlite3` 模块的基本用法。如需更复杂的功能，可以结合 Python 的其他库（如 Pandas）进行数据处理。

### 参考网址2：https://developer.aliyun.com/article/1481409



# 27. csv

### 参考网址1：https://developer.aliyun.com/article/524890

### 参考网址2：https://www.cnblogs.com/klb561/p/19342026

#### 操作示例

```
"""
python csv built-in module
"""
import csv

# 1.create a csv file method1
# data = [['姓名', '年龄'], ['张三', 25], ['李四', 30]]
# with open("test.csv",mode='w',encoding='utf-8-sig',newline='') as f:
#     csv_writer = csv.writer(f) # create a csv writer
#     csv_writer.writerows(data)

# # 2.create a csv method2
# fields = ["name","age","gender"]   
# rows =[
#    {"name":"Magret","age":19,"gender":"female"}, 
#    {"name":"Mark","age":17,"gender":"male"}, 
#    {"name":"Jerry","age":18,"gender":"male"}, 
#    {"name":"Jesse","age":18,"gender":"female"}, 
#    {"name":"Beckey","age":18,"gender":"female"}, 
# ] 
# with open("test2.csv",mode='w',encoding='utf-8-sig',newline='') as f:
#     dict_writer = csv.DictWriter(f,fieldnames=fields)
#     dict_writer.writeheader() # no params
#     # dict_writer.writerow({"name":"Mary","age":18,"gender":"female"})
#     dict_writer.writerows(rows)

# 3.read method1
# with open("test2.csv",mode='r',encoding='utf-8-sig',newline='') as f:
#     csv_reader = csv.reader(f)
#     for row in csv_reader:
#         print(row)

# 4.read csv method 2
with open("test2.csv",mode='r',encoding='utf-8-sig',newline='') as f:
    dict_reader = csv.DictReader(f)
    for row in dict_reader:
        print(row)
```



# 28 . argparse

**作用：** argparse 是 Python 内置的一个用于命令项选项与参数解析的模块，通过在程序中定义好我们需要的参数，argparse 将会从 sys.argv 中解析出这些参数，并自动生成帮助和使用信息。当然，Python 也有第三方的库可用于命令行解析，而且功能也更加强大，比如 docopt，Click。

### 1. 命令行参数分为位置参数和选项参数：

- 位置参数就是程序根据该参数出现的位置来确定的
  - 如：[root@openstack_1 /]# ls root/ #其中root/是位置参数
- 选项参数是应用程序已经提前定义好的参数，不是随意指定的
  - 如：[root@openstack_1 /]# ls -l # -l 就是ls命令里的一个选项参数

### 2. 使用步骤：

（1）import argparse 首先导入模块
（2）parser = argparse.ArgumentParser（） 创建一个解析对象
（3）parser.add_argument() 向该对象中添加你要关注的命令行参数和选项
（4）parser.parse_args() 进行解析

### argparse.ArgumentParser（）方法参数须知：一般我们只选择用description

- description - 命令行帮助的开始文字，大部分情况下，我们只会用到这个参数
- epilog - 命令行帮助的结尾文字
- prog - (default: sys.argv[0])程序的名字，一般不需要修改，另外，如果你需要在help中使用到程序的名字，可以使用%(prog)s
- prefix_chars - 命令的前缀，默认是-，例如-f/–file。有些程序可能希望支持/f这样的选项，可以使用prefix_chars=”/”
- fromfile_prefix_chars - (default: None)如果你希望命令行参数可以从文件中读取，就可能用到。例如，如果fromfile_prefix_chars=’@’,命令行参数中有一个为”@args.txt”，args.txt的内容会作为命令行参数
- add_help - 是否增加-h/-help选项 (default: True)，一般help信息都是必须的，所以不用设置啦。
- parents - 类型是list，如果这个parser的一些选项跟其他某些parser的选项一样，可以用parents来实现继承，例如parents=[parent_parser]
- 三个允许的值： # class argparse.RawDescriptionHelpFormatter 直接输出description和epilog的原始形式（不进行自动换行和消除空白的操作） # class argparse.RawTextHelpFormatter 直接输出description和epilog以及add_argument中的help字符串的原始形式（不进行自动换行和消除空白的操作） # class argparse.ArgumentDefaultsHelpFormatter 在每个选项的帮助信息后面输出他们对应的缺省值，如果有设置的话。这个最常用吧！
- argument_default - (default: None)设置一个全局的选项的缺省值，一般每个选项单独设置，所以这个参数用得少，不细说
- usage - (default: generated)如果你需要修改usage的信息（usage: PROG [-h] [–foo [FOO]] bar [bar …]），那么可以修改这个，一般不要修改。
- conflict_handler - 不建议使用。这个在极端情况下才会用到，主要是定义两个add_argument中添加的选项的名字发生冲突时怎么处理，默认处理是抛出异常。

### 4. add_argument()方法参数须知：

- name or flags - 指定参数的形式，想写几个写几个，不过我们一般就写两个，一个短参数，一个长参数，看下面的例子”-f”, “–file”

- 可选的选项，位置不固定，想怎么写就怎么写，默认是可选的 # parser.add_argument(“-f”, “–file”, help=”test test test”)

- 位置固定的选项，例如”prog i_am_bar”，这样子的话，i_am_bar就是bar选项的值啦，默认是必须有的 # parser.add_argument(“bar”, help=”test test test”)

- nargs - 指定这个参数后面的value有多少个，例如，我们希望使用-n 1 2 3 4，来设置n的值为[1, 2, 3, 4] #parser.add_argument(“-n”, “–num”, nargs=”+”, type=int) # 这里nargs=”+”表示，如果你指定了-n选项，那么-n后面至少要跟一个参数，+表示至少一个,?表示一个或0个,0个或多个 。

- default - 如果命令行没有出现这个选项，那么使用default指定的默认值 #parser.add_argument(“+g”, “++gold”, help=”test test test”,default=”test_gold”)#需要prefix_chars包含”+” 。

- type - 如果希望传进来的参数是指定的类型（例如 float, int or file等可以从字符串转化过来的类型），可以使用 #parser.add_argument(“-x”, type=int) 。

- choices - 设置参数值的范围，如果choices中的类型不是字符串，记得指定type哦 #parser.add_argument(“-y”, choices=[‘a’, ‘b’, ‘d’])

- required - 通常-f这样的选项是可选的，但是如果required=True那么就是必须的了 #parser.add_argument(“-z”, choices=[‘a’, ‘b’, ‘d’], required=True)

- metavar - 参数的名字，在显示 帮助信息时才用到. # parser.add_argument(“-o”, metavar=”OOOOOO”)

- help - 设置这个选项的帮助信息

- dest - 设置这个选项的值就是解析出来后放到哪个属性中 #parser.add_argument(“-q”, dest=”world”)

- args = parser.parse_args(args) # 如果你没有args参数，那么就使用sys.argv，也就是命令行参数啦。有这个参数，就方便我们调试啊 。# args.world就是-q的值啦

  ## 参考文档2：

  Python的`argparse`模块是标准库中用于解析命令行参数的工具，功能强大且易于使用。本文将详细介绍`argparse`的基本用法、参数设置、类型转换、默认值、范围限制等内容，并通过实际案例展示如何构建命令行工具。

  #### 1. argparse模块简介

  `argparse`是Python标准库中的模块，用于解析命令行参数。通过`argparse`，可以轻松实现命令行工具的参数解析功能，支持短参数（如`-h`）和长参数（如`--help`），并能自动生成帮助信息。

  ```python
  import argparse
  
  # 创建解析器对象
  parser = argparse.ArgumentParser(description="这是一个简单的命令行工具")
  
  # 添加参数
  parser.add_argument('--name', type=str, help="输入你的名字")
  
  # 解析命令行参数
  args = parser.parse_args()
  
  # 输出解析结果
  print(f"Hello, {args.name}!")
  1.2.3.4.5.6.7.8.9.10.11.12.13.
  ```

  #### 2. 参数类型与设置

  `argparse`支持多种参数类型，包括位置参数和可选参数。以下是对两种参数的详细介绍。

  ##### 2.1 位置参数

  位置参数是必须提供的参数，通常用于接收核心输入值。

  ```python
  import argparse
  
  parser = argparse.ArgumentParser(description="计算正方形的面积")
  parser.add_argument('square', type=int, help="正方形的边长")
  args = parser.parse_args()
  
  # 计算并输出面积
  print(f"正方形的面积是 {args.square ** 2}")
  1.2.3.4.5.6.7.8.
  ```

  ##### 2.2 可选参数

  可选参数是可选的参数，通常用于控制工具的行为。

  ```python
  import argparse
  
  parser = argparse.ArgumentParser(description="控制输出详细程度")
  parser.add_argument('--verbose', action='store_true', help="增加输出的详细程度")
  args = parser.parse_args()
  
  if args.verbose:
      print("详细模式已开启")
  else:
      print("普通模式")
  1.2.3.4.5.6.7.8.9.10.
  ```

  #### 3. 参数的高级设置

  ##### 3.1 设置默认值

  通过`default`参数可以设置默认值，当用户未提供参数时使用默认值。

  ```python
  import argparse
  
  parser = argparse.ArgumentParser(description="设置默认值")
  parser.add_argument('--port', type=int, default=80, help="指定端口号")
  args = parser.parse_args()
  
  print(f"使用端口号 {args.port}")
  1.2.3.4.5.6.7.
  ```

  ##### 3.2 设置参数范围

  通过`choices`参数可以限制参数的取值范围。

  ```python
  import argparse
  
  parser = argparse.ArgumentParser(description="限制参数范围")
  parser.add_argument('--level', type=int, choices=[1, 2, 3], help="选择级别")
  args = parser.parse_args()
  
  print(f"选择的级别是 {args.level}")
  1.2.3.4.5.6.7.
  ```

  ##### 3.3 类型转换

  `argparse`支持多种类型转换，如`int`、`float`、`str`等。

  ```python
  import argparse
  
  parser = argparse.ArgumentParser(description="类型转换")
  parser.add_argument('--number', type=float, help="输入一个浮点数")
  args = parser.parse_args()
  
  print(f"输入的浮点数是 {args.number}")
  1.2.3.4.5.6.7.
  ```

  #### 4. 实际案例：端口扫描器

  以下是一个简单的端口扫描器案例，展示如何使用`argparse`解析命令行参数。

  ```python
  import argparse
  
  # 创建解析器
  parser = argparse.ArgumentParser(description="端口扫描器")
  
  # 添加位置参数（IP地址）
  parser.add_argument('ip', type=str, help="目标IP地址")
  
  # 添加可选参数（端口号）
  parser.add_argument('--port', type=int, default=80, help="指定端口号")
  
  # 解析参数
  args = parser.parse_args()
  
  # 输出解析结果
  print(f"扫描目标: {args.ip}")
  print(f"端口号: {args.port}")
  1.2.3.4.5.6.7.8.9.10.11.12.13.14.15.16.17.
  ```

  #### 5. 常见问题解答（FAQ）

  | 问题               | 答案                                                         |
  | ------------------ | ------------------------------------------------------------ |
  | 如何添加位置参数？ | 使用`parser.add_argument('参数名', type=类型, help="帮助信息")`添加位置参数。 |
  | 如何添加可选参数？ | 使用`parser.add_argument('--参数名', type=类型, help="帮助信息")`添加可选参数。 |
  | 如何设置默认值？   | 在`add_argument`中使用`default=值`设置默认值。               |
  | 如何限制参数范围？ | 在`add_argument`中使用`choices=[值1, 值2, ...]`限制参数范围。 |
  | 如何实现布尔参数？ | 使用`action='store_true'`或`action='store_false'`实现布尔参数。 |

  #### 6. argparse与其他模块的对比

  | 模块                 | 优点                       | 缺点                     |
  | -------------------- | -------------------------- | ------------------------ |
  | `argparse`           | 功能强大，支持复杂参数设置 | 相对复杂，学习曲线较高   |
  | `getopt`             | 简单易用                   | 功能有限，不支持类型转换 |
  | `optparse`（已废弃） | 功能较丰富                 | 已废弃，不推荐使用       |

  通过对比可以看出，`argparse`是功能最强大且灵活的命令行解析模块，适合构建复杂工具。

  ------

  本文通过详细解析`argparse`模块的基本用法、参数设置、类型转换等内容，并结合实际案例，帮助读者掌握如何使用`argparse`构建命令行工具。

# 29 . pathlib

## **为什么要用pathlib？**

以前我们处理文件路径时,经常要用到os和os.path模块:

```python
import os

# 拼接路径
path = os.path.join('folder', 'subfolder', 'file.txt')

# 获取文件名
basename = os.path.basename(path)

# 获取目录名
dirname = os.path.dirname(path)

# 判断是否存在
exists = os.path.exists(path)
```

这样写代码有几个问题:

1. 要记住很多零散的函数
2. 不同系统的路径分隔符不一样
3. 路径还是普通字符串,容易拼错

而用pathlib后:

```python
from pathlib import Path

# 创建路径对象
path = Path('folder') / 'subfolder' / 'file.txt'

# 获取文件名
basename = path.name

# 获取目录名
dirname = path.parent

# 判断是否存在
exists = path.exists()
```

代码更简洁,更直观,更不容易出错!

## **Path对象详解**

### **创建Path对象**

有很多方法可以创建Path对象:

```python
from pathlib import Path

# 从字符串创建
p1 = Path('folder/file.txt')

# 从多个部分创建
p2 = Path('folder', 'file.txt')

# 用/运算符连接
p3 = Path('folder') / 'file.txt'

# 从home目录创建
home = Path.home()

# 当前目录
current = Path.cwd()

# 绝对路径
abs_path = Path('file.txt').absolute()
```

### **路径信息获取**

Path对象提供了丰富的属性来获取路径信息:

```python
path = Path('/home/user/docs/file.txt')

# 文件名相关
path.name          # 'file.txt'
path.stem          # 'file'
path.suffix        # '.txt'
path.suffixes      # ['.tar', '.gz']用于多扩展名
path.with_suffix('.md')  # 更改扩展名

# 目录相关
path.parent        # 父目录 /home/user/docs
path.parents[0]    # 父目录 /home/user/docs
path.parents[1]    # 祖父目录 /home/user
path.parts         # ('/', 'home', 'user', 'docs', 'file.txt')

# 路径类型
path.is_absolute() # 是否是绝对路径
path.is_relative_to('/home')  # 是否是某个路径的子路径
```

### **常用属性和方法汇总**

以下是Path对象最常用的属性和方法:

### **路径信息**

- `name`: 文件名
- `stem`: 不带后缀的文件名
- `suffix`: 文件后缀
- `suffixes`: 所有文件后缀列表
- `parent`: 父目录
- `parents`: 所有父目录的序列
- `parts`: 路径的各个部分
- `drive`: 驱动器名称(Windows)
- `anchor`: 驱动器和根目录
- `root`: 根目录

### **路径判断**

- `exists()`: 是否存在
- `is_file()`: 是否是文件
- `is_dir()`: 是否是目录
- `is_absolute()`: 是否是绝对路径
- `is_symlink()`: 是否是[符号链接](https://zhida.zhihu.com/search?content_id=254515571&content_type=Article&match_order=1&q=符号链接&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzgxODE1MjksInEiOiLnrKblj7fpk77mjqUiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNTQ1MTU1NzEsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.vmdcCL0OTj6_L9Cfk3wNx261EeP2COZa_Zim5zUa9dQ&zhida_source=entity)
- `is_socket()`: 是否是套接字
- `is_fifo()`: 是否是管道
- `is_block_device()`: 是否是块设备
- `is_char_device()`: 是否是字符设备

### **路径操作**

- `resolve()`: 解析绝对路径,处理符号链接
- `absolute()`: 返回绝对路径
- `relative_to()`: 计算相对路径
- `with_name()`: 更改文件名
- `with_suffix()`: 更改文件后缀
- `joinpath()`: 拼接路径
- `match()`: 匹配[通配符模式](https://zhida.zhihu.com/search?content_id=254515571&content_type=Article&match_order=1&q=通配符模式&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzgxODE1MjksInEiOiLpgJrphY3nrKbmqKHlvI8iLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNTQ1MTU1NzEsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9._bbZzVcakc17NbGVe-i7fFsMjKIueodZKsbrEwVPBiM&zhida_source=entity)
- `expanduser()`: 展开用户路径(~)

### **文件操作**

- `touch()`: 创建空文件
- `unlink()`: 删除文件
- `rename()`: 重命名
- `replace()`: 覆盖重命名
- `chmod()`: 修改权限
- `lchmod()`: 修改符号链接权限
- `symlink_to()`: 创建符号链接
- `hardlink_to()`: 创建[硬链接](https://zhida.zhihu.com/search?content_id=254515571&content_type=Article&match_order=1&q=硬链接&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzgxODE1MjksInEiOiLnoazpk77mjqUiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNTQ1MTU1NzEsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.IbTsB1Ia2Cx0uKLwLHioVWOYlxswoE6VED9NTtkiE8c&zhida_source=entity)
- `stat()`: 获取文件状态
- `lstat()`: 获取符号链接状态
- `owner()`: 获取所有者
- `group()`: 获取所属组

### **目录操作**

- `mkdir()`: 创建目录
- `rmdir()`: 删除目录
- `iterdir()`: 遍历目录
- `glob()`: 使用通配符搜索
- `rglob()`: 递归使用通配符搜索

### **文件读写**

- `read_text()`: 读取文本
- `read_bytes()`: 读取二进制
- `write_text()`: 写入文本
- `write_bytes()`: 写入二进制
- `open()`: 打开文件

## **实际应用举例**

### **1. 基本文件操作**

```python
from pathlib import Path

# 创建文件
path = Path('test.txt')
path.touch()

# 写入内容
path.write_text('Hello World')

# 读取内容
content = path.read_text()

# 删除文件
path.unlink()
```

### **2. 目录操作**

```python
from pathlib import Path

# 创建目录
path = Path('new_folder')
path.mkdir(exist_ok=True)

# 创建多级目录
path = Path('a/b/c')
path.mkdir(parents=True, exist_ok=True)

# 遍历目录
for item in path.iterdir():
    print(item.name)

# 搜索文件
for py_file in path.glob('*.py'):
    print(py_file)
```

### **3. 路径处理**

```python
from pathlib import Path

path = Path('docs/images/logo.png')

# 获取上级目录
parent = path.parent  # docs/images
grandparent = path.parent.parent  # docs

# 修改文件名
new_path = path.with_name('icon.png')  # docs/images/icon.png

# 修改扩展名
new_path = path.with_suffix('.jpg')  # docs/images/logo.jpg

# 获取相对路径
rel_path = path.relative_to('docs')  # images/logo.png
```

## **使用技巧**

1. **路径连接**

- 使用 / 运算符,不要用字符串拼接
- 可以连接字符串或Path对象

```python
path = Path('folder') / 'subfolder' / 'file.txt'
```

1. **文件判断**

- 操作前检查文件是否存在
- 区分文件和目录

```python
if path.exists() and path.is_file():
    # 处理文件
```

1. **编码处理**

- 读写文本时指定编码

```python
content = path.read_text(encoding='utf-8')
path.write_text(content, encoding='utf-8')
```

1. **异常处理**

- 捕获可能的异常

```python
try:
    path.unlink()
except FileNotFoundError:
    print('文件不存在')
except PermissionError:
    print('没有权限')
```

## **常见问题**

1. Path对象不能直接和字符串相加

```python
# 错误
path = Path('folder') + '/file.txt'

# 正确
path = Path('folder') / 'file.txt'
```

1. mkdir()默认不创建父目录

```python
# 创建多级目录要加parents=True
Path('a/b/c').mkdir(parents=True)
```

1. unlink()和rmdir()的区别

- unlink()删除文件
- rmdir()只能删除空目录

1. resolve()和absolute()的区别

- resolve()会处理符号链接
- absolute()只是返回绝对路径

pathlib的优势:

1. 面向对象的API,更符合Python风格
2. 自动处理不同系统的路径差异
3. 提供丰富的路径操作方法
4. 代码更简洁易读

建议:

1. 新项目优先使用pathlib
2. 路径处理统一使用Path对象
3. 注意正确处理异常情况
4. 考虑文件编码问题

# 30 .glob

**glob模块**也是Python标准库中一个重要的模块，主要用来**查找符合特定规则的目录和文件**，并将搜索的到的**结果返回到一个列表中**。使用这个模块最主要的原因就是，该模块支持几个特殊的[正则通配符](https://zhida.zhihu.com/search?content_id=199065431&content_type=Article&match_order=1&q=正则通配符&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzgxODY2NTYsInEiOiLmraPliJnpgJrphY3nrKYiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoxOTkwNjU0MzEsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.tnrED2rb2mf4pFWBhsLGpyDIwcW6eNSTPDO78U276Vg&zhida_source=entity)，用起来贼方便，这个将会在下方为大家进行详细讲解。

![img](https://pic2.zhimg.com/v2-7fd0b20a09e63aba2da1c874a0ca64a7_1440w.jpg)

## 一、支持4个常用的通配符

使用glob模块能够快速查找我们想要的目录和文件，就是由于它支持*、**、? 、[ ]这三个通配符，那么它们到底是 什么意思呢？

*：匹配0个或多个字符；

**：匹配所有文件、目录、子目录和子目录里的文件（3.5版本新增）；

?：代匹配一个字符；

[]：匹配指定范围内的字符，如[0-9]匹配数字，[a-z]匹配小写字母；

注意：这3个通配符的用法，将在讲函数的时候，一起带大家操作一遍；

## 二、glob库中主要的3个函数

其实glob库很简单，只有3个主要函数供我们使用，它们分别是glob()、iglob()、escape()函数，因此学习起来特别容易。

glob.glob()：返回符合匹配条件的所有文件的路径；

glob.iglob()：返回一个迭代器对象，需要循环遍历获取每个元素，得到的也是符合匹配条件的所有文件的路径；

glob.escape()：escape可以忽略所有的特殊字符，就是星号、问号、中括号，用处不大；

recursive=False：代表递归调用，与特殊通配符“**”一同使用，默认为False，False表示不递归调用，True表示递归调用；

#### 示例1.glob.glob() ->list

```
import glob #获取指定目录下的所有图片
print glob.glob(r"E:/Picture/*/*.jpg") #获取上级目录的所有.py文件
print glob.glob(r'../*.py') #相对路径
```

#### 示例2.glob.iglob()  ->generator

```
import glob

print(glob.iglob("../lesson3-builtin-modules1/*.py")) # <generator object _iglob at 0x00000160A491C7C0>
for i in glob.iglob("../lesson3-builtin-modules1/*.py"):
    print(i)
```



# 31 . tempfile

临时目录就是个生命周期很短的文件夹，专门用来存放那些不需要长期保留的数据。用完之后连同里面的内容一起删掉，文件系统保持干净。

Python 的 `tempfile` 模块提供了一套完整的解决方案，这些临时文件和目录在不需要的时候会自动清理掉。

### 为什么要用临时目录

临时目录在实际开发中有几个明显的好处：

自动清理机制省去了手动删除的步骤，每个临时目录都有唯一标识避免文件名冲突。系统会自动选择安全的存储位置，Unix 系统用 `/tmp`，Windows 用 `%TEMP%`。多线程和多进程环境下也能稳定工作，特别适合测试场景和需要中间存储的情况。

### 什么场景下需要临时目录

需要一个临时空间来存放中间计算结果或临时文件。写单元测试的时候模拟文件操作，完了自动清理。下载或解压的数据不需要长期保存。处理用户上传的文件，在保存最终结果之前需要一个缓冲区。构建自动化流程时，要确保不留下任何痕迹。

### tempfile 模块基础用法

```
import tempfile  
import os  
# Create a temporary directory
with tempfile.TemporaryDirectory() as temp_dir:  
    print(f"Temporary directory created at: {temp_dir}")  
    # Create a temporary file inside the directory
    file_path = os.path.join(temp_dir, "sample.txt")  
    with open(file_path, "w") as f:  
        f.write("Hello, Temporary World!")  
    # Read back the file
    with open(file_path, "r") as f:  
        print(f.read())  
# At this point, the directory and its contents are deleted automatically
 print("Temporary directory cleaned up automatically.")
```

### 手动控制临时目录的生命周期

有时候需要更精细的控制，比如临时目录的生命周期超出单个函数作用域，这时候可以用 `tempfile.mkdtemp()`：

```
import shutil  
import os  
# Create a temporary directory manually
temp_dir = tempfile.mkdtemp()  
print(f"Created temporary directory: {temp_dir}")  
# Work inside it
file_path = os.path.join(temp_dir, "example2.txt")  
with open(file_path, "w") as f:  
    f.write("Manual cleanup required!")  
print("Files inside temp dir:", os.listdir(temp_dir))  
# Clean up manually when done
shutil.rmtree(temp_dir)  
print("Temporary directory removed.")
```

### 自定义临时目录的命名和位置

`tempfile` 支持给临时目录添加前缀和后缀，方便调试时识别：

```javascript
 import tempfile  
 # Create with custom prefix and suffix
 with tempfile.TemporaryDirectory(prefix="myapp_", suffix="_data") as temp_dir:  
     print(f"Created: {temp_dir}")
```

输出类似这样：

```javascript
 Created: /tmp/myapp_abcd1234_data
```

还可以指定父目录：注意，这个父目录必须存在

```javascript
 with tempfile.TemporaryDirectory(dir="/path/to/parent") as temp_dir:  
     print(temp_dir)
```

当系统默认的临时目录权限不够或者空间不足时，这个功能就派上用场了。

### 实战案例：安全处理 ZIP 文件

下载大型 ZIP 文件后临时解压处理，处理完就清理掉：

```javascript
import tempfile  
import zipfile  
def extract_and_process(zip_path):  
    with tempfile.TemporaryDirectory() as tmp_dir:  
        print(f"Extracting to {tmp_dir}")  
        with zipfile.ZipFile(zip_path, "r") as zip_ref:  
            zip_ref.extractall(tmp_dir)  
        # Process extracted files
        for file in os.listdir(tmp_dir):  
             print("Processing:", file)
```

整个流程结束后，解压的文件夹自动删除，磁盘不会留下任何垃圾文件。

### 实战案例：动态生成报告

应用程序按需生成报告文件（PDF、CSV 之类），不需要永久存储：

```javascript
import tempfile  
import csv  
import os  
def generate_temp_report(data):  
    with tempfile.TemporaryDirectory() as tmp_dir:  
        file_path = os.path.join(tmp_dir, "report.csv")  
        with open(file_path, "w", newline="") as csvfile:  
            writer = csv.writer(csvfile)  
            writer.writerow(["Name", "Age"])  
            writer.writerows(data)  
        print(f"Report generated at: {file_path}")  
         # Here you can upload it, email it, or read the content directly
```

生成的报告可以直接上传、发邮件或者读取内容，不会在本地留存。

### 实战案例：单元测试中的文件操作

写单元测试时在项目目录下创建很多文件夹显然不是好主意，所以临时目录完美解决这个问题：

```javascript
import tempfile  
import unittest  
import os  
class TestFileOperations(unittest.TestCase):  
    def test_temp_directory(self):  
        with tempfile.TemporaryDirectory() as temp_dir:  
            file_path = os.path.join(temp_dir, "test.txt")  
            with open(file_path, "w") as f:  
                f.write("test data")  
              
             self.assertTrue(os.path.exists(file_path))
```

每个测试用例都在独立的临时环境中运行，互不干扰，也不需要手动清理。

### 嵌套临时目录

复杂场景下可能需要嵌套的临时目录结构：

```javascript
 import tempfile  
 import os  
 with tempfile.TemporaryDirectory() as root_dir:  
     print(f"Root: {root_dir}")  
     sub_dir = tempfile.mkdtemp(dir=root_dir)  
     print(f"Nested: {sub_dir}")
```

多阶段数据处理流程中，每个阶段可以有自己的独立沙箱环境。

### 使用临时目录的几个注意事项

始终使用上下文管理器 `with tempfile.TemporaryDirectory()` 来确保自动清理。不要硬编码 `/tmp` 路径，用 `tempfile.gettempdir()` 获取系统临时目录。如果用了 `mkdtemp()` 就必须手动调用 `shutil.rmtree()` 清理。给临时目录加上有意义的前缀方便调试时快速定位。临时数据随时可能被系统清理，不要在里面存放需要持久化的信息。

### 几个实用技巧

获取系统临时目录路径：

代码语言：javascript

AI代码解释



```javascript
 importtempfile
 print(tempfile.gettempdir())
```

生成唯一文件名（但不创建文件）：

```javascript
 tempfile.mktemp()
```

不过要注意，直接用 `mktemp()` 有安全风险，生产环境建议用 `NamedTemporaryFile` 或 `TemporaryDirectory`。

### 生产环境中的实际应用

下面这段代码展示了如何在 PDF 处理项目中使用临时目录。整个流程包括 PDF 转图片、图片转 Markdown、最后合并成完整文档：

```javascript
import os  
import io  
import shutil  
import tempfile  
from pathlib import Path  
from typing import Iterable, Optional, Callable, Tuple  

# Requires: pip install pymupdf pillow  
import fitz  # PyMuPDF  
 from PIL import Image  
```

代码语言：javascript

AI代码解释



```javascript
 def process_pdfs_to_markdown(  
    pdf_paths: Iterable[str | os.PathLike],  
    output_dir: str | os.PathLike,  
    *,  
    page_image_dpi: int = 200,  
    image_format: str = "PNG",  
    llm_page_markdown_fn: Optional[Callable[[Path], str]] = None,  
) -> Tuple[list[Path], list[Path]]:  
    """  
    Convert each input PDF into page images using a temporary workspace, run an LLM on each page image to get  
    Markdown, save one MD per page (still in a temp workspace), then merge the per-PDF Markdown into a single  
    non-temporary Markdown file per PDF in `output_dir`.  
      
    Non-temp file handling is kept simple (write final merged .md into `output_dir`), while the heavy lifting  
    uses temp directories that auto-clean on success or error.  
      
    Parameters  
    ----------  
    pdf_paths : Iterable[str | PathLike]  
        Paths to PDF files to process.  
    output_dir : str | PathLike  
        Directory where FINAL merged Markdown files (non-temp) will be written.  
    page_image_dpi : int, optional  
        Rendering resolution for converting PDF pages to images. Higher DPI → sharper (default 200).  
    image_format : str, optional  
        Image format for page renders (e.g., "PNG", "JPEG"). Default "PNG".  
    llm_page_markdown_fn : Callable[[Path], str], optional  
        A callable that takes a Path to a page image and returns Markdown text for that page.  
        If not provided, a placeholder stub will be used.  
      
    Returns  
    -------  
    Tuple[list[Path], list[Path]]  
        A tuple (final_markdown_files, per_page_markdown_files_flattened)  
        - final_markdown_files: list of merged Markdown file paths written in output_dir (non-temp)  
        - per_page_markdown_files_flattened: flattened list of all per-page MD files (in temp, ephemeral)  
          (Returned for inspection/logging; these will be deleted when temp dir goes away.)  
      
    Notes  
    -----  
    - Uses a single top-level TemporaryDirectory for the whole batch to keep structure neat.  
    - For each PDF, creates `/tmp/.../<pdf_stem>/images` and `/tmp/.../<pdf_stem>/md`.  
    - Each page is rendered to an image file named `page-<index>.<ext>`.  
    - Each page's Markdown is saved to `page-<index>.md`.  
    - Finally, merges all page MDs for that PDF into `<output_dir>/<pdf_stem>.md` (non-temp).  
    - Replace `llm_stub_markdown_from_image` with your actual LLM call (OpenAI, local VLM, etc.).  
      
    Pseudocode hint for real LLM integration  
    ----------------------------------------  
    def llm_page_markdown_fn(img_path: Path) -> str:  
        # pseudo:  
        # bytes = img_path.read_bytes()  
        # resp = my_llm_client.vision_to_md(image=bytes, system_prompt="Extract content as Markdown.")  
        # return resp.markdown  
        pass  
    """  
    output_dir = Path(output_dir)  
    output_dir.mkdir(parents=True, exist_ok=True)  

    # --- Local helper: default LLM stub (replace this with your LLM call) ---  
    def llm_stub_markdown_from_image(img_path: Path) -> str:  
        # This is a placeholder. Swap with a real LLM/VLM call to convert the image to Markdown.  
        # You can pass the image bytes and ask the model to produce clean Markdown with headings, tables, lists, etc.  
        return f"# Page extracted (stub)\n\n_Image: {img_path.name}_\n\n> Replace this with real LLM Markdown output."  

    # Choose the LLM function (user-supplied or stub)  
    llm_to_md = llm_page_markdown_fn or llm_stub_markdown_from_image  

    final_markdown_files: list[Path] = []  
    per_page_markdown_files_flattened: list[Path] = []  

    # Top-level temp root for the entire run  
    with tempfile.TemporaryDirectory(prefix="pdf2img-md_") as temp_root:  
        temp_root = Path(temp_root)  

        for pdf_path in map(Path, pdf_paths):  
            if not pdf_path.exists() or pdf_path.suffix.lower() != ".pdf":  
                # Skip invalid entries gracefully; alternatively raise ValueError  
                continue  

            pdf_stem = pdf_path.stem  
            pdf_temp_dir = temp_root / pdf_stem  
            images_dir = pdf_temp_dir / "images"  
            md_dir = pdf_temp_dir / "md"  
            images_dir.mkdir(parents=True, exist_ok=True)  
            md_dir.mkdir(parents=True, exist_ok=True)  

            # --- 1) Render pages to images in temp ---  
            # Using PyMuPDF: fast, no external poppler dependency  
            pages_rendered: list[Path] = []  
            with fitz.open(pdf_path) as doc:  
                # scale based on DPI (PyMuPDF normally uses zoom factors; convert DPI to zoom)  
                # Base DPI ~72; zoom = target_dpi / 72  
                zoom = page_image_dpi / 72.0  
                mat = fitz.Matrix(zoom, zoom)  

                for page_index in range(doc.page_count):  
                    page = doc.load_page(page_index)  
                    pix = page.get_pixmap(matrix=mat, alpha=False)  # no alpha for standard formats  
                    img_bytes = pix.tobytes(output=image_format.lower())  

                    img_name = f"page-{page_index + 1}.{image_format.lower()}"  
                    img_path = images_dir / img_name  

                    # Save via PIL to ensure consistent headers/metadata if needed  
                    with Image.open(io.BytesIO(img_bytes)) as im:  
                        im.save(img_path, format=image_format)  

                    pages_rendered.append(img_path)  

            # --- 2) For each page image, call LLM to get Markdown; save per-page MD in temp ---  
            page_md_files: list[Path] = []  
            for img_path in pages_rendered:  
                md_text = llm_to_md(img_path)  # <-- your real LLM call here  
                md_path = md_dir / (img_path.stem + ".md")  
                md_path.write_text(md_text, encoding="utf-8")  
                page_md_files.append(md_path)  
                per_page_markdown_files_flattened.append(md_path)  

            # --- 3) Merge per-page MD into a FINAL non-temp Markdown file (one per PDF) ---  
            final_md_path = output_dir / f"{pdf_stem}.md"  
            # If you want sophisticated merging rules, implement here (e.g., front matter, TOC).  
            # Pseudocode for richer post-processing could be:  
            #   combined = render_front_matter(pdf_path) + "\n" + concatenate_markdown(page_md_files) + "\n" + add_toc()  
            #   final_md_path.write_text(combined, encoding="utf-8")  
            with final_md_path.open("w", encoding="utf-8") as fout:  
                fout.write(f"<!-- Source PDF: {pdf_path.name} -->\n")  
                fout.write(f"# {pdf_stem}\n\n")  
                for i, md_file in enumerate(sorted(page_md_files, key=lambda p: p.name), start=1):  
                    fout.write(f"\n\n---\n\n<!-- Page {i} -->\n\n")  
                    fout.write(md_file.read_text(encoding="utf-8"))  

            final_markdown_files.append(final_md_path)  

        # NOTE:  
        # All temp content (images & per-page MDs) is automatically cleaned up on exit.  

     return final_markdown_files, per_page_markdown_files_flattened
```

这段代码的亮点在于所有中间文件（图片、单页 Markdown）都存放在临时目录里，处理完自动清理，只保留最终合并后的文档。整个流程非常干净，不会在磁盘上留下任何垃圾文件。

实际使用时把 `llm_stub_markdown_from_image` 替换成真正的 LLM 调用（比如 OpenAI 的 Vision API 或者本地视觉模型），就能实现完整的 PDF 文档处理流程。

### 总结

临时目录在 Python 开发中确实是个实用的工具，文件处理更高效也更安全。不管是处理用户上传、写单元测试还是构建数据流水线，`tempfile.TemporaryDirectory()` 都能让代码更简洁、更可靠。掌握它的用法能省不少麻烦，代码质量也能上个台阶。

# 32 . xml

## 参考文档1

## 一、Python XML解析

在Python中，解析XML文件通常使用内置的`xml.etree.ElementTree`模块，它提供了一个轻量级、高效的方式来解析XML文档。此外，还有其他的第三方库，如`lxml`和`xml.dom`，它们提供了更多的功能和灵活性。

下面是使用`xml.etree.ElementTree`模块解析XML文件的一个基本示例：

首先，假设你有一个名为`example.xml`的XML文件，内容如下：

```xml
<root>
    <element1 attribute="value1">
        <subelement1>Text inside subelement1</subelement1>
        <subelement2 attribute2="value2">Text inside subelement2</subelement2>
    </element1>
    <element2>
        <subelement3>Text inside subelement3</subelement3>
    </element2>
</root>
```

接下来，你可以使用`xml.etree.ElementTree`来解析这个文件：

```python
import xml.etree.ElementTree as ET

# 解析XML文件
tree = ET.parse('example.xml')
root = tree.getroot()

# 遍历所有子元素
for child in root:
    print(child.tag, child.attrib)  # 打印标签名和属性

    # 遍历子元素的子元素
    for subchild in child:
        print(subchild.tag, subchild.attrib, subchild.text)  # 打印子标签名、属性和文本内容

# 查找具有特定标签的元素
for element in root.iter('subelement1'):
    print(element.text)  # 打印subelement1的文本内容

# 查找具有特定属性的元素
for element in root.iter('subelement2'):
    print(element.attrib)  # 打印subelement2的属性
```

上面的代码示例演示了如何使用`xml.etree.ElementTree`来解析XML文件，并遍历其中的元素和属性。`iter()`方法用于查找具有特定标签的元素。

## 二、Python 操作XML

在Python中操作XML文件通常涉及读取、解析、修改和写入XML内容。下面是一个使用`xml.etree.ElementTree`模块来操作XML文件的案例。

首先，我们创建一个简单的XML文件`example.xml`：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<students>
    <student rollno="101">
        <firstname>John</firstname>
        <lastname>Doe</lastname>
        <marks>95</marks>
    </student>
    <student rollno="102">
        <firstname>Jane</firstname>
        <lastname>Doe</lastname>
        <marks>88</marks>
    </student>
</students>
```

接下来，我们将使用Python代码来读取这个XML文件，对其进行修改，然后再写入到一个新的文件中。

```python
import xml.etree.ElementTree as ET

# 读取XML文件
tree = ET.parse('example.xml')
root = tree.getroot()

# 遍历所有学生并打印他们的信息
for student in root.findall('student'):
    rollno = student.get('rollno')
    firstname = student.find('firstname').text
    lastname = student.find('lastname').text
    marks = student.find('marks').text
    print(f"Student Roll No: {rollno}, Name: {firstname} {lastname}, Marks: {marks}")

# 修改学生信息
for student in root.findall('student'):
    if student.get('rollno') == '101':
        # 修改第一个学生的成绩
        student.find('marks').text = '98'

# 写入到新的XML文件
tree.write('modified_example.xml')
```

运行上面的代码后，你会在控制台看到每个学生的信息，并且`modified_example.xml`文件会被创建或覆盖，其中第一个学生的成绩被更新为`98`：

```xml
<?xml version='1.0' encoding='UTF-8'?>
<students>
    <student rollno="101">
        <firstname>John</firstname>
        <lastname>Doe</lastname>
        <marks>98</marks>  <!-- 这里成绩被修改了 -->
    </student>
    <student rollno="102">
        <firstname>Jane</firstname>
        <lastname>Doe</lastname>
        <marks>88</marks>
    </student>
</students>
```

在这个案例中，我们展示了如何使用`xml.etree.ElementTree`来解析XML文件，遍历元素，修改元素内容，并将修改后的XML写回到文件中。`findall`方法用于查找所有匹配的元素，`find`方法用于查找第一个匹配的元素，`get`方法用于获取元素的属性值。`write`方法用于将修改后的树写回到文件中。

如果你想执行更复杂的XML操作，比如添加新的元素或删除现有的元素，你可以使用`SubElement`和`remove`方法。此外，`lxml`库提供了更多功能和灵活性，特别是当处理大型或复杂的XML文件时。

## 三、ContentHandler 类方法介绍

在Python中，`ContentHandler` 类通常与`xml.sax`模块相关联，它是SAX（Simple API for XML）解析器中的一个关键组件。SAX是一个基于事件的XML解析方法，而`ContentHandler`则是定义这些事件处理程序的基类。通过继承`ContentHandler`类并重写其方法，你可以自定义XML解析过程中的行为。

下面是一些`ContentHandler`类的主要方法及其描述：

- `startDocument()`: 当文档开始解析时被调用。
- `endDocument()`: 当文档解析结束时被调用。
- `startElement(name, attrs)`: 当遇到XML元素的开始标签时被调用，`name`是元素的名称，`attrs`是元素的属性字典。
- `endElement(name)`: 当遇到XML元素的结束标签时被调用，`name`是元素的名称。
- `characters(content)`: 当遇到XML元素或属性的字符数据时被调用，`content`是字符数据的内容。

下面是一个使用`ContentHandler`类的简单案例代码，该代码读取一个XML文件并打印出所有元素的名称和属性：

```python
import xml.sax
from xml.sax.handler import ContentHandler

class MyContentHandler(ContentHandler):
    def startElement(self, name, attrs):
        print(f"开始元素: {name}")
        for attr_name, attr_value in attrs.items():
            print(f"  属性: {attr_name} = {attr_value}")

    def endElement(self, name):
        print(f"结束元素: {name}")

    def characters(self, content):
        print(f"字符数据: {content.strip()}")

# 创建一个SAX解析器
parser = xml.sax.make_parser()

# 将自定义的ContentHandler关联到解析器
parser.setContentHandler(MyContentHandler())

# 打开XML文件并解析
with open('example.xml', 'r') as f:
    parser.parse(f)
```

在这个案例中，我们创建了一个`MyContentHandler`类，它继承自`ContentHandler`。我们重写了`startElement`、`endElement`和`characters`方法来处理XML文档中的不同事件。然后，我们创建了一个SAX解析器，并将我们的`MyContentHandler`实例设置为解析器的内容处理程序。最后，我们打开XML文件并使用解析器进行解析。

请注意，这个案例仅打印了元素名称、属性和字符数据。在实际应用中，你可能需要根据XML文档的结构和内容进行更复杂的处理。此外，SAX解析器是基于事件的，因此它通常比DOM解析器更快，特别是在处理大型XML文件时。

## 参考文档2 ： https://www.cnblogs.com/qing-chen/p/7289202.html

## 参考文档3： https://www.cnblogs.com/kn-zheng/p/17013201.html

# 33 . string

# python string模块详解



**简介** 在python编程程序时经常要使用到对字符的处理功能，字符在python中被分为好几类，比如字母、数字、其它字符等，这样在处理时需要程序员针对不同类型进行不同对待。为了方便

   在python编程程序时经常要使用到对字符的处理功能，字符在python中被分为好几类，比如字母、数字、其它字符等，这样在处理时需要程序员针对不同类型进行不同对待。为了方便大家对各类字符数据的处理和操作，在python语言中，提供一个字符串模块，叫string模块。Python中的string模块用于对字符串的一些分类和操作，下面整理了string的主要常量、函数及用法。
  string模块在使用时要导入模块,使用如下命令：

```python
import string
```

## 字符串常量

| 常数                       | 含义                                                 |
| -------------------------- | ---------------------------------------------------- |
| **string.ascii_lowercase** | 小写字母'abcdefghijklmnopqrstuvwxyz'                 |
| **string.ascii_uppercase** | 大写的字母'ABCDEFGHIJKLMNOPQRSTUVWXYZ'               |
| **string.ascii_letters**   | ascii_lowercase和ascii_uppercase常量的连接串         |
| **string.digits**          | 数字0到9的字符串:'0123456789'                        |
| string.hexdigits           | 字符串'0123456789abcdefABCDEF'                       |
| string.octdigits           | 字符串'01234567'                                     |
| string.punctuation         | 所有标点字符                                         |
| string.printable           | 可打印的字符的字符串。包含数字、字母、标点符号和空格 |
| string.whitespace          | 空白字符 '\t\n\x0b\x0c\r '                           |

例如代码如下：

```python
import string
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.ascii_letters)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print(string.punctuation)
```

程序运行屏幕显示为：
![img](https://www.ddbji.com/d/file/2022/03/07772.png)

## 常用方法，这些其实是str类的方法

| 常用方法                                     | 描述                                                         |
| -------------------------------------------- | ------------------------------------------------------------ |
| str.capitalize()                             | 把字符串的首字母大写                                         |
| str.center(width)                            | 将原字符串用空格填充成一个长度为width的字符串，原字符串内容居中 |
| str.count(s)                                 | 返回字符串s在str中出现的次数                                 |
| str.decode(encoding='UTF-8',errors='strict') | 以指定编码格式解码字符串                                     |
| str.encode(encoding='UTF-8',errors='strict') | 以指定编码格式编码字符串                                     |
| str.endswith(s)                              | 判断字符串str是否以字符串s结尾                               |
| str.find(s)                                  | 返回字符串s在字符串str中的位置索引，没有则返回-1             |
| str.index(s)                                 | 和find()方法一样，但是如果s不存在于str中则会抛出异常         |
| str.isalnum()                                | 如果str至少有一个字符并且都是字母或数字则返回True,否则返回False |
| str.isalpha()                                | 如果str至少有一个字符并且都是字母则返回True,否则返回False    |
| str.isdigit()                                | 如果str只包含数字则返回 True 否则返回 False                  |
| str.islower()                                | 如果str存在区分大小写的字符，并且都是小写则返回True 否则返回False |
| str.isspace()                                | 如果str中只包含空格，则返回 True，否则返回 False             |
| str.istitle()                                | 如果str是标题化的(单词首字母大写)则返回True，否则返回False   |
| str.isupper()                                | 如果str存在区分大小写的字符，并且都是大写则返回True 否则返回False |
| str.ljust(width)                             | 返回一个原字符串左对齐的并使用空格填充至长度width的新字符串  |
| str.lower()                                  | 转换str中所有大写字符为小写                                  |
| str.lstrip()                                 | 去掉str左边的不可见字符                                      |
| str.partition(s)                             | 用s将str切分成三个值                                         |
| str.replace(a, b)                            | 将字符串str中的a替换成b                                      |
| str.rfind(s)                                 | 类似于 find()函数，不过是从右边开始查找                      |
| str.rindex(s)                                | 类似于 index()，不过是从右边开始                             |
| str.rjust(width)                             | 返回一个原字符串右对齐的并使用空格填充至长度width的新字符串  |
| str.rpartition(s)                            | 类似于 partition()函数,不过是从右边开始查找                  |
| str.rstrip()                                 | 去掉str右边的不可见字符                                      |
| str.split(s)                                 | 以s为分隔符切片str                                           |
| str.splitlines()                             | 按照行分隔，返回一个包含各行作为元素的列表                   |
| str.startswith(s)                            | 检查字符串str是否是以s开头，是则返回True，否则返回False      |
| str.strip()                                  | 等于同时执行rstrip()和lstrip()                               |
| str.title()                                  | 返回"标题化"的str,所有单词都是以大写开始，其余字母均为小写   |
| str.upper()                                  | 返回str所有字符为大写的字符串                                |
| str.zfill(width)                             | 返回长度为 width 的字符串，原字符串str右对齐，前面填充0      |

# 34. difflib

# [difflib模块详解 ](https://www.cnblogs.com/machangwei-8/p/15583728.html)

## 1、两个字符串对比

![img](https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif)

[![复制代码](https://assets.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
import difflib
text1=""" test1 #定义字符串
hellow
my name is machanwei!
difflib document v7.4
add str
"""
text1_lines=text1.splitlines() #以行进行分隔，以便进行对比
text2="""text2:   #定义字符串2
hellow
my name is machangwei!
difflib document v7.5
"""
text2_lines=text2.splitlines()
d=difflib.Differ()  #创建Differ()对象
diff=d.compare(text1_lines,text2_lines)    #采用compare方法对字符串进行比较
print('\n'.join(list(diff)))
```

[![复制代码](https://assets.cnblogs.com/images/copycode.gif)](javascript:void(0);)

执行结果：

![img](https://img2020.cnblogs.com/blog/1286512/202111/1286512-20211121104648106-255642880.png)

 

 \- + 好像分别代表不同的文本，来区分文本用。这里-是1的，+是文本2的。？是有区别的地方，有区别的地方会标记箭头，只有-没有+，也就是不是成对出现应该是只有某一方有文本

![img](https://img2020.cnblogs.com/blog/1286512/202111/1286512-20211121105540167-710991530.png)

 ![img](https://img2020.cnblogs.com/blog/1286512/202111/1286512-20211121110230268-717721161.png)

[回到顶部](https://www.cnblogs.com/machangwei-8/p/15583728.html#_labelTop)

## 2、对比文件生成html文档

执行生成html语句

![img](https://img2020.cnblogs.com/blog/1286512/202111/1286512-20211121110637409-331419722.png)

(venv) D:\python_mcw>python python自动化运维书\difflib模块学习.py >>..\diffres.html

 ![img](https://img2020.cnblogs.com/blog/1286512/202111/1286512-20211121111735999-1060091968.png)

 

 挺好对比的

![img](https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif)

[![复制代码](https://assets.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
import difflib
text1=""" test1 #定义字符串
hellow
my name is machanwei!
difflib document v7.4
add str
"""
text1_lines=text1.splitlines() #以行进行分隔，以便进行对比
text2="""text2:   #定义字符串2
hellow
my name is machangwei!
difflib document v7.5
"""
text2_lines=text2.splitlines()

# #将下面的
# d=difflib.Differ()  #创建Differ()对象
# diff=d.compare(text1_lines,text2_lines)    #采用compare方法对字符串进行比较
# print('\n'.join(list(diff)))

#替换成下面这些：
d=difflib.HtmlDiff()
print(d.make_file(text1_lines,text2_lines))
```

[![复制代码](https://assets.cnblogs.com/images/copycode.gif)](javascript:void(0);)

![img](https://img2020.cnblogs.com/blog/1286512/202111/1286512-20211121111939239-530207107.png)

[回到顶部](https://www.cnblogs.com/machangwei-8/p/15583728.html#_labelTop)

## 3、对比文件差异

![img](https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif)

[![复制代码](https://assets.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
[root@hecs-358404 ~]# cat mcw.py 
# __*__ coding:utf-8 _*_
#!/usr/bin/env python
import difflib
import sys

try:
    mcwfile1=sys.argv[1]  #第一个配置文件路径参数
    mcwfile2=sys.argv[2] #第二个配置文件路径参数
except Exception as e:
    print("Error："+str(e))
    print("Usage: mcw.py  mcwfile1 mcwfile2")
    sys.exit()

def readfile(filename): #文件读取分隔函数
    try:
        fileHandle=open(filename,'rb')
        text=fileHandle.read().splitlines()   #读取后以行进行分隔
        fileHandle.close()
        return text
    except IOError as error:
        print('Read file Error:'+str(error))
        sys.exit()
if mcwfile1=="" or mcwfile2=="":
    print("Usage: mcw.py  mcwfile1 mcwfile2")
    sys.exit()
text1_lines=readfile(mcwfile1) #调用函数，获取分隔后的字符串
text2_lines=readfile(mcwfile2)
d=difflib.HtmlDiff()
print(d.make_file(text1_lines,text2_lines))
```

[![复制代码](https://assets.cnblogs.com/images/copycode.gif)](javascript:void(0);)

![img](https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif)

[![复制代码](https://assets.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
server {

       listen       80;

       server_name  blog.etiantian.org;

       location / {

                root   html/blog;

                index  index.html index.htm;

          }

        location ~* .*\.(php|php5)?$ {

          root html/blog;

              fastcgi_pass  127.0.0.1:9000;

              fastcgi_index index.php;

              include fastcgi.conf;

          }

}
```

[![复制代码](https://assets.cnblogs.com/images/copycode.gif)](javascript:void(0);)

![img](https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif)

[![复制代码](https://assets.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
#server {

       listen       80;

            server_name  blog.etiantian.org;

       location / {

                root   html/blog;

                index  index.html index.htm;

          }

        machangwei
        location ~* .*\.(php|php5)?$ {

          root html/blog;

              fastcgi_pass  127.0.0.1:9000;

              fastcgi_index index.php;

              include fastcgi.conf;

          }
        fffffff
}
```

[![复制代码](https://assets.cnblogs.com/images/copycode.gif)](javascript:void(0);)

![img](https://img2020.cnblogs.com/blog/1286512/202111/1286512-20211121115108511-752117355.png)

 

 对比结果如下：

![img](https://img2020.cnblogs.com/blog/1286512/202111/1286512-20211121115413650-572304161.png)

 

 ![img](https://img2020.cnblogs.com/blog/1286512/202111/1286512-20211121120419412-1599113988.png)

 



# 35. **textwrap**

### extwrap

在Python中，处理文本是一项常见且重要的任务。无论是生成报告、发送邮件还是处理用户输入，良好的文本格式都是确保信息清晰传达的关键。textwrap库是Python标准库中的一个模块，它提供了一系列功能强大的工具，帮助开发者轻松地对文本进行包装、缩进和填充。

Python官方文档：[textwrap模块](https://cloud.tencent.com/developer/tools/blog-entry?target=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftextwrap.html&objectId=2520823&objectType=1&contentType=undefined)

**直白一点来说就是：**

`textwrap` 库可以帮你把长长的文字，分成几行，让它看起来更整齐，就像把长长的纸条折成几段一样。 它可以帮你控制每行的长度，也可以帮你把文字自动换行，避免一行文字太长。 简单来说，它就是个帮文字“排版”的小工具。

#### 应用场景

1. 格式化日志输出：    
   - 在日志记录中，经常需要将日志条目格式化为特定宽度，以便于阅读和分析。textwrap库可以帮助将日志信息自动换行和填充，确保每行不超过指定的字符数。
2. 生成报告：    
   - 在生成文本报告时，可能需要将长文本缩短或包装以适应报告布局。textwrap库的fill和shorten函数可以派上用场，确保报告内容既美观又易于阅读。
3. 用户界面文本显示：    
   - 在[命令行工具](https://cloud.tencent.com/product/cli?from_column=20065&from=20065)或图形用户界面中，文本信息的显示需要符合一定的格式要求。textwrap库可以用于调整文本宽度、添加缩进等，以提高文本的可读性和美观性。
4. 帮助信息和文档：    
   - 编写命令行脚本时，提供美观的帮助信息对于用户体验至关重要。textwrap库可以帮助格式化帮助文本，使其更加清晰易读。
   - 在文档编写中，textwrap库也可以用于调整段落宽度、添加缩进等，使文档内容更加整齐。
5. 自动化脚本和CLI应用程序：    
   - 在自动化脚本和CLI（命令行界面）应用程序中，textwrap库可以用于处理用户输入和输出文本，确保文本信息在终端中正确显示。
6. 文本处理和转换：    
   - 在文本处理和转换任务中，textwrap库可以用于去除文本中的不必要缩进、添加缩进或进行文本包装等预处理操作。
7. 数据整理：    
   - 从文件中读取的数据可能包含不一致的空白或缩进，textwrap库的dedent函数可以帮助去除这些不必要的空白，使数据更加整洁。
8. 社交媒体和消息传递：    
   - 在社交媒体或消息传递应用程序中，发送的文本信息可能需要符合特定的字符限制。textwrap库的shorten函数可以用于缩短文本并添加占位符，以符合这些限制。

#### 基本功能：文本包装

textwrap.fill()和textwrap.wrap()是textwrap库中最基础的两个函数，它们用于将长文本分割成指定宽度的多行文本。

##### textwrap.fill(text, width, **kwargs)

将文本text按width指定的宽度进行包装，并返回包装后的多行字符串。

代码语言：javascript

AI代码解释



```javascript
import textwrap

text = "Python的textwrap库是一个非常有用的文本处理工具，它可以帮助我们轻松地对长文本进行包装。"
wrapped_text = textwrap.fill(text, 20)
print(wrapped_text)
```

输出：

代码语言：javascript

AI代码解释



```javascript
Python的textwrap库是一个非
常有用的文本处理工具，它可以帮助我们轻松
地对长文本进行包装。
```

##### textwrap.wrap(text, width, **kwargs)

与fill()类似，但返回的是一个字符串列表，每个元素代表一行。

代码语言：javascript

AI代码解释



```javascript
wrapped_lines = textwrap.wrap(text, 20)
for line in wrapped_lines:
    print(line)
```

输出与fill()相同，但每行作为独立的字符串输出。

代码语言：javascript

AI代码解释



```javascript
Python的textwrap库是一个非
常有用的文本处理工具，它可以帮助我们轻松
地对长文本进行包装。
```

#### 高级功能：缩进与填充

除了基本的文本包装，textwrap库还提供了对文本进行缩进和填充的功能。

##### textwrap.indent(text, prefix)

为文本text的每一行添加前缀prefix。

代码语言：javascript

AI代码解释



```javascript
indented_text = textwrap.indent(wrapped_text, '    ')
print(indented_text)
```

输出：

代码语言：javascript

AI代码解释



```javascript
    Python的textwrap库是一个非常有用的文本处理工具，它可以帮助我们轻松地对长文本进行包装。
```

##### textwrap.dedent(text)

去除文本text中所有行的共同缩进。

代码语言：javascript

AI代码解释



```javascript
import textwrap
txt = '   这是一个有缩进的文本。'
dedented_text = textwrap.dedent(txt)
print(dedented_text)
```

输出：

代码语言：javascript

AI代码解释



```javascript
这是一个有缩进的文本。
```

##### 填充（Padding）

虽然textwrap库没有直接提供填充函数，但可以通过组合其他函数实现类似效果。例如，使用str.ljust或str.rjust在文本前后添加空格。

#### 自定义行为：初始缩进与后续缩进

textwrap库允许用户自定义文本的首行缩进和后续行缩进。

##### initial_indent和subsequent_indent

这两个参数可以分别设置首行和后续行的缩进。

代码语言：javascript

AI代码解释



```javascript
import textwrap
text = "Python的textwrap库是一个非常有用的文本处理工具，它可以帮助我们轻松地对长文本进行包装。"
custom_wrapped_text = textwrap.fill(text, 20, initial_indent='* ', subsequent_indent='  * ')
print(custom_wrapped_text)
```

输出：

代码语言：javascript

AI代码解释



```javascript
* Python的textwrap库是一
  * 个非常有用的文本处理工具，它可以
  * 帮助我们轻松地对长文本进行包装。
```

#### 处理空白字符

textwrap库提供了一些参数来控制空白字符的处理，如expand_tabs、replace_whitespace和fix_sentence_endings。

1. expand_tabs：将制表符（\t）转换为空格。
2. replace_whitespace：将所有连续的空白字符替换为单个空格。
3. fix_sentence_endings：尝试修复句子末尾的空格，以便更好地进行包装。

代码语言：javascript

AI代码解释



```javascript
import textwrap
text = "" \
       "Python的textwrap库是一个非常有用的文本处理工具，   它可以帮助我们轻松地对长文本进行包装。    "
fixed_text = textwrap.fill(text, 20, expand_tabs=True, replace_whitespace=True, fix_sentence_endings=True)
print(fixed_text)
```

输出：

代码语言：javascript

AI代码解释



```javascript
Python的textwrap库是一个非
常有用的文本处理工具，
它可以帮助我们轻松地对长文本进行包装。
```

#### textwrap库的主要函数及其参数

| 函数名                                     | 描述                                       | 主要参数                                                     |
| :----------------------------------------- | :----------------------------------------- | :----------------------------------------------------------- |
| fill(text, width)                          | 按指定宽度包装文本并返回字符串             | text（待包装文本），width（每行宽度），initial_indent，subsequent_indent，expand_tabs，replace_whitespace，fix_sentence_endings，drop_whitespace，break_long_words，break_on_hyphens |
| wrap(text, width)                          | 按指定宽度包装文本并返回字符串列表         | 同上                                                         |
| indent(text, prefix)                       | 为文本每一行添加前缀                       | text（待缩进文本），prefix（前缀字符串）                     |
| dedent(text)                               | 去除文本所有行的共同缩进                   | text（待去缩进文本）                                         |
| shorten(text, width, placeholder=' [...]') | 缩短文本以适应指定宽度，并在末尾添加占位符 | text（待缩短文本），width（最大宽度），placeholder（占位符，默认为’ […]'） |

# 36 . **heapq**

**一、heapq库简介**

heapq 库是Python标准库之一，提供了构建小顶堆的方法和一些对小顶堆的基本操作方法(如入堆，出堆等)，可以用于实现堆排序算法。

堆是一种基本的数据结构，堆的结构是一棵完全二叉树，并且满足堆积的性质：每个节点(叶节点除外)的值都大于等于(或都小于等于)它的子节点。

堆结构分为大顶堆和小顶堆，在heapq中使用的是小顶堆：

1. 大顶堆：每个节点(叶节点除外)的值都大于等于其子节点的值，根节点的值是所有节点中最大的。
2. 小顶堆：每个节点(叶节点除外)的值都小于等于其子节点的值，根节点的值是所有节点中最小的。

在heapq库中，heapq使用的数据类型是Python的基本数据类型 list ，要满足堆积的性质，则在这个列表中，索引 k 的值要小于等于索引 2*k+1 的值和索引 2*k+2 的值(在完全二叉树中，将数据按广度优先插入，索引为k的节点的子节点索引分别为2*k+1和2*k+2)。在heapq库的源码中也有介绍，可以读一下heapq的源码，代码不多。

使用Python实现堆排序可以参考：Python实现堆排序

完全二叉树的特性可以参考：二叉树简介

**二、使用heapq创建堆**

代码语言：javascript

AI代码解释



```javascript
# coding=utf-8
import heapq


array = [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]
heap = []
for num in array:
    heapq.heappush(heap, num)
print("array:", array)
print("heap: ", heap)

heapq.heapify(array)
print("array:", array)
```

运行结果：

代码语言：javascript

AI代码解释



```javascript
array: [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]
heap:  [5, 7, 21, 15, 10, 24, 27, 45, 17, 30, 36, 50]
array: [5, 7, 21, 10, 17, 24, 27, 45, 15, 30, 36, 50]
```

heapq中创建堆的方法有两种。

heappush(heap, num)，先创建一个空堆，然后将数据一个一个地添加到堆中。每添加一个数据后，heap都满足小顶堆的特性。

heapify(array)，直接将数据列表调整成一个小顶堆(调整的原理参考上面堆排序的文章，heapq库已经实现了)。

两种方法实现的结果会有差异，如上面的代码中，使用heappush(heap, num)得到的堆结构如下。

![img](https://ask.qcloudimg.com/http-save/yehe-8302741/bkxechx923.png)

使用heapify(array)得到的堆结构如下。

![img](https://ask.qcloudimg.com/http-save/yehe-8302741/wzyzfztnyj.png)

不过，这两个结果都满足小顶堆的特性，不影响堆的使用(堆只会从堆顶开始取数据，取出数据后会重新调整结构)。

**三、使用heapq实现堆排序**

代码语言：javascript

AI代码解释



```javascript
array = [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]
heap = []
for num in array:
    heapq.heappush(heap, num)
print(heap[0])
# print(heapq.heappop(heap))
heap_sort = [heapq.heappop(heap) for _ in range(len(heap))]
print("heap sort result: ", heap_sort)
```

运行结果：

代码语言：javascript

AI代码解释



```javascript
5
heap sort result:  [5, 7, 10, 15, 17, 21, 24, 27, 30, 36, 45, 50]
```

先将待排序列表中的数据添加到堆中，构造一个小顶堆，打印第一个数据，可以确认它是最小值。然后依次将堆顶的值取出，添加到一个新的列表中，直到堆中的数据取完，新列表就是排序后的列表。

heappop(heap)，将堆顶的数据出堆，并将堆中剩余的数据构造成新的小顶堆。

**四、获取堆中的最小值或最大值**

代码语言：javascript

AI代码解释



```javascript
array = [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]
heapq.heapify(array)
print(heapq.nlargest(2, array))
print(heapq.nsmallest(3, array))
```

运行结果：

代码语言：javascript

AI代码解释



```javascript
[50, 45]
[5, 7, 10]
```

nlargest(num, heap)，从堆中取出num个数据，从最大的数据开始取，返回结果是一个列表(即使只取一个数据)。如果num大于等于堆中的数据数量，则从大到小取出堆中的所有数据，不会报错，相当于实现了降序排序。

nsmallest(num, heap)，从堆中取出num个数据，从最小的数据开始取，返回结果是一个列表。

这两个方法除了可以用于堆，也可以直接用于列表，功能一样。

**五、使用heapq合并两个有序列表**

代码语言：javascript

AI代码解释



```javascript
array_a = [10, 7, 15, 8]
array_b = [17, 3, 8, 20, 13]
array_merge = heapq.merge(sorted(array_a), sorted(array_b))
print("merge result:", list(array_merge))
```

运行结果：

代码语言：javascript

AI代码解释



```javascript
merge result: [3, 7, 8, 8, 10, 13, 15, 17, 20]
```

merge(list1, list2)，将两个有序的列表合并成一个新的有序列表，返回结果是一个迭代器。这个方法可以用于归并排序。

**六、heapq替换数据的方法**

代码语言：javascript

AI代码解释



```javascript
array_c = [10, 7, 15, 8]
heapq.heapify(array_c)
print("before:", array_c)
# 先push再pop
item = heapq.heappushpop(array_c, 5)
print("after: ", array_c)
print(item)

array_d = [10, 7, 15, 8]
heapq.heapify(array_d)
print("before:", array_d)
# 先pop再push
item = heapq.heapreplace(array_d, 5)
print("after: ", array_d)
print(item)
```

运行结果：

代码语言：javascript

AI代码解释



```javascript
before: [7, 8, 15, 10]
after:  [7, 8, 15, 10]
5
before: [7, 8, 15, 10]
after:  [5, 8, 15, 10]
7
```

heappushpop(heap, num)，先将num添加到堆中，然后将堆顶的数据出堆。

heapreplace(heap, num)，先将堆顶的数据出堆，然后将num添加到堆中。

两个方法都是即入堆又出堆，只是顺序不一样，可以用于替换堆中的数据。具体的区别可以看代码中的例子

# 37. **bisect**

## Python中的二分查找：Bisect库详解与实战

在算法和数据结构中，[二分查找](https://zhida.zhihu.com/search?content_id=238285114&content_type=Article&match_order=1&q=二分查找&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzgyNTA3MTEsInEiOiLkuozliIbmn6Xmib4iLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyMzgyODUxMTQsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.Gf3tFaYzuXLf9PJQyzWLxNCh9mi9rWlyigmvNLxErF0&zhida_source=entity)是一种高效的搜索算法，可用于有序数据集合的查找。Python的`bisect`库为我们提供了便捷的二分查找实现。本文将深入探讨Bisect库的使用方法、性能优势，并通过丰富的示例代码展示其在实际应用中的灵活性和效果。

## **安装与基础用法**

首先，需要安装`bisect`库：

```text
pip install bisect
```

Bisect库提供了两个主要的函数：`bisect_left`和`bisect_right`，用于查找元素在有序序列中的插入点。

以下是基础用法示例：

```text
import bisect

# 示例有序列表
sorted_list = [1, 3, 3, 5, 7, 9]

# 查找元素5的插入点
insert_point = bisect.bisect_left(sorted_list, 5)
print(f"元素5的插入点：{insert_point}")
```

## **库的高级特性**

### **1. 插入元素**

Bisect库不仅用于查找，还可以用于在有序序列中插入元素，保持序列的有序性：

```text
import bisect

# 示例有序列表
sorted_list = [1, 3, 3, 5, 7, 9]

# 插入元素4
bisect.insort_left(sorted_list, 4)
print(f"插入元素4后的列表：{sorted_list}")
```

### **2. 自定义比较函数**

Bisect库允许我们通过自定义比较函数来应对更复杂的数据结构：

```text
import bisect

# 示例复杂对象列表
class Item:
    def __init__(self, value):
        self.value = value

items = [Item(1), Item(3), Item(5), Item(7)]

# 自定义比较函数
def compare(item, value):
    return item.value - value

# 查找元素4的插入点
insert_point = bisect.bisect_left(items, 4, key=lambda x: compare(x, 4))
print(f"元素4的插入点：{insert_point}")
```

## **性能比较**

为了全面了解Bisect库在大型数据集上的性能表现，我们将其与传统的线性搜索进行对比。考虑一个有序列表，我们将在其中执行查找操作，分别使用Bisect库和线性搜索，并记录它们的执行时间。

### **使用Bisect库的性能**

```text
import bisect
import timeit

# 生成大型有序列表
large_sorted_list = list(range(1, 1000001))

# 测试Bisect库性能
def bisect_search():
    bisect.bisect_left(large_sorted_list, 500000)

bisect_time = timeit.timeit(bisect_search, number=1000)
print(f"Bisect库执行时间：{bisect_time} 秒")
```

### **使用线性搜索的性能**

```text
import timeit

# 测试线性搜索性能
def linear_search():
    target = 500000
    for i, num in enumerate(large_sorted_list):
        if num >= target:
            break

linear_time = timeit.timeit(linear_search, number=1000)
print(f"线性搜索执行时间：{linear_time} 秒")
```

通过比较上述两个例子的执行时间，可以清晰地了解Bisect库在大型数据集上的性能优势。在有序数据中执行查找操作时，Bisect库通常能够以更短的时间完成任务，这使得它成为处理大规模数据集时的首选工具。

## **实际应用场景**

假设有一个包含大量日志条目的日志文件，其中每个条目都包含一个时间戳。希望快速找到某个特定时间戳的日志条目。这是Bisect库的一个理想的实际应用场景。

```text
import bisect
import datetime

# 示例日志数据（假设按时间戳排序）
log_timestamps = [
    datetime.datetime(2023, 1, 1, 12, 0, 0),
    datetime.datetime(2023, 1, 1, 12, 15, 0),
    datetime.datetime(2023, 1, 1, 12, 30, 0),
    datetime.datetime(2023, 1, 1, 12, 45, 0),
    # ... 更多日志时间戳 ...
]

# 查找特定时间戳的日志条目
target_timestamp = datetime.datetime(2023, 1, 1, 12, 30, 0)
index = bisect.bisect_left(log_timestamps, target_timestamp)

if index != len(log_timestamps) and log_timestamps[index] == target_timestamp:
    print(f"找到时间戳为 {target_timestamp} 的日志条目，索引为 {index}")
else:
    print(f"未找到时间戳为 {target_timestamp} 的日志条目")
```

在这个实际的应用场景中，Bisect库帮助快速定位到特定时间戳的位置，而不需要遍历整个日志文件。这种高效的查找对于大型日志文件的处理至关重要，能够快速定位到感兴趣的时间戳对应的日志信息。

## **注意事项与最佳实践**

在使用Bisect库时，有一些注意事项和最佳实践，以确保正确性和性能。以下是一些建议：

1. **数据必须有序：** Bisect库要求输入的数据必须是有序的。在执行Bisect操作之前，请确保你的数据集已经按照需要的顺序排列。
2. **处理边界情况：** 考虑处理边界情况，确保你的代码能够正确处理查找目标值小于或大于整个数据集范围的情况。在使用`bisect_left`和`bisect_right`时，确保在边界情况下返回合适的索引。

```text
# 处理边界情况的示例
index = bisect.bisect_left(sorted_list, target)
if index == 0:
    print("目标值小于整个数据集范围")
elif index == len(sorted_list):
    print("目标值大于整个数据集范围")
else:
    print(f"目标值的插入点：{index}")
```

1. **异常处理：** 在实际应用中，考虑使用适当的异常处理机制，以处理可能的异常情况，如数据集未按顺序排列等。

```text
try:
    index = bisect.bisect_left(unsorted_list, target)
except ValueError as e:
    print(f"发生错误：{e}")
```

1. **性能考虑：** 考虑使用Bisect库的高级特性，如`insort_left`和`insort_right`，以在有序序列中执行元素的插入，避免手动维护有序性。

```text
# 示例：使用 insort_left 插入元素并保持有序性
bisect.insort_left(sorted_list, new_element)
```

1. **理解比较函数：** 当处理复杂对象时，理解比较函数的作用是至关重要的。确保比较函数返回负数、零或正数，以正确指示目标值在数据集中的位置。

```text
def compare(item, value):
    return item.value - value

index = bisect.bisect_left(items, target, key=lambda x: compare(x, target))
```

## **总结**

在本文中，深入探讨了Python中的Bisect库，一个专注于二分查找的强大工具。从基础用法开始，介绍了`bisect_left`和`bisect_right`的使用方式，以及如何插入元素并保持序列有序。通过性能比较，清晰展示了Bisect库在大型数据集上相对于线性搜索的优越性能。

进一步探讨了Bisect库的高级特性，如自定义比较函数、处理复杂对象等。通过实际应用场景的案例，展示了Bisect库在处理有序数据集时的实际价值，尤其在日志时间戳查找等实际问题中。最后，总结了使用Bisect库时的一些建议和最佳实践，包括数据必须有序、处理边界情况、异常处理、性能考虑等。帮助大家更好地理解和应用Bisect库，确保其在各种情况下都能够安全、高效地发挥作用。

总体而言，Bisect库作为Python的标准库之一，为开发者提供了一种简单而高效的二分查找工具，适用于各种有序数据集合的场景。通过学习本文，大家将更加熟练地运用Bisect库，提升搜索算法的效率，并在实际项目中更好地处理有序数据。

# 38. **operator**

## Python [operator模块](https://zhida.zhihu.com/search?content_id=240291458&content_type=Article&match_order=1&q=operator模块&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzgyNjkyOTUsInEiOiJvcGVyYXRvcuaooeWdlyIsInpoaWRhX3NvdXJjZSI6ImVudGl0eSIsImNvbnRlbnRfaWQiOjI0MDI5MTQ1OCwiY29udGVudF90eXBlIjoiQXJ0aWNsZSIsIm1hdGNoX29yZGVyIjoxLCJ6ZF90b2tlbiI6bnVsbH0.suqHLF8rTYgBQqXkTaYbRPoi-oXjxV_vf0pRaFD2BFM&zhida_source=entity)

Python的`operator`模块提供了一系列内置的操作符函数，这些函数对应于Python语言中的内建操作符。使用`operator`模块可以使代码更加清晰和易读，同时也能提高性能，因为它通常比使用Python内建操作符更快。

下面是一些`operator`模块中常用的函数：

### 1. 算术操作符

- `operator.add(a, b)`: 返回 `a + b`。
- `operator.sub(a, b)`: 返回 `a - b`。
- `operator.mul(a, b)`: 返回 `a * b`。
- `operator.truediv(a, b)`: 返回 `a / b`（浮点数除法）。
- `operator.floordiv(a, b)`: 返回 `a // b`（整数除法）。
- `operator.mod(a, b)`: 返回 `a % b`（取余）。
- `operator.pow(a, b)`: 返回 `a ** b`（幂运算）。
- `operator.neg(a)`: 返回 `-a`（取负）。
- `operator.pos(a)`: 返回 `+a`（取正）。
- `operator.abs(a)`: 返回 `abs(a)`（绝对值）。

### 2. 比较操作符

- `operator.eq(a, b)`: 如果 `a == b` 返回 `True`。
- `operator.ne(a, b)`: 如果 `a != b` 返回 `True`。
- `operator.lt(a, b)`: 如果 `a < b` 返回 `True`。
- `operator.le(a, b)`: 如果 `a <= b` 返回 `True`。
- `operator.gt(a, b)`: 如果 `a > b` 返回 `True`。
- `operator.ge(a, b)`: 如果 `a >= b` 返回 `True`。

### 3. 逻辑操作符

- `operator.and_(a, b)`: 返回 `a and b`（逻辑与）。
- `operator.or_(a, b)`: 返回 `a or b`（逻辑或）。
- `operator.not_(a)`: 返回 `not a`（逻辑非）。

### 4. 序列操作符

- `operator.concat(a, b)`: 返回 `a + b`（字符串或序列拼接）。
- `operator.contains(a, b)`: 如果 `b` 在 `a` 中，返回 `True`（例如，`b` 是否是 `a` 的子字符串或子序列）。
- `operator.countOf(a, b)`: 返回 `b` 在 `a` 中出现的次数（仅对序列有效）。
- `operator.indexOf(a, b, [start, [stop]])`: 返回 `b` 在 `a` 中首次出现的索引，如果 `b` 不在 `a` 中则返回 `-1`（仅对序列有效）。

### 5. 映射和集合操作符

- `operator.itemgetter(item)`: 返回一个可调用对象，该对象从其操作数中获取指定的项目。
- `operator.attrgetter(attr)`: 返回一个可调用对象，该对象从其操作数中获取指定的属性。
- `operator.methodcaller(method, *args, **kwargs)`: 返回一个可调用对象，该对象调用其操作数的指定方法。

### 6. 其他操作符

- `operator.truth(a)`: 如果 `a` 为真（即非零或非空），返回 `a`。
- `operator.false(a)`: 如果 `a` 为假（即零或空），返回 `a`。
- `operator.index(a)`: 返回 `a` 的“索引”值，这通常是 `a` 本身，但对于字符串，它返回字符串的哈希值。
- `operator.getitem(obj, index)`: 相当于 `obj[index]`，用于获取对象（通常是映射或序列）中指定索引或键的值。
- `operator.setitem(obj, index, value)`: 相当于 `obj[index] = value`，用于设置对象（通常是映射或序列）中指定索引或键的值。
- `operator.delitem(obj, index)`: 相当于 `del obj[index]`，用于删除对象（通常是映射或序列）中指定索引或键的项。
- `operator.has_key(obj, key)`: 检查对象（通常是映射）中是否包含指定的键，相当于 `key in obj`。注意：这个函数在Python 3中已被移除，应该使用`in`关键字替代。

这些函数可以作为`functools.reduce()`函数或其他需要二元操作符的函数的参数，以在映射上进行操作。

## 二、operator模块案例

### 1. 案例一

假设我们有一个字典，我们想使用`operator.getitem`来获取字典中某个键的值：

```python
import operator

# 创建一个字典
my_dict = {'a': 1, 'b': 2, 'c': 3}

# 使用 operator.getitem 获取键 'b' 的值
value = operator.getitem(my_dict, 'b')
print(value)  # 输出: 2
```

假设我们还有一个列表的列表（即二维列表），我们想使用`operator.getitem`来获取每个子列表的第一个元素：

```python
import operator

# 创建一个二维列表
two_dim_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 使用 operator.getitem 和 map 函数获取每个子列表的第一个元素
first_elements = list(map(operator.getitem, two_dim_list, [0]*len(two_dim_list)))
print(first_elements)  # 输出: [1, 4, 7]
```

在这个例子中，`map()`函数接受三个参数：`operator.getitem`函数，二维列表`two_dim_list`，以及一个包含多个0的列表（与`two_dim_list`的长度相同）。`map()`函数将`operator.getitem`应用到`two_dim_list`的每个子列表上，并使用0作为索引来获取每个子列表的第一个元素。

### 2. 示例二

```python
import operator

# 使用算术操作符
result = operator.add(3, 4)
print(result)  # 输出: 7

# 使用比较操作符
is_equal = operator.eq(result, 7)
print(is_equal)  # 输出: True

# 使用序列操作符
str1 = "Hello"
str2 = "World"
combined = operator.concat(str1, " ")
combined = operator.concat(combined, str2)
print(combined)  # 输出: Hello World
```

## 参考文档2

\```operator`` 模块为 Python 提供了一个 ``"功能性"` `的标准操作符接口. 当使用 ````map```` 以及`

\`````filter```` 一类的函数的时候, ``operator`` 模块中的函数可以替换一些 ````lambda```` 函式.`

```
而且这些函数在一些喜欢写晦涩代码的程序员中很流行. [Example ``1``-``62` `#eg-1-62] 展示了
```

\```operator`` 模块的一般用法.`

### 示例1

```
import operator
from functools import reduce
 
sequence = 1, 2, 4
 
print("add", "=>", reduce(operator.add, sequence))
print("sub", "=>", reduce(operator.sub, sequence)) 
print("mul", "=>", reduce(operator.mul, sequence)) 
print("concat", "=>", operator.concat("spam", "egg")) 
print("getitem", "=>", operator.getitem(sequence, 2))
print("indexOf", "=>", operator.indexOf(sequence, 2)) 

```

#### 参考网址：https://www.geeksforgeeks.org/python/operator-functions-in-python-set-1/




# 39 . **decimal**

## Python 精确计算：告别浮点数陷阱，[decimal 模块](https://zhida.zhihu.com/search?content_id=269374998&content_type=Article&match_order=1&q=decimal+模块&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzgyNzYyOTMsInEiOiJkZWNpbWFsIOaooeWdlyIsInpoaWRhX3NvdXJjZSI6ImVudGl0eSIsImNvbnRlbnRfaWQiOjI2OTM3NDk5OCwiY29udGVudF90eXBlIjoiQXJ0aWNsZSIsIm1hdGNoX29yZGVyIjoxLCJ6ZF90b2tlbiI6bnVsbH0.1Bk0GmE12mQ1Pc5B_gkTrND1XfEW9zwyegazIz-EElE&zhida_source=entity)实战指南

### 第一章：浮点数的“原罪”：为什么你的计算结果总是怪怪的？

在 Python 编程的世界里，有一个几乎每个开发者都会遇到的“灵异事件”：

```python
>>> 0.1 + 0.2
0.30000000000000004
```

明明是简单的加法，为什么结果却多出了长长的一串尾巴？如果你正在开发一个金融系统，或者处理任何对精度要求极高的场景，这种微小的误差简直是噩梦。

### 1.1 罪魁祸首：[IEEE 754](https://zhida.zhihu.com/search?content_id=269374998&content_type=Article&match_order=1&q=IEEE+754&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzgyNzYyOTMsInEiOiJJRUVFIDc1NCIsInpoaWRhX3NvdXJjZSI6ImVudGl0eSIsImNvbnRlbnRfaWQiOjI2OTM3NDk5OCwiY29udGVudF90eXBlIjoiQXJ0aWNsZSIsIm1hdGNoX29yZGVyIjoxLCJ6ZF90b2tlbiI6bnVsbH0.QPq8Ri78FnrOoHRHtHqrdfQxZ4w7_1_6ShUuY4iGUYs&zhida_source=entity) 标准

这并不是 Python 的 Bug，而是计算机处理浮点数的通用标准——IEEE 754 的特性。在二进制计算机中，无法精确表示所有的小数（就像十进制无法精确表示 1⁄3 一样）。`0.1` 和 `0.2` 在二进制中都是无限循环小数，计算机只能截断存储，导致了精度的丢失。

**真实案例：** 假设你正在编写一个简单的电商购物车程序：

```python
price = 2.30
quantity = 2
total = price * quantity
# 结果是 4.6000000000000005
# 如果你按照四舍五入显示给用户看可能没问题，但如果你需要累加成千上万次订单，这些微小的误差累积起来会非常惊人。
```

### 1.2 什么时候我们需要绝对精确？

虽然在做机器学习、图像处理或物理模拟时，这点误差通常可以忽略不计，但在以下领域，我们必须较真：

- **[金融计算](https://zhida.zhihu.com/search?content_id=269374998&content_type=Article&match_order=1&q=金融计算&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzgyNzYyOTMsInEiOiLph5Hono3orqHnrpciLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNjkzNzQ5OTgsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.M9jouXz7KE9nEGrgemtYb7KJ0VbbjdJ_e7OmZZKKFEA&zhida_source=entity)：** 利息、汇率、手续费计算，一分钱都不能差。
- **[支付网关](https://zhida.zhihu.com/search?content_id=269374998&content_type=Article&match_order=1&q=支付网关&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzgyNzYyOTMsInEiOiLmlK_ku5jnvZHlhbMiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNjkzNzQ5OTgsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.l_jE67-6Bb7nEHj0RxbYFDGjY6tx3N3ccAu67ctLKO4&zhida_source=entity)：** 涉及资金流转，必须保证账实相符。
- **[科学计算](https://zhida.zhihu.com/search?content_id=269374998&content_type=Article&match_order=1&q=科学计算&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzgyNzYyOTMsInEiOiLnp5HlraborqHnrpciLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNjkzNzQ5OTgsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.fhZyTvnbw4HiH_aFNKijLTDBFExP7bNeG-j25bssAt0&zhida_source=entity)：** 某些高精度实验数据的处理。

这就是为什么我们需要引入 Python 的 `decimal` 模块。

### 第二章：decimal 模块详解：高精度计算的守护神

Python 的 `decimal` 模块提供了一种替代数据类型 `Decimal`，它专为**浮点 arithmetic** 而设计，能够避免浮点数的精度问题。它实现了任意精度的十进制算术，是金融和货币计算的首选。

### 2.1 入门第一步：正确的初始化方式

使用 `decimal` 的第一步，也是最容易踩坑的一步，就是如何创建一个 Decimal 对象。

**❌ 错误的方式（精度已在传入时丢失）：**

```python
from decimal import Decimal
# 即使你用 Decimal 包装，它内部依然是浮点数的近似值
d = Decimal(0.1) 
print(d)  # 输出: Decimal('0.1000000000000000055511151231257827021181583404541015625')
```

**✅ 正确的方式（使用字符串初始化）：**

```python
from decimal import Decimal
# 传入字符串，decimal 会精确解析
d = Decimal('0.1')
print(d + Decimal('0.2'))  # 输出: Decimal('0.3')
```

> **核心原则：** 永远使用字符串来初始化 Decimal，除非你完全知道自己在做什么。

### 2.2 上下文（Context）：精度的控制中心

`decimal` 模块最强大的地方在于它的“上下文”（Context）。你可以把它想象成一个全局的配置环境，控制着计算的精度（precision）、舍入方式（rounding）以及溢出处理等。

```python
from decimal import Decimal, getcontext, ROUND_HALF_UP

# 查看当前默认上下文
print(getcontext())
# 默认精度通常是 28 位，舍入模式是 ROUND_HALF_EVEN（银行家舍入法）

# 修改全局精度为 6 位
getcontext().prec = 6

# 计算 1 / 7
print(Decimal('1') / Decimal('7'))  # 输出: Decimal('0.142857')

# 修改舍入模式为我们熟悉的“四舍五入”
getcontext().rounding = ROUND_HALF_UP

# 计算 2.5 舍入到整数
print(Decimal('2.5').quantize(Decimal('1')))  # 输出: Decimal('3')
```

### 2.3 常用舍入模式详解

在金融计算中，舍入方式至关重要。`decimal` 模块提供了多种舍入模式：

- **ROUND_CEILING (Ceiling):** 总是向无穷大方向舍入（正数向上，负数向零）。
- **ROUND_FLOOR (Floor):** 总是向负无穷方向舍入（正数向零，负数向下）。
- **ROUND_HALF_UP (四舍五入):** 我们最熟悉的模式。
- **ROUND_HALF_EVEN (银行家舍入):** 靠近偶数一边。这是默认模式，能减少累积误差。

**案例：计算利息** 假设我们需要计算 $10000 存款，年利率 3.5%，存期 1 年，结果保留两位小数。

```python
principal = Decimal('10000')
rate = Decimal('0.035')
interest = principal * rate

# 使用 quantize 方法进行小数点后两位的精确舍入
final_amount = interest.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
print(f"利息: {final_amount}")  # 利息: 350.00
```

### 第三章：decimal 实战技巧与避坑指南

掌握了基础语法后，我们需要深入实战，看看在复杂业务逻辑中如何优雅地使用 `decimal`。

### 3.1 避免混合运算陷阱

虽然 Python 3 的 `decimal` 做了优化，但在高性能计算中，混合使用 `int`、`float` 和 `Decimal` 仍然会产生不必要的转换开销，甚至引发 `TypeError`。

**建议：** 在涉及 `decimal` 的计算逻辑中，尽量保持类型统一。如果必须混合运算，显式转换比隐式转换更安全。

```python
# 推荐做法
amount = Decimal('100')
discount_rate = Decimal('0.9')
# 不要写 amount * 0.9，虽然 Python 3 允许，但最好写成：
final_price = amount * discount_rate
```

### 3.2 性能考量：速度与精度的平衡

`decimal` 是纯 Python 实现的（部分底层由 C 拓展支持），相比硬件加速的 float，它的运算速度要慢得多。

**测试对比（仅供参考）：**

- `float` 运算：极快，适合大规模科学计算。
- `decimal` 运算：较慢，适合少量但高精度的金融运算。

**优化策略：**

1. **仅在必要时使用：** 只有在涉及金额、库存、关键计量单位时才使用 `Decimal`。
2. **利用 `quantize` 批量处理：** 尽量减少中间计算过程的精度，尽早将结果 `quantize` 到业务需要的精度。

### 3.3 序列化与存储

当你需要将 Decimal 对象存入数据库或转换为 JSON 时，它会变成字符串。

```python
import json
from decimal import Decimal

data = {'price': Decimal('99.99')}
# 直接转 JSON 会报错，需要自定义 default 函数
# json.dumps(data) # TypeError: Object of type Decimal is not JSON serializable

# 正确做法
def decimal_to_str(obj):
    if isinstance(obj, Decimal):
        return str(obj)
    raise TypeError

json_str = json.dumps(data, default=decimal_to_str)
print(json_str)  # {"price": "99.99"}
```

在存入数据库（如 PostgreSQL 或 MySQL）时，通常建议使用字符串格式或者数据库原生的 `DECIMAL` 类型进行对接。

### 第四章：进阶应用：结合 logging 进行审计追踪

在金融或关键业务系统中，光算得准还不够，我们还需要**记录**每一笔计算的详细过程，以便审计和排查问题。这时，我们可以结合 Python 的 `logging` 模块。

### 4.1 为什么需要记录计算过程？

当用户投诉“这笔手续费算错了”时，如果你的日志里只有一行 `Calculated fee: 0.5`，你无法证明它是怎么来的。我们需要记录：

- 输入参数
- 使用的精度上下文
- 中间结果
- 最终结果

### 4.2 实战：构建一个带审计日志的计算类

下面是一个结合了 `decimal` 和 `logging` 的简单封装示例：

```python
import logging
from decimal import Decimal, getcontext, ROUND_HALF_UP

# 配置日志格式
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

class FinancialCalculator:
    def __init__(self, precision=4):
        self.precision = precision
        # 设置局部上下文
        getcontext().prec = precision + 2  # 计算过程保留更多位数，防止中间误差
        getcontext().rounding = ROUND_HALF_UP
        logger.info(f"计算器初始化，精度设置为: {precision}")

    def calculate_tax(self, amount, rate):
        """
        计算税额
        :param amount: 金额 (Decimal or str)
        :param rate: 税率 (Decimal or str)
        """
        # 强制转换为 Decimal，并记录输入
        amt = Decimal(str(amount))
        rt = Decimal(str(rate))
        
        logger.info(f"开始计算税额 | 输入金额: {amt}, 税率: {rt}")
        
        # 计算原始值
        raw_tax = amt * rt
        logger.debug(f"原始计算结果: {raw_tax}")
        
        # 最终舍入
        final_tax = raw_tax.quantize(Decimal('0.01'))
        
        logger.info(f"计算完成 | 税额: {final_tax}")
        return final_tax

# 使用示例
calc = FinancialCalculator(precision=6)
tax = calc.calculate_tax('1234.56', '0.08')
# 输出日志示例:
# 2023-10-27 10:00:00 - [INFO] - 计算器初始化，精度设置为: 6
# 2023-10-27 10:00:00 - [INFO] - 开始计算税额 | 输入金额: 1234.56, 税率: 0.08
# 2023-10-27 10:00:00 - [INFO] - 计算完成 | 税额: 98.76
```

通过这种方式，当出现问题时，我们可以通过日志回溯整个计算链路，确保每一笔钱的去向都有据可查。

### 总结

在 Python 开发中，`decimal` 模块是处理高精度计算的银弹。虽然它比原生的 `float` 稍显繁琐且性能稍低，但在金融、支付和关键业务领域，它提供的**数据准确性**和**安全性**是无价的。

**核心回顾：**

1. **初始化：** 永远使用 `Decimal('0.1')` 而不是 `Decimal(0.1)`。
2. **上下文：** 善用 `getcontext()` 控制精度和舍入。
3. **类型安全：** 避免与浮点数混用，保持类型纯净。
4. **审计：** 结合 `logging` 记录计算过程，让系统更加健壮。

**互动话题：** 你在开发中是否遇到过因为浮点数精度导致的“Bug”？或者在使用 `decimal` 时踩过什么坑？欢迎在评论区分享你的经历，我们一起避坑！

# 40. **fractions**

ractions模块提供了分数类型的支持。

------

## Fraction类

该类是fractions模块的核心，它继承了numbers.Rational类并且实现了该类所有的方法。

构造函数并不复杂：

class fractions.Fraction(numerator=0, denominator=1)
class fractions.Fraction(int|float|str|Decimal|Fraction)

可以同时提供分子（numerator）和分母（denominator）给构造函数用于实例化Fraction类，但两者必须同时是int类型或者numbers.Rational类型，否则会抛出类型错误。当分母为0，初始化的时候会导致抛出异常ZeroDivisionError。

而如果只提供一个参数，则可以用上述五种类型进行初始化。当使用字符串进行初始化时，fractions模块使用内置的正则表达式进行匹配。而使用浮点数或者Decimal进行初始化时，fractions模块会在内部调用as_integer_ratio()。

下面的代码示例来自官方文档，展示了各种实例化Fraction的方式：

```python
>>> from fractions import Fraction
>>> Fraction(16, -10)
Fraction(-8, 5)
>>> Fraction(123)
Fraction(123, 1)
>>> Fraction()
Fraction(0, 1)
>>> Fraction('3/7')
Fraction(3, 7)
>>> Fraction(' -3/7 ')
Fraction(-3, 7)
>>> Fraction('1.414213 \t\n')
Fraction(1414213, 1000000)
>>> Fraction('-.125')
Fraction(-1, 8)
>>> Fraction('7e-6')
Fraction(7, 1000000)
>>> Fraction(2.25)
Fraction(9, 4)
>>> Fraction(1.1)
Fraction(2476979795053773, 2251799813685248)
>>> from decimal import Decimal
>>> Fraction(Decimal('1.1'))
Fraction(11, 10)
```

### 限制分母

fractions.Fraction.limit_denominator(max_denominator=1000000)

有时候将浮点数或者Decimal作为Fraction实例的初始化数据可能会遇到舍入误差的问题，如上面调用`Fraction(1.1)`时不返回`Fraction(11, 10)`的例子。这时Fraction类提供了一个实例方法limit_denominator()用于减小这种误差。这个方法本来是为了通过限制分母来得到一个近似值，但是在出现舍入误差的时候反倒使得结果更加精确了，如下面的例子：

```python
>>> from fractions import Fraction
>>> Fraction(1.1)
Fraction(2476979795053773, 2251799813685248)
>>> Fraction(1.1).limit_denominator()
Fraction(11, 10)
```

### 将Fraction用于算术运算、关系运算和其他多种操作

上面提到，Fraction类继承了numbers.Rational类并且实现了该类所有的方法。所以Fraction类事实上通过重载很多特殊函数，使得其实例可以直接用于多种算术运算。

不仅支持算术运算，Fraction类同时也支持关系运算、pickle模块、copy模块和哈希值的计算。

```python
>>> from fractions import Fraction
>>> x = Fraction(1, 2)
>>> y = Fraction(1, 3)
>>> x + y
Fraction(5, 6)
>>> x - y
Fraction(1, 6)
>>> x * y
Fraction(1, 6)
>>> x / y
Fraction(3, 2)
>>> x ** 2
Fraction(1, 4)
>>> -x
Fraction(-1, 2)
>>> abs(x)
Fraction(1, 2)
>>> round(x)
0
>>> import math
>>> math.floor(x)
0
>>> math.ceil(x)
1
>>> x == y
False
>>> x > y
True
```

------

## 其他函数

fractions.Fraction.from_float(flt)
fractions.Fraction.from_decimal(dec)

在Python3.2之前，Fraction类不支持通过将浮点数和Decimal传入构造方法来获得实例。而是提供了上面两个类方法，通过调用类方法的方式来产生实例，目前版本（Python 3.6.1）这两个类方法仍然存在。

------

fractions.gcd(a, b)

用于计算最大公约数。这个函数在Python3.5之后就废弃了，官方建议使用math.gcd()

# 41. **urllib**

### **ython urllib库**

`Python urllib`库用于操作网页`URL`，并对网页的内容进行抓取处理。

`urllib`包 包含以下几个模块：

- `urllib.request` - 打开和读取`URL`。
- `urllib.error` - 包含`urllib.request`抛出的异常。
- `urllib.parse` - 解析`URL`。
- `urllib.robotparser` - 解析`robots.txt`文件。

需要用的就是每个模块的内置方法和函数。大概方法如下图：

![img](https://developer.qcloudimg.com/http-save/yehe-6888863/c1599f910c5d42327514afa3b489eba9.png)

### **urllib.request模块**

`urllib.request`定义了一些打开`URL`的函数和类，包含授权验证、重定向、浏览器`cookies`等。

`urllib.request`可以模拟浏览器的一个请求发起过程。

这里主要介绍两个常用方法，`urlopen`和`Request`。

#### **`urlopen`函数**

语法格式如下：

```javascript
urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
```

- `url`：`url`地址。
- `data`：发送到[服务器](https://cloud.tencent.com/product/cvm?from_column=20065&from=20065)的其他数据对象，默认为`None`。
- `timeout`：设置访问超时时间。
- `cafile` 和 `capath`：`cafile`为`CA`证书，`capath`为`CA`证书的路径，使用`HTTPS`需要用到。
- `cadefault`：已经被弃用。
- `context`：`ssl.SSLContext`类型，用来指定`SSL`设置。

示例：

```javascript
import urllib.request
#导入urllib.request模块
url=urllib.request.urlopen("https://www.baidu.com")
#打开读取baidu信息
print(url.read().decode('utf-8'))
#read获取所有信息，并decode()命令将网页的信息进行解码
```

运行结果

```javascript
<!DOCTYPE html><!--STATUS OK--><html><head><meta http-equiv="Content-Type" content="text/html;charset=utf-8"><meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"><meta content="always" name="
html{color:#000;overflow-y:scroll;overflow:-moz-scrollbars}
body,button,input,select,textarea{font-size:12px;font-family:Arial,sans-serif}  
h1,h2,h3,h4,h5,h6{font-size:100%}                  
em{font-style:normal}
small{font-size:12px}
ol,ul{list-style:none}
a{text-decoration:none}
a:hover{text-decoration:underline}
legend{color:#000}
fieldset,img{border:0}
button,input,select,textarea{font-size:100%} 
...
```

`response`对象是`http.client.HTTPResponse`类型，主要包含`read`、`readinto`、`getheader`、`getheaders`、`fileno`等方法，以及`msg`、`version`、`status`、`reason`、`debuglevel`、`closed`等属性。

常用方法：

- `read()`：是读取整个网页内容，也可以指定读取的长度，如`read(300)`。获取到的是二进制的乱码，所以需要用到`decode()`命令将网页的信息进行解码。
- `readline()`: 读取文件的一行内容。
- `readlines()`: 读取文件的全部内容，它会把读取的内容赋值给一个列表变量。
- `info()`：返回`HTTPMessage`对象，表示远程服务器返回的头信息。
- `getcode()`：返回`Http`状态码。如果是`http`请求，200请求成功完成;404网址未找到。
- `geturl()`：返回请求的链接。

#### **Request 类**

我们抓取网页一般需要对`headers`（网页头信息）进行模拟，否则网页很容易判定程序为爬虫，从而禁止访问。这时候需要使用到`urllib.request.Request`类：

```javascript
class urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
```

- `url`：`url`地址。
- `data`：发送到服务器的其他数据对象，默认为`None`。
- `headers`：`HTTP`请求的头部信息，字典格式。
- `origin_req_host`：请求的主机地址，`IP`或[域名](https://cloud.tencent.com/product/domain?from_column=20065&from=20065)。
- `unverifiable`：很少用整个参数，用于设置网页是否需要验证，默认是`False`。
- `method`：请求方法， 如 `GET`、`POST`、`DELETE`、`PUT`等。

示例：

```javascript
import urllib.request
#导入模块
url = "https://www.baidu.com"
#网页连接
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
}
#定义headers，模拟浏览器访问
req = urllib.request.Request(url=url,headers=headers)
#模拟浏览器发送，访问网页
response = urllib.request.urlopen(req)
#获取页面信息
print(response.read().decode("utf-8"))
```

### **urllib.error模块**

`urllib.error`模块为`urllib.request`所引发的异常定义了异常类，基础异常类是`URLError`。

`urllib.error`包含了两个方法，`URLError`和`HTTPError`。

`URLError`是`OSError`的一个子类，用于处理程序在遇到问题时会引发此异常（或其派生的异常），包含的属性`reason`为引发异常的原因。

`HTTPError`是`URLError`的一个子类，用于处理特殊`HTTP`错误例如作为认证请求的时候，包含的属性`code`为`HTTP`的状态码，`reason`为引发异常的原因，`headers`为导致`HTTPError`的特定`HTTP`请求的`HTTP`响应头。

区别：

- `URLError`封装的错误信息一般是由网络引起的，包括`url`错误。
- `HTTPError`封装的错误信息一般是服务器返回了错误状态码。

关系：

- `URLError`是`OSERROR`的子类，`HTTPError`是`URLError`的子类。

#### **`URLError` 示例**

```javascript
from urllib import request
from urllib import error

if __name__ == "__main__":
    #一个不存在的连接
    url = "http://www.baiiiduuuu.com/"
    req = request.Request(url)
    try:
        response = request.urlopen(req)
        html = response.read().decode('utf-8')
        print(html)
    except error.URLError as e:
        print(e.reason)
```

返回结果

```javascript
[Errno -2] Name or service not known
```

此错误的原因。它可以是一个消息字符串或另一个异常实例。

#### **HTTPError示例**

```javascript
from urllib import request
from urllib import error

if __name__ == "__main__":
    #网站服务器上不存在资源
    url = "http://www.baidu.com/no.html"
    req = request.Request(url)
    try:
        response = request.urlopen(req)
        html = response.read().decode('utf-8')
        print(html)
    except error.HTTPError as e:
        print(e.code)
```

output

```javascript
404
```

#### **`URLError`和`HTTPError`混合使用**

注意：由于`HTTPError`是`URLError`的子类，所以捕获的时候`HTTPError`要放在`URLError`的上面。

示例：

```javascript
from urllib import request
from urllib import error

if __name__ == "__main__":
    #网站服务器上不存在资源
    url = "http://www.baidu.com/no.html"
    req = request.Request(url)
    try:
        response = request.urlopen(req)
 #       html = response.read().decode('utf-8')
    except error.HTTPError as e:
        print(e.code)
    except error.URLError as e:
        print(e.code)
```

如果不用上面的方法，可以直接用判断的形式

```javascript
from urllib import request
from urllib import error

if __name__ == "__main__":
    #网站服务器上不存在资源
    url = "http://www.baidu.com/no.html"
    req = request.Request(url)
    try:
        response = request.urlopen(req)
 #       html = response.read().decode('utf-8')
    except error.URLError as e:
        if hasattr(e, 'code'):
            print("HTTPError")
            print(e.code)
        elif hasattr(e, 'reason'):
            print("URLError")
            print(e.reason)
```

output

```javascript
HTTPError
404
```

### **urllib.parse模块**

模块定义的函数可分为两个主要门类:`URL`解析和`URL`转码。

#### **urlparse()**

`urllib.parse`用于解析`URL`，格式如下：

```javascript
urllib.parse.urlparse(urlstring, scheme='', allow_fragments=True)
```

`urlstring`为字符串的`url`地址，`scheme`为协议类型。

`allow_fragments`参数为`false`，则无法识别片段标识符。相反，它们被解析为路径，参数或查询组件的一部分，并`fragment`在返回值中设置为空字符串。

标准链接格式为：

```javascript
scheme://netloc/path;params?query#fragment
```

对象中包含了六个元素，分别为：协议（scheme）、域名（netloc）、路径（path）、路径参数（params）、查询参数（query）、片段（fragment）。

示例：

```javascript
from urllib.parse import urlparse

o = urlparse("https://docs.python.org/zh-cn/3/library/urllib.parse.html#module-urllib.parse")

print('scheme  :', o.scheme)
print('netloc  :', o.netloc)
print('path    :', o.path)
print('params  :', o.params)
print('query   :', o.query)
print('fragment:', o.fragment)
print('hostname:', o.hostname)
```

output

```javascript
scheme  : https
netloc  : docs.python.org
path    : /zh-cn/3/library/urllib.parse.html
params  :
query   :
fragment: module-urllib.parse
hostname: docs.python.org
```

以上还可以通过索引获取，如通过

```javascript
print(o[0])
...
print(o[5])
```

#### **urlunparse()**

`urlunparse()`可以实现`URL`的构造。（构造`URL`）

`urlunparse()`接收一个是一个长度为6的可迭代对象，将`URL`的多个部分组合为一个`URL`。若可迭代对象长度不等于6，则抛出异常。

示例：

```javascript
from urllib.parse import urlunparse
url_compos = ['http','www.baidu.com','index.html','user= test','a=6','comment']
print(urlunparse(url_compos))
```

output

```javascript
http://www.baidu.com/index.html;user= test?a=6#comment
```

#### **urlsplit()**

`urlsplit()`函数也能对 `URL`进行拆分，所不同的是，`urlsplit()`并不会把 路径参数(params) 从 路径(path) 中分离出来。

当`URL`中路径部分包含多个参数时，使用`urlparse()`解析是有问题的，这时可以使用`urlsplit()`来解析.

`urlunsplit()`与`urlunparse()`类似，（构造`URL`），传入对象必须是可迭代对象，且长度必须是5。

示例：

```javascript
from urllib.parse import urlunsplit
url_compos = ['http','www.baidu.com','index.html','user= test','a = 2']
print(urlunsplit(url_compos))urlunsplit()
```

output

```javascript
http://www.baidu.com/index.html?user= test#a = 2
```

#### **urljoin()**

同样可以构造`URL`。

传递一个基础链接,根据基础链接可以将某一个不完整的链接拼接为一个完整链接.

注：连接两个参数的`url`, 将第二个参数中缺的部分用第一个参数的补齐,如果第二个有完整的路径，则以第二个为主。

#### **URL 转码**

`python`中提供`urllib.parse`模块用来编码和解码，分别是`urlencode()`与`unquote()`。

#### **编码quote(string)**

`URL`转码函数的功能是接收程序数据并通过对特殊字符进行转码并正确编码非`ASCII`文本来将其转为可以安全地用作`URL`组成部分的形式。它们还支持逆转此操作以便从作为`URL`组成部分的内容中重建原始数据，如果上述的`URL`解析函数还未覆盖此功能的话

语法：

```javascript
urllib.parse.quote(string, safe='/', encoding=None, errors=None)
```

使用`%xx`转义符替换`string`中的特殊字符。字母、数字和 '_.-~' 等字符一定不会被转码。在默认情况下，此函数只对`URL`的路径部分进行转码。可选的`safe`形参额外指定不应被转码的`ASCII`字符 --- 其默认值为 '/'。

`string`可以是`str`或`bytes`对象。

示例：

代码语言：javascript

AI代码解释



```javascript
from urllib import parse

url = "http://www.baidu.com/s?wd={}"
words = "爬虫"

#quote()只能对字符串进行编码
query_string = parse.quote(words)
url = url.format(query_string)
print(url)
```

执行结果：

```javascript
http://www.baidu.com/s?wd=%E7%88%AC%E8%99%AB
```

#### **编码urlencode()**

`quote()`只能对字符串编码，而`urlencode()`可以对查询字符串进行编码。

```javascript
# 导入parse模块
from urllib import parse

#调用parse模块的urlencode()进行编码
query_string = {'wd':'爬虫'}
result = parse.urlencode(query_string)

# format函数格式化字符串，进行url拼接
url = 'http://www.baidu.com/s?{}'.format(result)
print(url)
```

output

```javascript
http://www.baidu.com/s?wd=%E7%88%AC%E8%99%AB
```

#### **解码 unquote(string)**

解码就是对编码后的`url`进行还原。

示例：

```javascript
from urllib import parse
string = '%E7%88%AC%E8%99%AB'
result = parse.unquote(string)
print(result)
```

执行结果：

```javascript
爬虫
```

### **urllib.robotparser模块**

（在网络爬虫中基本不会用到，使用较少，仅作了解）

`urllib.robotparser`用于解析`robots.txt`文件。

`robots.txt`（统一小写）是一种存放于网站根目录下的`robots`协议，它通常用于告诉搜索引擎对网站的抓取规则。

`Robots`协议也称作爬虫协议，机器人协议，网络爬虫排除协议，用来告诉爬虫哪些页面是可以爬取的，哪些页面是不可爬取的。它通常是一个`robots.txt`的文本文件，一般放在网站的根目录上。

当爬虫访问一个站点的时候，会首先检查这个站点目录是否存在`robots.txt`文件，如果存在，搜索爬虫会根据其中定义的爬取范围进行爬取。如果没有找到这个文件，搜索爬虫会访问所有可直接访问的页面。

`urllib.robotparser`提供了`RobotFileParser`类，语法如下：

代码语言：javascript

AI代码解释



```javascript
class urllib.robotparser.RobotFileParser(url='')
```

这个类提供了一些可以读取、解析`robots.txt`文件的方法：

- `set_url(url)` - 设置`robots.txt`文件的`URL`。
- `read()` - 读取`robots.txt URL`并将其输入解析器。
- `parse(lines)` - 解析行参数。
- `can_fetch(useragent, url)` - 如果允许`useragent`按照被解析`robots.txt`文件中的规则来获取`url`则返回`True`。
- `mtime()` - 返回最近一次获取`robots.txt`文件的时间。这适用于需要定期检查`robots.txt`文件更新情况的长时间运行的网页爬虫。
- `modified()` - 将最近一次获取`robots.txt`文件的时间设置为当前时间。
- `crawl_delay(useragent)` - 为指定的`useragent`从`robots.txt` 返回`Crawl-delay`形参。如果此形参不存在或不适用于指定的`useragent` 或者此形参的`robots.txt`条目存在语法错误，则返回`None`。
- `request_rate(useragent)` -以 `named tuple RequestRate(requests, seconds)`的形式从`robots.txt`返回`Request-rate`形参的内容。如果此形参不存在或不适用于指定的`useragent`或者此形参的`robots.txt`条目存在语法错误，则返回`None`。
- `site_maps()` - 以`list()`的形式从`robots.txt`返回`Sitemap`形参的内容。如果此形参不存在或者此形参的`robots.txt`条目存在语法错误，则返回`None`



# 42 . **http**

## python http简单例子

python http框架主要有server和handler组成，server主要是用于建立网络模型，例如利用epoll监听socket；handler用于处理各个就绪的socket；先来看下python http简单的使用：

```stylus
stylus 体验AI代码助手 代码解读复制代码import sys
from http.server import HTTPServer,SimpleHTTPRequestHandler
ServerClass = HTTPServer
HandlerClass = SimpleHTTPRequestHandler
if __name__ == '__main__':
    port = int(sys.argv[2])
    server_address = (sys.argv[1],port)
    httpd = ServerClass(server_address,HandlerClass)
    sa=httpd.socket.getsockname()
    print("Serving HTTP on", sa[0], "port", sa[1], "...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received, exiting.")
        httpd.server_close()
        sys.exit(0)）
```



运行上述例子，可以得到如下：

> python3 myhttp.py 127.0.0.1 9999

此时如果在当前文件夹新建一个index.html文件，就可以通过[http://127.0.0.1:9999/index.html](https://link.juejin.cn?target=http%3A%2F%2F127.0.0.1%3A9999%2Findex.html)访问了index.html页面了。

这个例子的server类用的是HTTPServer，handler类是SimpleHTTPRequestHandler，因此当HTTPServer监听到有request到来时，就把这个request丢给SimpleHTTPRequestHandler类求处理；ok，了解这些之后，我们开始分别分析下server和handler.

## http之server

http模块的设计充分利用了面向对象的继承多态，因为之前有看了会tfs文件系统的代码，所以再看python http时，没那么大的压力；先给出server的继承关系

```gherkin
gherkin 体验AI代码助手 代码解读复制代码  +------------------+
+------------+         | tcpserver基类    |
| BaseServer +-------->| 开启事件循环监听 |
+-----+------+         | 处理客户端请求   |
      |                +------------------+
      v                +-----------------+
+------------+         | httpserver基类  |
| TCPServer  +-------->+  设置监听socket |
+-----+------+         | 开启监听        |
      |                +-----------------+
      v
+------------+
| HTTPServer |           
+------------+）
```



继承关系如上图所示，其中BaseServer和TCPServer在文件socketserver.py，HTTPServer在http/server.py；我们先看下来BaseServer；

## BaseServer

因为BaseServer是所有server的基类，因此BaseServer尽可能抽象出所有server的共性，例如开启事件监听循环，这就是每个server的共性，因此这也是BaseServer主要做的使;我们来看下BaseServer主要代码部分

```oxygene
oxygene 体验AI代码助手 代码解读复制代码def serve_forever(self, poll_interval=0.5):
        self.__is_shut_down.clear()
        try:
            with _ServerSelector() as selector:
                selector.register(self, selectors.EVENT_READ)
                while not self.__shutdown_request:
                    ready = selector.select(poll_interval)
                    if ready:
                        self._handle_request_noblock()
                    self.service_actions()
        finally:
            self.__shutdown_request = False
            self.__is_shut_down.set()）
```



代码中的selector其实就是封装了select,poll,epoll等的io多路复用，然后将服务自身监听的socket注册到io多路复用，开启事件监听，当有客户端连接时，此时会调用self._handle_request_noblock()来处理请求；接下来看下这个处理函数做了啥；

```reasonml
reasonml 体验AI代码助手 代码解读复制代码def _handle_request_noblock(self):
        try:
            request, client_address = self.get_request()
        except OSError:
            return
        if self.verify_request(request, client_address):
            try:
                self.process_request(request, client_address)
            except:
                self.handle_error(request, client_address)
                self.shutdown_request(request)
        else:
            self.shutdown_request(request)）
```



_handle_request_noblock函数是一个内部函数，首先是接收客户端连接请求，底层其实是封装了系统调用accept函数，然后验证请求，最后调用process_request来处理请求；其中get_request是属于子类的方法，因为tcp和udp接收客户端请求是不一样的(tcp有连接，udp无连接)

我们接下来再看下process_request具体做了什么；

```reasonml
reasonml 体验AI代码助手 代码解读复制代码def process_request(self, request, client_address):
       self.finish_request(request, client_address)
       self.shutdown_request(request)
# -------------------------------------------------
def finish_request(self, request, client_address):
        self.RequestHandlerClass(request, client_address, self)
def shutdown_request(self, request):
    self.close_request(request)）
```



process_request函数先是调用了finish_request来处理一个连接，处理结束之后，调用shutdown_request函数来关闭这个连接；而finish_request函数内部实例化了一个handler类，并把客户端的socket和地址传了进去，说明，handler类在初始化结束的时候，就完成了请求处理，这个等后续分析handler时再细看；

以上就是BaseServer所做的事，这个BaseServer不能直接使用，因为有些函数还没实现，只是作为tcp/udp的抽象层；总结下：

1. 先是调用serve_forever开启事件监听；
2. 然后当有客户端请求到来时，将请求交给handler处理；

## TCPServer

由上述BaseServer抽象出的功能，我们可以知道TCPServer或UDPServer应该完成的功能有，初始化监听套接字，并绑定监听，最后当有客户端请求时，接收这个客户端；我们来看下代码

```monkey
monkey 体验AI代码助手 代码解读复制代码BaseServer==>
def __init__(self, server_address, RequestHandlerClass):
        """Constructor.  May be extended, do not override."""
        self.server_address = server_address
        self.RequestHandlerClass = RequestHandlerClass
        self.__is_shut_down = threading.Event()
        self.__shutdown_request = False
#--------------------------------------------------------------------------------
TCPServer==>
def __init__(self, server_address, RequestHandlerClass, bind_and_activate=True):
       BaseServer.__init__(self, server_address, RequestHandlerClass)
       self.socket = socket.socket(self.address_family,
                                   self.socket_type)
       if bind_and_activate:
           try:
               self.server_bind()
               self.server_activate()
           except:
               self.server_close()
               rais）
```



TCPServer初始化时先是调用基类BaseServer的初始化函数，初始化服务器地址，handler类等，然后初始化自身的监听套接字，最后调用server_bind绑定套接字，server_activate监听套接字

```python
python 体验AI代码助手 代码解读复制代码def server_bind(self):
    if self.allow_reuse_address:
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.socket.bind(self.server_address)
    self.server_address = self.socket.getsockname()
def server_activate(self):
    self.socket.listen(self.request_queue_size）
```



TCPServer还实现了另一个函数，那就是接收客户端请求，

```ruby
ruby 体验AI代码助手 代码解读复制代码def get_request(self):
        return self.socket.accept()）
```



之前如果有学过linux编程，那么看这些代码应该会觉得很熟悉，因为函数名和Linux提供的系统调用名一模一样，这里也不多说了；

TCPServer其实已经把基于tcp的服务器主体框架搭起来了，因此HTTPServer在继承TCPServer基础上，只是重载了server_bind函数，设置reuse_address等；

ok，这里分析下上述例子程序的开启过程；

1. httpd = ServerClass(server_address,HandlerClass)这行代码在初始化HTTPServer时，主要是调用基类TCPServer的初始化方法，初始化了监听的套接字，并绑定和监听；
2. httpd.serve_forever()这行代码调用的是基类BaseServer的serve_forever方法，开启监听循环，等待客户端的连接；

如果有看过redis或者一些后台组件的源码，对这种并发模型应该很熟悉；ok，分析了server之后，接下来看下handler是如何处理客户端请求的。

## http之handler

handler类主要分析tcp层的handler和http应用层的handler,tcp层的handler是不能使用的，因为tcp层只负责传输字节，但是并不知对于接收到的字节要如何解析，如何处理等；因此应用层协议如该要使用TCP协议，必须继承TCP handler，然后实现handle函数即可;例如，http层的handler实现handle函数，解析http协议，处理业务请求以及结果返回给客户端；先来看下tcp层的handler

## tcp层handler

tcp层handler主要有BaseRequestHandler和StreamRequestHandler(都在socketserver.py文件)，先看下BaseRequestHandler代码，

```python
python 体验AI代码助手 代码解读复制代码class BaseRequestHandler:
    def __init__(self, request, client_address, server):
        self.request = request
        self.client_address = client_address
        self.server = server
        self.setup()
        try:
            self.handle()
        finally:
            self.finish()
    def setup(self):
        pass
    def handle(self):
        pass
    def finish(self):
        pas）
```



之前在看server时，知道处理客户端请求就是在handler类的初始化函数中完成；由这个基类初始化函数，我们知道处理请求大概经历三个过程：

1. setup对客户端的socket做一些设置；
2. handle真正处理请求的函数；
3. finish关闭socket读写请求；

这个BaseRequestHandler是handler top level 基类，只是抽象出handler整体框架，并没有实际的处理；我们看下tcp handler，

```python
python 体验AI代码助手 代码解读复制代码class StreamRequestHandler(BaseRequestHandler):
    timeout = None
    disable_nagle_algorithm = False
    def setup(self):
        self.connection = self.request
        if self.timeout is not None:
            self.connection.settimeout(self.timeout)
        if self.disable_nagle_algorithm:
            self.connection.setsockopt(socket.IPPROTO_TCP,
                                       socket.TCP_NODELAY, True)
        self.rfile = self.connection.makefile('rb', self.rbufsize)
        self.wfile = self.connection.makefile('wb', self.wbufsize)
    def finish(self):
        if not self.wfile.closed:
            try:
                self.wfile.flush()
            except socket.error:
                pass
        self.wfile.close()
        self.rfile.close(）
```



tcp handler实现了setup和finish函数，setup函数设置超时时间，开启nagle算法以及设置socket读写缓存；finish函数关闭socket读写；

由上述两个tcp层的handler可知，要实现一个基于http的服务器handler，只需要继承StreamRequestHandler类，并实现handle函数即可；因此这也是http层handler主要做的事；

## http层handler

由之前tcp层handler的介绍，我们知道http层handler在继承tcp层handler基础上，主要是实现了handle函数处理客户端的请求；还是直接看代码吧；

```ruby
ruby 体验AI代码助手 代码解读复制代码def handle(self):
        self.close_connection = True
        self.handle_one_request()
        while not self.close_connection:
            self.handle_one_request()）
```



这就是BaseHTTPRequestHandler的handle函数，在handle函数会调用handle_one_request函数处理一次请求；默认情况下是短链接，因此在执行了一次请求之后，就不会进入while循环在同一个连接上处理下一个请求，但是在handle_one_request函数内部会进行判断，如果请求头中的connection为keep_alive或者http版本大于等于1.1，则可以保持长链接；接下来看下handle_one_request函数是如何处理；

```python
python 体验AI代码助手 代码解读复制代码def handle_one_request(self):
    try:
        self.raw_requestline = self.rfile.readline(65537)
        if len(self.raw_requestline) > 65536:
            self.requestline = ''
            self.request_version = ''
            self.command = ''
            self.send_error(HTTPStatus.REQUEST_URI_TOO_LONG)
            return
        if not self.raw_requestline:
            self.close_connection = True
            return
        if not self.parse_request():
            return
        mname = 'do_' + self.command
        if not hasattr(self, mname):
            self.send_error(
                HTTPStatus.NOT_IMPLEMENTED,
                "Unsupported method (%r)" % self.command)
            return
        method = getattr(self, mname)
        method()
        self.wfile.flush()
    except socket.timeout as e:
        self.log_error("Request timed out: %r", e)
        self.close_connection = True
        retur）
```



这个handle_one_request执行过程如下：

1. 先是调用parse_request解析客户端http请求内容
2. 通过"do_"+command构造出请求所对于的函数method
3. 调用method函数，处理业务并将response返回给客户端

这个BaseHTTPRequestHandler是http handler基类，因此也是无法直接使用，因为它没有定义请求处理函数，即method函数；好在python为我们提供了一个简单的SimpleHTTPRequestHandler，该类继承了BaseHTTPRequestHandler，并实现了请求函数；我们看下get函数：

```python
python 体验AI代码助手 代码解读复制代码# SimpleHTTPRequestHandler
# ---------------------------------------------
def do_GET(self):
      """Serve a GET request."""
      f = self.send_head()
      if f:
          try:
              self.copyfile(f, self.wfile)
          finally:
              f.close(）
```



这个get函数先是调用do_GET函数给客户端返回response头部，并返回请求的文件，最后调用copyfile函数将请求文件通过连接返回给客户端；

以上就是http模块最基础的内容，最后，总结下例子程序handler部分：

1. server把请求传给SimpleHTTPRequestHandler初始化函数；
2. SimpleHTTPRequestHandler在初始化部分，对这个客户端connection进行一些设置；
3. 接着调用handle函数处理请求；
4. 在handle函数接着调用handle_one_request处理请求；
5. 在handle_one_request函数内部，解析请求，找到请求处理函数；
6. 我之前的访问属于get访问，因此直接调用do_GET函数将index.html文件返回给客户端；

python http模块到此已经分析结束；不知道大家有没发现，python自带的http模块使用起来不是很方便，因为它是通过请求方法来调用请求函数，这样当同一方法调用次数非常多时，例如get和post方法，会导致这个请求函数异常庞大，代码不好编写，各种情况判断；当然SimpleHTTPRequestHandler只是python提供的一个简单例子而已；

当然，python官方提供了针对http更好用的框架，即wsgi server和wsgi application；接下来文章先分析python自带的wsgiref模块



#  42_2 httplib2(第三方模块)



# 42_3 httpx(第三方模块)



# 42_4 html5lib(第三方模块)



# 43. **smtplib**



# 44 . **traceback**



# 45. **unittest**



# 46. **timeit**



# 47. fileinput



# 48 . array



# 49. enum



# 50. typing



# 51. zoneinfo



# 52. unicodedata



# 53. gzip



# 54. zipfile



# 55. tarfile



# 56.struct

