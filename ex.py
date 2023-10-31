import time
print("__Current Timing__")
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
Hour = int(time.strftime('%H'))
Name=input("Enter the name you want to wish:")
if ( Hour>= 0 and Hour<12 ):
    print("Good morning!!",Name)

elif (  Hour>= 12 and Hour<=17 ):
    print("Good afternoon!!",Name) 

elif(  Hour>17 and  Hour<=20) :
    print("Good evening!!",Name)
else:
    print("good Night!!",Name)


print(time.ctime(time.time()))


time_object=time.localtime()
# print(time_object,end="\n ")
local_time=time.strftime("%B %d %Y %H:%M:%S",time_object)
print(local_time)






