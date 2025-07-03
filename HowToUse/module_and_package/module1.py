"""此模块用于被module.py导入"""
name_="koishi"
def rua():
    print("Rua!")
    return

# #__name__为"__main__"或模块名/包名(__init__.py时)
if __name__=="__main__":#自身运行
    print("测试完成，无误")
if __name__=="module1":#作为模块被调用
    print("module1.py作为模块被调用")