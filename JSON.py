# email=input("enter a email:")

# Body=email[:email.index("@")]
# Domain=email[email.index('@')+1:]

# print(Body)
# print(Domain)

# email=input("enter a email:")

# Index_find=email.index("@")

# Body=email[:Index_find]
# Domain=email[Index_find +1:]
# print(f"The body is {Body} and the Domain is {Domain}")
import time
for i in reversed(range(1,2)):
    print(i)
    time.sleep(1)
print("boom happy birthday!!!")


try:
    Ui=int(input("Enter a number:"))
    for i in range(1,11):
     print(f'{Ui} X {i} = {Ui * i}')
except ValueError:
     print('invalid input')

try:
 tup1 = (1,2,3,4,5)
 tup1.insert(2,9)
 print(tup1) 
 # list1 = list(tup1)
 # list1.insert(2,9)
 # tup1 = tuple(list1)
 # print(tup1) 
except AttributeError :
  print("No changes can be made in a tuple directly, Once they are created")

