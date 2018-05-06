'''
Author: <ksh1ng>
Date: <2018.4.24>
Class: ISTA 130
Section Leader: <Johnny Hsu>

Description:
<hw01-(2)>
'''
import random
# put all of your import statements below this line and then delete this comment
def  is_alive(life_force):
    '''takes one integer argument, representing the life force of
       a character in a videogame. If the life force is 0 or less, return False.
    '''
    if life_force<=0:
        return False

    return True

def class_standing(num_units):
    '''
    takes one integer argument representing the number of units a student has completed.
    If the number of units is less than 30, return the string "Freshman"; at least 30
    and less than 60 return "Sophomore"; at least 60 and less than 90 return "Junior";
    otherwise, return "Senior".
    '''

    if num_units < 30:
        return "Freshman"

    elif num_units < 60:
        return "Sophomore"

    elif num_units < 90:
        return "Junior"

    else:
         return "Senior"


def soup(str):
    '''
     takes one string argument. If the argument is "Too hot" or
     "Too cold", return the string "Not this bowl". If it is "Just right!", return "I
     will eat this bear's soup!". Otherwise, return "Need better info"

    '''
    if str == "Too hot" or "Too cold":
        return "Not this bowl"

    elif str == "Just right!":
        return "I will eat this bear's soup!"

    else:
        return "Need better info"

def jailbreak():
    '''
     takes no arguments. Code a for loop that will
     execute 100 times. Inside it, use random.randint(1, 6) to get a random number between
     1 and 6 inclusive (simulating the roll of a die). Ask the user to give you a number between 1 and
     6. If the two numbers are the same, print the message "You escaped in _ rolls" and
     return. If not, keep playing.
    '''
    for i in range(100):
        user_number=int(input("Enter a number between 1 and 6: "))
        sim_number=random.randint(1, 6)
        if user_number == sim_number:
            print("You escaped in",i + 1,"rolls")
            return






# put all of your function definitions below this line and then delete this comment


#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''

    # put main code here, make sure each line is indented one level, and delete this comment
    jailbreak()


    #input('Press enter to end.')  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
