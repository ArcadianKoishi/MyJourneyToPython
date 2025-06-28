import time
"""
    这是一个多行注释
    这个和字符串没啥区别
    就好像下面的"1"一样不会被运行

Menu
注释 print的end和sep complex
type id
"""
1
# ctrl+/ 加上注释或者撤销注释
# print("hello world",end="\n")#end默认为\n
# print("你","好",sep="@")#sep默认为空格

# if (-2):#非0的数为真
#     print(True+False)#True默认为1，False默认为0

# #复数类型complex
# comp1=1+5j#虚数单位用j
# comp2=3+6j
# comp3=comp1+comp2
# print(comp3)
# a=int("123")
# b=str(123)#不是char也不是string,单引号多引号都可以
# c="""wow
# qwq
# oTATo
# """
# print(type(a),type(b),type(c),a,b,c)  #type用于查看类型
# print(id(a))                          #id用于查看内存地址
# name="1"
# age=18
# print("%s是%4d %.2f"%("我的学号",123,0.123456))#超出给定的位数原样输出，不足时补空格
# #此处的("我的学号",123,0.123456)是元组
# print(f"我的名字是{name},我今年{age}岁了")
# #/为除，结果一定为浮点数 //为整除 %为取余
# #其他运算有浮点数则结果为浮点数
#print(-1%8)
# #a+=b和a=a+b等价
# #+=中间不能加空格，不要手贱
# a=input("这是一条prompt")

# #基于\r的进度条
# for i in range(0,10,1):
#     print("="*i,"-"*(10-i),sep="",end="\r")
#     time.sleep(1)

# print(type(a),a,"\n",type(b),b,"\n",c)
# a not in b是正确的，不一定要写not(a in b)