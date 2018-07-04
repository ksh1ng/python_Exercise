'''
Lab 9 Exercises
ISTA 130
07/04/18
'''


def new_rjust(some_string, width):
    '''
    Replicates the str.rjust method
    You may not use the rjust method in this function

    Return some_string right-justified in a string of length width.
    If width is less than or equal to the length of the string
    return the original string.

    Examples:
    new_rjust("pigs", 7) --> "   pigs"
    new_rjust("tree", 10) --> "      tree"
    new_rjust("eagle", 4) --> "eagle"
    '''
    space_width = width - len(some_string)

    if space_width <= 0:
        return some_string

    return ' ' * space_width + some_string



def new_title(some_string):
    '''
    Replicates the str.title method
    You may not use the title method in this function

    Return a titlecased version of S, i.e. words start with title case
    characters, all remaining cased characters have lower case.
    Any character that is not a letter marks the end of a word.

    Examples:
    new_title("mObY DiCk") --> "Moby Dick"
    new_title("ac-DC") --> "Ac-Dc"
    new_title("they're bill's friends") --> "They'Re Bill'S Friends"
    '''
    result = some_string[0].upper()

    for i in range(1, len(some_string)):
        if not some_string[i - 1].isalpha():
            result += some_string[i].upper()
        else:
            result += some_string[i].lower()

    return result



def new_startswith(some_string, prefix):
    '''
    Replicates the str.startswith method
    You may not use the startswith method in this function

    Return True if some_string starts with the specified prefix,
    False otherwise.

    Examples:
    new_startswith("slinky", 's') --> True
    new_startswith("birthright", 'birth') --> True
    new_startswith("crazy", 'glue') --> False
    '''
    return some_string.find(prefix) == 0


def new_in(some_string, sub):
    '''
    Replicates the in operator
    You may not use the in operator or find method in this function

    Return True if some_string contains the specified substring sub,
    False otherwise.

    Examples:
    new_in('caricature', 'cat') --> True
    new_in('meddling', 'line') --> False
    new_in('aeiou', 'i') --> True
    '''
    for i in range(len(some_string)):
        if some_string[i : i + len(sub)] == sub:
            return True

    return False


def new_find(some_string, sub):
    '''
    Replicates the str.find method
    You may not use the find or index methods in this function

    Return the lowest index in some_string where substring sub is found.
    Return -1 on failure

    Examples:
    new_find("running", 'n') --> 2
    new_find("them", "the") --> 0
    new_find("bill", "ted") --> -1
    '''
    for i in range(len(some_string)):
        if some_string[i : i + len(sub)] == sub:
            return i

    return -1




def new_count(some_string, sub):
    '''
    Replicates the str.count method
    You may not use the count method in this function

    Return the number of occurrences of substring sub
    in some_string

    Examples:
    new_count('Happy Birthday', 'a') --> 2
    new_count('cornbread', 'ham') --> 0
    new_count('mississippi', 'iss') --> 2
    '''
    count = 0

    for i in range(len(some_string)):
        if some_string[i : i + len(sub)] == sub:
            count += 1

    return count


def main():
    '''Test your functions here'''


if __name__ == '__main__':
    main()
