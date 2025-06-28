def fun0(a,b=2,c=1):#c默认为1，传参时可缺省，缺省的变量可且仅可放在右侧
    """
    随便进行点啥函数体
    """
    # #无return返回None
    # return    #返回None
    # return a  #返回内容
    # return a,b,c  #返回元组
    # return (((a,b,c)))  #同return a,b,c套几层都认为是小括号，除非加个逗号
print(fun0(0,0))          #传参是实参赋值形参

# #可变参数(以元组形式接收实参)
def fun1(*args):     #args为arguments的缩写，意为参数，可以改为其他任意变量名
    print(args)
    return
fun1(1)
fun1(1,2,3)
fun1("456")

# #关键词参数(以字典形式接收实参)       #一般用于提供额外可选填的注册信息
def fun2(**kwargs):  #kwargs为keyword arguments的缩写,可以改为其他任意变量名
    print(kwargs)
    return
fun2()
fun2(name="koishi",sex="female")#实参需要以<变量名>=<元素>的方式传入，详见左侧案例