'''
Author: <ksh1ng>
Date: <2018.6.27>
Class: ISTA 130
Section Leader: <Johnny Hsu>

Description:
<WS0405>
'''

# put all of your import statements below this line and then delete this comment

# put all of your function definitions below this line and then delete this comment
def get_3(list):
    '''
    Description:
     It gets three numbers from the user in a loop, turns each one into
     a float, and appends it to the list.

    Parameter:
     list: list argument
    Return: None
    '''
    for i in range(3):
        number = float(input('Enter a number: '))
        list.append(number)

def mean_of_nine():
    '''
    Description:
     Initializes an empty list. It then calls get_3 three times,
     passing the list to get_3 each time. Finally, it calculates
     and returns the mean (average) of the nine elements in the list.

    Parameter: None
    Return: the mean (average) number.
    '''
    alist = []

    for i in range(3):
        get_3(alist)

    return round(sum(alist) / len(alist), 2)

def lists_2_dict(list1, list2):
    '''
    Description:
     takes two lists of the same length. Return a dictionary that
     maps each element in the first list to the corresponding element
     in the second list. If there are duplicate keys in the first list,
     overwrite the previous key-value pair in the dictionary.

    Parameter:
     list1, list2: two lists of the same length.
    Return: a dictionary
    '''
    dict = {}

    for i in range(len(list1)):
        dict[list1[i]] = list2[i]
    return dict




#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''

    # put main code here, make sure each line is indented one level, and delete this comment

    '''
    Write code creating a dictionary called state_caps that maps 'AZ'
    to 'Phoenix', 'CA' to 'Sacramento', and 'DE' to 'Dover' in two ways.
    '''
    #1.create an empty dictionary and add each key-value pair individually.
    state_caps1 = {}
    state_caps1['AZ'] = 'Phoenix'
    state_caps1['CA'] = 'Sacramento'
    state_caps1['DE'] = 'Dover'

    #2.create the whole thing in one statement with a dictionary literal.
    state_caps2 = {'AZ' : 'Phoenix', 'CA' : 'Sacramento', 'DE': 'Dover'}

    #Finally, add the key value pair 'ID': 'Boise'.
    state_caps1['ID'] = 'Boise'
    state_caps2['ID'] = 'Boise'



    #input('Press enter to end.')  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
