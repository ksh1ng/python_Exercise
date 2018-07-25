'''
Author: <ksh1ng>
Date: <2018.7.25>
Class: ISTA 130
Section Leader: <Johnny Hsu>

Description:
<WS0114>
'''

# put all of your import statements below this line and then delete this comment

# put all of your function definitions below this line and then delete this comment


 # traverses by index
def square_list1(alist):
    '''
    Description:
     Return a new list which contains the squares of the elements in the argument.
    Parameter:
     alist: (list) a list of numbers.
    Return: (list)
    '''
    nlist = []
    for i in range(len(alist)):
        nlist.append(alist[i] ** 2)

    return nlist

 # traverses by element
def square_list2(alist):
    nlist = []

    for num in alist:
        nlist.append(num ** 2)
    return nlist


 # uses a while loop
def square_list3(alist):
    nlist = []
    i = 0

    while i < len(alist):
        nlist.append(alist[i] ** 2)
        i += 1

    return nlist

 # for loop
def square_list_ip1(alist):
    ''' ip stands for 'in place' '''

    for i in range(len(alist)):
        alist[i] = alist[i] ** 2

 # while loop
def square_list_ip2(alist):
    i = 0
    while i < len(alist):
        alist[i] = alist[i] ** 2
        i += 1

def squares_list(num):
    '''
    returns a list containing the squares of the integers between one and
    the parameter (inclusive).
    '''
    nlist = []
    for i in range(num):
        nlist.append((i+1) ** 2)

    return nlist

def squares_dict(num):
    '''
     returns a dictionary mapping the integers between one and the parameter
     (inclusive) to their squares.
    '''
    dict = {}
    for i in range(num):
        dict[i+1] = (i+1) ** 2

    return dict

class Square:
    '''create different kind of square instance'''
    def __init__(self, sidelen):
        self.side = sidelen

    def perimeter(self):
        return self.side * 4

    def area(self):
        return self.side ** 2

#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''

    # put main code here, make sure each line is indented one level, and delete this comment

    #test
    '''
    alist = [1, 2, 3]
    print(square_list3(alist))
    '''

    '''
    blist = [1, 3, 9]
    square_list_ip2(blist)
    print(blist)
    '''
    '''
    print(squares_dict(5))
    '''

    #test class
    square = Square(10)
    print(square.perimeter())
    print(square.area())

    #input('Press enter to end.')  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
