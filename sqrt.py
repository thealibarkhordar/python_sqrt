import math
from math import sqrt
list_num=[]

n = int(input())
c = 0
while c < n:
    num = int(input())
    num2 = abs(num)
    num2 = round(sqrt(num2),4)
    list_num.append(float(num2))
    c += 1

for i in range (0,len(list_num )):
    print ('%.4f'%(list_num[i]))
    