import turtle
import random
wn=turtle.Screen()
wn.bgcolor('lightblue')

def race(t1,t2):
    for i in range(40):
        t1.forward(random.randrange(1,10));t2.forward(random.randrange(1,10))


nick=turtle.Turtle()
benson=turtle.Turtle()

nick.shape("turtle")
benson.shape("turtle")

nick.color("red")
benson.fillcolor("green")

nick.up()
benson.up()
nick.position(-300,20);benson.position(-300,-20)
nick.down()

race(nick,benson)



wn.exitonclick()
