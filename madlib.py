'''
Author: <ksh1ng>
Date: <2018.6.26>
Class: ISTA 130
Section Leader: <Johnny Hsu>

Description:
<hw07>
'''

# put all of your import statements below this line and then delete this comment
def print_report(filename):
    '''
    Description:
     i.) Read the given file and print a report giving the following information:
         a.) the total number of vowels in the file (for this assignment ‘y’ is not a
            vowel.)
         b.) the total number of consonants in the file
         c.) the total number of white spaces in the file (spaces, tabs, newlines)
         d.) the total number of punctuation characters in the file (for this assignment
             assume that punctuation is anything that is neither a letter from the
             alphabet nor a white space)
         e.) the total number of characters in the file
         f.) the percent of the file composed of vowels, consonants, white spaces,
             and punctuation characters
         g.) begin and end with a blank line.
    Parameters:
     filename: a single string parameter.

    Return: None
    '''
    f = open(filename, 'r')
    count_vowels = count_consonants = count_white_spaces = count_punctuation = 0
    num_characters = 0

    for line in f:
        for ch in line:
            num_characters += 1

            if ch in 'AEIOUaeiou':
                count_vowels += 1
            elif ch.isalpha()  and  ch not in  'AEIOUaeiou':
                count_consonants += 1
            elif ch.isspace():
                count_white_spaces += 1
            else:
                count_punctuation += 1
    f.close()

    p_vowels = round(count_vowels / num_characters *100, 1)
    p_consonants = round(count_consonants / num_characters *100, 1)
    p_spaces = round(count_white_spaces / num_characters *100, 1)
    p_punctuation = round(count_punctuation / num_characters *100, 1)

    title =  filename.center(25, '-')
    print('\n' + title)

    items_dict1 = {'Vowels:' : count_vowels, 'Consonants:' : count_consonants, 'Whitespace:':count_white_spaces, 'Punctuation:' : count_punctuation}

    items_dict2 = {'Percent vowels:' : p_vowels, 'Percent consonants:' : p_consonants,
                   'Percent spaces:': p_spaces, 'Percent punctuation:' : p_punctuation}

    for (item1, value1) in items_dict1.items():
        print(item1.ljust(20) + str(value1).rjust(5))

    print('-' * len(title))
    print('Total:'.ljust(20) + str(num_characters).rjust(5) + '\n')

    for (item2, value2) in items_dict2.items():
        print(item2.ljust(20) + str(value2).rjust(5))

    print('=' * len(title) + '\n')


def replace_parts_of_speech(replaced, part_of_speech):
    '''
    Description:
     i.) For each occurrence of the given part of speech in the given
         string ask the user for a word of the appropriate types.
     ii.) Replace the part of speech label with the word provided by the user
     iii.) After replacing all parts of speech of the indicated type,
           return the new version of the given string.
         @@For example, calling the function like this:
              -->replace parts of speech("the NOUN VERB PAST the NOUN", "NOUN")
             would ask the user to enter two nouns.
            Assuming the user entered “dog” for the first noun and “duck”
             for the second, the function would return:
                 >>"the dog VERB PAST the duck"

    Parameter:
     changed_str: a string containing part of speech labels that need to be replaced
           by words (e.g. “The ADJECTIVE NOUN in the NOUN VERB PAST.”)
     toreplace_str: a string indicating which part of speech label to replace,
           e.g. “NOUN”.

    Return: a new string such as example above.
    '''
    new_str = replaced

    for i in range(replaced.count(part_of_speech)):
        new = input('Enter ' + part_of_speech.lower() + ': ')
        new_str = new_str.replace(part_of_speech, new, 1)


    return new_str





def complete_mad_lib(file):
    '''
    Description:
     i.) Read the indicated template file line by line and
         • Replace all part of speech labels with words entered
           by the user
             - you’ll need to figure out how to use the function
               you wrote to accomplish this
             - Do it in this order: PLURAL NOUN, VERB PAST, VERB, NOUN,
               ADJECTIVE

     ii.) Write the completed story out to a new file:
          • the new file should have the same name as the original
            file, prepended with the string “MAD_”
        (e.g. if the original file was named “tortoise.txt” the new
         file should be “MAD_tortoise.txt”)

    Parameter:
     file: a string parameter for the name of a Mad Lib template
           file to read.
    Return: None
    '''
    f = open(file, 'r')
    new_f = open('MAD_' + file, 'w')
    label_order = ['PLURAL NOUN', 'VERB PAST', 'VERB', 'NOUN', 'ADJECTIVE']

    for line in f:
        for label in label_order:
                line = replace_parts_of_speech(line, label)

        new_f.write(line)








# put all of your function definitions below this line and then delete this comment


#==========================================================
def main():
    '''
    i.) Ask the user to enter the name of a Mad-Lib template file
        (assume the file is in the same directory as this program)
    ii.) Call your function to print the character report on that file
    ii.) Call your function to have the user complete the Mad Lib story
    '''

    user_file = input('Enter file name: ')

    print_report(user_file)

    complete_mad_lib(user_file)



    # put main code here, make sure each line is indented one level, and delete this comment

    #test functions:
    '''
    print_report('test.txt')

    print(replace_parts_of_speech("the NOUN VERB PAST the NOUN", "VERB"))

    complete_mad_lib('test1.txt')
    '''

    #input('Press enter to end.')  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
