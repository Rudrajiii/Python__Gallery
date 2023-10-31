'''print("hello")
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)'''
# for i in range (1,20):
#     print(i*"🖕")
#     for k in range (50):
#         print(k*"😁")
# for j in range(1,20):
#     print(j*"🖕")

'''zex_li=["Vicky","Ram","Roshan","Rony","Riya","deepika","Sakshi"]

sup_li=["priya","Sikha","william","Pragati","Tanvi"]

copy_li=[]
while(True):
  wish_all=input("Whom do u wanna wish from your friend")
  if(wish_all in zex_li):
   print("Have a grt day ahead!!",wish_all)
  elif(wish_all in sup_li):
   print("invalid name, Type it Again")
   continue
    
  else:
   print()
  copy_li.append(wish_all)
    
  rep_t=input("want to wish another one?\nY/N\n:")
  if(rep_t=='N'):
    break

print("All the names you wished\n")

# for zex_l in copy_li:
print(copy_li)
    '''
   
# import time
# print("__Current Timing__")
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# Hour = int(input("Enter the time(0-23)"))
# # Name=input("Enter the name you want to wish:")
# if (Hour >= 0 and Hour<12 ):
#     print("Good morning!!")

# elif (Hour>= 12 and Hour<=17 ):
#     print("Good afternoon!!") 

# elif( Hour >17 and Hour <=20) :
#     print("Good evening!!")
# else:
#     print("good Night!!")


def perrin_seq(n):
    sequence = [3,0,2]
    for i in range(3,n):
        Next_Num = sequence[i-2]+sequence[i-3]
        sequence.append(Next_Num)
    return sequence
n=int(input("Enter a number:"))
print(perrin_seq(n))


# program of scrinning Diamond
def py_show(n):
  for i in range(n):
    print(' '*(n-i-1)+'* '*(i+1))
  for j in range(n-1,0,-1):
    print(' '*(n-j)+'* '*(j))

n=4

print(py_show(n))
    
# program of scrinning letter A
for row in range(7):
  for col in range(5):
    if ((col==0 or col==4) and row!=0) or ((row==0 or row==3) and (col>0 and col<4)):
      print("*",end='')
    else:
      print(end=" ")

  print()
    
# program of scrinning letter A
# for row in range(7):
#   for col in range(5):
#     if (col==0 or col==4) or ((row==0 or row==3) and (col>0 and col<4)):
#       print("*",end='')
#     else:
#       print(end=" ")

#   print()
# program of scrinning letter B
for row in range(7):
  for col in range(5):
    if ((col==0)or (col==4 and (row!=0 and row!=3 and row!=6 ))) or ((row==0 or row==3 or row==6) and (col>0 and col<4)):
      print("*",end='')
    else:
      print(end=" ")

  print()

# program of scrinning letter A  
str1=""
for row in range(7):
  for col in range(5):
    if ((col==0 or col==4) and row!=0) or ((row==0 or row==3) and (col>0 and col<4)):   
      str1=str1+"*"
    else:
      str1=str1+" "

  str1=str1+'\n'

print(str1)