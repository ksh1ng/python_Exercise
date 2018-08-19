def largest_num(nums):
    '''
    This function takes in a list of integers. Your task is to print
    the largest number in the list.

        Example:
            nums = [ 1, 2, 45, 2002, 3]

            2002 should be printed
    '''
    print(max(nums))





def concat_name(names_list):
    '''
    This function takes a list of strings that represent either a first or
    last name.
        Example: ['King', 'Kong', 'Stephen', 'Hawking', ...]

    Your task is to CREATE and RETURN a new SORTED list that contains
    the first and last names concatenated with a space. You
    can assume that the names_list will follow the pattern of
    first name, last name, first name, last name etc.
        Example of returned list:
            ['King Kong', 'Stephen Hawking', ...]
    '''
    blist = []
    i = 0

    while i < len(names_list):
        blist.append(names_list[i] + ' ' + names_list[i + 1])
        i += 2

    return sorted(blist)





def reverse_name_alter_case(name_str):
    '''
    This function takes in a string that represents a name. The string will
    only consist of a first and last name.

    Your task is to reverse name_str to last name then first and alternate
    the letter cases.

    This function should return a string.

        Example:
            name_str = 'Stephen Hawking'

            Function returns: 'HaWkInG StEpHeN'

    Note: the that every word must start with an upper case letter and then
    alternate between upper and lower case.

        Hints: split, list, and join may be useful in this function.

    '''
    name = name_str.lower().split()
    name.reverse()
    name = [list(name[0])] + [list(name[1])]  #become list of lists


    for i in range(len(name)):
        for j in range(len(name[i])):
            if j % 2 == 0:
                name[i][j] = name[i][j].upper()
        name[i] = ''.join(name[i])


    return ' '.join(name)



def organize_symbols(sym_lst):
    '''
    This function takes in a list that contains single string elements. Each
    element in the string is a symbol.

        Example: sym_lst = ['@', '@', '!', '+' , '&']

    You will need to re-arrange the mixed up list based on the given order.

        order = "!@#$%^&*()_+"  #This is given bellow

        Example:

            sym_lst = ['@', '@', '!', '+' , '&']

            After function execution:

                sym_lst = ['!', '@', '@', '&', '+']


    This function shouldn't return anything, alter the list in place.


    Hint: Will be useful to use clear() and extend()
    '''
    order = "!@#$%^&*()_+"
    order_lst = []
    for str in sym_lst:
        order_lst.append(order.find(str))

    sym_lst.clear()

    for order_num in sorted(order_lst):
        sym_lst.append(order[order_num])




def find_the_smiley(stringy, key):
    '''
    This function take in two strings. This first parameter, stringy contains a
    random sequence of text emoji smilies. The second parameter, key, will consist
    of a singe emoji smiley which will serve as your key.

    Given a string with smilies count how many times the key smiley appears in
    the string

    Example:

        stringy = ":):):(:(:P:$:]"
        key =  ":)"

        function returns: 2
    '''
    find = stringy.find(key)
    times = 0
    while find != -1:
        times += 1

        find = stringy.find(key, find + 1)

    return times


def sum_main_diagonal(LOL):
    '''
    This function takes in a lists of lists as its sol argument.

    Your task is to PRINT the sum of the main diagonal.

    Example LOL = [[5, 0, 1],
                   [1, 9, 3],
                   [3, 8, 2]]

        Function prints: 16
    '''
    sum = 0
    for i in range(len(LOL)):
        sum += LOL[i][i]

    print(sum)




def organize_list_of_lists(LOL):
    '''
    This function takes in a lists of lists as its sol argument.

    Organize the list of lists. Order the inner list in ascending order,
    then re-arrange the list of list based on the first of the element in
    ascending.

    Return None, use clear and extend if you want but do you have to?

    Example LOL = [[5, 0, 1],
                   [1, 9, 3],
                   [3, 8, 2]]

            would result in

            LOL = [[0, 1, 5],
                   [1, 3, 9],
                   [2, 3, 8]]
    '''
    for i in range(len(LOL)):
        LOL[i].sort()
    LOL.sort()





def main():
    '''
    test your functions in main
    '''
    nums = [ 1, 2, 45, 2002, 3]

    '''
    names = ['King', 'Kong', 'Stephen', 'Hawking', 'Beyonce', 'Knowles', \
              'Henry', 'Cavill', 'Chuck', 'Norris', 'Bruce', 'Lee']
    print(concat_name(names))


    name_str = 'Stephen Hawking'
    print(reverse_name_alter_case(name_str))


    sym_lst = ['@', '@', '!', '+' , '&']
    organize_symbols(sym_lst)
    print(sym_lst)



    stringy = ":):):(:(:P:$:]"
    key =  ":)"
    print(find_the_smiley(stringy, key))


    LOL = [[5, 0, 1], [1, 9, 3], [3, 8, 2]]
    sum_main_diagonal(LOL)


    LOL = [[5, 0, 1], [1, 9, 3], [3, 8, 2]]

    organize_list_of_lists(LOL)
    print(LOL)
    '''
    syms = ['@', '@', '!', '+' , '&']

    sm= ":):):(:(:P:$:]"
    key=  ":)"

    LOL = [[1,2,3], [2,9,4], [1,90,5]]


if __name__ == '__main__':
    main()
