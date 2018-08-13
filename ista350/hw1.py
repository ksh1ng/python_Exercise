'''
Author: <ksh1ng>
Date: <2018.8.13>
Class: ISTA 350
Section Leader: <Johnny Hsu>

Description:
<hw01>
'''

# put all of your import statements below this line and then delete this comment

# put all of your function definitions below this line and then delete this comment

def sort_int_string(string):
    '''
    Description:
     if the argument is "43 -1 17", the function returns "-1
     17 43".
    Parameters:
     string: be a series of integers separated by spaces. Ignore
             any extra whitespace.

    Return: (str) with the argument’s integers separated by spaces
                  but now in sorted order.
    '''
    lst = []

    for num in string.split():
        lst.append(int(num))

    lst.sort()

    for i in range(len(lst)):
        lst[i] = str(lst[i])

    return ' '.join(lst)


def dash_reverse(string):
    '''
    Description:
     takes one string argument and returns a new string with the same
     characters as in the argument but in reverse order and separated by dashes.
    Parameters:
     string: (str)
    Return: (str)
    '''
    lst = list(string)
    lst.reverse()

    return '-'.join(lst)


def xslice_replace(start_string, start, end, step, replacement_string):
    '''
    Description:
     mimic the functionality of extended slices for lists
     with the string function.

    Parameters:
        start_string, replacement_string: (str)
        start, end, step: (int)
    Return: (str)new string
    '''
    lst = list(start_string)
    lst[start:end:step] = list(replacement_string)

    return ''.join(lst)

def element_ip_replace(start_list, item, replacement_value=None):
    '''
    Description:
     This list function mimics Python’s replace method for strings.
     Replace every occurrence of the item in the list with the replacement
     value.

    Parameters:
     start_list: (list) a list to be altered
     item: (value)an item to be searched for
     replacement_value: (value)that will replace the item wherever
                               it is found in the list
    Return:None
    '''
    for i in range(len(start_list)):
        if start_list[i] is item:              #because 1 == True is True,
            start_list[i] = replacement_value  #this is not reasonable.

#like the function above, except with a return of new list.
def element_nl_replace(start_list, item, replacement_value=None):
    nlist = []
    for i in range(len(start_list)):
        if start_list[i] is item:
            nlist.append(replacement_value)
        else:
            nlist.append(start_list[i])
    return nlist

def lreplace(lst1, lst2, lst3=[]):
    '''
    Description:
     This function acts like the replace method for strings, except that it
     alters the list in place instead of returning a new one.

    Parameters:
     lst1,2,3: (lst) Search the lst1. Every place where the lst2
                     occurs as a sublist of the lst1,
                     replace it with the items in the lst3.
    Return: None.
    '''
    i = 0

    while i < len(lst1):

        if len(lst2) == 0 and len(lst3) == 0:   #lst2,3=[]
            break


        if lst1[i:i+len(lst2)] == lst2:

            lst1[i:i+len(lst2)] = lst3


            if lst2 == []:    #solve edge condition
                i += len(lst3) + 1
            else:
                i += len(lst3)



        else:
            i += 1

#solve edge condition

    if lst2 == []:
        lst1[i:i+len(lst2)] = lst3


    if lst1 == [] and lst2 == []:   #lst1,2=[]
        lst1[:] = lst3






lst1 = [777, 777, 777, 88, 777, 777]
lst2 = [777]

m = []
lreplace(m, [], [777])
print(m)


def list_lt(lst1, lst2):
    '''
    Description:
     Every entry in the new list will be either True or False.
     The entry in the new list at a given index will be True
     if the element at that index in the first list is less
     than the corresponding element in the second list, False otherwise.

    Parameters:
     lst1,2: (lst)just two lists with any type element.
    Return: (lst) new list
    '''
    nlst = []

    if len(lst1) != len(lst2):
        return None

    for i in range(len(lst1)):
        if lst1[i] < lst2[i]:
            nlst.insert(i, True)
        else:
            nlst.insert(i, False)

    return nlst


def sum_of_powers(bases_lst, exponents_lst):
    '''
    Description:
      For example, if the first argument is [1, 2, 3] and the second
      argument is [2], then the function returns [14],
      calculated 12 + 22 + 32.
.
    Parameters:
    bases_lst: (lst) a list of bases.
    exponents_lst: (lst) a list of exponents.

    Return: (lst) new list.
    '''
    nlst = []
    i = 0

    while i < len(exponents_lst):
        sum = 0
        j = 0
        while j < len(bases_lst):
            sum += bases_lst[j] ** exponents_lst[i]
            j += 1

        nlst.append(sum)
        i += 1

    return nlst



def trace(matrix):
    '''
    Description:
     find the trace of a matrix.
    Parameters:
     matrix: (lst)– a list of lists representing the matrix(square).
                  assume that the argument is a nonempty square matrix of
                  numbers.
    Return: (int/float) the trace of that matrix.
    '''
    trace = 0
    for i in range(len(matrix)):
        trace += matrix[i][i]

    return trace

def str_by_twos(str):
    '''
    Description:
     generate a list of each pair of adjacent characters in order.

    Parameters:
     str: (str)
    Return:(lst)
    '''
    lst = []

    for i in range(len(str)-1):
        lst.append(str[i:i+2])
    return lst



#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''


    # put main code here, make sure each line is indented one level, and delete this comment
    '''
    print(sort_int_string('43 -1 17'))

    print(dash_reverse('aevbewhih'))


    start_string = 'kshing'
    replacement_string = 'abc'

    print(xslice_replace(start_string, 0, 5, 2, replacement_string))



    start_list = ['nick', 'benson', 1, 2, 'nick', True]
    element_ip_replace(start_list, 'nick', 10)
    print(start_list)

    element_ip_replace(start_list, 'nick')
    print(start_list)



    start_list = ['nick', 'benson', 1, 2, 'nick', True]
    nlist = element_nl_replace(start_list, 'nick', 10)
    print(start_list)
    print(nlist)



    lst1 = [[1, 2], 'nick', ['nick', 'benson'], 4, [1, 2], [3, 4], ]
    lst2 = [1, 2]

    lreplace(lst1, lst2, lst3=['kshing', 'ksh1ng'])
    print(lst1)


    lst1 = ['nick', 'kshing', 171, 64]
    lst2 = ['benson', 'cat', 171, 56]
    print(list_lt(lst1, lst2))


    bases_lst = [1, 2, 3, 5]
    exponents_lst = [2, 6, 8]
    print(sum_of_powers(bases_lst, exponents_lst))




    matrix = [[15, 777, -12], [ 5, 4, 13], [11, 7, -1]]
    print(trace(matrix))


    str = 'kshing'
    print(str_by_twos(str))
    '''
    #input('Press enter to end.')  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
