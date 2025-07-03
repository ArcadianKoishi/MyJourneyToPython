# #抛出异常  raise 异常名err    只有自定义异常需要raise，ValueError和ZeroDivisonError等都会自动抛出异常
# #创建异常  err=Exception(描述异常的字符串)  #Exception实际上就是一个异常基类,err是实例化对象
# def errorfun():
#     raise Exception("Hey!man!")#不在try内时结束整个程序
# errorfun()
# print("hi")

# #捕获异常
# #创建尝试用的函数
def meet_condition():
    if (input("请输入pwd")=="pwd"):
        return "ok"
    else:
        err=Exception("pwd:错误")
        raise err
# #try-except结构
try:
    print(meet_condition())
except Exception as o:#将返回的异常命名为o
    print(o)
print("a")#try内的raise不影响程序继续运行
