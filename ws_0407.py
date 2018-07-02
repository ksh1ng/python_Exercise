'''
Author: <ksh1ng>
Date: <2018.7.2>
Class: ISTA 130
Section Leader: <Johnny Hsu>

Description:
<WS0407>
'''

# put all of your import statements below this line and then delete this comment
import string

# put all of your function definitions below this line and then delete this comment
def pet_dict():
    '''
    Description:
     This function contains a loop, which will build a dictionary.
     Pet types, such as 'dog' or 'cat', will be the keys. Values will
     be lists of pet names.
    Parameter:
     None.
    Return: a dict.
    '''
    pets = {}

    while True:
        user_enter = input("Enter pet type and pet name separated by a space or 'q' to quit: ")

        if user_enter in 'Qq':
            return pets
        else:
            type = user_enter.split()[0]
            name = user_enter.split()[1]

        if type not in pets:
            pets[type] = []
        pets[type].append(name)


def pop_empty(dict):
    '''
    Description:
     It traverses the dictionary, popping (removing) any key-value pair
     where the value is the empty list.
    Parameter:
     dict: a dictionary argument.
    Return:
     a dict after processing.
    '''
    #collect the keys where the value is the empty list.
    alist = []
    for key in dict:
        value = dict[key]

        if value == []:
            alist.append(key)

    #remove value of empty list:
    for item in alist:
        dict.pop(item)

    return dict


def get_keys(dict, value):
    '''
    Description:
     It returns a list of every key that maps to the given value.
    Parameter:
     dict: a dictionary.
     value: a argument of any type.
    Return:
     list
    '''
    alist = []

    for key in dict:
        if dict[key] == value:
            alist.append(key)

    return alist


#apply 'get_keys' finction to generate the 'pop_empty1' function
def pop_empty1(dict):
    key_list = get_keys(dict, [])

    for goal_key in key_list:
        dict.pop(goal_key)

    return dict
#print(pop_empty1({'1': [], '2': 'a', '3': []}))


def word_count(file):
    '''
    Description:
     Return a dictionary that maps each word in the dictionary to the number of
     times it occurs. Make all words lowercase as you extract them from the file.
     If the last character in the word is not a letter, get rid of it.

    Parameter:
     file: a filename(str).
    Return:
     a dict
    '''

    f = open(file, 'r')
    count = {}
    for line in f:
        #remove punctuation in every line.
        for punctuation in string.punctuation:
            line = line.replace(punctuation, ' ')

        for word in line.split():
            #fix the situation that the last character in the word is not a letter
            if not word[-1].isalpha():
                word = word[:-1].lower()

            if word.isalpha():
                if word in count:
                    count[word] += 1
                else:
                    count[word] = 1

    f.close()
    return count




#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''

    # put main code here, make sure each line is indented one level, and delete this comment
    print(word_count1('nick.txt'))


    #input('Press enter to end.')  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
