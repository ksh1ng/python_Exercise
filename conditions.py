'''
Author: <ksh1ng>
Date: <2018.5.13>
Class: ISTA 130
Section Leader: <Johnny Hsu>

Description:
<hw04->
'''

# put all of your import statements below this line and then delete this comment
def word_length(str,int):
    '''
    Two parameters. The first will be a string and the second will be an integer. The
    function first prints a message about the relationship between the length of the word and the
    integer, as shown in the following examples.

        word_length('liversnaps', 7)
        Longer than 7 characters: liversnaps

        word_length('earwax', 5)
        Longer than 5 characters: earwax

        word_length('chickenfat', 10)
        Exactly 10 characters: chickenfat

        word_length('Gross!', 13)
        Shorter than 13 characters: Gross!

    '''
    if len(str) > int:
        print("Longer than",int,"characters:",str)

    elif len(str) < int:
        print("Shorter than",int,"characters:",str)

    else:
        print("Exactly",int,"characters:",str)


def  stop_light(current_color,duration):
    '''
    determines whether a stop light should change color,and, if so, what color it should change to.
    It takes two arguments. The value of the first will be either "green", "yellow", or "red".
    This represents the stop light's current color. The second parameter tells the function how long
    this color has been showing.

    1.If green has been showing longer than 60 seconds, return "yellow".
    2.If yellow has been showing longer than 5 seconds, return “red”.
    3.If red has been showing longer than 55 seconds, return “green”.
    If the color hasn’t been showing long enough (e.g. green has
    been showing for 17 seconds), return the current color.

            EX:
                stop_light('green', 61) --> 'yellow'
                stop_light('yellow', 5) --> 'yellow'
                stop_light('yellow', 6) --> 'red'
                stop_light('red', 12) --> 'red'
                stop_light('red', 56) --> 'green'
    '''
    if current_color == 'green':
        if duration > 60:
            return 'yellow'
        return current_color        #else contain will return current_color
    elif current_color == 'yellow':
        if duration > 5:
            return 'red'
        return current_color
    else:
        if duration > 55:
            return 'green'
        return current_color

def is_normal_blood_pressure(systolic_blood_pressure, diastolic_blood_pressure):
    '''
    Two integer parameters.
    The first represents systolic blood pressure (the top number in a blood pressure reading). The
    second represents diastolic blood pressure (the bottom number in a blood pressure reading).
    The function should return True if systolic is less than 120 and diastolic is less than 80 (i.e.
    blood pressure is normal). Otherwise it returns False.

        EX:
            is_normal_blood_pressure(120, 80) --> False
            is_normal_blood_pressure(119, 80) --> False
            is_normal_blood_pressure(119, 79) --> True
            is_normal_blood_pressure(120, 79) --> False
    '''
    if systolic_blood_pressure < 120 and diastolic_blood_pressure < 80:
        return True
    return False

def doctor():
    '''
    The function will ask the user to enter his/her systolic blood pressure reading(int).
    It will then ask for the diastolic reading(int). The function then prints either
    “Your blood pressure is normal.” or “Your blood pressure is high.” depending
    on the values entered. This function should use the function you wrote in the previous
    question
    '''
    user_systolic_blood_pressure=int(input("systolic blood pressure: "))
    user_diastolic_blood_pressure=int(input("Enter your diastolic reading: "))
    if is_normal_blood_pressure(user_systolic_blood_pressure,user_diastolic_blood_pressure):
        print("Your blood pressure is normal.")
    else:
        print("Your blood pressure is high.")


def pants_size(user_waist_inches):
    '''
    Only a single parameter (the value will be an integer)
    representing a person’s waist size in inches. The function returns a string.
    The string returned will be either "small", "medium", or "large" depending
    on the parameter value.
        @@Regulations:
                    1.Waist measurements that are 34 inches or larger should return large.
                    2.Measurements that are 30 inches or larger, but not large enough to be in the large category,
                      should return medium.
                    3.Anything smaller should return small.
    --------------------------------------------------------------------------------------------
                    EX:
                    pants_size(38) --> 'large'
                    pants_size(34) --> 'large'
                    pants_size(33) --> 'medium'
                    pants_size(29) --> 'small'
                    pants_size(-20) --> 'small'
                    pants_size(2000) --> 'large'

    '''
    if user_waist_inches >= 34:
        return 'large'
    elif user_waist_inches >= 30:
        return 'medium'
    else:
        return 'small'

def pants_fitter():
    '''
     No arguments. The function should first ask the user for his/her name.
     It then greets the user by name. Next it asks the user for his/her
     waist size in inches (a positive integer). It then asks the user how many pairs of pants he/she
     would like to buy (a positive integer). Next it asks what type of pants the user wants to buy
     (either “regular” or “fancy”). Next it calculates the cost of the pants (integer). Regular pants
     cost $40 per pair. Fancy pants cost $100 per pair. Finally it prints out the number of pairs, the
     size, the type, and the total cost. The following examples show the format that your prompts
     and output should be in. This function should use the function you wrote in the previous
     question.
    '''
    user_name=input("Enter your name: ")
    print("Greetings",user_name,"welcome to Pants-R-Us")
    waist_size=int(input("Enter your waist size in inches: "))
    num_pairs=int(input("How many pairs of pants would you like: "))
    #pants_type=input("Would you like regular or fancy pants? ")
    cost=0
    is_legitimate_type=True

    while is_legitimate_type:
        pants_type=input("Would you like regular or fancy pants? ")
        if pants_type == 'regular':
            cost=num_pairs*40
            break
        elif pants_type == 'fancy':
            cost=num_pairs*100
            break
        else:
            print("Please try again!")

    print(num_pairs,"pairs of",pants_size(waist_size),pants_type,"pants: $",cost)

