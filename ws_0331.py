'''
Author: <ksh1ng>
Date: <2018.6.26>
Class: ISTA 130
Section Leader: <Johnny Hsu>

Description:
<WS0331>
'''

# put all of your import statements below this line and then delete this comment

# put all of your function definitions below this line and then delete this comment

# 1.traverse by element:
def just_letters1(str):
    '''
    Description:
     traverses that string argument building a new string that
     contains only the letters in the string.

    Parameter:
     str: a string argument
    Return: the new string　
    '''
    new_str = ''

    for ch in str:
        if ch.isalpha():
            new_str += ch

    return new_str

# 2.traverse by index:
def just_letters2(str):
    new_str = ''

    for i in range(len(str)):
        if str[i].isalpha():
            new_str += str[i]

    return new_str

# 3.with a while loop:
def just_letters3(str):
    new_str = ''
    i = 0

    while i < len(str):
        if str[i].isalpha():
            new_str += str[i]
        i += 1

    return new_str

def word_lengths(str):
    '''
    Description:
     For example:
        word_lengths('I heart Rocket.') -> [1, 5, 7]

    Parameter:
     str: a string argument
    Return: a list containing the length of each word
            (including punctuation).
    '''
    result = []
    str_list = str.split()

    for i in range(len(str_list)):
        result.append(len(str_list[i]))

    return result

def third(list):
    '''
    Description:
     It takes one list argument and replaces every third
     element with the number 3.
     For example:
        third(['you', 77, True, 0.5, 'me', 'hmm']) ->
                ['you', 77, 3, 0.5, 'me', 3]

    Parameter:
     list: one list argument
    Return: None
    '''
    for i in range(len(list)):
        if i % 3 == 2:
            list[i] = 3



def separator(str1, str2):
    '''
    Description:
     (Assume no leading or trailing whitespace!!)
     E.g.:
        third('I heart Rocket', '---') -> 'I---heart---Rocket'
    Parameter:
     str1: string argument.
     str2: has the whitespace between words in the str1 replaced by
           this string argument.
    Return: a new string.
    '''
    str_list = str1.split()

    return str2.join(str_list)

def r_words(filename):
    '''
    Description:
     takes a filename argument and returns a list of all of the words
     that start with 'r' or 'R' in the file. Include duplicates
     and punctuation.
    Parameter:
     filename: a string argument.
    Return: a list.
    '''
    f = open(filename, 'r')
    result_list = []

    for line in f:
        line = line.split()

        for word in line:
            if word[0] in 'Rr':
                result_list.append(word)
    f.close()
    return result_list



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
