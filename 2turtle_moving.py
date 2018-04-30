import turtle
import random

def move_random(t):

        coin=random.randrange(0,2)
        angle=random.randrange(0,91)
        if coin==0:
            t.left(angle)
        else:
            t.right(angle)
        t.forward(50)

def is_collide(t1,t2):
    if t1.distance(t2)<1:
        return True
    else:
        return False


def is_in_screen(w,t):
    leftbound=-200
    rightbound=200
    topbound=200
    bottombound=-200

    turtleX=t.xcor()
    turtleY=t.ycor()

    if turtleX>rightbound or turtleX<leftbound:
        return False
    elif turtleY>topbound or turtleY<bottombound:
        return False

    else:
        return True


wn=turtle.Screen()
wn.setworldcoordinates(-200,-200,200,200)
nick=turtle.Turtle()
nick.shape("turtle")
benson=turtle.Turtle()
benson.shape("turtle")
nick.up()
nick.goto(random.randrange(-200,201),random.randrange(-200,201))
nick.setheading(random.randrange(0,361))
nick.down()

benson.up()
benson.goto(random.randrange(-200,201),random.randrange(-200,201))
benson.down()

while True:
    move_random(nick)
    move_random(benson)

    if is_collide(nick,benson):
        nick.left(180)
        benson.left(180)
        nick.forward(50)
        benson.forward(50)
    elif not is_in_screen(wn,nick):
        nick.left(180)
        nick.forward(50)
    elif not is_in_screen(wn,benson):
        benson.left(180)
        benson.forward(50)




wn.exitonclick()
