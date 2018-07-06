'''
Author: <ksh1ng>
Date: <2018.7.6>
Class: ISTA 130
Section Leader: <Johnny Hsu>

Description:
<WS0412>
'''

# put all of your import statements below this line and then delete this comment

# put all of your function definitions below this line and then delete this comment
def upper_list(alist):
    '''
    Description:
     Converts a list of strings all to uppercase.
     The function should alter the original list and return None.
    Parameter:
     alist: (list)  a list of strings.
    Return: None
    '''
    for i in range(len(alist)):
        alist[i] = alist[i].upper()

#test
'''
a = ['nick', 'benson', 'nlanc']
upper_list(a)
print(a)
'''

def upper_list2(alist):
    '''
    Description:
     It returns a new list containing all of the strings from the original list in uppercase.
     The function should "NOT" alter the original list.
    Parameter:
     alist: (list) a list of strings.
    Return: (list) a new list.
    '''
    nlist = []

    for str in alist:
        nlist.append(str.upper())
    return nlist

#test
'''
a = ['nick', 'benson', 'nlanc']
upper_list2(a)
print(a)
print(upper_list2(a))
'''

def upper_values(dict):
    '''
    Description:
     The function converts all of the strings in all of the lists which are values of dict
     to uppercase. It should alter the original lists and return None.
    Parameter:
     dict: (dict) This dictionary maps keys, which may be any immutable object,
                  to values, which are lists of strings.
    Return: None.
    '''
    for key in dict:
        upper_list(dict[key])
#test
'''
dict = {1: ['nick','cujsl'], 2: ['benson','cuahei', 'csbkjbk'],3: ['dkuacbk','cbsjkc','dcabdjk']}
upper_values(dict)

print(dict)
'''

def upper_values2(dict):
    '''
    Description:
     The function converts all of the strings in all of the lists which are values of dict
     to uppercase. It should "NOT" alter the original dictionary.
    Parameter:
     dict: (dict) This dictionary maps keys, which may be any immutable object,
                  to values, which are lists of strings.
    Return: (dict) a new dict.
    '''
    new_dict = {}

    for key in dict:
        new_dict[key] = upper_list2(dict[key])
    return new_dict

#test
'''
dict = {1: ['nick','cujsl'], 2: ['benson','cuahei', 'csbkjbk'],3: ['dkuacbk','cbsjkc','dcabdjk']}
upper_values2(dict)

print(dict)
print(upper_values2(dict))
'''

def load_grade_book(file):
    '''
    Description:
     Build and return a dictionary from the file that maps student id's (strings)
     to a list of grades (floats). The same student may have more than one line
     in the file. For example, if the file's content is
            321321,89.5,87,93
            140907,78,69.5,73.5,87
            321321,95
     the function returns
            {'321321': [89.5, 87, 93, 95],
             '140907': [78, 69.5, 73.5, 87]
            }
    Parameter:
     file: (str)  A filename, the file is in CSV format (comma separated values).
                  Data in CSV files is separated by commas.
                  The first value is a student id, which is followed by a series of grades.
    Return: (dict) a dict.
    '''
    grades = {}
    f = open(file, 'r')
    for line in f:
        line = line.strip().split(',')
        student = line[0]
        grade = line[1:]
        grade = [float(num) for num in grade] #convert the type of everyone grades to float.

        if not student in grades:
              grades[line[0]] = []

        grades[line[0]].extend(grade)
    f.close()

    return grades


#test
'''
print(load_grade_book('nick.txt'))
'''


def load_grade_book2(file, grades_dict):
    '''
    Description:
     Instead of creating a grade book dictionary from scratch, this
     version adds the information in the file to the existing dictionary
    Parameter:
     file: (str)  filename.
     dict: (dict)  a grade book dictionary.
    Return: None.
    '''
    f = open(file, 'r')

    for line in f:
        line = line.strip().split(',')
        student = line[0]
        grade = line[1:]
        grade = [float(num) for num in grade] #convert the type of everyone grades to float.

        if not student in grades_dict:
              grades_dict[line[0]] = []

        grades_dict[line[0]].extend(grade)

    f.close()

#test
'''
adict = {'56461': ['1', '2']}
load_grade_book2('nick.txt', adict)
print(load_grade_book('nick.txt'))
print()
print(adict)
'''

def mean_grades(grades_dict):
    '''
    Description:
     It returns a new dictionary that maps student id's to average grades.
    Parameter:
     grades_dict: (dict) a grade book dictionary.
    Return:
     (dict) a new dictionary.
    '''
    mean_dict = {}

    for student in grades_dict:
        mean_dict[student] = sum(grades_dict[student]) / len(grades_dict[student])

    return mean_dict
#test
grade_book = load_grade_book('nick.txt')
print(mean_grades(grade_book))
#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''

    # put main code here, make sure each line is indented one level, and delete this comment



    #input('Press enter to end.')  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
