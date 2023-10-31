import random

define_name = ['Snake', 'Gun', 'Water']
# bulian_py = [1, 0, -1]
num_values_to_select = 1
selected_value = random.sample(define_name, num_values_to_select)
choose_amg = "".join(random.sample(define_name, num_values_to_select))
Total_point=[]
while(True):
 try:
    user_input = (input("Choose among Snake/Gun/Water:"))
    print(f"Computer chose {choose_amg}")

    if user_input not in define_name:
    #  raise TypeError("Invalid input")
     print("Invalid input_01")
     break

    if choose_amg == user_input:
        print("It's a Draw")
    else:
        if choose_amg == 'Gun' and user_input == 'Snake':
            print("Loss")
        elif choose_amg == 'Gun' and user_input == 'Water':
            print("Win")
            Total_point.append(1)
        elif choose_amg == 'Snake' and user_input == 'Gun':
            print("Win")
            Total_point.append(1)
        elif choose_amg == 'Snake' and user_input == 'Water':
            print("Loss")
        elif choose_amg == 'Water' and user_input == 'Snake':
            print("Win")
            Total_point.append(1)
        elif choose_amg == 'Water' and user_input == 'Gun':
            print("Loss")
    Inpu_again=input("Wanna play again?(y/n):")
    if Inpu_again == 'n':
       break 

 except TypeError:
    print("Invalid input, please choose among snake / gun / water only")
 finally:
    print("Tnx for Playing")

Total=sum(Total_point)
print(f"Your Total point is {Total}")


import random
choices = {
            "Snake":1,
            "Water":2,
            "Gun":3
}
possible_choices = [1,2,3]
try:
    player_choice = int(input("Enter your choice:-\n1 for Snake\n2 for Water\n3 for Gun\n>>> "))
    if player_choice>=4:
      raise ValueError
except ValueError:
    print("You Entered a wrong choice! Try Again")
    print("There is a value Error")
    exit()
computer_choice = random.choice(list(choices.keys()))
print(computer_choice)
if player_choice == 1:
    print("Player chose:- Snake")
elif player_choice == 2:
    print("Player chose:- Water")
else:
    print("Player chose:- Gun")
print(f"Computer chose:- {computer_choice}")
if player_choice == 1 and choices[computer_choice] == 1 or player_choice == 2 and choices[computer_choice] == 2 or player_choice == 3 and choices[computer_choice] == 3:
    print("The Game is a DRAW!")
elif player_choice == 1 and choices[computer_choice] == 2 or player_choice == 2 and choices[computer_choice] == 3 or player_choice == 3 and choices[computer_choice] == 1:
    print("You WIN!")
else:
    print("You LOSE!")