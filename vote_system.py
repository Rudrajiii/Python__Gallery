user_name=input("Enter your name:")
candidate_1=input("Enter the name of your 1st candidate:")
candidate_2=input("Enter the name of your 2nd candidate:")
candidate_1_votes=0
candidate_2_votes=0
voter_id=[100,101,102,103,104,105,106]
print(f"Total voter is {len(voter_id)}")
voted=[]
while True:
    if voter_id==[]:
        print("Vote is already completed!!")
        if candidate_1 > candidate_2 :
            print(f"{candidate_1} has won the election with {candidate_1_votes} votes")
        elif candidate_2 > candidate_1 :
            print(f"{candidate_2} has won the election with {candidate_2_votes} votes")
        elif candidate_1 == candidate_1 :
            print("Draw!!!")
        
        break
    else:
        voter=int(input("Enter your id: "))
        exit_out=input("Want to exit?(y/n) :")
        if exit_out=='y':
            print(f"{user_name} exits successfully")
            print(f"{candidate_1} got {candidate_1_votes} votes")
            print(f"{candidate_2} got {candidate_2_votes} votes")
            break
        elif voter in voted :
            print("Already voted")
        else:
            if voter in voter_id:
                print(f"1 for ->{candidate_1}\n2 for ->{candidate_2}")
                ur_choice=int(input("Enter your choice: "))
                if ur_choice==1:
                   candidate_1_votes+=1
                   print(f"You voted {candidate_1}")
                elif ur_choice==2:
                   candidate_2_votes+=1
                   print(f"You voted {candidate_2}")
                   
                voter_id.remove(voter)
                voted.append(voter)
            else:
               print(f"Your id {voter} is wrong , please enter the correct one")
            

            

