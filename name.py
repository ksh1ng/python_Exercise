'''
Author: <ksh1ng>
Date: <2018.4.24>
Class: ISTA 130
Section Leader: <Johnny Hsu>

Description:
<hw01-(1)>
'''
import turtle
# put all of your import statements below this line and then delete this comment
def draw_N(t):
    '''draw "N" '''
    t.pensize(5)
    t.left(90)
    t.forward(100)
    t.right(150)
    t.forward(200/3**0.5)
    t.left(150)
    t.forward(100)


def draw_i(t):
    '''draw "i" '''
    t.down()
    t.left(90)
    t.forward(70)
    t.up()
    t.forward(30)
    t.shape("circle")
    t.stamp()
    t.shape("classic")

def draw_c(t):
    '''draw "c" '''
    t.up()
    t.forward(30)
    t.left(90)
    t.forward(15)
    t.down()
    t.right(240)
    for i in range(240):
        t.forward(0.5)
        t.right(1)

def draw_k(t):
    '''draw "k" '''
    t.down()
    t.left(90)
    t.forward(50)
    for i in range(3):
        t.forward(50)
        t.forward(-50)
        t.right(60)



#def draw_c(t):
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

    draw_N(nick)
    nick.up()
    nick.home()
    nick.forward(100)
    draw_i(nick)
    nick.up()
    nick.home()
    nick.forward(150)
    draw_c(nick)
    nick.up()
    nick.home()
    nick.forward(220)
    draw_k(nick)
    wn.exitonclick()
    # put main code here, make sure each line is indented one level, and delete this comment



    #input('Press enter to end.')  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
