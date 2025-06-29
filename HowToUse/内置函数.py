# #内置函数和常量列表
# import builtins
# print(dir(builtins))


# #abs() sum() max() min()不多说

# print(max(-10,5,key=abs)) #先求绝对值再求最大,min()同理

# #zip(a,b)
# #将两个可迭代对象进行一一对应打包
# l1=[1,2,3,4]
# l2={"a","b","c"}    #元素个数不同时按照个数较少的打包
# zi1=zip(l1,l2)
# #类似range(范围对象)和generator(生成器),不可直接print出来，需要先list()或for语句提取
# print(type(zi1),zi1,list(zi1),sep="\n")
# for i in zi1:
#     print(i,end=" ")
# print()

# #map批量进行函数
# #map(一元函数func,可迭代对象iterl)
# a=map(int,"123 456".split())    #返回map类对象，需要list()或for语句提取
# print(type(a),a,list(a))
# #map(多元函数func,可迭代对象1,可迭代对象2...)
# Plusfun = lambda a,b:a+b
# a=map(Plusfun,["1","2","3","4","5"],"67890qwp") #可迭代对象的个数不一致时按照少的来
# print(list(a))
# #map(无参函数,用不上的迭代器)     正常人谁用无参函数批量操作可迭代对象啊

# #reduce依次将序列中的所有元素进行二元运算
# #reduce(只有一个同类型返回值的二元函数fun,含至少两个值的序列squence)
# import functools
# Plusfun = lambda a,b:a+2*b
# a=functools.reduce(Plusfun,[1,2,3,4])
# #[1,2,3,4] 1+2*2=5 [5,3,4] 5+2*3=11 [11,4] 11+2*4=19 [19] 19
# print(a)