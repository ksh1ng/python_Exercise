def alternate_case(str):
    '''
    Return the given string with all vowels uppercase and all consonants lowercase.

    alternate_case("HELLO") --> hEllO
    alternate_case("homework") --> hOmEwOrk
    alternate_case("I like vowels") --> I lIkE vOwEls
    '''
    vowel = 'aeiou'
    str = str.lower()

    for ch in vowel:
         str = str.replace(ch, ch.upper())
    return str



def max_age():
    '''
    Read the age.txt file and print out the largest number.

    Each number in the file is on its own line.
    '''
    f = open('age.txt', 'r')
    alist = []

    for line in f:
        alist.append(int(line.strip()))

    f.close()

    print('The largest number: ' + str(max(alist)))


def print_range(stop_number, output_file_name):
    '''
    Write every number between zero and the stop number to the file.

    stop_number (int) -- The number to stop printing at
    output_file_name (str) -- The file to write to

    The stop number itself should not be written to the file. Each number
    should be written on its own line.
    '''
    f = open(output_file_name, 'w')

    for i in range(stop_number):
        f.write(str(i) + '\n')

    f.close()



def condense_whitespace(input_file_name):
    '''
    Make a copy of the given file that has more compact whitespace.

    input_file_name (str) -- The name of the input file

    A new file should be written to that has the same name as the input
    file except that it starts with FIXED. So if the input file was named
    data.txt, the output file should be called FIXED_data.txt. All tabs
    should be replaced with spaces, and two spaces should never touch each
    other.
    '''
    f = open(input_file_name, 'r')
    n_f = open('FIXED_' + input_file_name, 'w')

    for line in f:
        line = ' '.join(line.split())

        if line == '':     #remove extra newline
            n_f.write(line)
        else:
            n_f.write(line + '\n')

    f.close()
    n_f.close()

#test
'''
condense_whitespace('spaces.txt')
'''
def convert_indentation(input_file_name, output_file_name):
    '''
    Given a file that uses tabs for indentation, write a copy of it that uses
    spaces for indentation.

    input_file_name (str) -- The name of the file that uses tabs
    output_file_name (str) -- The name of the file that should use spaces
    '''
    f = open(input_file_name, 'r')
    o_f = open(output_file_name, 'w')

    for line in f:
        line = line.replace('\t', ' ')
        o_f.write(line)

    f. close()
    o_f.close()

#convert_indentation('indented_code.py', 'FIXED_indented_code.py')


def combine1(list_one, list_two):
    '''
    Given two lists, combine them into one and return the result.

    list_one (list) -- A list
    list_two (list) -- A different list

    The two original lists should not be modified. This function
    should return a new (third) list.
    '''
    return list_one + list_two

#test
'''
a = ['n', 'i']
b = ['c', 'k']
print(combine1(a, b))
print(a, b)
'''

def remove_evens(numbers):
    '''
    Given a list of integers, remove all of the evens.

    numbers (list) -- A list of integers

    This function should modify the list. It should not return anything.
    Hint: Use a while loop. For loops won't work out here.
    '''


    i = 0

    while i < len(numbers):
        if numbers[i] % 2 == 0:
            numbers.pop(i)
            print(len(numbers))

        else:               #we do not increment our loop control
            i += 1          # variable if an item is removed;
                            #because the act of removing an element is akin to
                            # incrementing our LCV dynamically.



#test
'''
a = [1,3,5,7,9,10,12,14,16,18]

remove_evens(a)
print(a)
'''



def insert_user_name(list_of_names):
    '''
    Ask the user for their name, then insert it at the beginning of the list.

    list_of_names (list) -- A list containing names (strings)

    This function should mutate the list. It should not return anything.
    '''
    name = input('Enter your name: ')
    list_of_names.insert(0, name)

#test
'''
name = []
insert_user_name(name)
print(name)
insert_user_name(name)
print(name)
'''

