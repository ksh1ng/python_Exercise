import turtle
import random
wn=turtle.Screen()
wn.bgcolor('lightblue')
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
for i in range(40):
    nick.forward(random.randrange(1,10));benson.forward(random.randrange(1,10))



wn.exitonclick()
