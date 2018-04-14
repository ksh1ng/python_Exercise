import turtle
import random
wn=turtle.Screen()
wn.bgcolor('green')
nick=turtle.Turtle()
benson=turtle.Turtle()

nick.shape("turtle")
benson.shape("turtle")

nick.color("red")
benson.fillcolor("lightblue")

nick.up()
benson.up()
nick.goto(-300,20);benson.goto(-300,-20)

for i in range(40):
    nick.forward(random.randrange(1,10));benson.forward(random.randrange(1,10))



wn.exitonclick()
