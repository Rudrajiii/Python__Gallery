import re
def is_valid_email(email):
    pattern = ("^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$")

    
    if re.match(pattern, email):
        return True
    else:
        return False
store_email=[]
print("|put your email like \'_____@.gmail.com\' format & don't give space while writing|")

email = input("Enter an email address: ")

# Call the function
if is_valid_email(email):
    print("Valid email address")
    store_email.append(email)
    
else:
    print("Invalid email")
print(store_email)






    
