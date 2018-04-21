import turtle
def drawbar(t,height,fill_color,i):
    t.fillcolor(fill_color)
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.up()

    if height<0:
        t.goto(20*(2*i-1)-3,2)
    else:
        t.goto(20*(2*i-1)-3,height+2)

    t.write(str(height))
    t.goto((40*i),0)
    t.down()


xs = [48, 117, 200, 240, -160, 260, 220]
maxheight=max(xs)
minheight=min(xs)
numbars=len(xs)
border=10

wn=turtle.Screen()
wn.setworldcoordinates(0-border,minheight-border,40*numbars+border,maxheight+border)
wn.bgcolor("lightgreen")

nick=turtle.Turtle()
nick.pensize(3)
nick.speed(0)


x=0
for h in xs:
    x=x+1
    if h>=200:
        color="red"
    elif h>=100 and h<200:
        color="yellow"
    else:
        color="green"
    drawbar(nick,h,color,x)

wn.exitonclick()
