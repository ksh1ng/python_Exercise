'''
Author: <ksh1ng>
Date: <2018.5.8>
Class: ISTA 130
Section Leader: <Johnny Hsu>

Description:
<WS>
'''
import random
# put all of your import statements below this line and then delete this comment

def  add_nums():
    '''
    gets numbers(float/int) from the user until the user decides to quit
    and keeps a running total of them. When the user quits, return the total. Use this prompt
    "Enter a number or 'q' to quit".
    '''
    total=0

    user=input("Enter a number or 'q' to quit")

    while user != 'q':
        total += float(user)
        user=input("Enter a number or 'q' to quit: ")

    return total

def randoms():
    '''
     prints random numbers until the user decides to quit.
     First, get the maximum that the numbers can be from the user. Then enter a loop in which you
     print a random number between 0 and the user-specified maximum, including 0 and the max, and
     then ask if the user wants another.
    '''
    max=input("Enter a number you want ,it will print a random number from 0 to the number you choose:(or 'q' to quit):")
    print(random.randint(0,int(max)))
    while  max != 'q':
        prompt_1=input("Do you want another random number from 0 to {}?(y/n): ".format(max))
        if prompt_1 == 'y':
            print(random.randrange(0,int(max)))
        elif prompt_1 == 'n':
            prompt_2=input("Do you want to enter a number again?(y/n): ")

            if prompt_2 == 'y':
                max=input("Enter a number you want ,it will print a random number from 0 to the number you choose:(or 'q' to quit)")
            elif prompt_2 == 'n':
                print("OK,BYE~")
                max='q'
        else:
            max='q'




# put all of your function definitions below this line and then delete this comment


#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''



    #Rewrite the following code replacing for loops with equivalent while loops:
    '''
    i=0
    while i < 7:
        print("i**2:", i * i)
        i += 1


    i=0
    while i < len(string):
        print('*' * i, string, '*' * i)
        i += 1




    total=0
    i=0
    while i <= 19:
        total += 3 * (i + 1) + 4
        i += 1

    print(str(i-1) + ':', total)
    '''



    #test function:
    '''
    print(add_nums())
    '''

    randoms()

    # put main code here, make sure each line is indented one level, and delete this comment



    #input('Press enter to end.')  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
