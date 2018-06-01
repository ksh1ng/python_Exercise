'''
Author: <ksh1ng>
Date: <2018.6.1>
Class: ISTA 130
Section Leader: <Johnny Hsu>

Description:
<LAB06>
'''
import random
# put all of your import statements below this line and then delete this comment

# put all of your function definitions below this line and then delete this comment

def can_pay(money,total_cost):
    '''
    1.This function takes two parameters,
      how much money the user has and the total_cost of a ride or activity.
    2.If there is enough money to pay for the activity, return the boolean True, otherwise
      return False.
    '''
    if money >= total_cost:
        return True
    return False

def ride_rollercoaster(money):
    '''
    1.This function takes one parameter, how much money the user has.
    2.It asks which ride the user would like to ride and if they have enough money, prints
      out a ride message and returns his money minus the total_cost of the ride.

    @@Price for ride:Brunch Buster->$3
                     Ghastly Gasper->$4
                     Mega Monsoon->$5
                     Super Slider->$6
    3.If the user enters an incorrect name, print out a warning and ask again.
    4.If there isn’t enough money, print a warning message and return money.
    '''
    play='y'
    while play in 'Yy':
        print("which ride would you like to ride?\n-(1)Brunch Buster$3")
        print("-(2)Ghastly Gasper$4\n-(3)Mega Monsoon$5\n-(4)Super Slider$6")
        ride=input("Enter your choice:　")
        if ride not in '1234':
            print("Error! Please enter the item on the list~")


        while ride in '1234':
            if ride == '1':
                if can_pay(money,3):
                    print("OK! You chose ",ride)
                    money -= 3
                    #print("====Money $"+str(money),"====")

                    break

                else:
                    print("Sorry! You did not have enough money~")
                    #print("====Money $"+str(money),"====")
                    return money

            elif ride == '2':
                if can_pay(money,4):
                    money -= 4
                    print("OK! You chose ",ride)
                    #print("====Money $"+str(money),"====")
                    break

                else:
                    print("Sorry! You did not have enough money~")
                    #print("====Money $"+str(money),"====")
                    return money

            elif ride == '3':
                if can_pay(money,5):
                    print("OK! You chose ",ride)
                    money -= 5
                    #print("====Money $"+str(money),"====")
                    break

                else:
                    print("Sorry! You did not have enough money~")
                    #print("====Money $"+str(money),"====")
                    return money

            elif ride == '4':
                if can_pay(money,6):
                    print("OK! You chose ",ride)
                    money -= 6
                    #print("====Money $"+str(money),"====")
                    break

                else:
                    print("Sorry! You did not have enough money~")
                    #print("====Money $"+str(money),"====")
                    return money

        play=input("Do you want to play other?(y/n)")
    print("Thank you for coming!")
    return money





def buy_food(money):
    '''
    1.This function takes one parameter, how much money the user has.
      It asks a user for a item from the menu and how many they would like. Keep taking
      the order until the user decides to stop
    2.Calculate the total_cost of order and check to see if they have enough money.
    3.If they do, return the money minus the total_cost, otherwise print out a warning message
      and return the money.

      Price for food:hamburger->$4
                     hotdog   ->$3

    '''
    num_hamburger=0
    num_hotdog=0
    total_cost=0
    while True:
        print("------------------")
        print("What would you like??")
        print("Current order: Hamburger:",num_hamburger,"Hotdog:",num_hotdog)
        print("total_cost:",total_cost)
        print("-hamburger $4\n-hotdog $3\n-that's all")
        choice=input("Enter your choice: ")

        if choice == 'hamburger':
            order_num=int(input("How many would you like? "))
            hamburger_cost=order_num*4
            total_cost += hamburger_cost
            if can_pay(money,hamburger_cost):
                num_hamburger += order_num
                money -= hamburger_cost
                print("rest of money:",money)
            else:
                print("Sorry! You don't have enough money")
                return money



        elif choice == 'hotdog':
            order_num=int(input("How many would you like? "))

            hotdog_cost = order_num*3
            total_cost += hotdog_cost

            if can_pay(money,hotdog_cost):
                num_hotdog += order_num
                money -= hotdog_cost
                print("rest of money:",money)
            else:
                print("Sorry! You don't have enough money")
                return money
        elif choice == "that's all":
            print("Enjoy!")

            print("====Money $"+str(money),"====")
            return money
        else:
            print("Sorry, that's not on the menu")
            print("----------------")

def guessing_game(money):
    '''
    Description:
     1.It costs 2 dollars to play the game.
       Check if the user has enough money to play
     2.It generates a random number between 0 and 100
       and lets the user take a guess.
     3.If the number is correct exit the while loop
       and print a victory message.
     4.While the guess is not correct print out whether
       the number is higher or lower than the random number
       and ask the user to enter another guess.

    Parameters:
     money:  how much money a person has.

    Return:
     If it is under 5 tries return their money plus 20 dollars
     for winning otherwise return their money minus 2.

    '''
    if not can_pay(money,2):
        print("Sorry! You don't have enough money")


    random_number = random.randint(0,100)
    times_guess = 1

    user_guess = int(input("Please guess a number between 0 and 100! "))
    while can_pay(money,2):

        if user_guess == random_number:
            print("That's it!")
            break
        elif user_guess > random_number:
            print("Too High!")
            times_guess += 1
        else:
            print("Too Low!")
            times_guess += 1

        print()
        user_guess = int(input("Please guess another number between 0 and 100 again! "))
    if times_guess < 5:
        print("You guessed correctly in under 5 tries! You win 5 dollars!")
        return money + 5
    else:
        print("You guessed correctly in more than 5 tries! You lose 2 dollars!")
        return money - 2








#==========================================================
def main():
    '''
     create a variable called total_money. This variable will store how much
     money the user has while at the park.
    '''
    total_money=20


    while True:
        print("\n~~~~Money $" + str(total_money), "~~~~\n")
        user_action = input("What would you like to do?\n" +
                            "\t-buy food\n" +
                            "\t-ride coaster\n" +
                            "\t-guessing game\n"
                            "\t-leave\n")
        if not (user_action == 'buy food' or user_action == 'ride coaster' or user_action == 'guessing game' or user_action == 'leave'):
            print("You can't do that here!")
            continue

        if user_action == 'buy food':
            total_money = buy_food(total_money)

        if user_action == 'ride coaster':
            total_money = ride_rollercoaster(total_money)

        if user_action == 'guessing game':
            total_money = guessing_game(total_money)

        if user_action == 'leave':
            print()
            print("Tks for your coming~")
            break



    print("You left with $"+str(total_money),"!")





    # put main code here, make sure each line is indented one level, and delete this comment
    '''
    ride_rollercoaster(20)
    '''
    #buy_food(10)

    #input('Press enter to end.')  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
