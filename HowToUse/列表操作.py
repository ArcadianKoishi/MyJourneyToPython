"""列表操作"""
"""Menu(通过ctrl+f找到具体用法)
append extend insert
a[i] 生成器 index
count len del pop
remove sort reverse
拆包
"""
# #定义列表
# a=[]              #定义空列表
# a=list()          #定义空列表
# a=[1,2,3]
# for i in [1,2,3,4,5,6]:           #用for进行迭代
#     print(i)
# a=[i for i in range(514)]       #用生成器定义列表
# #不可以用a=(i for i in range(514))，因为这是生成器，不是列表，会导致无法使用len等方法
# #顺带一提用生成器生成元组是a=tuple(i for i in range(514))
# #再提一嘴a=i for i in range(514)是语法错误
# [print(i) for i in range(0,10)]跑10次print并返回[None重复10次]
# li=[]
# [li.append(j) for j in range(0,10) if j%2==1]

#添加
# #append(元素)在列表末尾加一个元素,类似push_back(元素)，无返回值

# #extend(可迭代内容_此处为列表),类似list1+list2
# a=[1,2]
# a.extend([5,6])#效果为a后接上列表[5,6],无返回值

# #insert在指定位置插入元素，该下标及后方的元素均后移，无返回值
# #insert(下标,元素)

#创建与修改
# #用下标进行修改元素
# #a[i]=元素            #不会改变该列表的地址，其他容器同理

# #查询
# #index同理字符串
# #count同理字符串
# #len同理字符串

# #删除
# #del list1删除列表(del也可用于删除变量)
# #del list1[2]删除list1中下标为2的元素
# #del list1[2:5]删除list1中下标为2,3,4的元素

# #pop(可以省略的下标)根据元素的下标删除(默认末尾的)并返回该元素

# #remove(元素的值)根据元素的值删除(默认下标最小的满足条件的)

# #排序
# #sort默认从小到大排序，改变变量的值
# a=[9,2,4,8,6,45]
# a.sort()

# #reverse反转
# a.reverse()

# #拆包同理元组