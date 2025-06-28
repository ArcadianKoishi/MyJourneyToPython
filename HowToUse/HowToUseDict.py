"""字典操作"""
"""Menu(通过ctrl+f查找具体操作)
a[i] get del
clear pop popitem
len keys values
items
"""
# #定义字典
# a={}      #定义空字典
# a={"1":1,5:"1","name":"koishi"}
# a=dict()  #定义空字典

# #读取(均只可用键访问，因为字典没有下标)
# #a[i]其中i不是下标，是键
# a={"1":1,5:"1","name":"koishi"}
# print(a.get(5),a.get("1"),a.get("name"),a.get("sex"))     #1 1 koishi None
# #print(a[5],a["1"],a["name"],a["sex"])                    #1 1 koishi 报错

# #修改与添加
# a={"name":"koishi"}
# a["name"]=514         #修改键的值
# a["sex"]="female"     #新增元素

# #删除元素或整个字典
# a={"name":"koishi","sex":"female"}
# del a             #删除整个字典
# del a["name"]     #删除"name":"koishi"键值对
# a.pop("sex")     #删除"name":"koishi"键值对
# a.popitem()       #3.7以前的版本是随机删一个 3.7之后的版本是默认删最后一个
# a.clear()         #清空字典，但不删除

# #len求长度同理list

# #返回各种列表
# #a.keys()     #返回所有键名的列表
# #a.items()    #返回所有键值对的列表
# #a.values()   #返回所有值的列表
# a={1:2,3:4,5:6}
# print(a.keys())     #dict_keys([1, 3, 5])
# print(a.values())   #dict_values([2, 4, 6])
# print(a.items())    #dict_items([(1, 2), (3, 4), (5, 6)])
# for i in a:         #1,3,5,
#     print(i,end=",")