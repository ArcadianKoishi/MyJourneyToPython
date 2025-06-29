"""集合操作"""
"""Menu(...) set
无序 add update
remove pop discard
交集& 并集| 差集-
对称差^ 子集<= 超集>=
拆包
"""

# #定义集合
# a={1,2,3,4,5,6}
# b={}        #定义空字典
# c=set()     #定义空集合

# #无序性
# a={1,2,3,4,5,6,6,6,6,6,6}  #自动去重
# b={"a","b","c","d"}
# #Python 3.6-3.10 可能在某些情况下顺序“看起来稳定”，但仍然是无序的，不能依赖。
# #Python 3.11+ 更倾向于随机化顺序，防止开发者误用。
# print(a)  #python中int类型的hash值就是它本身，所以顺序不变
# print(b)  #其他数据的hash值每次都不同，故每次的结果都可能是不同的

# #添加
# a={1,2,3}
# a.add(4)
# print(a)
# a.add(1)  #已有不会添加
# print(a)
# #错误示范:a.add(5,6,4,7,5)    #一次只能添加一个元素
# a.add((5,6))                 #但是可以添加元组等可hash的元素(list和dict不可hash)
# print(a)
# #a.update(可迭代对象)
# a={1}
# a.update([1,5,3,88])
# print(a)
# a.update("4567")
# print(a)
# a.update((1,2,3))
# print(a)

# #删除
# a={1,2,3,4,"5",6}
# a.remove("5")         #删除失败会报错
# print(a)
# a.pop()               #默认删除hash表排序后的第一个元素
# a.discard(6)          #尝试删除元素，若没有则不会进行任何操作

# #交集、并集、差集、对称差集、子集、超集
# a={1,2,3,4}
# b={3,4,5,6}
# print(a&b)
# print(a|b)
# print(a-b)
# print(a^b)
# c={1,2,3}
# d={1,2,3,4,5}
# print(a>=c)
# print(a>=a)
# print(a<=d)
# print(a<=a)

# #拆包(类似元组)
# #方法一：直接拆包(不推荐)
# set1={1,2,3,4,5,6}
# a,b,c,d,e,f=set1
# print(a,b,c,d,e,f)
# #方法二：先转化为list再拆(推荐，但仍旧无序)
# #方法三：可变对象拆包
# set1={1,2,3,4,5,6}
# a,*b=set1
# print(a,b)