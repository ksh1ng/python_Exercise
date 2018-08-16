'''
Author: <ksh1ng>
Date: <2018.8.16>
Class: ISTA 350
Section Leader: <Johnny Hsu>

Description:
<WS0121>
'''

# put all of your import statements below this line and then delete this comment

# put all of your function definitions below this line and then delete this comment
def lreplace(alter_lst, search_lst, replace_lst=[]):
    '''
    This function acts like the replace method for strings. It has three parameters,
    all lists. It returns a new list that is the same as the first argument with all
    occurrences of the second argument replaced by the third argument. The third parameter
    has the empty list as its default argument.
    '''
    altered_lst = []
    if alter_lst != [] and search_lst != []:
        i = 0
        while i < len(alter_lst):
            if alter_lst[i:i + len(search_lst)] == search_lst:
                altered_lst.extend(replace_lst)
                i += len(search_lst)

            else:
                altered_lst.append(alter_lst[i])
                i += 1

    if alter_lst == [] and search_lst == []:
        altered_lst.extend(replace_lst)

    if alter_lst != [] and search_lst == []:
        i = 0

        altered_lst.extend(replace_lst)
        while i < len(alter_lst):
            altered_lst.append(alter_lst[i])
            altered_lst.extend(replace_lst)

            i += 1

    return altered_lst


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










#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''

    # put main code here, make sure each line is indented one level, and delete this comment
    '''
    alter_lst = [7, 7, 7, 7, 88, 7, 7]
    print(lreplace([7, 7, 7, 88, 7, 7], [7,7], []))




    '''


    #input('Press enter to end.')  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
