"""类的继承"""
"""Menu
直接继承 多层继承 多继承
super(见于多层继承和多继承) mro(决定继承顺序和能否继承)
"""
# #直接继承class 子类名(父类名):
# class Pet:
#     def __init__(self,kind,age,c):
#         self.kind=kind
#         self.__age=age
#         self.owner=c
#     def whose(self):
#         return f"{self.owner}的"
#     def how_old(self):
#         return self.__age
#     def which_kind(self):
#         return self.kind
#     def act(self):
#         print("Act")
#     def __del__(self):#pass None ...都是跳过
#         print("析构了")
# class Cat(Pet):
#     None
# class Clown(Pet):
#     ...
# """多层继承"""
# class FireCat(Cat):
#     kind="火焰猫"   #在构造函数之前改变，故构造函数会直接将其覆盖,正确方式是重写__init__
#     def act(self):  #重写override
#         print("喵~")
#         Pet.act(self)   #使用基类Pet的act方法
#         super().act()   #使用父类Cat的act方法(Cat若未重写就用Cat的父类的)
#         super(FireCat,self).act()
#         #上上行的本质是上行，可以使用super(基类或本身类,self).fun()调用参数1的父类的fun方法
# Kaenbyou_Rin=FireCat("猫",5,"Satori_Komeiji")
# Kaenbyou_Rin.act()
# print(Kaenbyou_Rin.kind)

class People:
    def act(self):
        print("p",end=" ")
class Father(People):
    def act(self):
        print("f",end=" ")
        super().act()
class Mother(People):
    def act(self):
        print("m",end=" ")
        super().act()
class Son(Father,Mother):
    def act(self):
        print("s",end=" ")
        super().act()
class Daughter(Mother,Father):
    def act(self):
        print("d",end=" ")
        super().act()
Tom=Son()
Mary=Daughter()
Mary.act()
print()
Tom.act()
# #继承方法的顺序(未重写时)根据mro链来
print(Son.__mro__)
# #mro链的算法详见mro.md