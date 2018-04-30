import turtle

def fruit_distributor(num_apples,num_person):
    per_person=num_apples//num_person
    Wilbur=num_apples%num_person
    print("the number of pieces per person is {} the number for Wilbur is {}".format(per_person,Wilbur))

def height(inches):
    '''12 inch =1 feet'''
    feet=inches//12
    rest_inches=inches%12
    print("Your height is:{:.2f} feet,{:.2f} inches".format(feet,rest_inches))

def drive(t,num_times):
    distance=int(input("Enter the distance when turtle moves:"))
    angle=int(input("Enter the angle when turtle turn left:"))
    for i in range(num_times):
        t.forward(distance)
        t.left(angle)
    print("{:.2f}".format(turtle.distance(t)))


def limit(n):
    sum=0
    for i in range(n+1):
        sum+=1/2**i
    print(sum)


def main():
    '''Every question on worksheet_0209'''
    #(1)
    fruit_distributor(100,22)

    #(2)
    user_inches=float(input("Enter your height in inches:"))
    height(user_inches)

    #(3)
    wn=turtle.Screen()
    nick=turtle.Turtle()
    drive(nick,2)
    wn.exitonclick()

    #(4)
    limit(1000)


if __name__ == '__main__':
    main()
