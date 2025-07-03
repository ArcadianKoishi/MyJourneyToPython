#斐波那契数列

# #迭代实现
a=1
b=1
c=0
for i in range(2,int(input("所需项数:"))):
    c=a+b
    a=b
    b=c
print(c)
# #递归实现
def fib(n):
    if n<=2:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(int(input("所需项数"))))