#S-1
# from pprint import pprint
import json

my_d: dict={

          'name':'Yash',
          'age': 30,
          'address':{
                
               'street':'206 Main Road',
               'city':'Kolkata',
               'pin':'736135',
               'contacts':{
               
                         'phone':+91-5467828,
                         'Email-address':'saharudra@gmail.com',
                         'insta-id':'__i_am_Saha__'
                         }

          },
           'hobbies': ['Drawing','Coding','Reading']

             }

print(json.dumps(my_d,indent=2))

#S-2
x=[1,2,4,5,1,3,1,6,5]
Most = max(x,key=x.count)

print(Most)

#S-3
my_Tuple=[[1,2],[3]]
my_Tuple[1].append(4)
print(my_Tuple)

#S-4 [part-1]
item=[
    'gem',
    'Harry',
    'Rudra',
    'Akhil'
     ]
indx=item.index('gem')
stor=item.pop(indx)
item.append(stor)
print(json.dumps(item,indent=2))
# item.sort()
# print(item)

#S-4 [part-2]
item=[
    'gem',
    'Harry',
    'Rudra',
    'Akhil'
     ]
indx=item.index('gem')
stor=item.pop(indx)
item.insert(2,stor)
print(json.dumps(item,indent=2))

#S-5
balance=940.23
while(True):
 try:
    num=input('deposit:')
    balance+=float(num)
    print(balance)
    break
 except ValueError:
    print(f'\"Donot input {num} ,input some valid number not string\"')
    
#s-6
inv={
     'sword':1,
     'Potion':3
     }
loot={
      'sword':1,
      'Potion':2,
      'shield':4
      }
new_dict={
    k: inv.get(k,0) + loot.get(k,0) \

    for k in set(inv | loot)
}
print(new_dict)

#s-7
a=[]
for i in range(10):
  a.append(i*++i)
for a[i] in a :
  print(a[i])

#S-8
# import time
# from itertools import cycle
# lights={
#        ('yellow',1),
#        ('green',1),
#        ('red',1)
#        }
# for c,s in cycle(lights):
#   print(c)
#   time.sleep(s)
# colors=cycle(lights)
# while True:
#  c,s=next(colors)
#  print(c)
#  time.sleep(s)


#s-9
num=156742.897111899
round_num=str(round(num,-1))
print(round_num)

#s-10
def tspeak(inputText):
  ledger={

       'a':'6',
       'b':'p',
       'c':'&',
       'd':'+',
       'e':'=',
       'f':'_',
       'g':'-',
       'h':')',
       'i':'(',
       'j':'"',
       'k':'#',
       'l':'@',
       'm':'!',
       'n':'~',
       'o':'`',
       'p':'*',
       'q':'^',
       'r':'%',
       's':'$',
       't':'/',
       'u':']',
       'v':'[',
       'w':'?',
       'x':'<',
       'y':'>',
       'z':'::'

}

  outputText=''
  for c in inputText:
   if c in ledger.keys():
    outputText=''.join([outputText,ledger[c]])
   else:
    outputText=''.join([outputText,c])
  return outputText
messege_secret=input("Enter the messege that you want to convert into a secret code:")
print(tspeak(messege_secret))


#s-11
num1=1_000_000_000
num2=2_000

ans=num1*num2
print(f'{ans:,}')
# print(ans)

#s-12 decoding the syntext:
def tspeak(inputText):
    ledger = {
        'a': '6',
        'b': 'p',
        'c': '&',
        'd': '+',
        'e': '=',
        'f': '_',
        'g': '-',
        'h': ')',
        'i': '(',
        'j': '"',
        'k': '#',
        'l': '@',
        'm': '!',
        'n': '~',
        'o': '`',
        'p': '*',
        'q': '^',
        'r': '%',
        's': '$',
        't': '/',
        'u': ']',
        'v': '[',
        'w': '?',
        'x': '<',
        'y': '>',
        'z': '::'
    }

    # Create a reverse lookup dictionary
    reverse_ledger = {}
    for key, value in ledger.items():
        if value not in reverse_ledger:
            reverse_ledger[value] = [key]
        else:
            reverse_ledger[value].append(key)

    outputText = ''
    i = 0
    while i < len(inputText):
        found = False
        for value, chars in reverse_ledger.items():
            if inputText.startswith(value, i):
                outputText += chars[0]
                i += len(value)
                found = True
                break
        if not found:
            outputText += inputText[i]
            i += 1

    return outputText
   
   

message = 'p$+# &)]* %=) p)=~ # @`+= )6)6 $`%%>'
encoded_message = tspeak(message)
# print(encoded_message)

# Reverse the transformation
decoded_message = tspeak(encoded_message)
print(decoded_message)

#Weight mesurement
unit=input("Enter the unit of your weight in (K/P): ")
weight=float(input("Enter your weight: "))

if unit=='K':
   weight=weight * 2.20462
   ass_unit=' pbs'
   print(f"Your weight in pound is {weight}{ass_unit}")
elif unit=='P':
   weight=weight / 2.20462
   ass_unit=' kgs'
   print(f"Your weight in pound is {weight}{ass_unit}")
else:
   print(f"{unit} is invalid. please recheck.")
   
####Passward-hiding
# print("your password is ",password)
# print(var)
# print(var.islower())
import pwinput as pin
My_password='rudrasaha.'
while(True):
 password=pin.pwinput("Type your password of 10 digit :","X")
 var=(f"your password is {password}")  
 if password==My_password and len(password)==10:
   print("verrified")
   break
 else:
   print("password is wrong.Please Re-enter the password.")
   continue
   
from calendar import month
from datetime import datetime

now= datetime.now()
d, m , y = now.day , now.month , now.year

print(f"Date:{d}",month(themonth=m,theyear=y))

