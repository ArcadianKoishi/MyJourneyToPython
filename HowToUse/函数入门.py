"""函数操作"""
"""Menu
def return 可变参数*args
关键词参数**kwargs 作用域(包含golbal和nonlocal) lambda
闭包 装饰器 函数名的意义
"""

# def fun0(a,b=2,c=1):#c默认为1，传参时可缺省，缺省的变量可且仅可放在右侧
#     """
#     随便进行点啥函数体
#     """
#     # #无return返回None
#     # return    #返回None
#     # return a  #返回内容
#     # return a,b,c  #返回元组(可不加小括号，但最好括上，和lambda统一)
#     # return (((a,b,c)))  #同return a,b,c套几层都认为是小括号，除非加个逗号
# print(fun0(0,0))          #传参是实参赋值形参

# #可变参数(以元组形式接收实参)
# def fun1(*args):     #args为arguments的缩写，意为参数，可以改为其他任意变量名
#     print(args)
#     return
# fun1(1)
# fun1(1,2,3)
# fun1("456","789")

# #关键词参数(以字典形式接收实参)       #一般用于提供额外可选填的注册信息
# def fun2(**kwargs):  #kwargs为keyword arguments的缩写,可以改为其他任意变量名
#     print(kwargs)
#     return
# fun2()
# fun2(name="koishi",sex="female")#实参需要以<变量名>=<元素>的方式传入，详见左侧案例

"""
如果同时存在*args和**kwargs作为形参,调用时必须先传args,再传kwargs,举例如下
def fun(*args,**kwargs):
    ......
fun(1,2,3,7,name="koishi",power_level=5)
"""

# #作用域

# #函数内部定义函数
# def fun3():
#     def fun4():
#         print(4)
#     fun4()
# fun3()
# fun4()#外部无法调用fun4(),因为fun4()的定义只在fun3()的函数体这个作用域内有效

# #全局变量与局部变量与global
# #golbal相对于nonlocal而言，是绝对的全局变量而非相对的"全局变量"
# a=10
# qwp=77
# def fun5(qwp):
#     print(qwp)  #函数的形参有定义，直接使用局部变量
#     qwp=11
#     print(a)    #函数内没有a的定义，故寻找全局变量
#     print(qwp)  #函数内更改形参
# fun5(a)
# print(a)        #未加上global，不影响实参的值
# def fun6():
#     a=12        #创建局部变量，而非改变全局变量
#     print(a)
# fun6()
# print(a)        #运行fun6()不改变全局变量a的值
# def fun7():
#     global a,b  #将a,b修改为 同名的(若存在)/新的(不存在) 全局变量
#     a=14
#     b=7
# fun7()
# print(a)
# print(b)    #切记需要先运行fun7()
# def fun8():
#     def fun9():
#         global a
#         a=16
#     fun9()
# fun8()
# print(a)

# #nonlocal的用法
# #函数中定义内层函数时，外层函数的局部变量相当于内层的全局变量
# #nonlocal是以上一层为全局的golbal
# a=1
# b=10
# def outer():
#     a=2    
#     b=20
#     def middle():
#         a=3
#         nonlocal b
#         b=30
#         def inner():
#             a=4
#             nonlocal b
#             b=40
#         inner()
#         print("inner后的a:",a)
#         print("inner后的b:",b)
#     middle()
#     print("middle后的a:",a)
#     print("middle后的b:",b)
# outer()
# print("outer后的a:",a)
# print("outer后的b:",b)

# #匿名函数lambda(用于需求较简单的函数)
""""供对比用的Add函数
def Add(a,b,c):
    return a+b+c
"""
# #匿名函数的格式:   函数名 = lambda 形参:返回值(多个返回值必须加小括号表示元组)
# itselfplus1 = lambda a:a+1
# print(itselfplus1(1))
# #无参,多参,默认参,可变参,关键词参类比普通的函数
# #以下为防止重复定义仅注释参考
# Add=lambda :"+"
# Add=lambda a,b:a+b
# Add=lambda a,b=10:a+b
# BuildList=lambda *args:[i for i in args]
# GetKeys=lambda **kwargs:[i for i in kwargs]
# #展示屎:comp = lambda a,b : "a>b" if a>b else "a<=b"

# #闭包函数
"""(具体含义详见下方的函数名的意义)
1在函数内定义函数
2内部函数调用了外部函数的局部变量
3外部函数的返回值是内部函数的函数名
"""
# def outer():
#     n=10
#     def inner():
#         print(n)
#     return inner
# #使用方式1
# outer()() #如果outer有参数的话在第一个括号内写参数，inner有参数则在第二个括号内写参数
# #使用方式2
# fun=outer()
# fun()
# #我知道你在想要是外层函数return两个变量名会怎样,没错,就是你想的那样
# def outer(name_):
#     def inner1():
#         print("hi",name_)
#     def inner2():
#         print("hello",name_)
#     return inner1,inner2
# #使用方法1
# outer("koishi")[0]()
# outer("koishi")[1]()
# #使用方法2
# ot=outer("koishi")
# ot[0]()
# ot[1]()

# #闭包的实际作用(可以只输入一次name_,避免重复调用外部函数)
# #为什么不使用全局变量储存name_?因为函数外部无法改变name_(除了生存周期结束自动消亡),保证了数据安全
# def insertname(name_):
#     def react(flag):
#         if flag:
#             return "hi,"+name_
#         return "bye,"+name_
#     return react
# ot=insertname("koishi")
# print(ot(True))
# print(ot(False))

# #装饰器(屎山的起点)
# def fun_origin1():
#     print("发财")
# def fun_origin2():
#     print("高升")
# def intergrate(fn):   #整合函数
#     def inner():
#         #给多个函数都能用的新加的功能
#         print("恭喜",end="")
#         fn()           #调用原有功能
#     return inner
# ot1 = intergrate(fun_origin1)
# ot2 = intergrate(fun_origin2)
# ot1()
# ot2()
# #python特有的装饰器:语法糖
def outer(fn):
    print("hi")
    def inner():
        fn()
        print("new fun1")
    return inner
def dec(fn):
    print("hello")
    def inner():
        fn()
        print("new fun2")
    return inner
"""
@后接装饰原有函数的装饰函数的引用
若outer外层还有一层函数more_outer
more_outer的返回值为outer
则改为写@more_outer(*args,**kwargs)
"""
@dec    #有多个装饰器时，就近原则(离被装饰函数近的语法糖先装饰)
@outer  #必须和被修饰函数紧贴，中间连注释都不能有(这一条不算中间)
def origin():
    print("origin fun")
# origin=outer(origin)#语法糖实际干的事,因此会在装饰的时候立刻调用outer中的功能，如178行
origin()#若被修饰函数有形参，则inner函数必须至少获取被装饰函数的参数



# #函数名的意义
# #函数名实际上也是一个变量，它是函数在内存中地址的引用，()是对函数地址进行操作的运算符
# def print123():
#     print(123)
# w=print123
# w()