def digdug(int_num):
    '''
     Takes a single argument number (assume it will always be a positive integer).
     For every integer from 1 up to and including number, the function will print a
     message if warranted.
     If the integer is evenly divisible by 3 the function will print "dig".
     If the integer is evenly divisible by 5 it prints "dug".
     If the integer is evenly divisible by both 3 and 5 , it prints "digdug".
     If the integer is not divisible by either 3 or 5 it does not print anything.
    '''
    i=1
    while i < int_num:
        i += 1
        if i%15 == 0:
            print(i,": digdug")
        elif i%3 == 0:
            print(i,": dig")
        elif i%5 == 0:
            print(i,": dug")

def  beef_type(percent_lean):
    '''
    Takes a single parameter, percent_lean(float).
    1.If the value of percent_lean is less than 78%, return "Hamburger".
    2.If it is at least 78% and less than 85%, then return "Chuck".
    3.At least 85% but less than 90% return "Round".
    4.90-95% inclusive return "Sirloin".
    5.If percent_lean doesn’t fall within one of these ranges,return "Unknown".
    '''
    if percent_lean < 78:
        return "Hamburger"
    elif percent_lean < 85:
        return "Chuck"
    elif percent_lean < 90:
        return "Round"
    elif percent_lean <= 95:
        return "Sirloin"
    else:
        return "Unknown"

def species_height(species,height):
    '''
     Takes 2 arguments:
     The first is either "Human" or "Klingon".
     The second is a positive float representing the height (in inches) of
     this human or Klingon. In this homework assignment, the average human height is 67 inches.
     The average Klingon height is 71 inches. For the parameters given, print out if it is above, below
     or at the average height for its species.

        EX:
            species_height("Human", 62.1)
            Below Average

            species_height("Klingon", 73)
            Above Average

            species_height("Klingon ", 71)
            Average
    '''
    if species in ' Human  ':
        if height == 67:
            print("Average")
        elif height > 67:
            print("Above Average")
        else:
            print("Below Average")
    elif species in ' Klingon  ':
        if height == 71:
            print("Average")
        elif height > 71:
            print("Above Average")
        else:
            print("Below Average")

def sooner_date(month,day,month1,day1):
    '''
    There are 4 integer parameters:
        The first is a number between 1 and 12 (inclusive) that represents a month. 1 is January, 2 is February, etc.
        The second is a number between 1 and 31 (inclusive) that represents a day.
        The third parameter is another integer representing a month.
        The fourth is another integer parameter representing a day.
        So essentially you have 2 dates (the first 2 parameters and the second 2 parameters).
        Figure out which date would come sooner, then print out that date in the format month / day.

        EX:
            sooner_date(1, 1, 1, 2)
            >>1 / 1
            sooner_date(2, 5, 1, 3)
            >>1 / 3
            sooner_date(8, 25, 7, 30)
            >>7 / 30
    '''
    if month > month1:
        print(month1,"/",day1)
    elif month < month1:
        print(month,"/",day)
    else:
        if day > day1:
            print(month1,"/",day1)
        else:
            print(month,"/",day)

# put all of your function definitions below this line and then delete this comment



#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    '''
    word_length('liversnaps', 7)
    word_length('earwax', 5)
    word_length('chickenfat', 10)
    word_length('Gross!', 13)
    '''
    '''
    print(stop_light('green', 61))
    print(stop_light('yellow', 5))
    print(stop_light('yellow', 6))
    print(stop_light('red', 12))
    print(stop_light('red', 56))
    '''

    '''
    print(is_normal_blood_pressure(120, 80))
    print(is_normal_blood_pressure(119, 80))
    print(is_normal_blood_pressure(119, 79))
    print(is_normal_blood_pressure(120, 79))
    '''
    '''
    doctor()
    '''
    '''
    print(pants_size(38))
    print(pants_size(34))
    print(pants_size(33))
    print(pants_size(29))
    print(pants_size(-20))
    print(pants_size(2000))
    '''
    '''
    pants_fitter()
    '''
    '''
    digdug(15)
    '''
    '''
    print(beef_type(91.2))
    print(beef_type(78))
    print(beef_type(87))
    print(beef_type(95.1))
    '''
    '''
    species_height("Human", 62.1)
    species_height("Klingon", 73)
    species_height("Klingon ", 71)
    '''

    sooner_date(1, 1, 1, 2)
    sooner_date(2, 5, 1, 3)
    sooner_date(8, 25, 7, 30)
    # put main code here, make sure each line is indented one level, and delete this comment



    #input('Press enter to end.')  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
