'''
Author: <ksh1ng>
Date: <2018.6.5>
Class: ISTA 130
Section Leader: <Johnny Hsu>
Description:
<WS0324>
'''

# put all of your import statements below this line and then delete this comment



# put all of your function definitions below this line and then delete this comment
def last_3(str):
    '''
    Description:
      Takes one string argument and returns a new string
      containing the argument's last 3 characters
    Parameters:
     str: a string argument
    Return:
      a new string containing the argument's last 3 characters.
      If the argument doesn't have 3 characters, return it
    '''

    if len(str) < 3:
        return str
    else:
        return str[-3:]


def alphabetize(str1, str2):
    '''
    Description:
     Takes two string arguments and prints them in
     alphabetical order on one line separated by ' <= '
     (Consider upper and lower case of the same letter as the same)
    Parameters:
     str1, str2: string arguments
    Return: None
    '''
    upper_str1 = str1.upper()
    upper_str2 = str2.upper()

    if upper_str1 <= upper_str2:
        print(str1 + ' <= ' + str2)
    else:
        print(str2 + ' <= ' + str1)

def dashes1(str):
    '''
    Description:
      EX: dashes('dog') returns 'd-o-g'
    Parameters:
     str: string argument
    Return:
      a new string that has the characters of the argument
      separated by dashes.
    '''
    result = ''

    for i in range(len(str)):
        result += str[i] + '-'

    return result[:-1]

def dashes2(str):
    result = ''

    for ch in str:
        result += ch + '-'

    return result[:-1]

def full_name(str):
    '''
    Description:
      Examples:
        full_name("fudd, elmer") -> "Elmer Fudd"
        full_name("DUCK, donald") -> "Donald Duck"
    Parameters:
     str:  string argument has format "last, first"
           (letters may be upper or lowercase)
    Return:  the string "First Last"
    '''
    comma_position = str.find(',')

    result = str[comma_position+2:].capitalize() + ' ' + str[:comma_position].capitalize()
    return result

def verify_float(str):
    '''
    Description:
     Takes a string and returns True if the string can
     safely be passed to the float typecasting function,
     False otherwise
    Parameters:
     str: a string.
    Return: bool
    '''
    position_decimal_point = str.find('.')

    while position_decimal_point != -1:

        if len(str) <= 1:
            return False

        if str[0] == '-':
            str = str[1:]
            position_decimal_point = str.find('.')

        if str[:position_decimal_point].isdigit() and str[position_decimal_point+1:].isdigit():
            return True

        return False

    return False


print(verify_float('nick.6'))





#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''

    # put main code here, make sure each line is indented one level, and delete this comment



    #input('Press enter to end.')  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
