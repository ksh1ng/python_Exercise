

'''
Author: <ksh1ng>
Date: <2018.5.7>
Class: ISTA 130
Section Leader: <Johnny Hsu>

Description:
<hw01-(2)>
'''

# put all of your import statements below this line and then delete this comment

def gradepoint(score):
    '''Input is score ,return accordingly gradepoint for output'''
    if score >= 90:
        gradepoint=4

    elif score >= 80:
        gradepoint=3

    elif score >= 70:
        gradepoint=2

    elif score >= 60:
        gradepoint=1

    else:
        gradepoint=0
    return gradepoint

def cost_orange(num_pound_oranges):
    '''
    1.A fruit company sells oranges for 32 cents a pound plus $7.50 per order for shipping.
      If an order is over 100 pounds, shipping cost is reduced by $1.50.

    2.Parameter:(1)the number of pounds of oranges

    3.return:the cost of the order
    '''
    if num_pound_oranges <= 100:
        cost=32*num_pound_oranges+7.5

    else:
        cost=32*num_pound_oranges+(7.5-1.5)

    return cost



def which_is_largest(n1,n2,n3):
    '''
    takes three integers as parameters and returns the largest
    '''
    if n1 >= n2 and n1 >= n3:
        largest=n1

    elif  n2 >= n3 and n2 >= n1:
        largest=n2
    else:
        largest=n3

    return largest


def pay(pay_rate,num_hours_worked):
    '''
    takes two parameters, a pay rate(float/int) and the number of hours(float/int) worked, and returns the pay(float).
    '''
    if num_hours_worked < 40:
        return num_hours_worked*pay_rate

    else:
        overtime=num_hours_worked-40
        return pay_rate*40 + overtime*pay_rate*1.5
# put all of your function definitions below this line and then delete this comment


#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''

    # put main code here, make sure each line is indented one level, and delete this comment

    #test gradepoint function :
    '''
    print(gradepoint(95))
    print(gradepoint(85))
    print(gradepoint(75))
    print(gradepoint(65))
    print(gradepoint(55))
    '''

    #test cost_orange function:
    '''
    print(cost_orange(99))
    print(cost_orange(101))
    '''

    #test which_is_largest function:
    '''
    print(which_is_largest(1,2,3),"3")
    print(which_is_largest(1,1,2),"2")
    print(which_is_largest(1,2,2),"2")
    print(which_is_largest(10,9,10),"10")
    print(which_is_largest(1,2,1),"2")
    print(which_is_largest(10,10,10),"10")

    print(which_is_largest(1,3,5),"5")
    print(which_is_largest(1,5,3),"5")
    print(which_is_largest(3,5,1),"5")
    print(which_is_largest(3,1,5),"5")
    print(which_is_largest(5,1,3))
    print(which_is_largest(5,3,1))
    '''





    #test pay function:
    '''
    print(pay(0.5,39))
    print(pay(0.5,40))
    print(pay(0.5,50))
    '''
if __name__ == '__main__':
    main()
