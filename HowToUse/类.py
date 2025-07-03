"""类相关内容"""
"""Menu
class 类参数 方法
self 对象 构造
析构 公有 私有
保护
"""
# #class 类名:
# #class 类名():
# #class 类名(object):
# #以上三者全都是类的定义写法
class Vehicle:
    speed=10    #类中的变量成为类参数
    position=0  #全都是public
    def move(self):#必须包含self参数，理由见car1.iden的实际意义(可以随便改成s之类的，不过规范是self)
        print("前进中...")
        self.position+=self.speed
    def check(self):    #类中的函数成为类方法
        print("目前位置:",self.position)
    def iden(self):
        return self
"""下方大量注释部分简而言之就是,操作对象不改变类,操作类改变对象"""
# print(Vehicle.speed)    #可直接访问类的类参数
# Vehicle.class_args1=1    #可直接为类添加参数
car1=Vehicle()  #实例化对象
# print(car1.speed)       #可直接访问对象的类参数
# car1.speed=70           #改变对象的对象参数不改变类的参数
# print(Vehicle.speed)
# car1.obj_args=1         #可直接为对象添加参数
# #print(Vehicle.obj_args)#为对象添加参数不改变类的参数
# print(car1.class_args1) #在创建对象前添加的参数显然会为对象也创建该参数
# Vehicle.class_args2=2
# print(car1.class_args2) #为类添加参数，不管是否已经创建对象，都会为对象添加新的参数
# car1.class_args1=3
# print(Vehicle.class_args1)#改变对象的类参数不影响类的参数
car1.move()
car1.check()
print(car1,car1.iden)
#self表示调用该方法的对象,即car1.iden()实际上是Vehicle.iden(car1),因此方法必须含有self参数

# #构造与析构
class Pet:
    def __init__(self,kind,age,c): #构造函数
        print("调用构造函数")
        self._kind=kind#单下划线的变量(protected),仅用于提示这个玩意最好不要直接改
        self.__age=age #双下划线的变量(private),无法被直接访问和继承
        self.owner=c
    """
    保护的方法和私有的方法同理,不多说
    """
    def whose(self):
        return f"{self.owner}的"
    def how_old(self):
        return self.__age
    def which_kind(self):
        return self.kind
    def __del__(self):              #析构函数(先进行析构函数的内容再del 对象)
        print("析构中")
Kaenbyou_Rin=Pet("cat","4","Satori_Komeiji")
print(f"阿燐是{Kaenbyou_Rin.which_kind()}")
print(f"阿燐的主人是{Kaenbyou_Rin.owner}")
try:
    print(f"阿燐的年龄是{Kaenbyou_Rin.__age}")
except:
    print("打探女孩子的年龄可不是一个好行为哦")
Kaenbyou_Rin._Pet__age=5   #python的私有成员还对应一个公有变量:_类名__成员变量名,但是少用
print("阿燐长大了一岁")
print(f"阿燐的年龄是{Kaenbyou_Rin.how_old()}")
del Kaenbyou_Rin
print("阿燐！！")