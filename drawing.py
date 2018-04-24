'''
Author: <ksh1ng>
Date: <2018.4.24>
Class: ISTA 130
Section Leader: <Johnny Hsu>

Description:
<hw01-(3)>
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




# put all of your function definitions below this line and then delete this comment


#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    nick=turtle.Turtle()
    wn=turtle.Screen()
    nick.pensize(10)
    nick.speed(0)

    s=20
    for _color_ in ["blue","red","yellow","green","purple","orange"]:
        nick.down()
        nick.color(_color_)
        shape(nick,s)
        s+=10
        nick.up()
        nick.left(270/6)
        nick.forward(100)





    wn.exitonclick()
    # put main code here, make sure each line is indented one level, and delete this comment



    #input('Press enter to end.')  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
