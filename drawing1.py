'''
Author: <ksh1ng>
Date: <2018.4.24>
Class: ISTA 130
Section Leader: <Johnny Hsu>

Description:
<hw01-(2)>
'''
import turtle
# put all of your import statements below this line and then delete this comment

def shape(t,size):
    t.shape("circle")
    t.stamp()
    t.shape("classic")
    for i in range(20):
        t.forward(size)
        t.forward(-size)
        t.left(18)

def rotated_shapes(t,size,number,angle):
    '''
    The first parameter is for a turtle. The second parameter is the size of
    shape to draw. The third parameter is the number of shapes to draw. The
    fourth parameter is the angle between each shape.
    '''
    for j in range(number):
        shape(t,size)
        t.left(angle)


# put all of your function definitions below this line and then delete this comment


#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    wn=turtle.Screen()
    nick=turtle.Turtle()
    nick.speed(0)

    size=0
    num=0
    for k in ["red","blue","yellow"]:
        size+=100
        num+=4
        nick.color(k)
        rotated_shapes(nick,size,num,1)
        nick.up()
        nick.left(90)
        nick.forward(200+size)
        nick.down()





    wn.exitonclick()
    # put main code here, make sure each line is indented one level, and delete this comment



    #input('Press enter to end.')  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
