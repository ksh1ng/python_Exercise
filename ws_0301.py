'''
Author: <ksh1ng>
Date: <2018.5.15>
Class: ISTA 130
Section Leader: <Johnny Hsu>

Description:
<WS0301>
'''
import random
# put all of your import statements below this line and then delete this comment
def build_string():
    '''
    Get strings from the user until the user enters the empty string.
    Return a string that consists of all of the strings concatenated together.
    Hint: build the string using concatenation just like you would accumulate a sum
    '''
    str=input("Enter the 'string' or 'empty string' for exit): ")
    sum=''
    while str != '':
        sum += str
        str=input("Enter the 'string' or 'empty string' for exit): ")
    return sum
def num_sevens(n):
    '''
     Only one integer argument. It returns the number of
     integers between '0' and the argument, inclusive, that are divisible by 7.
    '''

    count=0
    for i in range(n+1):
        if i%7 == 0:

            count += 1
    return count

def is_even(n):
    if n != 0:
        if n%2 == 0:
            return True
    return False

def is_odd(n):
    if n != 0:

        if n%2 != 0:
            return True
    return False

def is_same(n1,n2):
    if n1 == n2:
        return True
    return False

def roulette(maxium_allowed):
    '''
    It takes one integer argument, the maximum allowed bet.
    It allows the user to spin the wheel until he/she decides to quit.
    It returns the user's net profit/loss. The user may bet on a single number
    or on odd or on even.
    In a loop get an amount(int) the user wants to bet.
    In the prompt, include the maximum allowed bet. Get the bet – '00', '0',
    '1',… '36', 'odd', 'even'. Get a random number between 0 and 37 (37 for '00')
    using random.randint. Print the result. If the user bet on a number and wins, increase
    his/her total by 35 * the amount bet. If not, decrease by the amount bet.
    In the case of odd/even,0 and 00 always count as a loss.
    If the user bet on odd/even and wins, increase his/her total by the amount bet.
    If not, decrease by the amount bet. Print the user's total so far
    '''
    total=0
    play='y'
    while play in 'Yy':
        random_number=random.randint(0,37)
        amount=int(input("Enter the amount you want to bet(maximum allowed bet:{}): ".format(maxium_allowed)))
        bet_number=input("Enter the number you bet between 0 and 37 (37 for '00')or'even','odd': ")
        if bet_number == '00':
            bet_number='37'

        if random_number == 37:
            print("The ball lands on 00!")
        else:
            print("The ball lands on:",str(random_number)+"!")

        if bet_number in 'odd,even':
            if random_number == 0 or random_number == 37:
                print("You lose~")
                total -= amount
            elif bet_number == 'odd' and is_odd(random_number):
                print("You win!")
                total += amount
            elif bet_number == 'even' and is_even(random_number):
                print("You win!")
                total += amount

            else:
                print("You lose~")
                total -= amount

        elif int(bet_number) in range(0,38):
            if is_same(bet_number,random_number):
                print("You win! ")
                total += 35*amount
            else:
                print("You lose~ ")
                total -= amount
        print("Your net profit(+)/loss(-) so far:",total)
        play=input("Do you want to continue?(y/n): ")

    return total








# put all of your function definitions below this line and then delete this comment


#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    '''
    print(build_string())
    '''


    #print(num_sevens(30))
    print("Your net profit(+)/loss(-):",roulette(20))



    # put main code here, make sure each line is indented one level, and delete this comment



    #input('Press enter to end.')  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
