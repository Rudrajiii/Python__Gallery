num=['1','3','90']
num=list(map(int,num))
# for i in range(len(num)):
#     num[i]=int(num[i])
# num[2]+=1
# print(num[2])
# def sqr(a):
#     return a*a
squre=list(map(lambda x:x*x,num))    
print(squre)

def sq(q):
    return q**2
def cube(q):
    return q**3
function=[sq,cube]

for i in range(5):
    val= list(map(lambda x:x(i),function ))
    print(val)


l=[1,2,3,4,5,6,7,8,9,10]
def l_greater_com(num):
    return num>5
gr_than_5 =list(filter(l_greater_com,l))
print(gr_than_5)

from functools import reduce
list1=[1,2,3,4]
print(reduce(lambda x,y:x+y ,list1))