7.18
# 1.
# a,b,c  = eval(input('请输入a,b,c的值:'))
# gen = b**2 - 4*a*c
# r1 = (-b + gen** 0.5)/(2*a)
# r2 = (-b - gen** 0.5)/(2*a)
# if gen > 0:
#     print(r1,r2)
# elif gen == 0:
#     print(r1)
# else:
#     print('没有根奥，弟弟')

2.
# import numpy as np
# num1 = np.random.choice(101)
# num2 = np.random.choice(101)
# he = int(input('%d,%d为两个整数，请输入他们的和'%(num1,num2)))
# if he == (num1 + num2):
#     print('nice兄弟！给力给力')
# else:
#     print('算都能算歪来？')

3.
# def week():
#     today = int(input('请输入今天'))
#     future = int(input('请输入预算天数'))
#     a = future%7
#     b = today+a
#     c = b%7
#     print('今天是星期%d and 预算的天数是星期%d'%(today,c))
# week()

4.
# a,b,c = eval(input('请输入三个整数：'))
# shengxu = [a,b,c]
# shengxu.sort
# print('升序排列为%s'%shengxu)

5.
# jia1,zhong1 = eval(input('第一种大米的价格和重量:'))
# jia2,zhong2 = eval(input('第一种大米的价格和重量:'))
# pingjun1 = jia1/zhong1
# pingjun2 = jia2/zhong2
# if pingjun1 > pingjun2:
#     print('第二种更优')
# elif pingjun1 < pingjun2:
#     print('第一种更优')
# else :
#     print('两者都可以')

# 6.
# def day(year,month):
#     days = ['null','31','29','31','30','31','30','31','31','30','31','30','31']
#     sum = days[month]
#     print('%d年%d月份有%s天'%(year,month,sum))
# def start():
#     year = int(input('请输入年份'))
#     month = int(input('请输入月份'))

7.
# import numpy as np
# AI = np.random.choice(['反','正',])
# sel = input('猜猜是正还是反:')
# if sel == AI:
#     print('奥力给！')
# else :
#     print('8太行啊？铁子')

8.
# import numpy as np
# res = np.random.choice(['0','1','2'])
# sel = input('0表示剪刀，1表示石头，2表示步：')
# if sel == res:
#     print('算你运气好')
# elif sel == '0' and res == '1':
#     print('臭弟弟，人机都打不过？')
# elif sel == '1' and res == '2':
#     print('臭弟弟，人机都打不过？')
# elif sel == '2' and res == '0':
#     print('臭弟弟，人机都打不过？')
# else :
#     print('出师了，兄弟！')

9.
# def function():
#     year = int(input('年'))
#     mounth = int(input('月'))
#     data = int(input('天'))
#     k = year % 100
#     j = year / 100
#     h = (data + (26 * (mounth + 1) / 10) + k + (k / 4) +(j/4) + 5 * j ) % 7
#     print('这一天是星期%d'%h)

# function()

10.
# import numpy as np
# shu = np.random.choice(['ace','1','2','3','4','5','6','7','8','9','10','jack','queen','king'])
# hua = np.random.choice(['梅花','方片','红桃','黑桃'])
# print(hua,shu)

11.
# huiwen = input('请输入一个三位数')
# h = huiwen[0]
# u = huiwen[1]
# i = huiwen[2]
# if h == i  :
#     print('这是一个回文数')
# else :
#     print('这不是回文数')

12.
# a,b,c = eval(input('请输入三角形的三个边长'))
# zc = a+b+c
# if a+b>c and  a+c>b and b+c>a:
#     print('周长为%d'%zc)
# else:
#     print('该三角形不合法')

7.19
1.
zheng = 0
fu = 0
he = 0
for i in range(200):
    a = int(input('请输入整数:'))
if a != 0:
    if a > 0:
        zheng += 1
    else:
        fu += 1
else:
    pass
he += a
junzhi = he / (zheng + fu)
print('您输入的正数有%d个，负数有%d个，平均值是%.2f'%(zheng,fu,junzhi))