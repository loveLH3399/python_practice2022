#!/usr/bin/env python
# coding: utf-8

# In[3]:


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 ⌘F8 切换断点。
if __name__ == '__main__':
    print_hi('Congyi')

import time
scale = 50
print("执行开始".center(scale//2,"-"))
start = time.perf_counter()
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale-i)
    c = (i/scale)*100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end="")
    time.sleep(0.1)
print("\n"+"执行结束".center(scale//2,'-'))


# In[17]:


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 ⌘F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('Congyi')

#TextProBarV1.py
import time
for i in range(101):
    print("\r{:3}%".format(i),end="")
    time.sleep(0.1)
scale = 10
print("-----执行开始-----")
for i in range(scale+1):
    a = '*'* i
    b = '.'*(scale-1)
    c = (i/scale)*100
    print("{:^3.0f}%[{}->{}]".format(c,a,b))
    time.sleep(0.1)
print("-----执行结束-----")


# In[12]:


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 ⌘F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('Congyi')

height, weight = eval(input("请输入身高（米）和体重（公斤）【逗号隔开】"))
#eval() is used to evaluate the user's input as a Python expression
#height and weight - two variables
bmi = weight/(pow(height,2))#指数函数 height^2
print("BMI数值为：{:2f}".format(bmi))
#表示要插入一个浮点数，并以带有两位小数的格式显示

who, nat = "",""
if bmi < 18.5:
    who, nat = "偏瘦", "偏瘦"
elif 18.5 <= bmi < 24:
    who, nat = "正常", "正常"
elif 24 <= bmi < 25:
    who, nat = "正常", "偏胖"
elif 25 <= bmi < 28:
    who, nat = "偏胖", "偏胖"
elif 28 <= bmi < 30:
    who, nat = "偏胖", "肥胖"
else:
    who, nat = "肥胖", "肥胖"
print("BMI指标为：国际'{0}',国内'{1}'".format(who, nat))


# In[6]:


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 ⌘F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('Congyi')

pi = 0
N = 100#循环次数
for k in range(N):
    pi +=1/pow(16,k)*(        4/(8*k+1)-2/(8*k+4)-        1/(8*k+5)-1/(8*k+6))
print("圆周率值是：{}".format(pi))


# In[5]:


def print_hi(name):
    print(f'Hi, {name}')
    
if __name__ == '__main__':
    print_hi('Congyi')

from random import random
from time import perf_counter
DARTS = 1000*1000
hits = 0.0
start= perf_counter()
for i in range(1, DARTS+1):
    x, y = random(), random()
    dist = pow(x ** 2 + y **2, 0.5)#判断点在不在圆内，即任意点到圆点的距离和1比大小
    if dist <= 1.0:
        hits = hits + 1
pi = 4*(hits/DARTS)
print("圆周率值是：{}".format(pi))
print("运行时间是：{:.5f}s".format(perf_counter()-start))


# In[7]:


# 这是一个示例 Python 脚本。
#daydayupq1.py
dayup =pow(1.001, 365)
daydown= pow(0.999, 365)
print("向上:{:.2f},向下:{:.2f}".format(dayup, daydown))
# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 ⌘F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助


# In[6]:


# 这是一个示例 Python 脚本。

# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。
#daydayupq2.py
dayfactor=0.005
dayup = pow(1+dayfactor, 365)
daydown = pow(1-dayfactor, 365)
print("向上:{:.2f}, 向下:{:.2f}".format(dayup, daydown))

def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 ⌘F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助


# In[8]:


# 这是一个示例 Python 脚本。

# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。
#daydayupq3.py
dayup=1.0;
dayfactor=0.01;
for i in range(365):
    if 1 % 7 in [6.0]:
        dayup=dayup*(1-dayfactor);
    else:
        dayup=dayup*(1+dayfactor);
print("工作日的力量：{:.2f}".format(dayup));


# In[10]:


#daydayupq4.py
def dayUP(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [6,0]:
            dayup = dayup*(1 - 0.01)
        else:
            dayup = dayup*(1 + df)
        return dayup
    dayfactor = 0.01
    while dayUP(dayfactor) < 37.78:
        dayfactor += 0.001
    print("工作日的努力参数是：{:.3f}".format(dayfactor))


# In[13]:


from scipy import stats
import scipy
import numpy
# 导入统计的包
ob_matrix = [[527,72],[206,102]]
#真实矩阵

# Define the observed contingency table
observed_matrix = [[527, 72], [206, 102]]

# Perform the chi-squared test
chi2, p, dof, expected = stats.chi2_contingency(observed_matrix)

# Print the results
print("Chi-Square Value:", chi2)
print("P-value:", p)
print("Degrees of Freedom:", dof)
print("Expected Frequencies Table:")
print(expected)

# 1、卡方值 2、p值 3、自由度 4、理论矩阵
# 卡方值理论值
# 卡方值大，相关性大
# p值大小，不相关大概率


# In[13]:


# TempConvert.py
TempStr = input("请输入带有符号的温度值：")
if TempStr[-1] in ['F', 'f']:
    C=(eval(TempStr[0:-1]) - 32)/1.8;
    print("转换后的温度是{:.2f}C".format(C));
elif TempStr[-1] in ['C' , 'c']:
    F=1.8*eval(TempStr[0:-1]) + 32;
    print("转换后的温度是{:.2f}F".format(F))# 按
else:
    print("输入格式错误");# ⌃R 执行或将其替换为您的代码。


# In[18]:


# PythonDraw.py
import turtle;

turtle.setup(650, 350, 200, 200);
turtle.penup();#拿起画笔，停止作画
turtle.fd(-250);
turtle.pendown();#放下画笔，开始作画
turtle.pensize(25);
turtle.pencolor("purple");
turtle.seth(-40);
for i in range(4):
    turtle.circle(40, 80);
    turtle.circle(-40, 80);
turtle.circle(40, 80 / 2);
turtle.fd(40);
turtle.circle(16, 100);
turtle.fd(40 * 2 / 3);
turtle.done()#结束语


# In[ ]:




