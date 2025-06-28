import copy
"""
注意:此内容仅针对可变对象,如list,dict,set,其他不可变对象没有拷贝这一概念
注意:此内容仅针对可变对象,如list,dict,set,其他不可变对象没有拷贝这一概念
注意:此内容仅针对可变对象,如list,dict,set,其他不可变对象没有拷贝这一概念
"""
# #赋值(完全共享资源类似c里面的引用int* &l2=l1)
print("赋值演示:")
l1=[1,]
l2=l1
print("l1:",l1)
print("l2:",l2)
l1.append(2)
print("l1:",l1)
print("l2:",l2)
l2.append(3)
print("l1:",l1)
print("l2:",l2)
print("-"*20)
# #浅拷贝(l1和l2是不同的两个列表，但是其中的数据用的同一个地址)
print("演示浅拷贝")
l1=[1,[2,3]]
l2=copy.copy(l1)
print("l1:",l1)
print("l2:",l2)
l1.append(4)
l2.append(5)
print("l1:",l1)
print("l2:",l2)
l1[1].append(6)
print("l1:",l1)
print("l2:",l2)
print("-"*20)
# #深拷贝(l1,l2中的元素都不共用地址)
print("演示深拷贝")
l1=[1,[2,3]]
l2=copy.deepcopy(l1)
print("l1:",l1)
print("l2:",l2)
l1.append(4)
l2.append(5)
print("l1:",l1)
print("l2:",l2)
l1[1].append(6)
l2[1].append(7)
print("l1:",l1)
print("l2:",l2)