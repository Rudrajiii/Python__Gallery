#program of time countdown
import time
user_time=int(input("Enter your time in seconds:"))

for c in range(user_time,0,-1):
    seconds= c % 60
    minutes=int(c / 60) % 60
    hours =int(c / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("TIME's UP")    

import time

user_hours = int(input("Enter the number of hours:"))
total_seconds = user_hours * 3600

for c in range(total_seconds, 0, -1):
    seconds = c % 60
    minutes = int(c / 60) % 60
    hours = int(c / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME's UP")




import time

user_minutes = int(input("Enter the number of minutes:"))
total_seconds = user_minutes * 60

for c in range(total_seconds, 0, -1):
    seconds = c % 60
    minutes = int(c / 60) % 60
    hours = int(c / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME's UP")

