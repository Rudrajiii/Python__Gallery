# #Welcome To "KBC"
# print("To Play the game register your name below")
# Nox=input("Enter your name:")

# AGE = int(input("Enter your Age:"))

# if AGE>= 18 :
#     print("welcome to our game sir.")
# else:
#     # print("welcome to our game buddy.")
#     print()

# print("__Type '1' to start__\n")
# s=int(input())
# if s==1:
#     print("Your first question is for RS 50K")
# else:
#     print("type 'run' please.")

# Store_correct_Answers =[]
# #code start
# Q1="1. Grand Central Terminal, Park Avenue, New York is the world's"
# print(Q1)
# QQ=50000
# a=1
# b=2
# c=3
# d=4
# print('1)largest railway station',  '2)highest railway station')
# print('3)longest railway station',  '4)None of the above')


# ans1=int(input("I choose my answer as option: \n"))
# if ans1==3 :
#     print("Congratulations!! You are correct and you have won \"50K\"")
#     Store_correct_Answers.append(QQ)
# else:
#     print("correct option is 3")


#  #Next part of code


# Ask=input("Do you want to go for next question?{y/n}: ")
# if Ask=='y':
#     print("Cool!!your next question is going to be for 1 lakh.")
# else:
#     print('okk.just give a try in next one')


    
# Q2="Entomology is the science that studies"
# print(Q2)
# QQQ=100000
# e=1
# f=2
# g=3
# h=4
# print("1)Behavior of human beings",   "2)Insects")
# print("3)The origin and history of technical and scientific terms",   "4)The formation of rocks")


# ans2=int(input("I choose my answer as option: \n"))
# if ans2==2:
#     print("Congratulations!! You are correct and you have won \"1 lakh\"")
#     Store_correct_Answers.append(QQQ)
# else:
#     print("correct option is 2")
# #last part of code
# Ask_last=input("Do you wanna go for last question?{y/n}: ")
# if Ask_last=='y':
#     print("superb!!There is an golden chance to win 5lakhs ")
# else:
#     print("okk. you can just try next one!!")



# Q3="Excessive secretion from the pituitary gland in the children results in"
# print(Q3)
# QQQQ=500000
# i=1
# j=2
# K=3
# l=4
# print('1)increased height',   '2)retarded growth')
# print('3)weakening of bones',  '4)None of the above')


# ans3=int(input("I choose my answer as option: \n"))
# if ans3==1 :
#     print("ADH-BHUTTTTTTTTTT ADH-BHUTTTTTTTTTT you have got 5lakhs with giving the correct answer of the question")
#     Store_correct_Answers.append(QQQQ)
# else:
#     print("correct option is 1")
# #over the code


# print("All the prices you got \n")
# print(Store_correct_Answers)

# total_prize = sum(Store_correct_Answers)

# Display the total prize amount
# if total_prize == 650000:
    # print(f"Congratulations! You won {total_prize} Rs.")
# else:
    # print(f"you got total{total_prize}")

 
questions = [
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Who is your editor?", "Rudra", "yash", "Jarves",
    "Ghoi", "None", 1
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
for i in range(0, len(questions)):
  
  question = questions[i]
  print(f"\n\nQuestion for Rs. {levels[i]}")
  print(f"a. {question[1]}          b. {question[2]} ")
  print(f"c. {question[3]}          d. {question[4]} ")
  reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
  if (reply == 0):
    money = levels[i-1]
    break
  if(reply == question[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if(i == 4):
      money = 10000
    elif(i == 9):
      money = 320000
    elif(i == 14):
      money = 10000000
  else:
    print("Wrong answer!")
    break 

print(f"Your take home money is {money}")

