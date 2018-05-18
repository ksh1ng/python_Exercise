'''
Author: <ksh1ng>
Date: <2018.5.16>
Class: ISTA 130
Section Leader: <Johnny Hsu>

Description:
<LAB05>
'''

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
                    print("====Money $"+str(money),"====")

                    break

                else:
                    print("Sorry! You did not have enough money~")
                    print("====Money $"+str(money),"====")
                    return money

            elif ride == '2':
                if can_pay(money,4):
                    money -= 4
                    print("OK! You chose ",ride)
                    print("====Money $"+str(money),"====")
                    break

                else:
                    print("Sorry! You did not have enough money~")
                    print("====Money $"+str(money),"====")
                    return money

            elif ride == '3':
                if can_pay(money,5):
                    print("OK! You chose ",ride)
                    money -= 5
                    print("====Money $"+str(money),"====")
                    break

                else:
                    print("Sorry! You did not have enough money~")
                    print("====Money $"+str(money),"====")
                    return money

            elif ride == '4':
                if can_pay(money,6):
                    print("OK! You chose ",ride)
                    money -= 6
                    print("====Money $"+str(money),"====")
                    break

                else:
                    print("Sorry! You did not have enough money~")
                    print("====Money $"+str(money),"====")
                    return money
        play=input("Do you want to continue?(y/n)")
    print("Thank you for coming!")





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




#==========================================================
def main():
    '''
     create a variable called total_money. This variable will store how much
     money the user has while at the park.
    '''
    total_money=20
    total_money=ride_rollercoaster(total_money)
    print(total_money)


    # put main code here, make sure each line is indented one level, and delete this comment
    '''
    ride_rollercoaster(20)
    '''
    #buy_food(10)

    #input('Press enter to end.')  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
