'''
Author: <ksh1ng>
Date: <2018.8.22>
Class: ISTA 350
Section Leader: <Johnny Hsu>

Description:
<WS0128>
'''

# put all of your import statements below this line and then delete this comment

# put all of your function definitions below this line and then delete this comment
def is_diagonal(matrix):
    '''
    This Boolean function takes a rectangular list of lists and returns True
    if it represents a diagonal matrix (all off-diagonal terms are 0),
    False if not.
    '''
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i != j and matrix[i][j] != 0:
                return False

    return True

def line_count(fname):
    '''
    This function has one string parameter, the name of a file. It returns the number of
    lines in that file.
    '''
    return len(open(fname, 'r').readlines())



def dict_from_lists(lst1, lst2):
    '''
    takes two list parameters.
    If they have different lengths, return an empty dictionary.
    Otherwise, return a dictionary that maps each element in the
    first list to the element in the second list with the same index.
    '''
    dict = {}

    if len(lst1) == len(lst2):
        for i in range(len(lst1)):
            dict[lst1[i]] = lst2[i]

    return dict



def grade_book(fname):
    '''
    takes one argument, a string representing a filename, and returns a
    dictionary.
    An example line from the file: 887231: 95 81 87 92. The first number
    is a student id number, the rest are grades
    '''
    adict = {}

    for line in open(fname, 'r').readlines():
        id = line.split(':')[0]
        grades = line.split(':')[1].split()

        for i in range(len(grades)):
            grades[i] = float(grades[i])

        if id not in adict:
            adict[id] = []

        adict[id].extend(grades)

    return adict


def final_grades(grade_book):
    '''
    takes a grade_book(above)dictionary and returns a new dictionary that
    maps each id to the student's average grade.
    '''
    ndict = {}

    for key in grade_book:
        ndict[key] = round(sum(grade_book[key]) / len(grade_book[key]), 1)

    return ndict

grades = grade_book('test.txt')
print(grades)

print(final_grades(grades))

def grade_distribution(final_grades):
    '''
    takes a final_grades dictionary and returns a new dictionary that maps
    keys 'A', 'B', 'C', 'D', 'E' to the number of each in the class based on
    the traditional 90-80-70-60 cutoffs.
    '''
    ndict = {}
    for key in final_grades:
        fgrade = final_grades[key]

        if fgrade >= 90:
            ndict[key] = 'A'
        elif fgrade >= 80:
            ndict[key] = 'B'
        elif fgrade >= 70:
            ndict[key] = 'C'
        elif fgrade >= 60:
            ndict[key] = 'D'
        else:
            ndict[key] = 'E'
    return ndict

def class_median(final_grades):
    '''
    takes a final_grades dictionary and returns the median final grade
    for the class
    '''
    grades = sorted(final_grades.values())
    if len(grades) % 2 != 0:
        return grades[len(grades) // 2 - 1] #ex:grades[4-1] is the 4th float number in a list

    else:
        return (grades[len(grades) // 2 - 1] + grades[len(grades) // 2 ]) / 2

grades = grade_book('test.txt')
print(final_grades(grades))

print(class_median(final_grades(grades)))








#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''

    # put main code here, make sure each line is indented one level, and delete this comment
    '''
    matrix = [[1, 0, 0], [1, 2, 0], [0, 0, 3]]
    print(is_diagonal(matrix))


    print(line_count('test.txt'))


    print(dict_from_lists([22, 114, 22], [77, 78, 79]))





    grades = grade_book('test.txt')
    print(grades)

    print(final_grades(grades))

    '''


    #input('Press enter to end.')  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
