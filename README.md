[TOC]
# python3.5_exercise
This git is created for my own exercise
## 1_firstPython.py
第一个文件包含python简单的输入和输出。
## 2_variableAndList.py
### python的数据类型和变量
* python的变量感觉也是弱类型，变量不需要声明，可以任意赋值
* 常量用大写
* 运算符有个//，代表整除，and、or、not是与或非运算，None代表空
* 转义字符用\，用r''可以让内部字符都不转义，
## 3_listAndTuple
1. list:
    * 声明list：[]，支持下标访问，支持负数下标访问。
    * 增：append 插入：append(index,elemet) 删除pop(),pop(index)
    * 长度：len()
2. tuple:
    * 声明：()，如果tuple只有一个元素，tuple(1,)
    * 不可变,其他操作都一样。
## if\else\for in\while\break\continue
    这块没啥区别，就是都没有大括号而已
## 4_set and dictionary
1. dict
    * 初始化用{}，查找速度贼拉快，访问的时候用[]
    * 判断的时候用in，获取可以用get删除用pop
2. set
    * 不可重复的序列。
    * set可以做交并补的操作，非常六。
## 5_funcion.py
1. python里面的函数，是可以跟js一样，到处赋值的。
2. pass是个好东西，可以先运行起来没有写好的函数。
3. python里面的函数，可以返回多个返回值！！！尼玛！！！！发现了新的世界。

*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数

## 6_do_slice.py
1. 切片操作是可以在数组里直接用下标取值，支持正序倒叙
2. 切片操作还可以支持每n个取一个

## 7_do_iter.py

- Iterable的接口来自collections.abc，所以写from collections.abc import Iterable会报错！

## 8_do_listcompr.py

- 介绍了列表生成器怎么用