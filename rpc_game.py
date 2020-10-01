import random


def computer_choice():
    choice_num = random.randint(1, 30)
    if choice_num <= 10:
        comp_choice = "rock"
    elif choice_num <= 20:
        comp_choice = "paper"
    elif choice_num <= 30:
        comp_choice = "scissor" 
    return comp_choice


if __name__ == "__main__":
    comp_choice = computer_choice()
    # print (comp_choice)

    user_choice = input('''Enter your choice : "rock", "paper" or "scissor"\n''')
    # print("\n")

    if user_choice == comp_choice:
        print ("It is a Tie\n")

    else:
        if user_choice == "rock" and comp_choice == "paper":
            print ("You Lose. Better Luck Next Time\n")

        elif user_choice == "paper" and comp_choice == "rock":
            print ("Congratulatins! You Win\n")

        elif user_choice == "paper" and comp_choice == "scissor":
            print ("You Lose. Better Luck Next Time\n")

        elif user_choice == "scissor" and comp_choice == "paper":
            print ("Congratulatins! You Win\n")

        elif user_choice == "rock" and comp_choice == "scissor":
            print ("Congratulatins! You Win\n")

        elif user_choice == "scissor" and comp_choice == "rock":
            print ("You Lose. Better Luck Next Time\n")



    print ("Computer : " + comp_choice)
    print ("User :" + user_choice)
    
