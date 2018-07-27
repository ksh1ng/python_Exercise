'''
Author: <ksh1ng>
Date: <2018.7.26>
Class: ISTA 130
Section Leader: <Johnny Hsu>

Description:
<WS0119>
'''

# put all of your import statements below this line and then delete this comment

# put all of your function definitions below this line and then delete this comment
def string_mean(astring):
    '''takes a string representing numbers separated by spaces and returns their average.'''
    sum = 0
    for num in astring.split():
        sum += float(num)

    return sum / len(astring.split())

def make_string(alist, astr=' '):
    '''
    Description:
     Ex: make_string([True, 77.8, 'dog'], '---') --> 'True---77.8---dog'
    Parameters:
     alist: a list of Python objects.
     str: a string for separating in the textual representations of the objects.
    Return:
     a string containing the textual representations of the objects in the list separated
     from each other by the string.
    '''

    for i in range(len(alist)):
        alist[i] = str(alist[i])


    return astr.join(alist)





def xslice_replace(start_string, start, end, step, replacement_string):
    '''
    Description:
     mimic the functionality of extended slices for lists with the string function.
    Parameters:
     start_string, replacement_string: (str)
     start, end, step: (int)
    Return:
     new string after altering
    '''
    nstr = ''
    i = start
    j = 0 #the index of replacement_string

    while i < end:
        nstr = start_string.replace(start_string[i], replacement_string[j])
        start_string = nstr
        i += step
        j += 1

    return nstr

#improve def xslice_replace function
def xslice_replace2(start_string, start, end, step, replacement_string):
    start_string = list(start_string)
    replacement_string = list(replacement_string)
    start_string[start:end:step] = replacement_string

    return ''.join(start_string)



def lreplace(alist, sublist, replacement=[]):
    '''
    Description:
      It returns a new list that is the same as the first argument with all occurrences of
      the second argument replaced by the third argument.
    Parameters:
     alist, sublist, replacement: (list)
    Return:
     a new list
    '''
    nlist = []
    alist = make_string(alist, astr=' ')
    alist = alist.replace(make_string(sublist, astr=' '), make_string(replacement, astr=' '))

    for num in alist.split():
        nlist.append(int(num))

    return nlist


def trace(matrix):
    '''
    This function takes one argument – a list of lists representing the matrix and
    returns the trace of that matrix.
    '''
    trace = 0
    for i in range(len(matrix)):
        trace += matrix[i][i]

    return trace



#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''

    # put main code here, make sure each line is indented one level, and delete this comment

    #test
    '''
    print(string_mean('13 -7 -6 24.4'))

    print(make_string([True, 77.8, 'dog'], '---'))
    print(xslice_replace('nick', 0, 4, 2, 'ab'))

    print(lreplace([7, 7, 7, 88, 7, 7], [7, 7], [5]) )

    matrix = [[15, 777, -12], [ 5, 4, 13], [11, 7, -1]]
    print(trace(matrix))
    '''


    #input('Press enter to end.')  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
