'''
Modify the recursive tree program using one or all of the following ideas:

      Modify the thickness of the branches so that as the branchLen gets smaller,
      the line gets thinner.

      Modify the color of the branches so that as the branchLen gets very short
      it is colored like a leaf.

      Modify the angle used in turning the turtle so that at each branch point
      the angle is selected at random in some range. For example choose the angle between 15 and 45 degrees. Play around to see what looks good.

      Modify the branchLen recursively so that instead of always subtracting the
      same amount you subtract a random amount in some range.

'''
import random
import turtle

def toStr(n, base):
    convertString = '0123456789ABCDEFG'
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base, base) + convertString[n % base]




def TupleToString(a_tuple):
    str = ''

    for i in range(len(a_tuple)):
        str += toStr(a_tuple[i], 16)
    return str



def tree(branchLen, thickness, t):
    rand = random.randrange(10)
    randangle = random.randrange(15,46)  #the angle between 15 and 45 degrees.

    colortuple = (50-rand*5, 193-rand*5, 57-rand*5) #(50,193,57) just for green
    color = TupleToString(colortuple)

    if branchLen > 5 and thickness > 0:
        t.pensize(thickness)
        t.color('#' + color)
        t.forward(branchLen)
        t.right(randangle)
        tree(branchLen-rand, thickness-rand, t)
        t.left(randangle*2)
        tree(branchLen-rand, thickness-rand, t)
        t.right(randangle)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.speed(0)

    tree(60, 10, t)
    myWin.exitonclick()

main()