def populate(majors, hobbies, ages, genders):
    '''
    Given 4 lists, populate those lists from the columns of "students.csv"

    majors (list) -- An empty list
    hobbies (list) -- An empty list
    ages (list) -- An empty list
    genders (list) -- An empty list

    The ages list should be populated with ints. Every other list should be
    populated with strings. This function does not return anything.

    Hint: Use split to get each part of a row.
    '''
    f = open('students.csv', 'r')
    title_line = f.readline()  #for skipping the first title line in the file.

    line = f.readline()

    while line:
        line = line.strip().split(',')

        majors.append(line[0])
        hobbies.append(line[1])
        ages.append((line[2]))
        genders.append(line[3])
        line = f.readline()
    f.close()

#test
'''
majors = []
hobbies = []
ages = []
genders = []
populate(majors, hobbies, ages, genders)
print(majors, '\n', hobbies, '\n', ages, '\n', genders)
'''
def main():
    '''
        KEY | FUNCTION TESTED
    --------|---------------------    Assigning the variable 'test' in main to any key in the
        alt | alternate_case          'KEY' column will test the associated function found
    --------|---------------------    in the corresponding 'FUNCTION TESTED' column.
        age | max_age
    --------|---------------------    Assigning the variable 'test_all' to True will test all
      write | print_range             of your functions at once! Make sure this variable is assigned
    --------|---------------------    to False if you are trying to debug one function at a time.
     remove | condense_whitespace
    --------|---------------------
     indent | convert_indentation
    --------|---------------------
    combine | combine1                (No unit tests because this sort of just happened by accident
    --------|---------------------     and I don't want to fix it. Some tests are more exhaustive than others.)
      evens | remove_evens
    --------|---------------------
    prepend | insert_user_name        All mistakes in testing can be blamed on Cameron :(
    --------|---------------------
        csv | populate
    '''

    '''
    test = ""
    test_all = True

    # alternate_case tests
    if test_all or test == "alt":
        print("---TESTING alternate_case---")
        print(alternate_case("HELLO") + " (should be hEllO)")
        print(alternate_case("homework") + " (should be hOmEwOrk)")
        print(alternate_case("I like vowels") + " (should be I lIkE vOwEls)")
        print()
        input("Press enter to end current test.")
        print()

    # max_age tests
    if test_all or test == "age":
        print("---TESTING max_age---")
        print(max_age(), "(should be 79)")
        print()
        input("Press enter to end current test.")
        print()

    # print_range tests
    if test_all or test == "write":
        print("---TESTING print_range---")
        file_n = input("Where would you like to output your file to? (File name): ")
        print("Opening file: '" + file_n + "'...Done!")
        print("Outputing contents (0-6)...(tab included at beginning for readability)")
        print_range(7, file_n)
        file_reader = open(file_n, "r")
        for line in file_reader:
            print("\t" + line[:-1])
        file_reader.close()
        print()
        input("Press enter to end current test.")
        print()

    # condense_whitespace tests
    if test_all or test == "remove":
        print("---TESTING condense_whitespace---")
        print("Opening file: 'spaces.txt'...Done!")
        file_reader = open("spaces.txt", "r")
        for line in file_reader:
            print("BEFORE: " + line)
        file_reader.close()
        condense_whitespace("spaces.txt")
        print("Condensing whitespaces...Done! (Wrote to FIXED_spaces.txt)")
        file_reader = open("FIXED_spaces.txt", "r")
        for line in file_reader:
            print("AFTER: " + line)
        file_reader.close()
        print()
        input("Press enter to end current test.")
        print()

    # convert_indentation tests
    if test_all or test == "indent":
        print("---TESTING convert_indentation---")
        print("Opening file: 'indented_code.py'...Done!")
        convert_indentation("indented_code.py", "FIXED_indented_code.py")
        print("Writing tab-less version of file to FIXED_indented_code.py...Done!")
        print("=> NOTE! In order to keep output nice and tidy, verify this function ")
        print("         worked by checking the file by hand...sorry for the inconvinence :(")
        print()
        input("Press enter to end current test.")
        print()

    # combine1 tests
    if test_all or test == "combine":
        print("---TESTING combine1---")
        print("List1 = ['hi', 1, 'foo', 'bar']\nList2 = ['ika', True, None]")
        list1 = ['hi', 1, 'foo', 'bar']
        list2 = ['ika', True, None]
        list3 = combine1(list1, list2)
        print("List3 =        ", list3)
        print("  => should be: ['hi', 1, 'foo', 'bar', 'ika', True, None]")
        if not list1 == ['hi', 1, 'foo', 'bar']:
            print("Uh-oh! You alterted list1! Don't forget about your .copy() method...")
        print()
        if not list2 == ['ika', True, None]:
            print("Uh-oh! You alterted list2! Don't forget about your .copy() method...")
        print()
        input("Press enter to end current test.")
        print()

    # remove_evens tests
    if test_all or test == "evens":
        print("---TESTING remove_evens---")
        list1 = []
        list2 = [1,2,3,4]
        list3 = [2,4,6]
        list4 = [1,3,5,7]
        remove_evens(list1)
        remove_evens(list2)
        remove_evens(list3)
        remove_evens(list4)
        print("List1 = []")
        print("List1 after function call:", list1, "(should be [])\n")
        print("List2 = [1, 2, 3, 4]")
        print("List2 after function call:", list2, "(should be [1, 3])\n")
        print("List3 = [2, 4, 6]")
        print("List3 after function call:", list3, "(should be [])\n")
        print("List4 = [1, 3, 5, 7]")
        print("List4 after function call:", list4, "(should be [1, 3, 5, 7])\n")
        print()
        input("Press enter to end current test.")
        print()

    # insert_user_name tests
    if test_all or test == "prepend":
        print("---TESTING insert_user_name---")
        list1 = []
        insert_user_name(list1)
        print("List1 = []")
        print("List1 after function call:", list1, "(should only be the name you included)\n")
        list2 = ['Amelia', 'Grant']
        insert_user_name(list2)
        print("List2 = ['Amelia', Grant']")
        print("List2 after function call:", list2, "(should have name you included first)\n")
        input("Press enter to end current test.")
        print()

    # populate tests
    if test_all or test == "csv":
        print("---TESTING populate---")
        l1 = []
        l2 = []
        l3 = []
        l4 = []
        populate(l1, l2, l3, l4)
        print("Checking your lists...")
        if l1 == ['MIS', 'MIS', 'MIS', 'ISTA', 'ECE', 'ECE', 'ECE', 'MIS', 'Math', 'CS', 'Math', 'CS', 'ECE', 'MIS', 'CS', 'ISTA', 'ECE', 'CS', 'CS', 'Math']:
            print("Majors lists passed!")
        else:
            print("Majors list differed :( (Don't forget to remove the whitespace at the beginning and end of your words!)")
        if l2 == ['Sports', 'Sports', 'Studying', 'Video Gaming', 'Video Gaming', 'Sports', 'Studying', 'Sports', 'Sports', 'Sports', 'Video Gaming', 'Sports', 'Sports', 'Video Gaming', 'Video Gaming', 'Studying', 'Sports', 'Studying', 'Video Gaming', 'Sports']:
            print("Hobbies lists passed!")
        else:
            print("Hobbies lists differed :( (Don't forget to remove the whitespace at the beginning and end of your words!)")
        if l3 == [48, 21, 36, 20, 19, 20, 17, 43, 44, 21, 46, 21, 40, 22, 32, 20, 19, 44, 49, 36]:
            print("Ages list passed!")
        else:
            print("Ages lists differed :( (Don't forget to remove the whitespace at the beginning and end of your words!)")
        if l4 == ['Male', 'Female', 'Male', 'Female', 'Other', 'Female', 'Female', 'Male', 'Female', 'Female', 'Female', 'Male', 'Female', 'Other', 'Male', 'Female', 'Male', 'Male', 'Male', 'Female']:
            print("Genders list passed!")
        else:
            print("Genders lists differed :( (Don't forget to remove the whitespace at the beginning and end of your words!)")
    '''

if __name__ == '__main__':
    main()
