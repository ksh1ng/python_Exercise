'''
Author: <ksh1ng>
Date: <2018.5.14>
Class: ISTA 130
Section Leader: <Johnny Hsu>

Description:
<WS0225>
'''

# put all of your import statements below this line and then delete this comment
def first_longer(str1,str2):
    '''
    There are two string parameters and returns True if the first
    string is longer than the second, False otherwise.
    '''
    if len(str1) > len(str2):
        return True
    else:
        return False

def print_squares(int):
    '''
    It takes an integer argument. If the integer is not positive, print "nonpositive argument".
    Use a for loop to print the squares of all of the numbers between 1 and the argument,
    inclusive. Rewrite using a while loop.
    '''
    if int < 0:
        print("nonpositive argument")
    for i in range(1,int+1):
        print("The square of",i,"is",i**2)

#Rewrite using a while loop:
def print_squares1(int):
    if int < 0:
        print("nonpositive argument")
    i=1
    while i <= int:
        print("The square of",i,"is",i**2)
        i += 1

def oldest(name1, age1, name2, age2, name3, age3):
    '''
    It figures out which person is oldest and
    prints "<name of oldest> is <age of oldest> years old – oldest of them all".
    '''
    if age1 >= age2 and age1 >= age3:
        name_odest=name1
        age_odest=age1
    elif age2 >= age1 and age2 >= age3:
        name_odest=name2
        age_odest=age2
    elif age3 >= age1 and age3 >= age2:
        name_odest=name3
        age_odest=age3
    print(name_odest,"is",age_odest,"years old - oldest of them all")

def price_of_rocks():
    '''
    It has no parameters. In a while loop, get a rock type  and a weight(pound,float) from the user.
    Keep a running total of the price for all requested rocks. Repeat until the user wants to
    quit
    Quartz crystals cost $23 per pound.
    Garnets cost $160 per pound.
    Meteorite costs $15.50 per gram.
    Return the total price of all of the material.
    '''
    total_cost=0
    while True:
        rock_type=input("Enter the rock type(Quartz crystals/Garnets/Meteorite):<q:quit> ")
        if rock_type in 'Qq':
            break
        while rock_type not in 'Qq':
            weight=float(input("Enter the weight of the rock: "))
            if rock_type == 'Quartz crystals':

                total_cost=total_cost+23*weight
            elif rock_type == 'Garnets':

                total_cost=total_cost+160*weight
            elif rock_type == 'Meteorite':

                total_cost=total_cost+15.50*weight*(453.59237)

            else:
                print("Please enter the type in list! ")
            break

    print("Total cost:",total_cost)


# put all of your function definitions below this line and then delete this comment


#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    #Test function:
    '''
    print(first_longer('apple','orange'))

    print_squares1(6)
    '''
    price_of_rocks()



    # put main code here, make sure each line is indented one level, and delete this comment



    #input('Press enter to end.')  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
