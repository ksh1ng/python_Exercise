'''
Author: <ksh1ng>
Date: <2018.6.5>
Class: ISTA 130
Section Leader: <Johnny Hsu>

Description:
<WS0329>
'''

# put all of your import statements below this line and then delete this comment

# put all of your function definitions below this line and then delete this comment
def line_nums(file):
    '''
    Description:
     It opens the file, reads it and writes a new file with the same
     name but the string '_ln' added to the filename stem.
     For example, if the filename is 'textfile.txt', the stem
     is 'textfile' and new file for writing should be called
     'textfile_ln.txt'.

    Paremeter:
     file: a filename (string) argument. Assume the filename has an
           extension and only one dot.

    Return: None
    '''
    f = open(file, 'r')
    dot_position = file.find('.')
    new_f = open(file[:dot_position] + '_ln' + file[dot_position:], 'w')

    num_line = 0
    for line in f:
        num_line += 1
        new_f.write(repr(num_line) + ': ' + line)

    f.close()
    new_f.close()


def word_search(file, word):
    '''
    Description:
     The function prints "***** <word> *****" and then every line that contains
     the word with its line number added as above.
     Do not literally print <word>, print the value of the argument word.

    Parameter:
     file, word: string arguments

    Return: None
    '''
    f = open(file, 'r')
    print('*****' + word + '*****')
    num_line = 0

    for line in f:
        num_line += 1
        if word in line:

            print(repr(num_line) + ': ' + line.strip())

    f.close()

def add_elements(list1, list2):
    '''
    Description:
     Each element in the new list is the sum of the elements
     at the same position in the arguments.You may assume the
     lists are the same length.
     For example: add_elements([1, 2, 1, 3], [7, 14, 6, 33]) --> [8, 16, 7, 36]

    Parameter:
     list1, list2: list arguments

    Return: a new list.
    '''
    new_list = []

    for i in range(len(list1)):
        new_list.append(list1[i] + list2[i])

    return new_list



#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''

    '''
    line_nums('mystery.txt')

    word_search('mystery.txt', '1')
    '''
    #3 Write code that does the following (Hint: append, insert, pop)
    alist = ["Arizona", "California", "New Mexico"]

    alist.append('Utah')
    print(alist)

    alist.insert(0, 'Oregon')
    print(alist)

    for i in range(len(alist)):
        alist[i] = alist[i].upper()
    print(alist)

    j = 0
    while j < len(alist):
        alist[j] = alist[j].lower()
        j += 1
    print(alist)

    alist.pop()
    print(alist)

    alist.pop(0)
    print(alist)
    '''

    print(add_elements([1, 2, 1, 3], [7, 14, 6, 33]))
    '''
    # put main code here, make sure each line is indented one level, and delete this comment



    #input('Press enter to end.')  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
