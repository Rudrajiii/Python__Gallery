
def write_in_Folder(dict):
  with open("dict.txt", "a") as f:
    f.write('\n')
    f.write(dict['name']+"       "+dict['roll']+"      "+dict['sec']+"       "+dict['year']+"       "+dict['stream'])
    f.write('\n')
print("//Your data will be stored//")

while True:
    ask = input("Enter 1 to store data and 0 to quit:")
    
    if ask == '0':
        break
    elif ask != '1':
        print("Invalid input. Please enter 1 to store data or 0 to quit.")
        continue

    N = input("Enter your name:")
    S = input("Enter your sec:")
    Y = input("Enter your year:")
    A = input("Enter your stream:")
    R = input("Enter your roll no:")

    data_dict = {
        'name': N,
        'roll': R,
        'sec': S,
        'year': Y,
        'stream': A
    }
    
write_in_Folder(data_dict)

with open("dict.txt", "r") as f:
    content = f.read()

with open("tik.txt", "w") as add:
    add.write(content)

  
