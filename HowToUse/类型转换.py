a="56"
a=int(a)                #int("abc")是非法操作
print(type(a),":",a)
a=chr(int(a))
print(type(a),":",a)
a=float(a)
print(type(a),":",a)
a=str(a)
print(type(a),":",a)
b="abcdefff"
c=tuple(b)
d=list(c)
e=set(d)
print(type(b),b)
print(type(c),c)
print(type(d),d)
print(type(e),e)
eval(input("输入一个表达式，返回一个对象"))   #不建议使用，因为容易被注入
#正常使用可用于str转为list、tuple、dict
#[eval(input("输入表达式"))for i in range(114514)]超绝注入
