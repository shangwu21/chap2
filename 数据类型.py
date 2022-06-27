# -*- codeing=utf-8 -*-
# @Time: 17:28
# @Author :liuwei
# @File:数据类型.py\

#字符串索引
s='liuwei'
print(s[0])

print('北京欢迎您'[0])
a='北京欢迎您'
print(a[0:3])

#拼接字符串
x='今天'
y='天气很好'
print(x+y)

#多次输出
print(x*10)

#判断是否包含
print('很好'in y)
print('haha'in y)

#bool类型
b=True
print(b)

c=b+1
print(c)      #1+1
print(False+10) #0+10

#测试对象的bool值
print(bool(18))
print(bool(0),bool(0.0))

#数据转换
m=10
n=3
z=m/n
print(z,type(z))

#浮点数和整数
print("转换",int(3.14),int(1.9),float(6))