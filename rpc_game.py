import random


if __name__ == "__main__":

    points = int(input("How much point(s) game do you want to play : "))

    comp_score = 0
    user_score = 0

    while 1:

        if comp_score == points or user_score == points:
            break

        choice_num = random.randint(1, 30)

        if choice_num <= 10:
            comp_choice = "rock"

        elif choice_num <= 20:
            comp_choice = "paper"

        elif choice_num <= 30:
            comp_choice = "scissor"

        # print (comp_choice)

        user_choice = input(
            '''Enter your choice : "rock", "paper" or "scissor"\n''')
        # print("\n")

        if user_choice == comp_choice:
            print("It is a Tie")

        else:
            if user_choice == "rock" and comp_choice == "paper":
                print("You Lose. Better Luck Next Time")
                comp_score += 1

            elif user_choice == "paper" and comp_choice == "rock":
                print("Congratulatins! You Win")
                user_score += 1

            elif user_choice == "paper" and comp_choice == "scissor":
                print("You Lose. Better Luck Next Time")
                comp_score += 1

            elif user_choice == "scissor" and comp_choice == "paper":
                print("Congratulatins! You Win")
                user_score += 1

            elif user_choice == "rock" and comp_choice == "scissor":
                print("Congratulatins! You Win")
                user_score += 1

            elif user_choice == "scissor" and comp_choice == "rock":
                print("You Lose. Better Luck Next Time")
                comp_score += 1

        print("Computer : " + comp_choice)
        print("User :" + user_choice)

        print("Computer : ") 
        print(comp_score)
        print("User :") 
        print(user_score)

    
    print("Computer :") 
    print(comp_score)
    print("User :") 
    print(user_score)

    if comp_score == points:
        print("\nYou Lose. Better Luck Next Time\n")
    else:
        print("\nCongratulatins! You Win\n")