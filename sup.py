# i = 5
# while (i>=0):
#     print(i)
#     i=i-1

zex_li=["Vicky","Ram","Roshan","Rony","Riya","deepika","Sakshi"]

sup_li=["priya","Sikha","william","Pragati","Tanvi"]

copy_li=[]
while(True):
  wish_all=input("Whom do u wanna wish from your friend\n")
  if(wish_all in sup_li):
   print("Invalid syntext Type it again")
   continue
  else:
   print("have a grt day ahead!!",wish_all)
  copy_li.append(wish_all)
    
  rep_t=input("want to wish another one?\nY/N\n:")
  if(rep_t=='N'):
    break

print("All the names you wished\n")

# for zex_l in copy_li:
print(copy_li)
    
   
nums=range(2,1000)

def is_prime(nums):
  for c in range(2,nums):
    if (nums%c)==0:
      return False
  return True
primes=list(filter(is_prime,nums))  
print(primes)

#here generator has been used
# nums = range(2, 50)
# list = [i for i in range(2, max(nums)) if all(i % n != 0 for n in nums if n != i)]
# print(list)










    


