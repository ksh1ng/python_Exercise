'''
Author: <ksh1ng>
Date: <2018.5.27>
Class: ISTA 130
Section Leader: <Johnny Hsu>

Description:
<WS0303>
'''

# put all of your import statements below this line and then delete this comment
def first_and_last(str):
    '''
    Description:
     Take s str and return a new string containing g the first and
     last characters in the argument.

    Parameters:
     str:just a old string

    Return:
     a new string containing the first and last characters
     in the argument. If the argument is the empty string
     return None.
    '''

    if str != '':
        new_str = str[0]+str[-1]
        return new_str
    return None


def thirds(str):
    '''
    Description:
     takes one string argument and
     returns a new string containing the third, sixth,
     ninth, etc. characters in the argument.

    Parameters:
     str: a string argument

    Return:
     a new string containing the third, sixth, ninth, etc.
     characters in the argument. If there aren't at least three
     characters, return None
    '''
    if len(str) >= 3:
        i = 2
        new_str = ''

        while i < len(str):
            new_str += str[i]
            i += 3
        return new_str

    return None

def count(str,char):
    '''
    Description:
     Count the number of times a character appears in the
     string

    Parameters:
     str: a nonempty string
     char: a single character

    Return:
     the number of times the character appears in the
     string
    '''
    num_char = 0

    if str != '':

        for i in range(len(str)):

            if str[i] == char:
                num_char += 1
        return num_char

def  smallest(str):
    '''
    Description:
     Find the smallest character in a string.
     Assume the first character in the string is not
     a space, tab, or newline.

    Parameters:
     str: a nonempty string argument

    Return:
     the smallest character that is not a space, tab, or newline.
    '''
    if str != '':
        smallest_str = str[0]

        for i in range(len(str)):

            if str[i] < smallest_str:

                if str[i] in ' \t\n':
                    continue
                else:
                    smallest_str = str[i]

        return smallest_str



# put all of your function definitions below this line and then delete this comment


#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    #print(first_and_last(''))
    #print(thirds(""))
    #print(count('abkbacskb','k'))
    # put main code here, make sure each line is indented one level, and delete this comment
    print(smallest('cnlABCUISHsanckn'))


    #input('Press enter to end.')  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
