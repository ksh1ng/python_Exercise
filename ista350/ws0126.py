'''
Author: <ksh1ng>
Date: <2018.8.18>
Class: ISTA 350
Section Leader: <Johnny Hsu>

Description:
<WS0126>
'''

# put all of your import statements below this line and then delete this comment

# put all of your function definitions below this line and then delete this comment
def is_symmetric(matrix):
    '''
    this Boolean function takes a square matrix (list of lists) and determines if it is
    symmetric.
    '''


    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != matrix[j][i]:
                return False

    return True

def get_col(matrix, n):
    '''
    this list function takes a list of lists and returns a list of the values in column n (0-based),
    where n is a second argument (integer) passed to the function.
    If any row has length < n + 1, put -999 in the appropriate position in the resulting list.
    '''
    ncol = []
    for i in range(len(matrix)):     #is matrix is empty ncol will be []
        if len(matrix[i]) < n + 1:
            matrix[i].extend([-999] * (n + 1 - len(matrix[i])))
        ncol.append(matrix[i][n])

    return ncol


print(get_col([], 5))

def duplicates(lst):
    '''
    this Boolean function takes one list argument and returns True if the list contains any
    duplicate elements, False otherwise.
    '''
    for i in range(len(lst)-1):
        if lst[i] in lst[i + 1: ]:
            return True

    return False


def is_palindrome(lst):
    '''
    this Boolean function takes one sequence argument and returns True if the
    sequence is the same forward as backward, False otherwise.
    '''
    return lst[:] == lst[::-1]





#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''

    # put main code here, make sure each line is indented one level, and delete this comment

    '''
    print(get_col([[0, 45, 17, 51], [45, 32, 12], [17, 12, -2, 0, 731]], 3) )

    print(duplicates([1,3,2,6,'1']))

    print(is_palindrome([1,2,3,2,1]))

    '''

    #input('Press enter to end.')  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
