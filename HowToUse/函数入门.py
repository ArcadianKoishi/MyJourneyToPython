"""函数操作"""
"""Menu
def return 可变参数*args
关键词参数**kwargs 作用域 lambda
"""

def fun0(a,b=2,c=1):#c默认为1，传参时可缺省，缺省的变量可且仅可放在右侧
    """
    随便进行点啥函数体
    """
    # #无return返回None
    # return    #返回None
    # return a  #返回内容
    # return a,b,c  #返回元组(可不加小括号，但最好括上，和lambda统一)
    # return (((a,b,c)))  #同return a,b,c套几层都认为是小括号，除非加个逗号
print(fun0(0,0))          #传参是实参赋值形参

# #可变参数(以元组形式接收实参)
def fun1(*args):     #args为arguments的缩写，意为参数，可以改为其他任意变量名
    print(args)
    return
fun1(1)
fun1(1,2,3)
fun1("456","789")

# #关键词参数(以字典形式接收实参)       #一般用于提供额外可选填的注册信息
def fun2(**kwargs):  #kwargs为keyword arguments的缩写,可以改为其他任意变量名
    print(kwargs)
    return
fun2()
fun2(name="koishi",sex="female")#实参需要以<变量名>=<元素>的方式传入，详见左侧案例

# #作用域

# #函数内部定义函数
def fun3():
    def fun4():
        print(4)
    fun4()
fun3()
# fun4()#外部无法调用fun4(),因为fun4()的定义只在fun3()的函数体这个作用域内有效

# #全局变量与局部变量与global
# #golbal相对于nonlocal而言，是绝对的全局变量而非相对的"全局变量"
a=10
qwp=77
def fun5(qwp):
    print(qwp)  #函数的形参有定义，直接使用局部变量
    qwp=11
    print(a)    #函数内没有a的定义，故寻找全局变量
    print(qwp)  #函数内更改形参
fun5(a)
print(a)        #未加上global，不影响实参的值
def fun6():
    a=12        #创建局部变量，而非改变全局变量
    print(a)
fun6()
print(a)        #运行fun6()不改变全局变量a的值
def fun7():
    global a,b  #将a,b修改为 同名的(若存在)/新的(不存在) 全局变量
    a=14
    b=7
fun7()
print(a)
print(b)    #切记需要先运行fun7()
def fun8():
    def fun9():
        global a
        a=16
    fun9()
fun8()
print(a)

# #nonlocal的用法
# #函数中定义内层函数时，外层函数的局部变量相当于内层的全局变量
# #nonlocal是以上一层为全局的golbal
a=1
b=10
def outer():
    a=2    
    b=20
    def middle():
        a=3
        nonlocal b
        b=30
        def inner():
            a=4
            nonlocal b
            b=40
        inner()
        print("inner后的a:",a)
        print("inner后的b:",b)
    middle()
    print("middle后的a:",a)
    print("middle后的b:",b)
outer()
print("outer后的a:",a)
print("outer后的b:",b)

# #匿名函数lambda(用于需求较简单的函数)
""""供对比用的Add函数
def Add(a,b,c):
    return a+b+c
"""
# #匿名函数的格式:   函数名 = lambda 形参:返回值(多个返回值必须加小括号表示元组)
itself = lambda a:a
print(itself(1))
# #无参,多参,默认参,可变参,关键词参类比普通的函数
# #以下为防止重复定义仅注释参考
# Add=lambda :"+"
# Add=lambda a,b:a+b
# Add=lambda a,b=10:a+b
# BuildList=lambda *args:[i for i in args]
# GetKeys=lambda **kwargs:[i for i in kwargs]
# #展示屎:comp = lambda a,b : "a>b" if a>b else "a<=b"