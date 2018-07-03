'''
Lab 8 Exercises
ISTA 130
07/03/18
'''

def is_second_char_upper(some_string):
    '''
    Return True if the second character of the given string is in upper case.

    some_string (str) -- A string containing at least two characters.

    Examples:
    is_second_char_upper("Nope") --> False
    is_second_char_upper("yUp") --> True
    is_second_char_upper("aLtErNaTiNg") --> True
    '''
    return some_string[1].isupper()




def last_3_characters(some_string):
    '''
    Return the last 3 characters of the given string.

    some_string (str) -- Any string

    If the passed string has less than 3 characters, return what's there.

    Examples:
    last_3_characters("Hello") --> "llo"
    last_3_characters("computer") --> "ter"
    last_3_characters("a") --> "a"
    '''
    return some_string[-3:]



def last_upper(some_string):
    '''
    Return the string in all lowercase except the last character is uppercase.

    some_string (str) -- A string containing at least one character

    last_upper("Hello") --> "hellO"
    last_upper("AAA") --> "aaA"
    last_upper("two words") --> "two wordS"
    '''
    return some_string[:-1].lower() + some_string[-1].upper()

def the_location(some_string):
    '''
    Return the index of the first instance of 'the' in some_string.

    some_string (str) -- Any string.

    If 'the' cannot be found in the string, return -1.

    Examples:
    the_location("them") --> 0
    the_location("other") --> 1
    the_location("#yolo") --> -1
    '''
    return some_string.find('the')



def starts_with_love(some_string):
    '''
    Return True if the given string starts with 'love'.

    some_string (str) -- Any string.

    Examples:
    starts_with_love("radio") --> False
    starts_with_love("love you!") --> True
    starts_with_love("I love you!") --> False
    '''
    return some_string.find('love') == 0


def starts_with_number(some_string):
    '''
    Return True if the first character of the string is a number.

    some_string (str) -- A string containing at least on character

    Examples:
    starts_with_number("1 Apple") --> True
    starts_with_number("R2D2") --> False
    starts_with_number("4") --> True
    '''
    return some_string[0].isdigit()


def one_to_two(some_string):
    '''
    Replace all 1's in the string with 2's.

    some_string (str) -- Any string

    Examples:
    one_to_two("111") --> "222"
    one_to_two("222") --> "222"
    one_to_two("I have 1 dollar") --> "I have 2 dollar"
    '''
    return some_string.replace('1', '2')


def true_last_char(some_string):
    '''
    Return the last character of the given string while ignoring whitespace.

    some_string (str) -- A string with at least 1 non whitespace character.

    Examples:
    true_last_character("abc    ") --> "c"
    true_last_character("rex\t\n ") --> "x"
    true_last_character("bubbles") --> "s"
    '''
    some_string = some_string.strip()

    return some_string[-1]


def main():
    '''
    Test all of your functions here.
    '''


if __name__ == '__main__':
    main()
