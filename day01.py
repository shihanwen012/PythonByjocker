# cmatrix 数据雨
# s1   火车
# cowsay hello 牛说你好
# chr（）将整形转换成该编码对应的字符串（一个字符）
# ord（）将字符串（一个字符）转换成对应的编码（整数）
# format可以任何类型
# id(x)查看内存地址
# is与== is快 每个字符对应一个内存地址
# in时判断在容器中（可迭代对象）有没有这个东西
# 能被for循环的叫可迭代对象
# +=自加
#切片是一个前闭后开的区间
#[satrt:end:step]
#[开始：结束：间隔]
#命名变量要见名思意


#一到一百相加的和：
# def sum():
#     sum = 0
#     for n in range(1, 101):
#         sum = sum + n
#     return sum
 
# print('一到一百相加的和是:',sum())


#一到一百偶数相加的和：
# he=0
# for i in range(0,100,2):
#     he+=i
# print(he)



# #输入成绩判断等级：
 
# cj=float (input("请输入你的成绩："))
# if cj>=90 and cj<=100:
#     print("优秀")
# elif cj>=70 and cj<90:
#     print("良好")
# elif cj>=60 and cj<70:
#     print("及格")
# else:
#     print("你要努力了")


#a = float(input('请输入数字'))//基础运算
#b = float(input('请输入另一个数字'))
#print('%.2f * %.2f = %.2f'(a,b,a*b))
# print('{} + {} = {}'.format(a,b,a+b))

# email = '295966730@qq.com'//加密
# for e in email :
#     # o = ord(e)
#     # print(o)
#     o = ord(e)-10
#     print(chr(o),end="")

# F = float(input('请输入华氏度')) //华氏度准换摄氏度
# C = (F - 32) / 1.8
# print('%.2F摄氏度'%C)

# year = int(input('请输入年份'))//判断是否为闰年
# if year % 4 == 0 and year % 100!=0 or year % 400 == 0:
#     print("%dyes"%year)
# else:
#     print('%dno'%year)

# F = float(input('请输入华氏度')) //华氏度准换摄氏度
# C = (F - 32) / 1.8
# print('%.2F摄氏度'%C)

# Number = input('请输入一个数字:')

# bai = int(Number[0])//水仙花数
# shi = int(Number[1])
# ge = int(Number[2])

# if bai **3 + shi **3 + ge **3 == int(Number):
#     print('是水仙花')
# else:
#     print('不是水仙花')


7.17
# #1.
# C = float(input('请输入摄氏度')) #//摄氏度准换华氏度
# F = (C *9/5)+32
# print('%.2F华氏度'%F)

# # 2.
# rad = float(input('请输入半径'))
# high = float(input('请输入高'))
# ar = float (rad * rad * 3.14159265358979)
# v = float (ar * high)
# print('底面积为%.2f'%ar)
# print('体积为%.2f'%v)

# # 3.
# foot = float(input('请输入英尺数'))
# meter = foot * 0.305
# print('%.5f英尺 = %.5f米'%(foot,meter))

# #4.
# zw = float(input('请输入最终温度'))
# cw= float(input('请输入初始温度'))
# M = float(input('请输入千克为单位的水量'))
# Q = M * (zw - cw) * 4184
# print('能量为%.5f'%Q)

# # 5.
# ce = float(input('请输入差额'))
# nll = float(input('请输入年利率'))
# lx = ce*(nll/1200)
# print('下月利息为%.5f'%lx)

# # 6.
# v0 = float(input('请输入初速度'))
# v1 = float(input('请输入末速度'))
# t = float(input('请输入速度变化所占用时间'))
# a = (v1-v0)/t
# print('平均加速度为%.5f'%a)

# # 7.
# yue = float(input('存入总月数'))
# qian = float(input('存入金额'))
# jon = qian * (1 + 0.00417)
# feb = (qian + jon) * (1 + 0.00417)
# mar = (qian + feb) * (1 + 0.00417)
# apr = (qian + mar) * (1 + 0.00417)
# may = (qian + apr) * (1 + 0.00417)
# jun = (qian + may) * (1 + 0.00417)
# print('%f月后，账户存款变为%.5f'%(yue,jun))

# # 8.
# Number = int(input('请输入一个0-1000之间的数字'))
# a = int(Number % 100)
# b = a % 10 # 个位数
# c = int(a / 10) # 十位数
# d = int(Number / 100) #百位数
# sum = b + c + d
# print('最终和为 %d'%sum)
