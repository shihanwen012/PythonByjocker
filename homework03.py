# 1.
#五角数
# def getPentagona1Number(n):
#     if n % 10 == 0:
#         print(n)

# def start():
#         for n in range(1,101):
#             num = n*(3*n-1)/2
#             print(num,end=" ")
#             getPentagona1Number(n)
# start()

# 2.
#求一个整数各位数字和
# def sumDigits(n):
#     sum = 0
#     for i in range(len(n)):
#         sum = int(n[i]) + sum
#     print(sum)
# def star():
#     n = str(input('请输入一个整数'))
#     sumDigits(n)
# star()

# 3.
#让三个数升序
# def displaysortednumbers(num1,num2,num3):
#     Num = [num1,num2,num3]
#     Num.sort()
#     print(Num)
# def star():
#     num1 = float(input('请输入第一个数:'))
#     num2 = float(input('请输入第二个数:'))
#     num3 = float(input('请输入第三个数:'))
#     displaysortednumbers(num1,num2,num3)

# star()

# 4.
# 计算未来投资 1090
# def futureinves(investmentValue,monthrate,year):
#     i = 0
#     for i in range(1,year + 1):
#         weilai = investmentValue * ((1 + monthrate) ** i)
#         print(i,end = '')
#         print('投资%.2f'% weilai)
# def star():
#     investmentValue = float(input('请输入投资额：'))
#     monthrate = float(input('请输入年利率：'))
#     year = int(input('请输入年数：'))
#     futureinves(investmentValue,monthrate,year)

# star()


#5.
#显示字符
# def printChars(ch1,ch2):
#     for i in range(ch1,ch2+1):
#         j = chr(i)
#         print(j,end = " ")
#         if (i + 2) % 10 == 0:
#             print()

# def Start():
#     ch1 = 49
#     ch2 = 90
#     printChars(ch1,ch2)

# Start()

# 6. 
#一年的天数
# def numberOfDaysInAYear(year):
#     for i in range(year,year + 11):
#         print("%d年"%i,end = " ")
#         if i % 4 == 0:
#             print('366天')
#         else:
#             print('365天')

# def Start():
#     year = 2010
#     numberOfDaysInAYear(year)
# Start()

# 7.
#计算两点间距离
# def distance(x1,x2,y1,y2):
#     juli =((x2-x1)**2+(y2-y1)**2)**0.5
#     print(juli)
# def start():
#     x1 =float(input('输入第一个横坐标'))
#     x2 =float(input('输入第二个横坐标'))
#     y1 =float(input('输入第一个纵坐标'))
#     y2 =float(input('输入第二个纵坐标'))
#     distance(x1,x2,y1,y2)

# start()



# 9.
# import time
# def main():
#     localtime = time.asctime(time.localtime(time.time()))
#     print("本地时间为 :", localtime)
# main()


# 10.
#掷色子
import random
def yici(a,b):
    if a + b == 2 or a + b == 2 or a + b == 13:
        print('很遗憾，你输了')
    elif a + b == 7 or a + b == 11:
        print('恭喜你，你赢了')
    else:
        erci(a,b)

def erci(a,b):
    c = random.randint(1,7)
    d = random.randint(1,7)
    print(c)
    print(d)
    if c + d == 7:
        print('很遗憾，你输了')
    elif c + d == a + b:
        print('恭喜你，你赢了')
    else:
        erci(a,b)

def Start():
    a = random.randint(1,7)
    b = random.randint(1,7)
    print(a)
    print(b)
    yici(a,b)

Start()
