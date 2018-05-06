'''
Author: <ksh1ng>
Date: <2018.5.6>
Class: ISTA 130
Section Leader: <Johnny Hsu>

Description:
<hw01-(2)>
'''
import turtle
# put all of your import statements below this line and then delete this comment
def polygon(turtle,num_sides,_color_,side_length):
    '''Draw any polygon you want'''
    turtle.color(_color_)
    turtle.pensize(3)
    for i in range(num_sides):
        turtle.forward(side_length)
        turtle.left(360/num_sides)

# put all of your function definitions below this line and then delete this comment


#==========================================================
def main():
    '''
    1.) Ask the user how many polygon to draw.
    2.) For each of the polygons perform the following steps:
        a. Ask the user how many sides the polygon should have.
        b. Ask the user for the length of the side of the polygon.
        c. Using the values you got from the user, use a turtle to draw the polygon
    '''
    nick=turtle.Turtle()
    wn=turtle.Screen()

    num_polygons=int(input("Enter the number of polygons you’d like to see: "))
    for j in range(num_polygons):
        num_side=int(input("Enter the number of sides: "))
        color=input("Enter the color: ")
        side_len=int(input("Enter the side length for your polygon: "))
        print()

        polygon(nick,num_side,color,side_len)

    wn.exitonclick()
    # put main code here, make sure each line is indented one level, and delete this comment



    #input('Press enter to end.')  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
