"""字符串的常见操作"""
"""Menu(通过ctrl+f找到具体用法)
find index count
len isupper islower
startswith endswith replace
split isdigit encode
decode a[i]
"""

# #find返回a中找到的第一个子字符串的起始下标，未找到则返回-1
# #a.find(子字符串,可省略的查找开始下标，可省略的查找结束下标)

# #index和find功能基本一致，不过没找到会进行报错
# #a.index(子字符串,可省略的查找开始下标，可省略的查找结束下标)

# #返回a中子字符串出现的次数，每个字符仅可取用一次
# #a.count(子字符串,可省略的查找开始下标，可省略的查找结束下标)
# print("aaaaa".count("aa")) #输出为2

# #返回a中字符串长度
# #len(a)

# #a.isupper()  a.islower()返回全体字符是否全都是大写或小写
# #a.upper() a.lower()返回全体字符变大写或小写的字符串，不改变原字符串
# #a.capitalize()返回首字母大写，其他都小写的字符串，不改原字符串

# #startswith和endswith是以xxx为开头或者结尾，返回布尔值，甚至拼写还要注意三单)
# #a.startswith(子字符串,可省略的查找开始下标，可省略的查找结束下标)
# #a.endswith(子字符串,可省略的查找开始下标，可省略的查找结束下标)

# #replace替换内容,默认从左往右替换,返回替换的字符串，不改变原来的
# #a.replace(旧内容字符串,新内容字符串,替换次数)
# a="qwq"
# a.replace("q","p",1)
# print(a)                          #qwq
# print("qwq".replace("q","p",1))   #pwq
# a="pwp"                           #会更改a对应的内存地址,int,float,complex,tuple同理
# print(a)

# #split分割字符串,用于分割的字符串会被删掉，返回列表
# #a.split(可以省略默认为空格的字符串strA,可以省略的分割次数)
# #print("qwowp".split("w",1))      #["q","owp"]

# #isdigit看字符串是否是纯数字
# a="123"
# b="12q"
# print(a.isdigit(),b.isdigit())

# #进行加密和解密(编码)
# a="你好11"
# b=a.encode("utf-8")
# c=b.decode()

# #a[i]可以访问字符串某下标的字符，但不可更改该字符串
# #a[i:j:k]进行切片访问