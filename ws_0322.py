'''
Author: <ksh1ng>
Date: <2018.6.2>
Class: ISTA 130
Section Leader: <Johnny Hsu>

Description:
<WS0322>
'''

# put all of your import statements below this line and then delete this comment
def last_3(str):
    '''
    Description:
     Takes one string argument and returns a new string
     containing the argument's last 3 characters.

    Parameters:
     str: one string argument

    Return:
      A new string containing the argument's last 3 characters
      If the argument doesn't have 3 characters, return it
    '''
    if len(str) > 3:
        return str[-3:]

    return str


def alphabetize(str1, str2):
    '''
    Description:
     Takes two string arguments and prints them in
     alphabetical order on one line separated by ' <= '.

    Parameters:
     str1, str2: string arguments

    Return: None
    '''
    if str1.upper() <= str2.upper():
        print(str1 + " <= " + str2)
    else:
        print(str2 + " <= " + str1)

def dashes(str):
    '''
    Description:
     Takes one string argument and returns a new string
     that has the characters of the argument separated by dashes.
      @@EX: dashes('dog') returns 'd-o-g'.

    Parameters:
     str: string argument

    Return:
      A new string that has the characters of the argument
      separated by dashes
    '''
    new_str = ''
    i = 0

    while i < len(str)-1:
        new_str += str[i] + '-'
        i += 1

    return new_str + str[-1]
# put all of your function definitions below this line and then delete this comment


#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    word = "this is string example....wow!!! this is really string"
    print(word[1:-1])

    print(word.upper())

    print(word[:2] + word[-2:])

    print(word[:2]*3 + word[2:])



    # put main code here, make sure each line is indented one level, and delete this comment



    #input('Press enter to end.')  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
