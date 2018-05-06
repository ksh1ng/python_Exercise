'''
Author: <ksh1ng>
Date: <2018.5.5>
Class: ISTA 130
Section Leader: <Johnny Hsu>

Description:
<hw03-(1)>
'''
import math
# put all of your import statements below this line and then delete this comment
def print_word(times,str):
    '''The first is for an integer (assume it will always be non-negative). The second is for a string.
    The function will print the string on the given number of lines, each time preceded by a line number and an arrow'''
    for i in range(times):
        i+=1
        print(i,"-->",str)

def bacteria(num_minutes,num_generations):
    '''The first is an integer giving the number of minutes it takes for a bacterium to split into two new bacteria.
     The second is an integer giving the number of bacterial generations to include in the output
     Assume you always begin with a single bacterium in the dish and every bacterium always splits into
    exactly two bacteria at the end of each time period.'''
    for i in range(num_generations):
        i+=1
        print("after",i*num_minutes,"minutes: ",2**i,"bacteria")

def convert_to_copper(num_gold,num_silver,num_copper):
    '''Three integer parameters.The first represents a number of gold coins. The second represents a number of
       silver coins. The third represents a number of copper coins. The function will print
       the numbers of each type of coin followed by the total value of all of the coins
       when converted to copper.
       @The exchange rate for coins is:
       5 copper pieces (cp) = 1 silver piece (sp)
       10 silver pieces = 1 gold piece (gp)'''
    sum_copper=num_gold*50+num_silver*5+num_copper
    print(num_gold,"gp,",num_silver,"sp,",num_copper,"cp converted to copper is:",sum_copper,"cp")


def convert_from_copper(initial_copper):
    '''The function prints out the number of gold pieces (gp),silver pieces (sp), and copper pieces (cp)
       you would end up with if you first converted as many of the initial copper pieces to gold as
       possible and then converted as many of the remaining copper pieces as possible to silver pieces.'''
    num_gold=initial_copper//50
    num_silver=(initial_copper%50)//5
    remaining_copper=(initial_copper%50)%5
    print(initial_copper,"copper pieces is:",num_gold,"gp,",num_silver,"sp,",remaining_copper,"cp")


def repeat_word(word,num_row,num_col):
    ''' Three parameters.
        The first is for a word (a string). The second is for an integer representing a number of rows.
        The third is for an integer representing a number of columns. The function prints the word in a
        number of rows equal to the value of the rows parameter and each row contains the word
        repeated a number of times equal to the columns parameter.
    '''
    for i in range(num_row):
        print(word*num_col)


def text_triangle(integer):
    '''takes an integer parameter and prints X’s in a triangle shape.'''
    if integer<0:
        print()
    else:
        for i in range(integer):

            print("X"*(i+1))


def surface_area_of_cylinder(radius,height):
    ''' Two arguments. The first is a float representing the radius of a cylinder.
        The second is a float representing the height of a cylinder.
        The function calculates and prints the surface area of a cylinder with the given radius
        and height'''

    surface_area=2*math.pi*radius**2+2*math.pi*radius*height
    print("The surface area of a cylinder with radius",radius,"and height",height,"is",surface_area)


def  tree_height(distance,length_string):
    '''The first is a float representing the distance from you to the base of the tree.
       The second is a float representing the length of the kite string.'''
    height=math.sqrt(length_string**2-distance**2)
    print("Kite string: {}\nDistance: {}\nHeight: {}".format(length_string,distance,height))




# put all of your function definitions below this line and then delete this comment


#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    #print_word(5,'nick')
    #bacteria(3,3)
    #convert_to_copper(15,23,12)
    #convert_from_copper(1107)
    #repeat_word('kobold',5,3)
    #text_triangle(0)
    #surface_area_of_cylinder(10.0,10.0)
    #tree_height(100, 141.421356)


    # put main code here, make sure each line is indented one level, and delete this comment





if __name__ == '__main__':
    main()
