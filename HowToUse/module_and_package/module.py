"""此模块用于导入模块1、介绍内置模块和第三方模块"""

# #内置模块
# #如random,time,os,logging

# #第三方模块(又称为第三方库)
# #如pygame
# #下载方法:pip install 模块名
# #不要乱下多个版本，要求把path搞好

# #自定义模块(详见module1.py)
# #要求文件名符合变量的命名规范

# #导入模块和使用如下
# #import XX                  #使用内容等前需要加上前缀
# import module1
# module1.rua()
# #from XX import XX          #无需加上前缀，但是容易产生命名冲突
# from module1 import rua
# rua()
# from module1 import name_
# print(name_)
# #导入多个模块或导入多个模块中的函数或变量
# #import module1,module2....
# #from module1 import rua,name_
# #导入模块中的全部内容
# from module1 import *     #它与import module1的区别是调用函数时无需加上前缀module1.
# #给模块起别名
# import module1 as m1
# from module1 import rua as r