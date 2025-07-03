mro链是用于继承成员(方法或变量)时的选择优先级关系
以下都以形如A(B,C)的方式表示继承关系,括号内的类是括号外类的父类，并按照继承顺序排列
简写object类为obj

三条规则:
1子类必须出现在父类左侧
2先被继承的类必须在后被继承的类左侧
(若违反第一条，则类定义错误，直接报错)
如A(B,C) C(B)
(若由于A要满足第二条而导致B不满足第二条，直接报错)
如A(B,C) B(D,E) C(E,D)
3每个类只出现一次

1.A(B)
显然B是A的父类
A的mro链:A->B->obj

2.A(B,C)
A同时有多个父类，按照继承顺序写
A的mro链:A->B->C->obj

3.A(B,C) B(D)
A的父类B还有父类，因此先将B的链写完再写C的链
A的mro链:A->B->D->C->obj

4.A(B,C) B(BCF,BF) C(BCF,CF)
BCF需在会出现在A的mro链里的所有BCF的子类都出现后再出现,BF在BCF后，必须出现在BCF右侧
A的mro链:A->B->C->BCF->BF->CF

5.A(B,C) B(BF,BCF) C(BCF,CF)
同理4
A的mro链:A->B->BF->C->BCF->CF

6.A(B,C) B(BF,BCF) C(CF,BCF)
同理4
A的mro链:A->B->BF->C->CF->BCF

7.A(D,B,C) B(BCF,BF) C(BCF,CF) D(BCDF) BCF(BCDF)
A的mro链:A->D->B->C->BCF->BCDF->BF->CF