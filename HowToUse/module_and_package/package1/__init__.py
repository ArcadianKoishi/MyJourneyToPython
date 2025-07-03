"""初始化文件"""
# #作为包的标识文件，必须存在，内容随意

# #一般用于import包中的所有模块
from . import m1    #使用相对路径导入m1
from . import m2
from . import package2
# #__all__变量
__all__=["m1","m2"]#当用from package1 import *时，只导入__all__中的内容

# #放一些包中需要的变量(较少用到)


if __name__=="__main__":
    print("自身运行中")
if __name__=="package1":
    print("包package1运行中")